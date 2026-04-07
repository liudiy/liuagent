import asyncio
from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage, AIMessage
from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_model
from tong_agent.core.logger import logger
from tong_agent.tools.file_tools import list_directory, search_file_content, read_file_content

tools = [list_directory, search_file_content, read_file_content]
tool_map = {tool.name: tool for tool in tools}

async def parallel_worker_node(state: AgentState, config: RunnableConfig):
    """
    Parallel Worker Node (Map-Reduce)
    基于 Planner 拆解的子任务，拉起多个 Worker Agent 并行搜索，彻底解决串行思考的龟速瓶颈。
    """
    logger.info("--- [Node: Parallel Worker] 并行执行子任务 (Planner-Worker 架构) ---")
    plan = state.get("plan", [])
    if not plan:
        return {}
        
    async def run_worker(task: str, worker_id: int):
        logger.debug(f"  [Worker {worker_id}] 开始执行子任务: {task}")
        worker_model = get_model(config).bind_tools(tools)
        messages = [
            SystemMessage(content=f"你是一个专注且高效的 Worker Agent。\n你的任务是：{task}\n"
                                  f"请使用 list_directory, search_file_content, read_file_content 在本地知识库彻底搜索相关配置。\n"
                                  f"不要停留在概念，必须找到具体的文件路径、参数名或命令。\n"
                                  f"完成后，直接输出详细的发现总结。"),
            HumanMessage(content=task)
        ]
        
        # 简易内部 ReAct 循环 (最多 4 步)
        for step in range(4):
            response = await worker_model.ainvoke(messages, config=config)
            messages.append(response)
            
            if not response.tool_calls:
                break # 任务完成
                
            for tc in response.tool_calls:
                tool_name = tc["name"]
                tool_args = tc["args"]
                tool_instance = tool_map.get(tool_name)
                try:
                    if hasattr(tool_instance, "ainvoke"):
                        result = await tool_instance.ainvoke(tool_args, config=config)
                    else:
                        result = tool_instance.invoke(tool_args, config=config)
                except Exception as e:
                    result = f"Error: {e}"
                
                messages.append(ToolMessage(content=str(result), tool_call_id=tc["id"], name=tool_name))
                
        logger.debug(f"  [Worker {worker_id}] 子任务完成")
        return f"【Worker {worker_id} 探索结果】({task}):\n{messages[-1].content}"

    # 并发执行所有子任务 (加速核心)
    results = await asyncio.gather(*(run_worker(task, i+1) for i, task in enumerate(plan)), return_exceptions=True)
    
    valid_results = []
    for res in results:
        if isinstance(res, Exception):
            valid_results.append(f"子任务执行异常: {res}")
            logger.error(f"子任务执行异常: {res}")
        else:
            valid_results.append(res)
            
    summary_content = "\n\n".join(valid_results)
    logger.info("--- [Parallel Worker] 所有子任务并行执行完毕，汇总结果 ---")
    
    # 返回工作记忆，并伪装一条 AIMessage 供 Evaluator 节点进行质检
    return {
        "working_memory": valid_results,
        "messages": [AIMessage(content=f"这是并行 Worker 探索汇总的结果：\n{summary_content}")]
    }
