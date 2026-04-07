import asyncio
from langchain_core.messages import HumanMessage
from tong_agent.graph import graph
from langchain_core.runnables.config import RunnableConfig

async def test():
    query = "我有8台服务器，10.10.22.100-10.10.22.107，我该如何使用这些机器。安装TongHttpServer，Tongweb，TongRDS。每个产品，都需要支持集群。机器配置如下：10.10.22.100，CPU x86_64 32核，内存16G，硬盘500G,10.10.22.101，CPU x86_64 32核，内存16G，硬盘500G,10.10.22.102，CPU x86_64 16核，内存64G，硬盘500G,10.10.22.103，CPU x86_64 16核，内存64G，硬盘500G,10.10.22.104，CPU x86_64 16核，内存32G，硬盘500G,10.10.22.105，CPU x86_64 16核，内存32G，硬盘500G,10.10.22.106，CPU x86_64 32核，内存32G，硬盘500G,10.10.22.107，CPU x86_64 32核，内存32G，硬盘500G"
    
    config = RunnableConfig(
        configurable={"thread_id": "test_auto_run_01"},
        recursion_limit=250
    )
    
    inputs = {
        "messages": [HumanMessage(content=query)]
    }
    
    step = 0
    print("🚀 Starting Agent Test Run...")
    try:
        async for event in graph.astream_events(inputs, config=config, version="v1"):
            # 只打印关键节点的流转信息和最终结果，避免日志过多
            if event["event"] == "on_chain_end":
                name = event.get("name")
                if name in ["planner_node", "intent_parse_node", "tool_exec", "reflection_node", "continue_logic_node", "generate_response_node"]:
                    print(f"\n[{step}] ✅ Finished Node: {name}")
                    step += 1
                    
                if name == "generate_response_node":
                    output = event.get("data", {}).get("output", {})
                    if "messages" in output and len(output["messages"]) > 0: 
                        print("\n================ FINAL RESPONSE ================\n")
                        print(output["messages"][-1].content)
                        print("\n================================================\n")
                        
            elif event["event"] == "on_tool_end":
                tool_name = event.get("name")
                print(f"  🛠️ Tool Executed: {tool_name}")
                
    except Exception as e:
        print(f"\n❌ CRASHED at step {step} with error: {e}")

if __name__ == "__main__":
    asyncio.run(test())