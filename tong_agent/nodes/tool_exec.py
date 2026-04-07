import operator
from typing import Annotated, TypedDict, Literal, Optional

from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import ToolMessage

from tong_agent.core.state import AgentState
from tong_agent.core.tools_registry import tool_map
from tong_agent.core.logger import get_logger

logger = get_logger(__name__)

def tool_exec_node(state: AgentState, config: RunnableConfig):
    """
    3. Tool Execution Node
    执行 LLM 请求的工具。
    """
    logger.info("--- [Node: Tool Exec] 执行工具 ---")
    
    messages = state["messages"]
    last_message = messages[-1]
    
    tool_outputs = []
    new_working_memory = []
    
    # 解析并执行所有的 tool_calls
    for tool_call in last_message.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_call_id = tool_call["id"]
        
        # --- 强制思考拦截器 (MANDATORY THOUGHT INTERCEPTOR) ---
        # 检查上一条 AI Message 的文本内容中是否包含了 <thought> 标签
        # 注意：在使用 function calling 时，有的模型会把内容放在 message.content 中，有的会放在 tool_calls 之外的特殊字段
        has_thought = False
        if isinstance(last_message.content, str) and "<thought>" in last_message.content and "</thought>" in last_message.content:
            has_thought = True
        elif isinstance(last_message.content, list):
            for block in last_message.content:
                if isinstance(block, dict) and block.get("type") == "text":
                    text_content = block.get("text", "")
                    if "<thought>" in text_content and "</thought>" in text_content:
                        has_thought = True
                        break
                        
        if not has_thought:
            logger.warning(f"--- [Interceptor] 拦截：检测到模型未使用 <thought> 标签直接调用工具 {tool_name} ---")
            tool_outputs.append(ToolMessage(
                content="System Error: TOOL EXECUTION BLOCKED. You MUST wrap your reasoning inside <thought>...</thought> tags in your message text BEFORE calling any tools. Please retry and include your thought process.",
                tool_call_id=tool_call_id,
                name=tool_name,
                status="error"
            ))
            continue
            
        logger.debug(f"Executing tool {tool_name} with args: {tool_args}")
        
        if tool_name in tool_map:
            try:
                # 执行工具
                tool_instance = tool_map[tool_name]
                result = tool_instance.invoke(tool_args, config=config) # Pass config for tracing propagation
                
                # 构造 ToolMessage
                result_str = str(result)
                tool_msg = ToolMessage(
                    content=result_str,
                    tool_call_id=tool_call_id,
                    name=tool_name
                )
                tool_outputs.append(tool_msg)
                
                # --- 新增：工作记忆 (Working Memory) 提取机制 ---
                # 如果是重要文件阅读或精准搜索，将其内容摘录到工作记忆中，防止在长循环中被遗忘
                if tool_name in ["read_file_content", "search_file_content"]:
                    # 简单清洗：如果内容不是报错或过长，则作为重要线索记录
                    if "Error" not in result_str and len(result_str) > 10:
                        snippet = f"[{tool_name}] 线索提取:\n{result_str[:1500]}..." if len(result_str) > 1500 else f"[{tool_name}] 线索提取:\n{result_str}"
                        new_working_memory.append(snippet)
            except Exception as e:
                tool_outputs.append(ToolMessage(
                    content=f"Error executing {tool_name}: {e}",
                    tool_call_id=tool_call_id,
                    name=tool_name,
                    status="error"
                ))
                logger.error(f"Tool execution failed: {e}")
        else:
            tool_outputs.append(ToolMessage(
                content=f"Tool {tool_name} not found.",
                tool_call_id=tool_call_id,
                name=tool_name,
                status="error"
            ))
            logger.warning(f"Tool {tool_name} not found in tool map.")
            
    # 将工具输出添加到消息历史，并增加 step_count
    return {
        "messages": tool_outputs,
        "step_count": state.get("step_count", 0) + 1,
        "execution_result": "success" if tool_outputs else "failed",
        "working_memory": new_working_memory
    }
