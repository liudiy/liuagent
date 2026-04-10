import threading
from typing import Optional

from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import HumanMessage, AIMessage

from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_fast_model
from tong_agent.core.logger import get_logger
from tong_agent.mem0_client import get_mem0_client

logger = get_logger(__name__)

def retrieve_memory_node(state: AgentState, config: RunnableConfig):
    """
    根据用户最新的问题，去 Mem0 中检索相关记忆
    """
    logger.info("--- [Node: Retrieve Memory] 检索长期记忆 ---")
    
    # 从 config 中获取 user_id
    user_id = config.get("configurable", {}).get("user_id", "default_user")
    
    messages = state["messages"]
    
    # 获取用户最新的一条消息
    last_human_message = ""
    for m in reversed(messages):
        if isinstance(m, HumanMessage):
            last_human_message = m.content
            break
            
    if not last_human_message:
        return {}

    try:
        m = get_mem0_client()
        # search 方法返回相关的记忆列表
        # user_id 可以是固定值，或者从环境变量/请求中获取
        logger.debug(f"Searching memory for query: '{last_human_message}' user_id='{user_id}'")
        memories = m.search(last_human_message, user_id=user_id) 
        logger.debug(f"Search raw result type: {type(memories)}")
        
        # 处理 mem0 返回格式 (可能是 list 或 dict)
        if isinstance(memories, dict) and "results" in memories:
            memories = memories["results"]

        # If no memories found via search, try to list all memories for debugging
        if not memories:
            logger.debug(f"Search returned empty. Attempting to list all memories for {user_id}...")
            try:
                all_memories = m.get_all(user_id=user_id)
                
                # Normalize get_all return
                if isinstance(all_memories, dict) and "results" in all_memories:
                    all_memories_list = all_memories["results"]
                elif isinstance(all_memories, list):
                    all_memories_list = all_memories
                else:
                    all_memories_list = []
                    logger.debug(f"Unknown get_all return type: {type(all_memories)} - {all_memories}")

                logger.debug(f"All memories count (list): {len(all_memories_list)}")
                # output first few for debug
                if all_memories_list:
                    for i, mem in enumerate(all_memories_list[:3]):
                        logger.debug(f"Memory {i}: {mem}")
            except Exception as e:
                logger.error(f"Failed to list all memories: {e}")

        # 格式化记忆字符串
        memory_str = ""
        if memories and isinstance(memories, list):
             memory_list = []
             for mem in memories:
                 if isinstance(mem, dict):
                     memory_list.append(f"- {mem.get('memory', '')}")
                 elif isinstance(mem, str):
                     memory_list.append(f"- {mem}")
                 else:
                     memory_list.append(f"- {str(mem)}")
             
             memory_str = "\n".join(memory_list)
             logger.debug(f"Retrieved Memories:\n{memory_str}")
        else:
            logger.debug("No relevant memories found.")
            
        return {"retrieved_memories": memory_str}
        
    except Exception as e:
        logger.error(f"Error retrieving memory: {e}")
        return {"retrieved_memories": ""}

def save_memory_task(use_msg: str, ai_msg: str, user_id: str, config: Optional[RunnableConfig] = None):
    """
    后台线程执行的保存任务，不阻塞主流程。
    在保存前，使用 LLM 提炼对话中的核心事实和用户偏好，避免流水账。
    """
    if not use_msg or not ai_msg:
        return
    
    try:
        logger.info(f"--- [Async Background] 开始提炼并保存记忆 (user_id={user_id})... ---")
        
        # 使用轻量级模型进行提炼，传递 config 以便 Langfuse 能够追踪这个后台 LLM 调用
        llm = get_fast_model(config)
        
        prompt = f"""
        请分析以下用户和 AI 的一轮对话。
        提取出其中**真正值得长期记忆**的信息，例如：
        1. 用户的个人偏好（例如：习惯使用 Python，喜欢简短回答等）。
        2. 核心客观事实（例如：用户的工号、所在部门、关注的特定项目或报错等）。
        
        如果对话只是普通的寒暄或一次性的查询，请直接返回“无重要记忆”。
        如果有值得记忆的内容，请以简短的一句话总结。
        
        用户：{use_msg}
        AI：{ai_msg}
        """
        
        # 将字符串包装为 HumanMessage，并传递 config，这样 Langfuse 就能把这次提炼计入当前的 Trace 中
        extracted_memory = llm.invoke([HumanMessage(content=prompt)], config=config).content.strip()
        
        if "无重要记忆" not in extracted_memory and len(extracted_memory) > 5:
            m = get_mem0_client()
            m.add(extracted_memory, user_id=user_id)
            logger.info(f"--- [Async Background] 记忆提炼并保存成功: {extracted_memory} ---")
        else:
            logger.info(f"--- [Async Background] 无重要记忆，跳过保存 ---")
         
    except Exception as e:
        logger.error(f"--- [Async Background] 保存失败: {e} ---")

def save_memory_node(state: AgentState, config: RunnableConfig):
    """
    启动异步线程保存记忆，自身立即返回。
    """
    logger.info("--- [Node: Save Memory] 保存交互记忆 ---")
    
    # 从 config 中获取 user_id
    user_id = config.get("configurable", {}).get("user_id", "default_user")
    
    messages = state["messages"]
    
    # 提取最近的一轮对话 (用户问 + AI 答)
    user_msg = ""
    ai_msg = ""
    
    # 从后往前找最近的一个 AI 回复和对应的人类提问
    for m in reversed(messages):
        if isinstance(m, AIMessage) and not ai_msg:
            ai_msg = m.content
        if isinstance(m, HumanMessage) and not user_msg and ai_msg: 
            # 只有找到 AI 回复后，才找最近的人类提问，确保配对
            user_msg = m.content
        if user_msg and ai_msg:
            break
            
    if user_msg and ai_msg:
        try:
            # 传递 config 给后台线程，使得 Langfuse 能追踪到后台的 LLM 调用
            t= threading.Thread(target=save_memory_task, args=(user_msg, ai_msg, user_id, config))
            t.start()
        except Exception as e:
            logger.error(f"Error saving memory: {e}")
    else:
        logger.debug("No complete interaction found to save.")
            
    return {}
