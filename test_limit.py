import asyncio
from langchain_core.messages import HumanMessage
from tong_agent.graph import graph
from langchain_core.runnables.config import RunnableConfig

async def test():
    query = "我有8台服务器，安装TongHttpServer，Tongweb，TongRDS，需要支持集群"
    
    config = RunnableConfig(
        configurable={"thread_id": "test_limit_01"},
        recursion_limit=50 # 显式设置 limit
    )
    
    inputs = {
        "messages": [HumanMessage(content=query)]
    }
    
    step = 0
    try:
        async for output in graph.astream(inputs, config=config, stream_mode="updates"):
            step += 1
            for node_name, state_update in output.items():
                print(f"Step {step}: Executed node [{node_name}]")
    except Exception as e:
        print(f"\nCRASHED at step {step} with error: {e}")

if __name__ == "__main__":
    asyncio.run(test())
