from langchain_core.tools import tool

# 模拟的全局或状态绑定的 TODO 列表
# 在实际 LangGraph 中，我们通常会把这个放在 AgentState 中，
# 但为了工具能直接修改，我们可以通过工具返回特定格式的指令，
# 然后在节点中解析并更新 state，或者直接通过类/闭包绑定。

# 为了简单起见，这里我们定义一个全局变量或让 intent_parse_node 捕获特定工具。
# 但最符合 LangChain tool 规范的做法是，工具返回内容，然后 AgentState 的 reducer 会处理。
# 我们在 tools 中定义这个工具。

@tool
def update_todo_list(todos: list[str], current_focus: str, notes: str) -> str:
    """
    System-level Notebook / TODO tool (核心状态注入工具).
    
    当面对复杂任务（如需要查找多个组件、配置多个参数）时，你应该第一时间调用此工具。
    这会将你的计划和摘要强制注入到系统底层的 System Prompt 中，防止你在漫长的搜索中遗忘。
    
    Args:
        todos: 你的整体任务列表，例如 ["1. 找 Nginx 替代", "2. 找 Tomcat 替代", "3. 找 Redis 替代"]
        current_focus: 你当前正在执行的具体任务，例如 "1. 找 Nginx 替代"
        notes: 你目前为止已经查到的重要线索和结论（精简摘要）。例如 "已查到 Nginx 对应 THS，下一步去查 THS 配置。"
        
    Returns:
        状态更新成功的确认信息。
    """
    # 这个工具的返回值将被 intent_parse_node 特殊处理，
    # 并且提取这些信息存入 AgentState。
    import json
    return json.dumps({
        "_type": "todo_update",
        "todos": todos,
        "current_focus": current_focus,
        "notes": notes
    }, ensure_ascii=False)
