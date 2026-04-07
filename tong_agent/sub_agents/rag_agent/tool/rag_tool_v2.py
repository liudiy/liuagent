try:
    from langchain.retrievers import EnsembleRetriever
except ImportError:
    try:
        from langchain.retrievers.ensemble import EnsembleRetriever
    except ImportError:
        try:
            from langchain_community.retrievers import EnsembleRetriever
        except ImportError:
            try:
                # 尝试从 langchain_classic 导入
                from langchain_classic.retrievers import EnsembleRetriever
            except ImportError:
                print("❌ Critical Warning: EnsembleRetriever not found in any known location!")
                EnsembleRetriever = None

from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever
# 不再使用 langchain.retrievers，直接使用 MultiVectorRetriever 的等效逻辑
from langchain_core.retrievers import BaseRetriever
from langchain_core.stores import InMemoryStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pickle
import os
import torch

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from sentence_transformers import CrossEncoder

_cached_embedding = None
_cached_retriever = None
_cached_reranker = None
_cached_rewriting_llm = None
_cached_keyword_extraction_llm = None
_cached_query_analysis_llm = None
_cached_graph = None

def get_graph():
    global _cached_graph
    if not _cached_graph:
        try:
            from langchain_neo4j import Neo4jGraph
            _cached_graph = Neo4jGraph(url="bolt://localhost:7687", username="neo4j", password="password")
            print("✅ 成功连接到 Neo4j 知识图谱！")
        except Exception as e:
            print(f"❌ Neo4j 连接失败，图谱检索将被禁用: {e}")
            _cached_graph = None
    return _cached_graph

# 硬编码的同义词/实体扩展字典
SYNONYM_DICT = {
    "ths": ["THS", "TongHttpServer", "Tong Http Server"],
    "tongweb": ["TongWeb", "东方通应用服务器", "TongWeb7", "TongWeb8"],
    "rds": ["TongRDS", "RDS", "东方通缓存", "分布式缓存数据库"],
    "ths6": ["THS", "THS6", "TongHttpServer V6.0"],
    "tw": ["TongWeb"],
    "等保": ["等保", "等级保护", "安全配置"],
}

def expand_keywords(keywords: str) -> list:
    """
    根据实体字典扩展关键词，增加图谱匹配的命中率
    """
    kw_list = [k.strip() for k in keywords.split() if len(k.strip()) > 1]
    expanded_list = set(kw_list)
    
    for kw in kw_list:
        kw_lower = kw.lower()
        if kw_lower in SYNONYM_DICT:
            expanded_list.update(SYNONYM_DICT[kw_lower])
            
    return list(expanded_list)

def retrieve_from_graph(keywords: str) -> str:
    """
    利用提取的关键词在 Neo4j 图谱中进行子图匹配，召回相关实体及其 1 跳关系
    """
    graph = get_graph()
    if not graph:
        return ""
        
    # 执行实体扩展
    kw_list = expand_keywords(keywords)
    print(f"🔗 实体扩展后关键词: {kw_list}")
    
    if not kw_list:
        return ""
        
    # 优化点：
    # 1. 先匹配含关键词的节点，再扩展两跳邻居（平衡关联深度与信噪比）
    # 2. 去重源头节点 (WITH DISTINCT)
    # 3. 使用路径模式匹配多跳关系，并提取路径上的所有关系和节点
    cypher = """
    UNWIND $keywords AS kw
    MATCH (node)
    WHERE toLower(node.id) CONTAINS toLower(kw)
    WITH DISTINCT node
    // 扩展 1 到 2 跳的路径
    MATCH path = (node)-[*1..2]-(neighbor)
    // 提取路径中的所有关系
    UNWIND relationships(path) AS r
    WITH DISTINCT r
    RETURN 
      startNode(r).id AS source, 
      type(r) AS rel, 
      endNode(r).id AS target
    LIMIT 100
    """
    try:
        res = graph.query(cypher, params={"keywords": kw_list})
        if not res:
            return ""
            
        triplets = set()
        for row in res:
            source = row["source"] or ""
            rel = row["rel"] or ""
            target = row["target"] or ""
            triplets.add(f"({source}) -[{rel}]-> ({target})")
            
        if triplets:
            return "--- 图谱关联知识 (Graph Context) ---\n" + "\n".join(list(triplets)) + "\n"
        return ""
    except Exception as e:
        print(f"❌ 图谱检索执行错误: {e}")
        return ""

