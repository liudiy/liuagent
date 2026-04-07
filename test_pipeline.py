import asyncio
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

async def main():
    print("=== Testing TongRDS Retrieval ===")
    q1 = "TongRDS 的官方定义、集群类型（如高可用/读写分离/分片集群）及对服务器配置的具体要求"
    res1 = await retrieve_middleware_docs.ainvoke({"query": q1})
    print(f"\nResult Length: {len(res1)}")
    print(f"Preview: {res1[:800]}...\n")
    
    print("=== Testing TongHttpServer Retrieval ===")
    q2 = "TongHttpServer 的官方定义、集群架构要求及最低硬件配置规范"
    res2 = await retrieve_middleware_docs.ainvoke({"query": q2})
    print(f"\nResult Length: {len(res2)}")
    print(f"Preview: {res2[:800]}...\n")

if __name__ == "__main__":
    asyncio.run(main())