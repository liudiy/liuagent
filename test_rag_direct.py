import asyncio
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

async def main():
    q = "TongHttpServer 的官方定义、集群架构要求（如负载均衡机制、节点角色划分、高可用模式）及最低软硬件配置要求"
    print(f"Query: {q}")
    result = await retrieve_middleware_docs.ainvoke({"query": q})
    print("\n--- RAG Result ---")
    print(result[:1000])
    print("...")

if __name__ == "__main__":
    asyncio.run(main())