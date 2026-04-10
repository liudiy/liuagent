from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage, AIMessage, trim_messages
from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_model
from tong_agent.core.logger import logger
from tong_agent.prompts import INTENT_PARSE_NODE_INSTRUCTION
from tong_agent.tools.file_tools import list_directory, search_file_content, read_file_content
from tong_agent.tools.notebook_tools import update_todo_list
import json

tools = [list_directory, search_file_content, read_file_content, update_todo_list]
tool_map = {tool.name: tool for tool in tools}

def intent_parse_node(state: AgentState, config: RunnableConfig):
    """
    Intent Parse Node
    这是 Agentic RAG 的核心思考节点 (Thought)。
    它负责分析当前获取的信息，并决定是继续调用工具 (Action)，还是得出结论并提交给评估者。
    """
    logger.info("--- [Node: Intent Parse] 解析意图与规划 ---")
    
    model = get_model(config)
    
    # 解析并提取最近一次的 TODO 状态（从 ToolMessage 中）
    latest_todos = state.get("todos", [])
    latest_focus = state.get("current_focus", "")
    latest_notes = state.get("notebook_notes", "")
    
    # 如果还没有存到 state，我们从最新的 messages 中扫描 update_todo_list 的结果
    for msg in reversed(state["messages"]):
        if isinstance(msg, ToolMessage) and msg.name == "update_todo_list":
            try:
                data = json.loads(msg.content)
                if data.get("_type") == "todo_update":
                    latest_todos = data.get("todos", [])
                    latest_focus = data.get("current_focus", "")
                    latest_notes = data.get("notes", "")
                    break # 取最新的一条即可
            except Exception:
                pass
    
    # 构造系统提示词
    sys_msg_content = INTENT_PARSE_NODE_INSTRUCTION
    
    # =====================================================================
    # 🌟 核心优化：系统级任务状态注入 (System-level Notebook / TODO)
    # 将最新摘要和计划强制注入到 System Prompt 顶部，防止遗忘。
    # =====================================================================
    if latest_todos or latest_notes:
        sys_msg_content += "\n\n" + "="*40
        sys_msg_content += "\n【系统强制注入：你的工作日志与待办事项】\n"
        if latest_todos:
            sys_msg_content += f"总进度计划:\n- " + "\n- ".join(latest_todos) + "\n"
        if latest_focus:
            sys_msg_content += f"当前必须专注执行的任务: {latest_focus}\n"
        if latest_notes:
            sys_msg_content += f"目前为止收集到的核心结论和线索:\n{latest_notes}\n"
        sys_msg_content += "="*40 + "\n"
    
    summary = state.get("summary", "")
    if summary:
        sys_msg_content += f"\n\n【历史对话摘要】\n{summary}"
        
    sys_msg = SystemMessage(content=sys_msg_content)
    
    # =====================================================================
    # 🌟 核心优化：Claude Code 风格的 Token 上下文修剪 (Context Folding)
    # 规则：
    # 1. 历史的 ToolMessage (系统返回的长文本) -> 必须折叠！否则 Token 爆炸
    # 2. 所有的 AIMessage (大模型写的思考和计划) -> 绝对不折叠！这是它自己的工作记忆
    # =====================================================================
    
    optimized_messages = []
    last_tool_msg_idx = -1
    for i, msg in enumerate(state["messages"]):
        if isinstance(msg, ToolMessage):
            last_tool_msg_idx = i

    for i, msg in enumerate(state["messages"]):
        if isinstance(msg, ToolMessage):
            # 只保留最新一次的工具输出（截断到 4000 字符），历史工具输出全部折叠
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
                folded_content = f"[{msg.name} 执行完毕。原始输出已折叠回收 Token。]"
                optimized_messages.append(ToolMessage(
                    content=folded_content,
                    tool_call_id=msg.tool_call_id,
                    name=msg.name
                ))
        # 取消对 AIMessage 的折叠，让它看到自己之前的所有 <thought_process>
        else:
            optimized_messages.append(msg)

    messages = [sys_msg] + optimized_messages
    
    context_parts = []
    if state.get("retrieved_memories"):
        context_parts.append(f"<long_term_memory>\n{state['retrieved_memories']}\n</long_term_memory>")

    if context_parts:
        context_msg = SystemMessage(content="\n\n".join(context_parts))
        messages.insert(1, context_msg)
        
    # --- 防泥潭机制 ---
    recent_queries = state.get("recent_search_queries", [])
    if len(recent_queries) >= 3:
        last_3 = recent_queries[-3:]
        if last_3[2] == last_3[1] or last_3[2] == last_3[0]:
            logger.warning(f"--- [Intent Parse] 触发防泥潭熔断机制: 连续重复搜索 {last_3[2]} ---")
            circuit_breaker_msg = SystemMessage(
                content="⚠️ **系统强制熔断警告**：你在这个方向上已经连续尝试了多次相似的搜索且似乎没有进展！"
                        "请立即停止搜索相同的关键词，退回上一步。尝试换一个完全不同的搜索词、更换目录，或者思考是否你的假设是错的。"
            )
            messages.insert(1, circuit_breaker_msg)
            
    # --- 探索步数超时警告与强制交卷机制 ---
    step_count = state.get("step_count", 0)
    MAX_STEPS = 50
    
    if step_count >= MAX_STEPS:
        logger.warning(f"--- [Intent Parse] 探索步数已达 {step_count}，强制收缴工具权限，下达交卷命令 ---")
        
        # 终极修复：为了防止 DeepSeek/Qwen 等模型即使在没有 tools 的情况下也凭借肌肉记忆输出 XML，
        # 我们不仅要移除 tools，还要在最新的消息后面强行插入一个 User 消息，打断它的连贯性
        timeout_msg = HumanMessage(
            content=f"⚠️ **系统强制指令 (System Override)**：你已经进行了 {step_count} 轮深度的工具调用和探索，现在系统**已强制收回你的工具调用权限**。\n"
                    f"**绝对禁止生成任何 XML 格式的工具调用代码！禁止使用 `<|DSML|function_calls>` 标签！**\n"
                    f"你现在**必须且只能**直接用自然语言向我输出一份最终的总结回答。请把你刚才在 TODO notes 里收集到的所有信息告诉我。立刻开始你的总结，不要写其他废话。"
        )
        messages.append(timeout_msg)
        # 核心：剥夺工具调用权限，强制它只能输出纯文本
        model_with_tools = model.bind(response_format={"type": "text"}) # 强制文本模式
    else:
        model_with_tools = model.bind_tools(tools)
    
    logger.debug("Invoking model with tools...")
    try:
        response = model_with_tools.invoke(messages, config=config)
    except Exception as e:
        logger.error(f"--- [Intent Parse] LLM 调用失败 (可能超时或过载): {e} ---")
        # 兜底：如果模型调用失败，我们强制返回一个让系统反思的消息
        return {
            "current_intent": "conversation",
            "messages": [AIMessage(content=f"系统提示：大模型调用失败 ({e})，可能是上下文过长或 API 超时。请用户稍后再试或精简问题。")],
            "retry_count": state.get("retry_count", 0) + 1
        }
    
    if response.tool_calls:
        logger.info(f"--- [Intent Parse] 决定调用工具: {[tc['name'] for tc in response.tool_calls]} ---")
        
        new_search_queries = []
        for tc in response.tool_calls:
            if tc["name"] in ["search_file_content", "read_file_content"]:
                args_str = str(tc.get("args", {}))
                new_search_queries.append(f"{tc['name']}: {args_str}")
                
        return {
            "current_intent": "tool_call",
            "messages": [response],
            "retry_count": 0,
            "recent_search_queries": new_search_queries,
            "todos": latest_todos,
            "current_focus": latest_focus,
            "notebook_notes": latest_notes
        }
    else:
        logger.info("--- [Intent Parse] 决定直接回复/反思 ---")
        return {
            "current_intent": "conversation",
            "messages": [response],
            "retry_count": 0,
            "todos": latest_todos,
            "current_focus": latest_focus,
            "notebook_notes": latest_notes
        }
