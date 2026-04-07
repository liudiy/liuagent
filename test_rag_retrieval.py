import asyncio
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

async def test_retrieval():
    queries = [
        "TongHttpServer 的官方定义、集群架构要求及最低硬件配置",
        "TongWeb 的官方定义、集群部署模式（如负载均衡、高可用）及资源需求"
    ]
    
    for q in queries:
        print(f"\n{'='*50}\nTesting Query: {q}\n{'='*50}")
        try:
            result = await retrieve_middleware_docs.ainvoke({"query": q})
            print(f"\n--- Result Preview ---\n{result[:1000]}...\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_retrieval())
