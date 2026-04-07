from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage, AIMessage, trim_messages
from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_model
from tong_agent.core.logger import logger
from tong_agent.prompts import INTENT_PARSE_NODE_INSTRUCTION
from tong_agent.tools.file_tools import list_directory, search_file_content, read_file_content

tools = [list_directory, search_file_content, read_file_content]
tool_map = {tool.name: tool for tool in tools}

def intent_parse_node(state: AgentState, config: RunnableConfig):
    """
    Intent Parse Node
    这是 Agentic RAG 的核心思考节点 (Thought)。
    它负责分析当前获取的信息，并决定是继续调用工具 (Action)，还是得出结论并提交给评估者。
    """
    logger.info("--- [Node: Intent Parse] 解析意图与规划 ---")
    
    model = get_model(config)
    model_with_tools = model.bind_tools(tools)
    
    # 构造系统提示词
    sys_msg_content = INTENT_PARSE_NODE_INSTRUCTION
    
    summary = state.get("summary", "")
    if summary:
        sys_msg_content += f"\n\n【历史对话摘要】\n{summary}"
        
    sys_msg = SystemMessage(content=sys_msg_content)
    
    # =====================================================================
    # 🌟 核心优化：Claude Code 风格的 Token 上下文修剪 (Context Folding)
    # =====================================================================
    # 策略：除了最近的 1-2 轮交互，将历史中冗长的 ToolMessage 彻底折叠。
    # 因为 Agent 已经在上一步的 <thought> 中提炼过这些信息并存入了 working_memory，
    # 历史的原始长文本留在 Context 中纯属浪费 Token，还会引发“Lost in the middle”。
    
    optimized_messages = []
    # 找到最后一个 ToolMessage 的索引，以便我们保留最近的输出
    last_tool_msg_idx = -1
    for i, msg in enumerate(state["messages"]):
        if isinstance(msg, ToolMessage):
            last_tool_msg_idx = i

    for i, msg in enumerate(state["messages"]):
        if isinstance(msg, ToolMessage):
            # 如果是最近的1个ToolMessage，保留部分内容（最多4000字符）
            if i == last_tool_msg_idx:
                content_str = str(msg.content)
                if len(content_str) > 4000:
                    compressed_content = content_str[:4000] + "\n\n...[内容过长已截断，请使用 Read 工具精准读取]"
                    optimized_messages.append(ToolMessage(
                        content=compressed_content,
                        tool_call_id=msg.tool_call_id,
                        name=msg.name
                    ))
                else:
                    optimized_messages.append(msg)
            else:
                # 如果是历史 ToolMessage，彻底折叠 (Context Folding)
                folded_content = f"[{msg.name} 执行完毕。原始输出已折叠回收 Token，关键信息已在后续思考中提炼。]"
                optimized_messages.append(ToolMessage(
                    content=folded_content,
                    tool_call_id=msg.tool_call_id,
                    name=msg.name
                ))
        elif isinstance(msg, AIMessage) and msg.tool_calls:
            # =====================================================================
            # 🌟 进阶优化：折叠历史的 AIMessage (隐藏大段的 <thought>)
            # =====================================================================
            # 既然 ToolMessage 已经被折叠了，AI 之前长篇大论的 <thought> 也没有必要完全保留。
            # 只保留它的 Tool Calls 意图，将啰嗦的思考过程清空，进一步节省 50% 的输出 Token。
            if i < last_tool_msg_idx: # 只有当它属于历史轮次时才折叠
                optimized_messages.append(AIMessage(
                    content="[历史思考过程已折叠]", 
                    tool_calls=msg.tool_calls,
                    name=msg.name
                ))
            else:
                optimized_messages.append(msg)
        else:
            optimized_messages.append(msg)

    # 预埋 Prompt Caching (提示词缓存) 机制标记
    # 在生产环境中，对于 Anthropic (Claude) 或支持缓存的 API，
    # 我们应该在庞大的 sys_msg 后面加上 {"cache_control": {"type": "ephemeral"}}
    # 这样几万字的 System Prompt 每次请求只需要算很少的 Token。
    # 这里我们添加一个注释占位符，以便未来接入原生 Claude 时使用。
    # sys_msg.additional_kwargs["cache_control"] = {"type": "ephemeral"}
    
    messages = [sys_msg] + optimized_messages
    
    # 将检索到的长期记忆和工作记忆作为上下文补充给模型
    context_parts = []
    if state.get("retrieved_memories"):
        context_parts.append(f"<long_term_memory>\n{state['retrieved_memories']}\n</long_term_memory>")
        
    # 新增：注入短期工作记忆（本轮任务中收集到的线索）
    if state.get("working_memory"):
        working_mem_str = "\n---\n".join(state["working_memory"][-5:]) # 只取最近的5条核心线索，防止过长
        context_parts.append(f"<working_memory_clues>\n这是你在此次任务中已经阅读过的核心线索片段：\n{working_mem_str}\n</working_memory_clues>")

    if context_parts:
        context_msg = SystemMessage(content="\n\n".join(context_parts))
        messages.insert(1, context_msg)
        
    # --- 新增：防泥潭机制（Circuit Breaker）---
    # 如果连续 3 次都在搜索极其相似的内容，强制插入熔断提示
    recent_queries = state.get("recent_search_queries", [])
    if len(recent_queries) >= 3:
        last_3 = recent_queries[-3:]
        # 简单判断：如果最后一次搜索的字符串与倒数第二次或第三次完全相同
        if last_3[2] == last_3[1] or last_3[2] == last_3[0]:
            logger.warning(f"--- [Intent Parse] 触发防泥潭熔断机制: 连续重复搜索 {last_3[2]} ---")
            circuit_breaker_msg = SystemMessage(
                content="⚠️ **系统强制熔断警告**：你在这个方向上已经连续尝试了多次相似的搜索且似乎没有进展！"
                        "请立即停止搜索相同的关键词，退回上一步。尝试换一个完全不同的搜索词、更换目录，或者思考是否你的假设是错的。"
            )
            messages.insert(1, circuit_breaker_msg)
    
    logger.debug("Invoking model with tools...")
    response = model_with_tools.invoke(messages, config=config)
    
    # 解析意图
    if response.tool_calls:
        logger.info(f"--- [Intent Parse] 决定调用工具: {[tc['name'] for tc in response.tool_calls]} ---")
        
        # --- 新增：防泥潭机制记录搜索历史 ---
        new_search_queries = []
        for tc in response.tool_calls:
            if tc["name"] in ["search_file_content", "read_file_content"]:
                # 记录搜索关键词或读取路径，用于防死循环
                args_str = str(tc.get("args", {}))
                new_search_queries.append(f"{tc['name']}: {args_str}")
                
        return {
            "current_intent": "tool_call",
            "messages": [response],
            "retry_count": 0,  # 重置错误重试次数
            "recent_search_queries": new_search_queries # 将本次搜索加入历史
        }
    else:
        logger.info("--- [Intent Parse] 决定直接回复/反思 ---")
        return {
            "current_intent": "conversation",
            "messages": [response],
            "retry_count": 0
        }
