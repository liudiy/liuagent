import os
from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.storage import InMemoryStore
from langchain.retrievers import ParentDocumentRetriever
import pickle

# 设置路径和环境变量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "chroma_db_parent_child")
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# --- 1. 模拟数据加载 ---
def load_mock_documents() -> List[Document]:
    """
    模拟加载长文档。这里我们提供一段关于 TongWeb 的模拟长文档。
    实际应用中应该替换为 PyPDFLoader 或前面写的 llm_chunking_strategy 生成的文档。
    """
    text = """
    # 第一章 TongWeb 简介与核心架构
    TongWeb 是一个高性能的 Java EE 兼容中间件服务器。它提供了一个稳定、安全的运行环境。
    核心架构包括 Web 容器、EJB 容器、JMS 服务和数据库连接池管理。
    Web 容器负责处理 HTTP 请求，支持 Servlet 3.1 和 JSP 2.3 规范。
    
    # 第二章 数据库连接池配置与排查
    数据库连接池是中间件中极为关键的组件。配置不当会导致严重的性能问题或故障。
    
    ## 2.1 常见配置参数
    - max-pool-size: 最大连接数，建议根据数据库承载能力设置，默认 100。
    - min-pool-size: 最小空闲连接数，默认 10。
    - connection-timeout: 获取连接的超时时间，单位为毫秒。
    
    ## 2.2 常见报错排查
    1. **JDBCConnectionException: Communications link failure**
       这个报错通常意味着应用服务器与数据库服务器之间的网络连接被异常中断。
       可能的原因包括：
       - 防火墙拦截了 3306 等数据库端口。
       - 数据库端重启了服务。
       - 网络抖动导致 TCP 层面断开。
       排查方法：首先使用 ping 和 telnet 检查网络连通性。

    2. **PoolExhaustedException**
       表示连接池中的连接已被耗尽。说明当前并发请求量超过了 max-pool-size。
       排查方法：查看是否有慢 SQL 导致连接长时间未被释放。
    """
    return [Document(page_content=text, metadata={"source": "TongWeb_Manual.pdf"})]

# --- 2. 构建 Parent-Child Retriever ---
def build_parent_child_retriever(documents: List[Document]):
    """
    初始化并构建 ParentDocumentRetriever 架构
    """
    print("🚀 开始构建 Parent-Child Retriever 知识库...")
    
    # a. 初始化 Embedding 模型
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-zh-v1.5",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    # b. 初始化底层向量库 (Chroma)，专门用来存【子文档】的向量
    # 注意：这里的 collection_name 随意，主要是用于内部存储
    vectorstore = Chroma(
        collection_name="split_parents", 
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )
    
    # c. 初始化底层文档存储，专门用来存【父文档】的原文
    # 生产环境中推荐使用 RedisStore 或 LocalFileStore，这里为了演示使用内存存储
    # 如果想持久化，可以用 pickle 保存这个 store
    store = InMemoryStore()
    
    # d. 定义两套切分器
    # 1. 父文档切分器 (切成较大的逻辑块，比如 500-1000 字)
    parent_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, 
        chunk_overlap=100
    )
    
    # 2. 子文档切分器 (切成很小的块，比如 100-200 字，专门用来做高精度匹配)
    child_splitter = RecursiveCharacterTextSplitter(
        chunk_size=150, 
        chunk_overlap=30
    )
    
    # e. 组装 ParentDocumentRetriever
    retriever = ParentDocumentRetriever(
        vectorstore=vectorstore,
        docstore=store,
        child_splitter=child_splitter,
        parent_splitter=parent_splitter,
    )
    
    # f. 灌入数据
    print("⏳ 正在切分并入库数据 (这会自动处理父子关联)...")
    retriever.add_documents(documents)
    print("✅ 建库完成！")
    
    return retriever, store

# --- 3. 测试检索效果 ---
def test_retrieval(retriever, query: str):
    print(f"\n🔍 正在检索问题: '{query}'")
    
    # 直接调用 retriever 即可
    retrieved_docs = retriever.invoke(query)
    
    if not retrieved_docs:
        print("未检索到相关内容。")
        return
        
    print(f"🎯 召回了 {len(retrieved_docs)} 个【父文档】:")
    for i, doc in enumerate(retrieved_docs):
        print(f"\n--- 召回结果 {i+1} ---")
        print(f"元数据: {doc.metadata}")
        # 你会发现，虽然命中的可能是很小的一句话，但返回的是完整的大段落
        print(f"完整内容 (前 300 字): \n{doc.page_content[:300]}...")

if __name__ == "__main__":
    # 1. 加载文档
    docs = load_mock_documents()
    
    # 2. 构建 Retriever
    retriever, store = build_parent_child_retriever(docs)
    
    # 3. 模拟测试：针对具体的小细节提问
    test_retrieval(retriever, "发生 Communications link failure 报错是什么原因？")
    test_retrieval(retriever, "连接池最大连接数默认是多少？")
    
    # (可选) 将内存中的 store 保存到磁盘，以便下次直接加载
    with open(os.path.join(DB_DIR, "docstore.pkl"), "wb") as f:
        pickle.dump(list(store.yield_keys()), f) # 这里简单演示，实际应用可能需要更完善的持久化方案
