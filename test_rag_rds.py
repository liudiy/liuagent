import asyncio
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

async def main():
    q = "TongRDS 的官方定义、集群类型、高可用机制及节点角色"
    print(f"Query: {q}")
    result = await retrieve_middleware_docs.ainvoke({"query": q})
    print("\n--- RAG Result ---")
    print(result[:2000])

if __name__ == "__main__":
    asyncio.run(main())