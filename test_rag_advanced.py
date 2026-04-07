import asyncio
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

def test_retrieval():
    print("================ 测试查询 1: 复杂查询 (预期拆解) ================")
    query1 = "TongWeb怎么安装？它和Tomcat在配置连接池上有什么区别？"
    docs_str1 = retrieve_middleware_docs.invoke({"query": query1})
    print(f"检索结果总长度: {len(docs_str1)} 字符。")
    print(docs_str1)
    print("\n")

    print("================ 测试查询 2: 明确产品名称 (预期前置过滤) ================")
    query2 = "TongWeb 7.0 怎么配置集群？"
    docs_str2 = retrieve_middleware_docs.invoke({"query": query2})
    print(f"检索结果总长度: {len(docs_str2)} 字符。")
    print(docs_str2)
    print("\n")

if __name__ == "__main__":
    test_retrieval()
