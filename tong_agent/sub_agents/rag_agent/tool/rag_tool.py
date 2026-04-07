"""Tool wrapper for LangChain RAG with Hybrid Search (Vector + BM25 + Rerank)."""

import os
import sys
from typing import List, Optional

from langchain_core.tools import tool
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

# 如果没有安装 rank_bm25，请先运行: pip install rank_bm25

# ==========================================
# 配置部分
# ==========================================

# 1. 向量数据库路径 (指向最新的 v2 版本)
# 使用相对路径向上查找
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db_tongdata_v2")

# 2. Embedding 模型 (与构建时保持一致)
EMBEDDING_MODEL_NAME = "BAAI/bge-large-zh-v1.5"

# 3. Rerank 模型 (用于精排)
# 如果本地跑不动，可以先注释掉 Rerank 部分，只用混合检索
RERANK_MODEL_NAME = "BAAI/bge-reranker-base"

# 全局变量缓存 Retriever 实例
_hybrid_retriever = None

def _get_retriever():
    """
    获取或初始化混合检索器 (Hybrid Retriever)。
    包含:
    1. Vector Retriever (语义检索)
    2. BM25 Retriever (关键词检索)
    3. Ensemble Retriever (加权合并)
    """
    global _hybrid_retriever
    if _hybrid_retriever is not None:
        return _hybrid_retriever

    print(f"[RAG Init] 正在初始化混合检索系统...")
    print(f"[RAG Init] 数据库路径: {CHROMA_DB_PATH}")

    if not os.path.exists(CHROMA_DB_PATH):
        print(f"❌ 错误: 向量数据库不存在! 请先运行 build_vector_store.py")
        return None

    try:
        # 1. 加载 Embedding 模型
        print(f"[RAG Init] 加载 Embedding 模型: {EMBEDDING_MODEL_NAME}...")
        embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs={'device': 'cpu'}, # 有 GPU 改 'cuda'
            encode_kwargs={'normalize_embeddings': True}
        )

        # 2. 加载向量数据库 (Vector Store)
        vectorstore = Chroma(
            persist_directory=CHROMA_DB_PATH,
            embedding_function=embedding_model
        )
        
        # 3. 创建 Vector Retriever
        # search_kwargs={"k": 5} 表示向量检索取前 5 个
        vector_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
        print("[RAG Init] Vector Retriever 就绪.")

        # 4. 创建 BM25 Retriever
        # 注意：BM25 需要原始文档列表来构建索引。
        # 由于我们无法直接从 Chroma 反向取出所有原始文本构建 BM25 (效率太低)，
        # 这里的最佳实践是：
        #   a. 在 build 阶段就把 BM25 索引存下来 (最快)。
        #   b. 或者在这里只用 Vector (最简单)。
        #   c. 或者从 vectorstore.get() 取出所有文档 (内存消耗大)。
        
        # 为了演示完整流程，我们尝试方案 C (注意：如果数据量巨大，这步会慢)
        print("[RAG Init] 正在构建 BM25 索引 (读取所有文档)...")
        all_docs_data = vectorstore.get() # 获取所有 ID 和 Metadata
        # Chroma 的 .get() 返回的是 dict，我们需要重新构造 Document 对象
        # 注意：.get() 默认不返回 embedding，只返回 document 内容，速度还行
        all_texts = all_docs_data['documents']
        all_metadatas = all_docs_data['metadatas']
        
        bm25_docs = []
        if all_texts:
            for text, meta in zip(all_texts, all_metadatas):
                bm25_docs.append(Document(page_content=text, metadata=meta))
            
            bm25_retriever = BM25Retriever.from_documents(bm25_docs)
            bm25_retriever.k = 5
            print(f"[RAG Init] BM25 Retriever 就绪 (索引了 {len(bm25_docs)} 个文档).")
        else:
            print("⚠️ 警告: 数据库为空，跳过 BM25。")
            bm25_retriever = None

        # 5. 创建 Ensemble Retriever (混合检索)
        if bm25_retriever:
            # 权重：Vector 0.6, BM25 0.4 (可以调整)
            _hybrid_retriever = EnsembleRetriever(
                retrievers=[vector_retriever, bm25_retriever],
                weights=[0.6, 0.4]
            )
            print("[RAG Init] 混合检索 (Vector+BM25) 初始化完成!")
        else:
            _hybrid_retriever = vector_retriever
            print("[RAG Init] 降级为纯向量检索。")

        return _hybrid_retriever

    except Exception as e:
        print(f"❌ 初始化失败: {e}")
        return None

@tool
def retrieve_middleware_docs(query: str) -> str:
    """
    检索中间件相关的技术文档和知识库。
    
    当需要回答关于中间件（如 TongWeb）的配置、安装、报错、参数含义等具体技术问题时，
    必须使用此工具来获取准确的背景信息。
    
    Args:
        query: 用户的查询问题或关键词（例如："TongWeb 线程池配置" 或 "ERROR-001"）。
        
    Returns:
        包含相关文档片段的字符串。如果没有找到相关信息，返回提示信息。
    """
    print(f"\n🔍 [RAG Tool] 收到查询: {query}")
    retriever = _get_retriever()
    
    if not retriever:
        return "System Error: 知识库未初始化，请联系管理员。"
    
    try:
        # 1. 执行混合检索 (Vector + BM25)
        # 这步会返回去重后的候选文档 (例如 5+5=10个，去重后可能 8 个)
        docs = retriever.invoke(query)
        
        if not docs:
            return "未找到相关文档。"

        # 2. (可选) Rerank 重排序
        # 这里为了简单，我们先不做复杂的 Cross-Encoder Rerank，
        # 而是直接返回混合检索的前 5 个结果。
        # 如果你想加 Rerank，可以在这里引入 HuggingFaceCrossEncoder。
        
        final_docs = docs[:5]
        
        # 3. 格式化输出
        results = []
        for i, doc in enumerate(final_docs):
            source = os.path.basename(doc.metadata.get("source", "未知来源"))
            # 去掉 DeepSeek 生成的上下文前缀，只展示 Original Text 给用户看？
            # 不，展示上下文可能更有助于 Agent 理解！保留它。
            content = doc.page_content.strip()
            
            # 截断过长的内容，节省 Token
            if len(content) > 800:
                content = content[:800] + "...(已截断)"
                
            results.append(f"--- 文档片段 {i+1} (来源: {source}) ---\n{content}\n")
            
        print(f"✅ [RAG Tool] 检索完成，返回 {len(results)} 个结果。")
        return "\n".join(results)
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"检索出错: {str(e)}"
