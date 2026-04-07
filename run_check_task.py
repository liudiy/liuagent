import asyncio
import uuid
from tong_agent.graph import graph
from langchain_core.messages import HumanMessage

async def main():
    # 1. 构造任务指令
    task = "请帮我检查当前所有的服务器库存，找出哪些服务器满足 TongWeb 软件的安装要求。请列出符合要求的服务器数量和前几台的详情。"
    
    print(f"🚀 启动 Agent 执行任务: {task}\n")
    
    # 2. 初始化状态
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}
    
    initial_state = {
        "messages": [HumanMessage(content=task)],
        "retry_count": 0,
        "editor_context": "Current file: None",
        "summary": ""
    }

    # 3. 运行图 (Stream Mode)
    # 使用 astream 逐步获取输出，观察 Agent 的思考过程
    # 配置 LangFuse 回调以便追踪整个图的执行
    from langfuse.callback import CallbackHandler
    
    # 1. 初始化 CallbackHandler (推荐方式)
    # 这会自动创建一个 Trace，并将后续的所有操作作为子 Span 挂载
    langfuse_handler = CallbackHandler(
        session_id=thread_id,
        user_id="user_123",
        trace_name="TongAgent_Compliance_Check",
        metadata={"env": "dev", "task": "server_check"}
    )
    
    config["callbacks"] = [langfuse_handler]
    
    try:
        async for event in graph.astream(initial_state, config, stream_mode="values"):
            # 打印最新的一条消息
            if "messages" in event:
                last_msg = event["messages"][-1]
                role = last_msg.type
                content = last_msg.content
                
                if role == "ai":
                    print(f"\n🤖 [AI]: {content}")
                    # 检查是否有工具调用
                    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
                        for tc in last_msg.tool_calls:
                            print(f"   🛠️ [Tool Call]: {tc['name']} (args: {tc['args']})")
                elif role == "tool":
                    # 工具输出可能很长，截断一下
                    preview = str(content)[:200] + "..." if len(str(content)) > 200 else content
                    print(f"\n🔧 [Tool Output]: {preview}")
    finally:
        # 确保 Trace 数据上传完毕
        langfuse_handler.flush()

if __name__ == "__main__":
    asyncio.run(main())