class QueryAnalysis(BaseModel):
    sub_queries: List[str] = Field(description="将复杂的用户问题拆解为 1 到 3 个独立的子问题。如果原问题很简单，列表中只包含原问题。")
    product_filter: str = Field(description="用户提到的具体产品核心名称，仅限于：'TongWeb', 'TongRDS', 'THS', 'TongHttpServer'。如果没有明确提到，返回空字符串。")

async def aanalyze_query(query: str) -> dict:
    """
    异步分析查询：拆解复杂查询并提取产品过滤词
    """
    global _cached_query_analysis_llm
    if not _cached_query_analysis_llm:
        _cached_query_analysis_llm = ChatOpenAI(
            model="qwen-turbo", 
            api_key=os.environ.get("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.1
        )
    
    parser = JsonOutputParser(pydantic_object=QueryAnalysis)
    prompt = PromptTemplate(
        template="你是一个高级检索分析专家。你需要对用户的查询进行分析：\n"
                 "1. **查询拆解**：如果用户的查询包含多个问题，或者是一个非常复杂的问题，请将其拆解为 1-3 个具体的子问题。如果问题简单，直接返回原问题作为唯一的子问题。\n"
                 "2. **元数据过滤**：判断用户查询中是否明确提到了特定的产品。目前支持的产品有：'TongWeb', 'TongRDS', 'THS', 'TongHttpServer'。如果提到了，请提取出最匹配的产品核心名称，如果没有提到，或者询问的是多个产品的对比，请返回空字符串。\n\n"
                 "{format_instructions}\n\n"
                 "用户查询: {query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    chain = prompt | _cached_query_analysis_llm | parser
    return await chain.ainvoke({"query": query})


async def aquery_rewriting(query: str) -> str:
    """
    异步对用户查询进行重写，以提高检索效果。
    """
    global _cached_rewriting_llm
    if not _cached_rewriting_llm:
        _cached_rewriting_llm = ChatOpenAI(
            model="qwen-turbo", 
            api_key=os.environ.get("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.5
        )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """你是一个资深的技术专家。用户提出了一项技术问题，请你根据你的专业知识，写一段能够直接回答该问题的【假设性官方文档片段】。
注意：即使你不确定准确的具体参数或数值，也请写出相关的专业术语、可能的配置项名称，以及官方文档中常见的句式结构。
请直接输出这段假设性的文档内容，不要包含任何解释性语言。"""),
        ("human", "用户问题：{query}\n假设性文档片段：")
    ])
    output_parser = StrOutputParser()
    chain = prompt | _cached_rewriting_llm | output_parser
    return await chain.ainvoke({"query": query})

async def akeyword_extraction(query: str) -> str:
    """
    异步从用户查询中提取关键词，用于后续的检索。
    """
    global _cached_keyword_extraction_llm
    if not _cached_keyword_extraction_llm:
        _cached_keyword_extraction_llm = ChatOpenAI(
            model="qwen-turbo", 
            api_key=os.environ.get("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.5
        )
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的关键词提取器。用户会输入一个查询，你需要提取出查询中的主要名词、专有名词、报错代码或文件名。请仅以空格分隔返回这些关键词，不要包含其他任何解释性文字。"),
        ("human", "查询：{query}\n关键词：")
    ])
    output_parser = StrOutputParser()
    chain = prompt | _cached_keyword_extraction_llm | output_parser
    return await chain.ainvoke({"query": query})

def get_parent_dir(path, levels=1):
    """
    获取指定路径向上 N 级的父目录
    :param path: 基础路径（如 __file__）
    :param levels: 向上回溯的层级数
    :return: 回溯后的父目录路径
    """
    parent_dir = os.path.dirname(path)
    for _ in range(levels - 1):
        parent_dir = os.path.dirname(parent_dir)
    return parent_dir


BASE_DIR = get_parent_dir(__file__, levels=5) 
CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db_tongdata_v4_parent_child")
MODEL_PATH = os.path.join(BASE_DIR, "bge-large-zh-v1.5")

