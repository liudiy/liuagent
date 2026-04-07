import asyncio
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

async def main():
    res = retrieve_middleware_docs.invoke({"query": "TongWeb并发数相关的配置参数 线程池"})
    print(res)

if __name__ == "__main__":
    asyncio.run(main())
