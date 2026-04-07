import sys
import os
# 尝试从不同的路径导入，以兼容不同版本的 langchain
try:
    # 官方标准路径
    from langchain.retrievers import EnsembleRetriever
except ImportError:
    try:
        # 具体的子模块路径
        from langchain.retrievers.ensemble import EnsembleRetriever
    except ImportError:
        # 社区包路径 (如果主包没有)
        from langchain_community.retrievers import EnsembleRetriever
# 把当前目录加入 path，方便导入模块
sys.path.append(os.path.dirname(__file__))

# 导入你的新工具
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

def main():
    query = "如何安装tongweb和tonghttpserver，并且支持均衡负载"
    print(f"正在测试查询: {query}")
    
    try:
        # 直接调用工具函数
        # 注意：@tool 装饰过的函数，调用时要用 .invoke({"query": ...}) 或者直接传参？
        # LangChain @tool 装饰器会让函数变成一个对象，但直接调用它也是可以的（通常）。
        # 如果直接调用不行，试着打印一下 hretrieve_middleware_docs 的类型。
        
        result = retrieve_middleware_docs.invoke({"query": query})
        
        print("\n=== 测试结果 ===")
        print(result)
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()