def get_embeddings():
    global _cached_embedding
    if not _cached_embedding:
        # 使用 os.environ 动态设置 HuggingFace 镜像源，防止国内服务器下载失败
        import os
        os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
        print("🚀 Loading Embedding Model...")
        try:
            _cached_embedding = HuggingFaceEmbeddings(
                model_name=MODEL_PATH,
                model_kwargs={"device": "cpu"}, 
                encode_kwargs={"normalize_embeddings": True},
            )
            print("DEBUG: rag_tool_v2.py: Embedding 模型加载成功")
        except Exception as e:
            print(f"❌ Error loading Embedding model: {e}")
            _cached_embedding = None
    return _cached_embedding

def vector_vectorstore():
    """
    初始化并返回 Chroma 向量数据库 (使用 BGE-M3)。
    """
    global _cached_embedding
    if _cached_embedding is None:
        print("Loading BAAI/bge-m3 Embedding Model (使用 GPU 加速)...")
        # 经测试，RTX 5070 (sm_120) 需要 PyTorch 2.12 nightly 版本 (目前过大且下载超时)
        # 当前 PyTorch 2.6.0 不支持 sm_120，因此退回使用 CPU 确保流程顺利跑通
        local_model_path = os.path.join(BASE_DIR, "bge-m3")
        _cached_embedding = HuggingFaceEmbeddings(
            model_name=local_model_path,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
    return Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=_cached_embedding, collection_name="tongdata_children")

BM25_INDEX_PATH = os.path.join(BASE_DIR, "bm25_retriever.pkl")

def create_bm25_Retriever(vectorstore):
    if os.path.exists(BM25_INDEX_PATH):
        # Remove floppy disk emoji to avoid decoding issues
        print("Loading BM25 Index from disk...")
        try:
            with open(BM25_INDEX_PATH, 'rb') as f:
                bm25_retriever = pickle.load(f)
                print("✅ BM25 Index loaded successfully.")
                return bm25_retriever
        except Exception as e:
            print(f"❌ Failed to load BM25 Index from disk: {e}")
            # 如果加载失败，不返回 None，而是继续走重建流程
    
    print("Initializing BM25 Retriever from vectorstore documents...")
    
    # 修复 ChromaDB 大数据量下的 too many SQL variables 错误：分批获取数据
    all_documents = []
    all_metadatas = []
    limit = 5000
    offset = 0
    while True:
        batch_data = vectorstore.get(limit=limit, offset=offset)
        if not batch_data['documents']:
            break
        all_documents.extend(batch_data['documents'])
        all_metadatas.extend(batch_data['metadatas'])
        offset += limit
        print(f"  Loaded {len(all_documents)} documents from ChromaDB...")
        
    doc_objects = []
    for doc, meta in zip(all_documents, all_metadatas):
        doc_objects.append(Document(page_content=doc, metadata=meta))
    
    if not doc_objects:
        return None
    
    bm25_retriever = BM25Retriever.from_documents(doc_objects)
    # Remove floppy disk emoji to avoid decoding issues
    print("Saving BM25 Index to disk...")
    with open(BM25_INDEX_PATH, "wb") as f:
        pickle.dump(bm25_retriever, f)
    print("BM25 Retriever initialized.")
    return bm25_retriever


# 恢复使用 ParentDocumentRetriever
from langchain.retrievers import ParentDocumentRetriever
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.storage import InMemoryStore

_cached_vector_retriever = None
_cached_bm25_retriever = None
_cached_store = None

def get_base_retrievers():
    global _cached_vector_retriever, _cached_bm25_retriever, _cached_store
    if not _cached_vector_retriever:
        vectorstore = vector_vectorstore()
        
        # 挂载父文档存储库
        store_path = os.path.join(CHROMA_DB_PATH, "docstore.pkl")
        _cached_store = InMemoryStore()
        if os.path.exists(store_path):
            # Remove floppy disk emoji to avoid decoding issues
            print(f"Loading Parent Docstore from {store_path}...")
            try:
                with open(store_path, "rb") as f:
                    store_dict = pickle.load(f)
                    _cached_store.mset(list(store_dict.items()))
            except Exception as e:
                print(f"❌ Failed to load docstore: {e}")
        else:
            print("⚠️ 警告: 未找到 docstore.pkl，无法返回完整的父文档内容。")
            
        # 恢复使用原生的 ParentDocumentRetriever
        child_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=30)
        _cached_vector_retriever = ParentDocumentRetriever(
            vectorstore=vectorstore,
            docstore=_cached_store,
            child_splitter=child_splitter,
        )
        
        _cached_bm25_retriever = create_bm25_Retriever(vectorstore)
        if _cached_bm25_retriever:
            _cached_bm25_retriever.k = 10
    return _cached_vector_retriever, _cached_bm25_retriever

