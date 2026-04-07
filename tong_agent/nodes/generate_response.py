from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_model
from tong_agent.core.logger import get_logger
from tong_agent.prompts import GENERATE_RESPONSE_INSTRUCTION

logger = get_logger(__name__)

def generate_response_node(state: AgentState, config: RunnableConfig):
    """
    5. Generate Response Node
    根据工具执行结果和上下文，生成最终回复。
    """
    logger.info("--- [Node: Generate Response] 生成最终回复 ---")
    model = get_model(config)
    messages = state["messages"]
    
    # 简单的 Prompt，让模型根据上下文回答
    # 注意：此时 messages 已经包含了 ToolMessage (执行结果)
    
    # 为了保证效果，我们可以加一个 System Prompt 提醒它根据工具结果回答
    # 同时也包含了之前的 summary 和 context
    summary = state.get("summary", "")
    context = state.get("editor_context", "")
    memories = state.get("retrieved_memories", "")

    # ============================================================
    # 动态组装 Generate Response Prompt (反硬编码优化)
    # ============================================================
    
    # 1. 提取最新的真实用户问题
    last_human_message = "未知问题"
    for m in reversed(messages):
        if isinstance(m, HumanMessage):
            if not m.content.startswith("System Feedback:") and not m.content.startswith("Evaluator Feedback:"):
                last_human_message = m.content
                break
            
    # 2. 从消息历史中提取所有工具调用的 Observation 结果
    # 现在的架构下，不再依赖 gathered_knowledge 这种总结过的中间态，而是直接把探索到的原始信息喂给大模型
    tool_observations = []
    for msg in messages:
        if isinstance(msg, ToolMessage) and not msg.content.startswith("强制中断"):
            tool_observations.append(f"[{msg.name}]:\n{msg.content}")
    
    tool_result_section = "【执行工具收集到的原始线索】\n" + ("\n---\n".join(tool_observations[-5:]) if tool_observations else "无")
    
    # 3. 构造极简但约束力强的动态 Prompt
    user_input_section = f"【用户核心问题】\n{last_human_message}"
    summary_section = f"【历史对话摘要】\n{summary}" if summary else ""
    memory_section = f"【长期记忆参考】\n{memories}" if memories else ""
    context_section = f"【当前IDE上下文】\n{context}" if context else ""
    
    final_content = (
        f"{user_input_section}\n\n"
        f"{summary_section}\n\n"
        f"{memory_section}\n\n"
        f"{tool_result_section}\n\n"
        f"{context_section}"
    )

    # 构建基础消息
    messages_for_generation = [
        SystemMessage(content=GENERATE_RESPONSE_INSTRUCTION),
        HumanMessage(content=final_content)
    ]
    
    # 新增：注入短期工作记忆（本轮任务中收集到的所有线索）
    if state.get("working_memory"):
        working_mem_str = "\n---\n".join(state["working_memory"])
        context_msg = SystemMessage(content=f"<working_memory_clues>\n这是你在此次任务中收集到的所有核心线索片段。请基于这些线索生成最终回答：\n{working_mem_str}\n</working_memory_clues>")
        messages_for_generation.insert(1, context_msg)
        
    logger.debug("Invoking model for generation...")
    # 4. 调用模型
    response = model.invoke(messages_for_generation, config=config)
    
    return {"messages": [response]}
