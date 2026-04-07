import asyncio
import os
import sys
import json
from dotenv import load_dotenv

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 强制设置控制台输出为 utf-8，解决 Windows GBK 报错问题
import codecs
if sys.platform == 'win32':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# 禁用 Mem0 存储，避免多进程测试或连续测试时的 Qdrant 文件锁冲突
os.environ["DISABLE_MEM0"] = "true"

from langchain_core.messages import HumanMessage
from tong_agent.graph import get_graph

load_dotenv()

async def run_agentic_rag_test():
    print("==================================================")
    print("🚀 开始测试 Agentic RAG (文件系统检索范式)")
    print("==================================================")
    
    # 获取 LangGraph Agent
    from langgraph.checkpoint.memory import MemorySaver
    memory = MemorySaver()
    app = get_graph(checkpointer=memory)
    
    # 为了避免和上次测试的历史记忆冲突，这里改一下 thread_id
    config = {"configurable": {"thread_id": "test_agentic_rag_ls_tool_01", "user_id": "test_user"}, "recursion_limit": 300}
    
    # 测试问题：收敛式的 SSL 配置问题
    query = "一个环境部署了 THS、TongWeb 和 TongRDS。为了保证传输链路的安全，我需要为每一个产品配置 SSL/HTTPS。请列出这三个产品配置 SSL 的具体方法。"
    
    print(f"\n🗣️ 用户问题: {query}\n")
    
    # 构造初始状态
    initial_state = {
        "messages": [HumanMessage(content=query)],
        "retry_count": 0,
        "complexity": "COMPLEX", # 强制走规划器
        "current_intent": "conversation"
    }
    
    print("🧠 Agent 开始思考与检索...\n")
    
    # 运行 Agent，并打印中间步骤，观察它是否调用了 list_directory, search_file_content 等新工具
    try:
        async for output in app.astream(initial_state, config=config, stream_mode="updates"):
            for node_name, state_update in output.items():
                print(f"[{node_name}] 节点执行完成")
                
                # 如果是 tool_exec 节点，打印一下工具执行的结果概览
                if node_name == "tool_exec" and "messages" in state_update:
                    for msg in state_update["messages"]:
                        if msg.type == "tool":
                            tool_name = msg.name
                            content = str(msg.content)
                            print(f"  🔧 调用工具: {tool_name}")
                            print(f"  📄 结果预览: {content[:200]}...")
                            print("-" * 30)
                            
                # 如果是 generate_response 节点，这是最终结果
                if node_name == "generate_response" and "messages" in state_update:
                    print("\n" + "="*50)
                    print("✅ 最终回答:")
                    print("="*50)
                    # 找到最后一条 AIMessage
                    for msg in reversed(state_update["messages"]):
                        if msg.type == "ai":
                            print(msg.content)
                            break
                            
    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run_agentic_rag_test())
