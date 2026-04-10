import asyncio
from typing import Annotated, TypedDict, Literal, Optional

from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import ToolMessage

from tong_agent.core.state import AgentState
from tong_agent.core.tools_registry import tool_map
from tong_agent.tools.notebook_tools import update_todo_list
from tong_agent.core.logger import get_logger

# Register notebook tools into tool_map if they are not there yet
if update_todo_list.name not in tool_map:
    tool_map[update_todo_list.name] = update_todo_list

logger = get_logger(__name__)

async def tool_exec_node(state: AgentState, config: RunnableConfig):
    """
    3. Tool Execution Node (Parallel Tool Calling)
    并行执行 LLM 请求的多个工具。
    """
    logger.info("--- [Node: Tool Exec] 并行执行工具 (Parallel Tool Calling) ---")
    
    messages = state["messages"]
    last_message = messages[-1]
    
    tool_outputs = []
    
    async def execute_single_tool(tool_call):
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_call_id = tool_call["id"]
        
        logger.debug(f"Executing tool {tool_name} with args: {tool_args}")
        
        if tool_name in tool_map:
            try:
                tool_instance = tool_map[tool_name]
                # 支持异步或同步工具
                if hasattr(tool_instance, "ainvoke"):
                    result = await tool_instance.ainvoke(tool_args, config=config)
                else:
                    # 如果工具只有同步方法，将其放入线程池执行以免阻塞事件循环
                    result = await asyncio.to_thread(tool_instance.invoke, tool_args, config)
                
                result_str = str(result)
                tool_msg = ToolMessage(
                    content=result_str,
                    tool_call_id=tool_call_id,
                    name=tool_name
                )
                
                # 只需返回工具的执行结果即可，不需要额外的兜底机制，因为 Intent Parse 已经保留了 AIMessage
                return tool_msg
                
            except Exception as e:
                logger.error(f"Tool execution failed: {e}")
                return ToolMessage(
                    content=f"Error executing {tool_name}: {e}",
                    tool_call_id=tool_call_id,
                    name=tool_name,
                    status="error"
                )
        else:
            logger.warning(f"Tool {tool_name} not found in tool map.")
            return ToolMessage(
                content=f"Tool {tool_name} not found.",
                tool_call_id=tool_call_id,
                name=tool_name,
                status="error"
            )

    # 并发执行所有 tool_calls
    tasks = [execute_single_tool(tc) for tc in last_message.tool_calls]
    results = await asyncio.gather(*tasks)
    
    # 汇总并发执行的结果
    for tool_msg in results:
        tool_outputs.append(tool_msg)
            
    # 将工具输出添加到消息历史，并增加 step_count
    return {
        "messages": tool_outputs,
        "step_count": state.get("step_count", 0) + 1,
        "execution_result": "success" if tool_outputs else "failed"
    }
