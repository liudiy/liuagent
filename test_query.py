import asyncio
from langchain_core.messages import HumanMessage
from tong_agent.graph import get_graph

async def main():
    graph = get_graph()
    config = {"configurable": {"thread_id": "test_thread_3", "user_id": "test_user_3"}}
    query = "如何安装tongweb和tonghttpserver，并且支持均衡负载"
    
    print(f"User Query: {query}\n")
    print("Agent Response:\n")
    
    async for event in graph.astream_events(
        {"messages": [HumanMessage(content=query)]},
        config=config,
        version="v2"
    ):
        if event["event"] == "on_chat_model_stream":
            chunk = event["data"]["chunk"].content
            if chunk and isinstance(chunk, str):
                print(chunk, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
