from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import SystemMessage, HumanMessage, RemoveMessage

from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_model
from tong_agent.core.logger import get_logger
from tong_agent.prompts import SUMMARIZATION_NODE_INSTRUCTION

logger = get_logger(__name__)

def summarize_conversation_node(state: AgentState, config: RunnableConfig):
    """
    Summarize Conversation Node
    如果对话历史过长，生成摘要并归档旧消息。
    """
    messages = state.get("messages", [])
    summary = state.get("summary", "")
    
    # 阈值设置：如果消息超过 10 条，则进行摘要
    # 在生产环境中，这个阈值通常会更大 (如 20-50)
    # 这里为了演示效果，设为 6
    if len(messages) > 50:
        logger.info("--- [Node: Summarize] 对话过长，正在生成摘要 ---")
        
        # 1. 确定需要摘要的消息范围
        # 保留最后 2 条消息作为上下文 (Usually Human + AI response)
        # 摘要前面的所有消息
        messages_to_summarize = messages[:-2]
        
        # 2. 调用 LLM 生成摘要
        model = get_model(config)
        
        summary_prompt = (
            f"{SUMMARIZATION_NODE_INSTRUCTION}"
            f"\n\n【现有摘要】\n{summary}"
            "\n\n【新增对话】\n"
        )
        
        # 将消息转换为字符串
        conversation_str = "\n".join([f"{m.type}: {m.content}" for m in messages_to_summarize])
        
        response = model.invoke([
            SystemMessage(content=summary_prompt),
            HumanMessage(content=conversation_str)
        ], config=config) # Pass config for tracing propagation
        
        new_summary = response.content
        logger.info(f"--- [Node: Summarize] 新摘要: {new_summary[:50]}... ---")
        
        # 3. 构建移除消息的操作
        # 使用 RemoveMessage 标记要删除的消息 ID
        delete_messages = [RemoveMessage(id=m.id) for m in messages_to_summarize]
        
        return {
            "summary": new_summary,
            "messages": delete_messages
        }
        
    return {}
