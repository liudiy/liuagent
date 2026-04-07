from typing import Literal
from pydantic import BaseModel, Field

from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_model
from tong_agent.core.logger import get_logger
from tong_agent.prompts import EVALUATOR_NODE_INSTRUCTION

logger = get_logger(__name__)

class EvaluatorOutput(BaseModel):
    status: Literal["approved", "partial_approved", "rejected"] = Field(description="评估状态：完美解决、部分解决、或拒绝")
    feedback: str = Field(description="具体的反馈意见、肯定已完成的部分、或指出缺失的部分")
    
def evaluator_node(state: AgentState, config: RunnableConfig):
    logger.info("--- [Node: Evaluator] 评估者正在检查回答质量 ---")
    eval_count = state.get("eval_count", 0) + 1
    messages = state["messages"]
    
    # 统一处理未闭合的 tool_calls (比如因为 step_count 熔断而被强制跳转过来)
    dummy_tool_msgs = []
    if messages and isinstance(messages[-1], AIMessage) and messages[-1].tool_calls:
        for tc in messages[-1].tool_calls:
            dummy_tool_msgs.append(ToolMessage(
                content="强制中断。未执行该工具调用。",
                tool_call_id=tc["id"],
                name=tc["name"]
            ))
    
    # 超过最大评估次数，强制放行
    if eval_count > 5:
        logger.warning("--- [Evaluator] 达到最大评估次数，强制放行 ---")
        return {"eval_count": eval_count, "evaluator_approved": True, "messages": dummy_tool_msgs} if dummy_tool_msgs else {"eval_count": eval_count, "evaluator_approved": True}
        
    last_ai_msg = ""
    user_query = ""
    
    # 寻找最近的 AI 回答和最初的用户问题
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and msg.content and not msg.tool_calls:
            last_ai_msg = str(msg.content)
            break
    for msg in messages:
        if isinstance(msg, HumanMessage):
            user_query = str(msg.content)
            break
            
    # 获取当前正在执行的任务目标 (如果存在计划)
    plan = state.get("plan", [])
    current_idx = state.get("current_task_idx", 0)
    current_task_context = ""
    if plan and current_idx < len(plan):
        current_task_context = f"\n【当前子任务目标】\n这是用户大请求中的一个子任务：{plan[current_idx]}\n你需要评估该回答是否完成了这个特定的子任务。\n"

    evaluator_prompt = (
        f"{EVALUATOR_NODE_INSTRUCTION}\n\n"
        f"【用户原始问题】\n{user_query}\n"
        f"{current_task_context}\n"
        f"【生成者 Agent 当前给出的回答或线索摘要】\n{last_ai_msg}\n\n"
        "请评估该回答是否完全、准确地解答了目标问题。特别是：如果目标要求具体步骤/配置参数，回答中是否包含？"
        "如果仅仅是宏观废话或者说‘未找到’，请拒绝(approved=false)并给出详细建议。"
    )
    
    model = get_model(config)
    structured_evaluator = model.with_structured_output(EvaluatorOutput)
    
    try:
        result: EvaluatorOutput = structured_evaluator.invoke([SystemMessage(content=evaluator_prompt)])
        logger.info(f"--- [Evaluator] 评估结果: {result.status} ---")
        
        if result.status == "rejected":
            logger.info(f"--- [Evaluator] 彻底驳回: {result.feedback} ---")
            feedback_msg = HumanMessage(content=f"Evaluator Feedback: 你的回答被驳回。原因和建议：{result.feedback}。请根据建议继续使用工具探索。", name="Evaluator")
            return {
                "eval_count": eval_count, 
                "evaluator_approved": False,
                "step_count": 0, # 重置探索步数
                "messages": dummy_tool_msgs + [feedback_msg]
            }
        elif result.status == "partial_approved":
            logger.info(f"--- [Evaluator] 部分通过: {result.feedback} ---")
            feedback_msg = HumanMessage(content=f"Evaluator Feedback: [部分通过] {result.feedback}。请固化已完成的成果，继续解决剩下的问题。", name="Evaluator")
            return {
                "eval_count": eval_count, 
                "evaluator_approved": False, # 依然返回 False 让它继续跑 ReAct
                "step_count": 0, # 重置探索步数，给足弹药
                "messages": dummy_tool_msgs + [feedback_msg]
            }
        else: # approved
            logger.info(f"--- [Evaluator] 完美通过 ---")
            return {
                "eval_count": eval_count, 
                "evaluator_approved": True,
                **({"messages": dummy_tool_msgs} if dummy_tool_msgs else {})
            }
    except Exception as e:
        logger.error(f"--- [Evaluator] 评估出错，默认放行: {e} ---")
        return {
            "eval_count": eval_count, 
            "evaluator_approved": True,
            **({"messages": dummy_tool_msgs} if dummy_tool_msgs else {})
        }
