import asyncio
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

async def main():
    q = "TongHttpServer 的高可用机制"
    print(f"Testing Graph RAG with query: {q}")
    result = await retrieve_middleware_docs.ainvoke({"query": q})
    print("\n--- RAG Result ---")
    print(result[:2000])

if __name__ == "__main__":
    asyncio.run(main())