def get_reranker():
    global _cached_reranker
    if not _cached_reranker:
        import os
        # 设置更可靠的国内镜像源和代理
        os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
        
        # 针对 Windows + PyTorch + xdist 并发的致命问题，强制使用 CPU，并禁用 PyTorch 多线程
        import torch
        torch.set_num_threads(1)
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["MKL_NUM_THREADS"] = "1"
        
        device = "cpu"
        
        # 禁用重排时打印的进度条那么多文字，影响终端观感
        import logging
        logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
        
        print(f"Loading Reranker Model BAAI/bge-reranker-v2-m3 (device: {device})...")
        try:
            # 尝试加载模型，显式设置 local_files_only 防止并发下载导致的文件锁
            _cached_reranker = CrossEncoder("BAAI/bge-reranker-v2-m3", device=device, max_length=512)
            print("✅ Reranker model loaded successfully!")
        except Exception as e:
            print(f"❌ Failed to load reranker model, disabling reranking: {e}")
            _cached_reranker = "DISABLED"
    return _cached_reranker


import asyncio

@tool
def retrieve_middleware_docs(query: str):
    """
    混合检索工具，用于根据查询字符串检索文档。
    内部集成了 Query Rewriting (HyDE) 以提升检索效果。
    :param query: 查询字符串
    :return: 检索到的文档列表
    """
    # 获取一个新的事件循环（因为工具可能在同步上下文中被调用，但我们内部想用异步并发）
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    vector_retriever, bm25_retriever = get_base_retrievers()
    
    print(f"🔍 原始查询: {query}")
    
    # 1. & 2. 并发执行：分析查询(拆解与过滤)、关键词提取、查询重写(HyDE)
    async def gather_rewrites():
        analysis_task = aanalyze_query(query)
        kw_task = akeyword_extraction(query)
        rw_task = aquery_rewriting(query)
        return await asyncio.gather(analysis_task, kw_task, rw_task)
    
    try:
        if loop.is_running():
            # 如果已经在异步上下文中运行，直接创建任务，并等待（需要外层也是异步，但 tool 默认是同步的）
            # langchain 工具支持 async def，但为了兼容现有的 graph，我们用同步转异步的 hack
            import nest_asyncio
            nest_asyncio.apply()
            analysis, keywords, rewritten_query = loop.run_until_complete(gather_rewrites())
        else:
            analysis, keywords, rewritten_query = loop.run_until_complete(gather_rewrites())
            
        print(f"🔑 提取关键词: {keywords}")
        print(f"✨ 重写后查询 (HyDE):\n{rewritten_query}")
        
        sub_queries = analysis.get("sub_queries", [query])
        product_filter = analysis.get("product_filter", "")
        # print(f"🧩 查询拆解: {sub_queries}")
        # print(f"🎯 提取过滤器: {product_filter}")
        
    except Exception as e:
        print(f"⚠️ 并发分析与重写失败，退回使用原始查询。错误: {e}")
        keywords = query
        rewritten_query = ""
        sub_queries = [query]
        product_filter = ""
        
    # 3. 分别执行检索
    print("⏳ 正在执行三路混合检索 (Vector + BM25 + Graph)...")
    
    # 执行图谱检索
    graph_context = retrieve_from_graph(keywords)
    if graph_context:
        print("✅ 图谱检索成功，发现相关节点和关系！")
    
    # 动态应用前置过滤器 (Pre-filtering)
    # 注意: ChromaDB 对于 metadata 的 where 过滤不支持 $contains，只支持 $eq, $in 等。
    # 因为我们的 source 是全路径，无法直接 $eq，所以我们采取后置过滤的方式。
    # 为了保证过滤后的数量，我们适当增加底层的检索 k 值，工业级推荐 50-100
    vector_retriever.search_kwargs = {"k": 50}
    if _cached_bm25_retriever:
        _cached_bm25_retriever.k = 50
        
    # 执行 Vector 检索 (Query Decomposition: 对每个子问题执行检索，并将 HyDE 结果作为额外查询)
    vector_docs_raw = []
    # 【优化】不硬性截断，而是限制最大拆解数到 5，并在循环中添加极短的休眠，防止 ChromaDB SQLite 并发锁死
    queries_to_search = sub_queries[:5] 
    if rewritten_query:
        # 将 HyDE 生成的假设性文档也加入向量检索池
        queries_to_search.append(rewritten_query[:500]) # 截断避免太长
    
    for sq in queries_to_search:
        try:
            print(f"  -> Vector 正在检索: {sq[:50]}...")
            docs = vector_retriever.invoke(sq)
            vector_docs_raw.extend(docs)
            import time
            time.sleep(0.1) # 缓解 SQLite 锁争用
        except Exception as e:
            print(f"❌ Vector 检索失败: {e}")
            
    # 统一父文档还原函数 (解决隐患一)
    def restore_parent_docs(docs_raw):
        restored = []
        seen = set()
        for d in docs_raw:
            doc_id = d.metadata.get("doc_id")
            # 如果存在 doc_id 且挂载了内存存储，尝试还原为父文档
            if doc_id and _cached_store:
                parent = _cached_store.mget([doc_id])[0]
                if parent:
                    # 兼容不同存储格式，将当前 chunk 的内容替换为完整父文档内容
                    if hasattr(parent, 'page_content'):
                        d = Document(page_content=parent.page_content, metadata=d.metadata)
                    elif hasattr(parent, 'decode'):
                        try:
                            d = Document(page_content=parent.decode('utf-8'), metadata=d.metadata)
                        except UnicodeDecodeError:
                            # 尝试使用 GBK 解码
                            try:
                                d = Document(page_content=parent.decode('gbk'), metadata=d.metadata)
                            except Exception:
                                d = Document(page_content=str(parent), metadata=d.metadata)
                    else:
                        d = Document(page_content=str(parent), metadata=d.metadata)
            
            # 使用全文的 MD5 进行去重，确保完全相同的父文档不被重复添加
            import hashlib
            try:
                # 处理由于奇怪的字符导致的 encode 失败
                content_bytes = d.page_content.encode('utf-8', errors='ignore')
            except Exception:
                content_bytes = str(d.page_content).encode('utf-8', errors='ignore')
                
            doc_hash = hashlib.md5(content_bytes).hexdigest()
            if doc_hash not in seen:
                seen.add(doc_hash)
                restored.append(d)
        return restored

    # Vector 手动应用前置过滤器
    if product_filter:
        vector_docs_raw = [d for d in vector_docs_raw if product_filter.lower() in d.metadata.get('source', '').lower()]
        
    # 对 Vector 检索结果进行父文档还原和去重
    vector_docs = restore_parent_docs(vector_docs_raw)
            
    # 执行 BM25 检索
    bm25_docs_raw = []
    if bm25_retriever and keywords:
        try:
            print(f"  -> BM25 正在检索关键词: {keywords[:50]}...")
            bm25_docs_raw = bm25_retriever.invoke(keywords)
        except Exception as e:
            print(f"❌ BM25 检索失败: {e}")
            
        # BM25 手动应用前置过滤器
        if product_filter:
            bm25_docs_raw = [d for d in bm25_docs_raw if product_filter.lower() in d.metadata.get('source', '').lower()]
            
    # 去重并恢复 BM25 的父文档
    bm25_docs = restore_parent_docs(bm25_docs_raw)
    
    # 4. 手动实现 RRF (Reciprocal Rank Fusion) 融合
    def calculate_rrf(retriever_results: list, k_constant: int = 60) -> list:
        """
        计算 RRF 融合分数
        :param retriever_results: 格式为 [(docs, weight), (docs, weight)]
        :param k_constant: RRF 平滑常数，业界标准推荐 60
        """
        import hashlib
        rrf_scores = {}
        
        for docs, weight in retriever_results:
            for rank, doc in enumerate(docs):
                # 修复隐患二：Hash 碰撞，使用完整的文档内容 MD5 作为唯一键
                try:
                    content_bytes = doc.page_content.encode('utf-8', errors='ignore')
                except Exception:
                    content_bytes = str(doc.page_content).encode('utf-8', errors='ignore')
                    
                doc_hash = hashlib.md5(content_bytes).hexdigest()
                doc_id = f"{doc.metadata.get('source', '')}_{doc_hash}"
                
                if doc_id not in rrf_scores:
                    rrf_scores[doc_id] = {"doc": doc, "score": 0.0}
                
                # rank 从 0 开始，所以公式是 1 / (rank + 1 + k_constant)
                rrf_scores[doc_id]["score"] += weight * (1.0 / (rank + 1 + k_constant))
                
        # 根据 RRF 分数倒序排列
        sorted_results = sorted(rrf_scores.values(), key=lambda x: x["score"], reverse=True)
        return [item["doc"] for item in sorted_results]

    # 执行融合 (BM25 权重 0.4, Vector 权重 0.6)
    docs = calculate_rrf([
        (bm25_docs, 0.4),
        (vector_docs, 0.6)
    ])
    
    # [优化] 取前 40 个结果进行重排序，增加召回兜底
    final_docs = docs[:40]

    reranker = get_reranker()
    if reranker == "DISABLED":
        print("⚠️ 重排序模型未启用，将直接返回合并后的结果。")
        reank_docs = final_docs[:5]
    else:
        print(f"正在使用 BGE-M3 进行重排序，候选文档数量: {len(final_docs)}...")
        try:
            # Reranking 逻辑: 修复隐患三 (截断截杀)
            # 对于极长的父文档，如果只送给 Reranker，它只会看前 512 token，导致包含在文档末尾的正确答案被忽略
            # 改进：我们只让 Reranker 对 Query 和 "文档开头部分+文档末尾部分" 进行打分，或者直接使用 LangChain 默认行为
            # 由于重排序模型非常敏感，为了防止长父文档被打低分，我们提取可能包含关键字的片段送去打分
            pairs = []
            for doc in final_docs:
                content = doc.page_content
                # 如果文档很长，取开头和结尾拼接（通常开头有定义，结尾有配置）
                if len(content) > 1000:
                    eval_content = content[:500] + "\n...\n" + content[-500:]
                else:
                    eval_content = content
                pairs.append([query, eval_content])
                
            scores = reranker.predict(pairs)
            sorted_docs = sorted(zip(final_docs, scores), key=lambda x: x[1], reverse=True)
            # 即使重排序成功，也多返回一些结果，避免只返回 5 条时丢失关键信息
            reank_docs = [doc for doc, score in sorted_docs[:8]]
        except Exception as e:
            print(f"\u274c 重排序过程发生错误: {e}，回退到未排序结果")
            reank_docs = final_docs[:10]  # 如果重排序失败，多返回一些让大模型自己挑
    
    # 如果没有检索到任何文档，并且也没有图谱上下文，则返回明确的提示
    if not reank_docs and not graph_context:
        return "未找到相关文档，请尝试更换关键词。"
        
    formatted_results = []
    
    # 优先加入图谱上下文作为第一参考信息
    if graph_context:
        formatted_results.append(graph_context)
        
    for i,doc in enumerate(reank_docs):
        source = os.path.basename(doc.metadata.get("source", "未知来源"))
        # 提取所有可用的元数据信息
        title = doc.metadata.get("title", "未知章节")
        page = doc.metadata.get("page", "未知页码")
        category = doc.metadata.get("category", "")
        product = doc.metadata.get("product", "")
        
        content = doc.page_content.strip()
        # 截断过长的文档片段，防止 Token 溢出，提高上限给模型更多上下文
        # 以前只保留了前 1500 字，这会导致文档末尾的配置代码被无情切掉！
        # 修改为：保留前 1000 字和后 1000 字，中间截断
        if len(content) > 2000:
            content = content[:1000] + "\n\n...[内容过长，中间已截断]...\n\n" + content[-1000:]
            
        # 构建元数据标签字符串
        meta_tags = []
        if product: meta_tags.append(f"产品: {product}")
        if category: meta_tags.append(f"类别: {category}")
        meta_tags.append(f"标题/章节: {title}")
        meta_tags.append(f"页码: 第 {page} 页")
        
        meta_str = ", ".join(meta_tags)
            
        # 增强输出格式，包含所有有价值的定位信息
        formatted_results.append(f"--- 来源文档: {source} ({meta_str}) ---\n相关内容:\n{content}\n")
        
    result_str = "\n".join(formatted_results)
    if not result_str.strip():
        return "未找到相关文档。"
        
    return result_str
