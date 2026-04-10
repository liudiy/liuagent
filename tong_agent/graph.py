from typing import Literal

from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from tong_agent.core.state import AgentState
from tong_agent.core.logger import get_logger

# 导入核心节点
from tong_agent.nodes.intent_parse import intent_parse_node
from tong_agent.nodes.tool_exec import tool_exec_node
from tong_agent.nodes.evaluator import evaluator_node
from tong_agent.nodes.memory import retrieve_memory_node, save_memory_node
from tong_agent.nodes.summarize import summarize_conversation_node

logger = get_logger(__name__)

# ==========================================
# 路由函数定义 (Routing Logic)
# ==========================================

def route_intent(state: AgentState) -> Literal["tool_exec", "evaluator"]:
    intent = state.get("current_intent")
    
    if intent == "tool_call":
        return "tool_exec"
        
    # 如果不是 tool_call，说明 Agent 认为自己找够了，或者想直接回答
    # 交由 Evaluator 评估
    logger.info("--- [Route] Intent 判断无需工具（或准备交卷），交由 Evaluator 质检 ---")
    return "evaluator"

def route_tool_exec(state: AgentState) -> Literal["intent_parse"]:
    logger.info("--- [Route] 工具执行完成，返回 intent_parse 继续核心循环 ---")
    return "intent_parse"

def route_evaluator(state: AgentState) -> Literal["save_memory", "intent_parse"]:
    if state.get("evaluator_approved", False):
        logger.info("--- [Route] Evaluator 审核通过 -> 准备存档退出 ---")
        return "save_memory"
    else:
        logger.info("--- [Route] Evaluator 审核驳回 -> 返回 intent_parse 继续探索 ---")
        return "intent_parse"

# ==========================================
# 构建图 (Graph Construction)
# ==========================================

def get_graph(checkpointer=None):
    workflow = StateGraph(AgentState)
    
    # Add Nodes (核心铁三角 + 后勤)
    workflow.add_node("retrieve_memory", RunnableLambda(retrieve_memory_node).with_config(run_name="retrieve_memory_node"))
    workflow.add_node("summarize_conversation", RunnableLambda(summarize_conversation_node).with_config(run_name="summarize_conversation_node"))
    workflow.add_node("intent_parse", RunnableLambda(intent_parse_node).with_config(run_name="intent_parse_node"))
    workflow.add_node("tool_exec", tool_exec_node) # tool_exec_node 现在是 async 的
    workflow.add_node("evaluator", RunnableLambda(evaluator_node).with_config(run_name="evaluator_node"))
    workflow.add_node("save_memory", RunnableLambda(save_memory_node).with_config(run_name="save_memory_node"))
    
    # Add Edges
    # 1. 启动与后勤
    workflow.add_edge(START, "retrieve_memory")
    workflow.add_edge("retrieve_memory", "summarize_conversation")
    workflow.add_edge("summarize_conversation", "intent_parse")
    
    # 2. 大脑 (Intent Parse) 决策路由
    workflow.add_conditional_edges(
        "intent_parse",
        route_intent,
        {
            "tool_exec": "tool_exec",
            "evaluator": "evaluator"
        }
    )
    
    # 3. 工具执行完毕，必须交回给大脑
    workflow.add_conditional_edges(
        "tool_exec",
        route_tool_exec,
        {
            "intent_parse": "intent_parse"
        }
    )
    
    # 4. 质检员 (Evaluator) 路由
    workflow.add_conditional_edges(
        "evaluator",
        route_evaluator,
        {
            "save_memory": "save_memory",
            "intent_parse": "intent_parse"
        }
    )

    # 5. 存档完毕，结束
    workflow.add_edge("save_memory", END)
    
    return workflow.compile(checkpointer=checkpointer)

# ==========================================
# 导出图实例 (Export Graph)
# ==========================================
memory = MemorySaver()
graph = get_graph(checkpointer=memory)
