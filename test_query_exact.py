import asyncio
from langchain_core.messages import HumanMessage
from tong_agent.graph import get_graph
import warnings
warnings.filterwarnings("ignore")

async def run_query(query, thread_id):
    graph = get_graph()
    config = {"configurable": {"thread_id": thread_id, "user_id": "test_user_exact_001"}}
    print(f"\n--- 正在处理问题: {query} ---")
    print(">>>AGENT_START<<<")
    
    async for event in graph.astream_events(
        {"messages": [HumanMessage(content=query)]},
        config=config,
        version="v2"
    ):
        if event["event"] == "on_chat_model_stream":
            chunk = event["data"]["chunk"].content
            if chunk and isinstance(chunk, str):
                print(chunk, end="", flush=True)
    print("\n>>>AGENT_END<<<")

async def main():
    queries = [
        "tongweb支持Linux安装吗？如果并发数不够，应该如何调整参数？",
        "如何安装tongweb和tonghttpserver，并且支持均衡负载。"
    ]
    for i, q in enumerate(queries):
        await run_query(q, f"test_thread_exact_run_{i}")

if __name__ == "__main__":
    asyncio.run(main())
