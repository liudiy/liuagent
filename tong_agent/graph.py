from typing import Literal

from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from tong_agent.core.state import AgentState
from tong_agent.core.logger import get_logger

# 导入所有节点
from tong_agent.nodes.classifier import classifier_node
from tong_agent.nodes.planner import planner_node
from tong_agent.nodes.parallel_worker import parallel_worker_node
from tong_agent.nodes.intent_parse import intent_parse_node
from tong_agent.nodes.tool_exec import tool_exec_node
from tong_agent.nodes.evaluator import evaluator_node
from tong_agent.nodes.generate_response import generate_response_node
from tong_agent.nodes.memory import retrieve_memory_node, save_memory_node
from tong_agent.nodes.summarize import summarize_conversation_node

logger = get_logger(__name__)

# ==========================================
# 路由函数定义 (Routing Logic)
# ==========================================

def route_after_classifier(state: AgentState) -> Literal["planner", "intent_parse"]:
    complexity = state.get("complexity", "SIMPLE")
    if complexity == "COMPLEX":
        logger.info("--- [Route] 分类结果: COMPLEX -> 进入 Planner (Map-Reduce) ---")
        return "planner"
    else:
        logger.info("--- [Route] 分类结果: SIMPLE/DIRECT -> 进入 Intent Parse (单体 Agent) ---")
        return "intent_parse"

def route_intent(state: AgentState) -> Literal["tool_exec", "evaluator"]:
    intent = state.get("current_intent")
    
    # 获取并更新探索步数
    step_count = state.get("step_count", 0)
    
    # 达到最大步数，强制中断探索，交由评估者评估当前获取的信息
    if step_count >= 10:
        logger.warning(f"--- [Route] 达到最大探索步数限制 ({step_count}次)，强制跳转至评估节点 ---")
        return "evaluator"
        
    if intent == "tool_call":
        return "tool_exec"
        
    # 如果不是 tool_call，说明 Agent 认为自己找够了，或者想直接回答
    # 交由 Evaluator 评估
    logger.info("--- [Route] Intent 判断无需工具（或给出初步回答），交由 Evaluator 评估 ---")
    return "evaluator"

def route_tool_exec(state: AgentState) -> Literal["intent_parse"]:
    logger.info("--- [Route] 工具执行完成，返回 intent_parse 继续 ReAct 循环 ---")
    return "intent_parse"

def route_evaluator(state: AgentState) -> Literal["generate_response", "intent_parse"]:
    if state.get("evaluator_approved", False):
        logger.info("--- [Route] Evaluator 审核通过 -> 进入最终回答节点 ---")
        return "generate_response"
    else:
        logger.info("--- [Route] Evaluator 审核驳回 -> 返回 intent_parse 继续探索 ---")
        return "intent_parse"

# ==========================================
# 构建图 (Graph Construction)
# ==========================================

def get_graph(checkpointer=None):
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("classifier", RunnableLambda(classifier_node).with_config(run_name="classifier_node"))
    workflow.add_node("planner", RunnableLambda(planner_node).with_config(run_name="planner_node"))
    workflow.add_node("parallel_worker", RunnableLambda(parallel_worker_node).with_config(run_name="parallel_worker_node"))
    workflow.add_node("retrieve_memory", RunnableLambda(retrieve_memory_node).with_config(run_name="retrieve_memory_node"))
    workflow.add_node("summarize_conversation", RunnableLambda(summarize_conversation_node).with_config(run_name="summarize_conversation_node"))
    workflow.add_node("intent_parse", RunnableLambda(intent_parse_node).with_config(run_name="intent_parse_node"))
    workflow.add_node("tool_exec", RunnableLambda(tool_exec_node).with_config(run_name="tool_exec_node"))
    workflow.add_node("evaluator", RunnableLambda(evaluator_node).with_config(run_name="evaluator_node"))
    workflow.add_node("generate_response", RunnableLambda(generate_response_node).with_config(run_name="generate_response_node"))
    workflow.add_node("save_memory", RunnableLambda(save_memory_node).with_config(run_name="save_memory_node"))
    
    # Add Edges
    # 1. Start -> Retrieve Memory -> Summarize -> Classifier
    workflow.add_edge(START, "retrieve_memory")
    workflow.add_edge("retrieve_memory", "summarize_conversation")
    workflow.add_edge("summarize_conversation", "classifier")
    
    # 2. Classifier Routing
    workflow.add_conditional_edges(
        "classifier",
        route_after_classifier,
        {
            "planner": "planner",
            "intent_parse": "intent_parse"
        }
    )
    
    # 3. Planner -> Parallel Worker
    workflow.add_edge("planner", "parallel_worker")
    
    # 4. Parallel Worker -> Evaluator (并行完成后，交由质检员进行全局验收)
    workflow.add_edge("parallel_worker", "evaluator")
    
    # 5. Tool Exec -> Intent Parse
    workflow.add_conditional_edges(
        "tool_exec",
        route_tool_exec,
        {
            "intent_parse": "intent_parse"
        }
    )

    # 6. Intent Parse -> Tool Exec or Evaluator
    workflow.add_conditional_edges(
        "intent_parse",
        route_intent,
        {
            "tool_exec": "tool_exec",
            "evaluator": "evaluator"
        }
    )
    
    # 7. Evaluator Routing
    workflow.add_conditional_edges(
        "evaluator",
        route_evaluator,
        {
            "generate_response": "generate_response",
            "intent_parse": "intent_parse"
        }
    )
    
    # 8. Generate Response -> Save Memory
    workflow.add_edge("generate_response", "save_memory")

    # 9. Save Memory -> END
    workflow.add_edge("save_memory", END)
    
    return workflow.compile(checkpointer=checkpointer)

# ==========================================
# 导出图实例 (Export Graph)
# ==========================================
memory = MemorySaver()
graph = get_graph(checkpointer=memory)
