import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tong_agent.graph import get_graph
from langchain_core.messages import HumanMessage

async def main():
    graph = get_graph()
    question = "一个环境，安装了TongHttpServer，Tongweb，TongRDS，部署在8个不同的服务器上，如何保证全链路数据安全？"
    print(f"正在向 Agent 提问: {question}\n")
    
    config = {"configurable": {"thread_id": "test_broad_security_query_1", "user_id": "test_user"}, "recursion_limit": 100}
    
    try:
        async for event in graph.astream_events(
            {"messages": [HumanMessage(content=question)]},
            config=config,
            version="v2"
        ):
            if event["event"] == "on_chat_model_stream":
                chunk = event["data"]["chunk"].content
                if chunk and isinstance(chunk, str):
                    print(chunk, end="", flush=True)
        print("\n\n" + "="*50)
        print("回答结束")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    asyncio.run(main())