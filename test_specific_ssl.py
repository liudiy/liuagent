import asyncio
import os
import sys

# Ensure we're running from the right directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tong_agent.graph import get_graph
from langchain_core.messages import HumanMessage

async def main():
    graph = get_graph()
    question = "TongWeb 8 和 TongRDS 2 分别如何开启和配置 SSL 证书？请给出详细的配置步骤。"
    print(f"正在向 Agent 提问: {question}\n")
    print("Agent 正在思考...\n")
    
    # Use a specific thread_id to avoid colliding with other memories if any
    config = {"configurable": {"thread_id": "test_specific_ssl_question_456", "user_id": "test_user"}, "recursion_limit": 100}
    
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
        print("="*50 + "\n")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    asyncio.run(main())