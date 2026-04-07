import os
import json
import pickle
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document

# 加载环境变量
load_dotenv()

def main():
    print("🚀 开始测试 TongWeb 7 标准版用户手册的图谱抽取能力...")
    
    # 1. 初始化通用大模型 (我们不加任何特定于 JDBC 的 prompt，只说是中间件领域)
    llm = ChatOpenAI(
        model="qwen-plus", 
        api_key=os.environ.get("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.1
    )
    
    # 定义通用的中间件实体类型，不特意强调 jdbc 和 sql
    allowed_nodes = [
        "Product", "Component", "ConfigurationItem", 
        "LogFile", "Concept", "Error", "Operation"
    ]
    
    # 初始化图谱转换器
    llm_transformer = LLMGraphTransformer(
        llm=llm,
        allowed_nodes=allowed_nodes,
        # 允许大模型自由发挥提取关系，我们不限制边
    )
    
    # 2. 从您已有的 chunk 文件中，挑几段典型的涉及数据源和日志的文本进行测试
    # 为了快速演示，我们手动构造几个典型的、来源于标准手册的 Document
    # 这模拟了从 003_TongWeb_V7.0服务配置指南_7049_M9A01.pdf 中切分出的两段毫不相干的文本
    
    doc1 = Document(
        page_content="第4章 JDBC数据源配置。在配置数据源时，需要填写连接URL、用户名和密码。如果遇到 Communications link failure 错误，通常是因为客户端与数据库服务器之间的网络连接异常或配置不正确。请检查防火墙端口是否开放，以及连接超时设置。",
        metadata={"source": "003_TongWeb_V7.0服务配置指南.pdf"}
    )
    
    doc2 = Document(
        page_content="第13章 日志管理。13.2 SQL日志分析。SQL日志记录了时间、执行的SQL语句等信息。通过分析SQL日志可以找出处理耗时多的SQL语句。此页显示了由 TongWeb 中 JDBC 连接池生成的日志。",
        metadata={"source": "003_TongWeb_V7.0服务配置指南.pdf"}
    )
    
    doc3 = Document(
        page_content="当应用从数据源获取连接时进行校验，如果数据库状态不可用但连接池中仍有连接对象，会发生连接断开。建议配置 testOnBorrow 属性来定期检查连接有效性。",
        metadata={"source": "003_TongWeb_V7.0服务配置指南.pdf"}
    )

    docs = [doc1, doc2, doc3]
    
    print("\n⏳ 正在让大模型纯天然地提取实体和关系（不加任何预设立场）...")
    graph_documents = llm_transformer.convert_to_graph_documents(docs)
    
    print("\n✅ 提取完成！以下是大模型自己构建的图谱网络：\n")
    
    for i, g_doc in enumerate(graph_documents):
        print(f"================ 文档片段 {i+1} 提取结果 ================")
        print(f"原文: {docs[i].page_content}")
        print("\n【识别到的实体节点 (Nodes)】:")
        for node in g_doc.nodes:
            print(f"  - [{node.type}] {node.id}")
            
        print("\n【识别到的关系边 (Relationships)】:")
        if not g_doc.relationships:
            print("  (无)")
        for rel in g_doc.relationships:
            print(f"  - [{rel.source.id}] --({rel.type})--> [{rel.target.id}]")
        print("\n")

if __name__ == "__main__":
    main()
