import asyncio
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

async def main():
    result = await retrieve_middleware_docs.ainvoke({"query": "TongHttpServer 的官方定义、集群架构要求及最低硬件配置"})
    print("RESULT LENGTH:", len(result))
    print("RESULT PREVIEW:", result[:1000])

if __name__ == "__main__":
    asyncio.run(main())
