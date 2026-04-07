import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from tong_agent.graph import get_graph

# 加载环境变量
from dotenv import load_dotenv
load_dotenv()

# 初始化图
graph = get_graph()
config = {"configurable": {"thread_id": "test_thread"}}

def run_test(query, test_name):
    print(f"\n{'='*50}")
    print(f"🚀 开始测试: {test_name}")
    print(f"👉 用户输入: {query}")
    print(f"{'='*50}\n")
    
    # 初始化状态
    initial_state = {
        "messages": [HumanMessage(content=query)],
        "retry_count": 0
    }
    
    # 运行图
    for event in graph.stream(initial_state, config=config, stream_mode="values"):
        pass
    
    print(f"\n✅ 测试结束: {test_name}\n")

if __name__ == "__main__":
    # 测试 1：简单任务
    run_test("今天杭州天气", "简单测试 (Fast Path)")
    
    # 重置 thread_id 以清除记忆
    config = {"configurable": {"thread_id": "test_thread_2"}}
    
    # 测试 2：复杂任务
    run_test("帮我对比一下 DeepSeek V3 和 Qwen Max 的上下文长度，并总结谁更适合处理长文档", "复杂测试 (Planner Path)")
