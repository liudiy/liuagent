import asyncio
from langchain_core.messages import HumanMessage
from tong_agent.graph import graph
from langchain_core.runnables.config import RunnableConfig

async def test():
    query = """我有8台服务器，10.10.22.100-10.10.22.107，每台配置：16C32G、500G数据盘。要求：
部署东方通三大中间件：
1. 安装TongHttpServer，
2. 安装Tongweb，
3. 安装TongRDS。
每个产品，都需要支持集群。
请给我一个合理的部署分配方案。"""
    
    print(f"User Query:\n{query}\n")
    print("-" * 50)
    
    config = RunnableConfig(configurable={"thread_id": "test_deployment_02"})
    
    inputs = {
        "messages": [HumanMessage(content=query)],
        "gathered_knowledge": []
    }
    
    # We use astream to see updates node by node
    async for output in graph.astream(inputs, config=config, stream_mode="updates"):
        for node_name, state_update in output.items():
            print(f"\n[{node_name}] Update:")
            if state_update is None:
                continue
            
            if "plan" in state_update:
                print(f"  Plan: {state_update['plan']}")
            
            if "gathered_knowledge" in state_update:
                print(f"  Gathered Knowledge:\n  {state_update['gathered_knowledge']}")
                
            if "messages" in state_update:
                for msg in state_update["messages"]:
                    content = msg.content if hasattr(msg, 'content') else str(msg)
                    content_preview = content[:300].replace('\n', ' ') + ('...' if len(content) > 300 else '')
                    print(f"  Message ({msg.__class__.__name__}): {content_preview}")
            
            if "next_action" in state_update:
                print(f"  Next Action: {state_update['next_action']}")

    print("\n" + "="*50)
    print("--- Final Output ---")
    state = graph.get_state(config)
    if "messages" in state.values and len(state.values["messages"]) > 0:
        print(f"{state.values['messages'][-1].content}")
    else:
        print("No messages in final state.")

if __name__ == "__main__":
    asyncio.run(test())
