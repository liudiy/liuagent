import asyncio
import os
import sys
import json
import time

# Sync PATH from system to ensure 'rg' is available
if sys.platform == 'win32':
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment') as key:
            sys_path, _ = winreg.QueryValueEx(key, 'Path')
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment') as key:
            usr_path, _ = winreg.QueryValueEx(key, 'Path')
        os.environ['PATH'] = sys_path + os.pathsep + usr_path + os.pathsep + os.environ.get('PATH', '')
    except Exception:
        pass

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
    config = {"configurable": {"thread_id": "test_agentic_rag_ls_tool_09", "user_id": "test_user"}, "recursion_limit": 500}
    
    # 测试问题：收敛式的 SSL 配置问题
    query = "客户使用了nginx + tomcat+redis+activemq，tomcat上部署了办公系统，redis用于存储tomcat的session，以及作为办公系统的缓存使用。activemq，用于办公系统与外部系统交互，办公系统通过JMS与activemq交互。目前系统，每天大约有300万人使用，每天产生的数据，大概500G。用户需要做国产替代，1，给出国产替代方案，2，在每个产品，支持高可用的前提下，给出服务器最小数量，以及相应配置。进一步，给出合理的服务器数量和配置的建议。3，给出部署方案"
    
    print(f"\n🗣️ 用户问题: {query}\n")
    
    # 构造初始状态
    initial_state = {
        "messages": [HumanMessage(content=query)],
        "retry_count": 0,
        "current_intent": "conversation"
    }
    
    print("🧠 Agent 开始思考与检索...\n")
    
    start_time = time.time()
    
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
                            
                # 检查 Evaluator 是否通过，如果通过，intent_parse 输出的就是最终回答
                if node_name == "evaluator" and state_update.get("evaluator_approved"):
                    print("\n✅ Evaluator 审核通过，准备结束。")
                    
                if node_name == "save_memory":
                    print("\n" + "="*50)
                    print("✅ 最终回答:")
                    print("="*50)
                    # 从状态中找到最后一条 AIMessage（由 intent_parse 生成的最终回答）
                    final_state = app.get_state(config)
                    for msg in reversed(final_state.values["messages"]):
                        if msg.type == "ai" and not msg.tool_calls:
                            print(msg.content)
                            break
                            
    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        
    end_time = time.time()
    print("=" * 50)
    print(f"[测试完成] 总耗时: {end_time - start_time:.2f} 秒")

if __name__ == "__main__":
    asyncio.run(run_agentic_rag_test())
