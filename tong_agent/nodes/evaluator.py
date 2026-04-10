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
    step_count = state.get("step_count", 0)
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
    
    # 超过最大评估次数，或者探索步数已经耗尽，强制放行（否则会陷入死循环）
    if eval_count > 8 or step_count >= 50:
        logger.warning(f"--- [Evaluator] 达到最大评估次数({eval_count})或探索步数已耗尽({step_count})，强制放行 ---")
        return {"eval_count": eval_count, "evaluator_approved": True, "messages": dummy_tool_msgs} if dummy_tool_msgs else {"eval_count": eval_count, "evaluator_approved": True}
        
    last_ai_msg = ""
    user_query = ""
    recent_thoughts = []
    
    # 寻找最近的 AI 回答和最初的用户问题，同时收集最近几次的 <thought_process> 作为工作记忆
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and msg.content:
            if not msg.tool_calls and not last_ai_msg:
                last_ai_msg = str(msg.content)
            elif msg.tool_calls and len(recent_thoughts) < 3:
                # 收集 Agent 在调用工具前的思考过程，以便 Evaluator 理解其推理逻辑
                recent_thoughts.append(str(msg.content))
                
    for msg in messages:
        if isinstance(msg, HumanMessage):
            user_query = str(msg.content)
            break

    thoughts_context = "\n---\n".join(reversed(recent_thoughts))
    
    evaluator_prompt = (
        f"{EVALUATOR_NODE_INSTRUCTION}\n\n"
        f"【用户原始问题】\n{user_query}\n\n"
        f"【主 Agent 最近的思考与推理过程 (Working Memory)】\n{thoughts_context}\n\n"
        f"【生成者 Agent 当前准备提交的答案或线索摘要】\n{last_ai_msg}\n\n"
        "请评估该回答是否完全、准确地解答了目标问题。请严格遵循“信任证据链法则”，不要仅凭字面不匹配而驳回。\n"
        "如果目标要求具体步骤/配置参数，回答中是否包含？如果证据不足，请以“督导”身份给出渐进式的探索建议。"
    )
    
    model = get_model(config)
    structured_evaluator = model.with_structured_output(EvaluatorOutput)
    
    try:
        result: EvaluatorOutput = structured_evaluator.invoke([SystemMessage(content=evaluator_prompt)])
        logger.info(f"--- [Evaluator] 评估结果: {result.status} ---")
        
        if result.status == "rejected":
            logger.info(f"--- [Evaluator] 督导发问/纠偏: {result.feedback} ---")
            feedback_msg = HumanMessage(content=f"Evaluator Feedback (督导纠偏): 你的答案尚不完整或方向存疑。建议：{result.feedback}。请不要放弃，补齐证据后继续。", name="Evaluator")
            return {
                "eval_count": eval_count, 
                "evaluator_approved": False,
                "messages": dummy_tool_msgs + [feedback_msg]
            }
        elif result.status == "partial_approved":
            logger.info(f"--- [Evaluator] 部分通过: {result.feedback} ---")
            feedback_msg = HumanMessage(content=f"Evaluator Feedback: [部分通过] {result.feedback}。请固化已完成的成果，继续解决剩下的问题。", name="Evaluator")
            return {
                "eval_count": eval_count, 
                "evaluator_approved": False, # 依然返回 False 让它继续跑 ReAct
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
