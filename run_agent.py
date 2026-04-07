import asyncio
import os
import logging
import sys

# 强制刷新输出
print("--- Agent Startup Check ---", flush=True)

# 强制设置标准输出为 UTF-8 并启用无缓冲
sys.stdout.reconfigure(encoding='utf-8')

# 抑制 LiteLLM 的标准输出干扰
os.environ["LITELLM_LOG"] = "ERROR"
os.environ["MEM0_TELEMETRY"] = "False"
# 设置本地 MEM0_DIR 以避免全局配置冲突
os.environ["MEM0_DIR"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mem0_meta")

from dotenv import load_dotenv

# 加载.env环境变量
load_dotenv()
print("DEBUG: Environment loaded", flush=True)

try:
    print("DEBUG: Importing RedisSaver...", flush=True)
    from langgraph.checkpoint.redis import RedisSaver
    print("DEBUG: Importing Redis...", flush=True)
    from redis import Redis
    print("DEBUG: Importing MemorySaver...", flush=True)
    from langgraph.checkpoint.memory import MemorySaver
    print("DEBUG: Importing langchain messages...", flush=True)
    from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
    print("DEBUG: Importing get_graph...", flush=True)
    from tong_agent.graph import get_graph
    print("DEBUG: Importing CallbackHandler...", flush=True)
    from langfuse.langchain import CallbackHandler
    print("DEBUG: Imports completed.", flush=True)
except ImportError as e:
    print(f"ERROR: Failed to import LangGraph components: {e}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: Unexpected error during import: {e}")
    sys.exit(1)

# 配置日志 - 将级别调整为 INFO 以减少噪音
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logging.getLogger("httpx").setLevel(logging.WARNING)

async def main():
    print("正在初始化 TongAgent (基于 DeepSeek V3 / LiteLLM / LangGraph)...")
    
    # 检查 API Key
    deepseek_api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not deepseek_api_key:
        print("警告：未设置 DEEPSEEK_API_KEY 环境变量，请检查.env文件！")
        return

    # 初始化 Redis Checkpointer
    # 假设 Redis 运行在 localhost:6379，如果不同请修改
    # redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379")
    # memory = None
    
    # try:
    #     # 设置超时时间，避免长时间卡住
    #     redis_client = Redis.from_url(redis_url, socket_connect_timeout=2)
    #     # 尝试 ping 确保连接可用
    #     redis_client.ping()
    #     memory = RedisSaver(redis_client=redis_client)
    #     print("Redis checkpointer initialized successfully.")
    # except Exception as e:
    #     print(f"WARNING: Failed to connect to Redis: {e}")
    #     print("Falling back to MemorySaver (non-persistent).")
    #     print("To use Redis persistence, please ensure Redis is running at localhost:6379 or set REDIS_URL.")
    #     memory = MemorySaver()
    print("DEBUG: Forced MemorySaver usage (Redis disabled for debugging).")
    memory = MemorySaver()
    # print("DEBUG: Forced MemorySaver usage (Redis disabled for debugging).")
    # memory = MemorySaver()
    
    # 获取 Graph
    graph = get_graph(checkpointer=memory)
    
    # 配置会话 ID
    thread_id = "session_001"
    
    # 初始化 Langfuse CallbackHandler (用于监控)
    langfuse_handler = None
    try:
        import requests
        langfuse_host = os.environ.get("LANGFUSE_HOST", "http://localhost:3000")
        # 尝试连接 Langfuse 服务
        try:
            requests.get(langfuse_host, timeout=1)
            langfuse_handler = CallbackHandler()
            print("Langfuse CallbackHandler initialized.")
        except Exception:
            print(f"提示: 无法连接到 Langfuse ({langfuse_host})，监控功能已禁用。")
    except Exception as e:
        print(f"WARNING: Failed to initialize Langfuse: {e}")
    
    config = {
        "configurable": {"thread_id": thread_id},
        "callbacks": [langfuse_handler] if langfuse_handler else []
    }
    print(f"Session initialized: {thread_id} (Langfuse monitoring enabled)")
    
    print("\n--- 开始对话 ---\n")
    # 修改测试问题以更符合场景，测试真实RAG场景下的多轮对话和记忆能力
    queries = [
        # 测试长期记忆：第二轮通过模糊指代询问，看能否提取之前的身份和任务信息
        "我的工号是多少？我是做什么的？"
    ]
    
    for i, query in enumerate(queries):
        print(f"\n[第 {i+1} 轮] 用户: {query}")
        
        try:
            # 使用 astream_events 获取流式事件，包括工具调用和 token 生成
            async for event in graph.astream_events(
                {"messages": [HumanMessage(content=query)]},
                config,
                version="v1"
            ):
                kind = event["event"]
                
                # 处理模型生成的 Token 流
                if kind == "on_chat_model_stream":
                    content = event["data"]["chunk"].content
                    if content:
                        # 检查这是否是最终回复的一部分（通常在工具调用结束后）
                        # 这里简单处理：所有 chat_model 的输出都视为回复内容
                        # 为了让最终回复明显，我们可以在第一次收到 token 时打印一个前缀
                        # 但由于流式输出，这比较难判断确切的开始点，
                        # 更好的方式是把所有 token 收集起来，或者用不同的颜色/前缀标记
                        print(content, end="", flush=True)
                
                # 处理工具调用开始
                elif kind == "on_tool_start":
                    print(f"\n\n[工具调用] {event['name']} Inputs: {event['data'].get('input')}")
                
                # 处理工具调用结束
                elif kind == "on_tool_end":
                    print(f"\n[工具结果] Length: {len(str(event['data'].get('output')))}")
                    print(f"\n\n{'='*10} AI 最终回复 {'='*10}\n") # 工具调用结束后，通常紧接着就是 AI 的最终解释/回复
            
            print(f"\n\n{'='*20} 第 {i+1} 轮回复结束 {'='*20}\n")

        except Exception as e:
            print(f"\n运行过程中出错: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
