import os
import shutil
import pickle
import hashlib
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from preprocess_docs import load_pdf_docs, chunk_docs
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.storage import InMemoryStore
from langchain.retrievers import ParentDocumentRetriever

# 1. 确定原始文档路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
DOCS_DIR = os.path.join(BASE_DIR, "Tongdata")

# 2. 向量数据库持久化路径 (升级为 v4_parent_child 以构建全新库)
CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db_tongdata_v4_parent_child")
STORE_PATH = os.path.join(CHROMA_DB_PATH, "docstore.pkl")

def build_parent_child_store():
    # 步骤 1: 加载并切分文档
    print("开始加载文档...")
    documents = load_pdf_docs(DOCS_DIR) 
    if not documents:
        print("没有找到文档，请检查路径。")
        return
        
    print(f"成功加载 {len(documents)} 页文档。")
    
    # 步骤 2: 调用 preprocess_docs.py 中新的 chunk_docs (LLM Semantic Chunking)
    # 内部自带断点续传机制
    print("开始执行大模型提纲式切分 (生成高质量父文档)...")
    parent_documents = chunk_docs(documents)
    
    # 步骤 3: 初始化 Embeddings
    print("正在加载 BAAI/bge-m3 Embedding 模型 (使用 GPU 加速)...")
    # 我们已经通过脚本将其下载到了根目录的 bge-m3 文件夹中，避免缓存损坏问题
    # 经测试，RTX 5070 (sm_120) 需要 PyTorch 2.12 nightly 版本 (目前过大且下载超时)
    # 当前 PyTorch 2.6.0 不支持 sm_120，因此退回使用 CPU 确保流程顺利跑通
    local_model_path = os.path.join(BASE_DIR, "bge-m3")
    embeddings = HuggingFaceEmbeddings(
        model_name=local_model_path,
        model_kwargs={'device': 'cpu'}, 
        encode_kwargs={'normalize_embeddings': True} 
    )

    # 步骤 4: 构建 Parent-Child 架构 (移除每次强制删除的逻辑，改为断点续传)
    print(f"正在构建或加载 Parent-Child Retriever (路径: {CHROMA_DB_PATH})...")
    
    vectorstore = Chroma(
        collection_name="tongdata_children",
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_PATH
    )
    
    store = InMemoryStore()
    
    # 尝试加载已有的 docstore.pkl 以实现断点续传
    if os.path.exists(STORE_PATH):
        try:
            with open(STORE_PATH, "rb") as f:
                store_dict = pickle.load(f)
                store.mset(list(store_dict.items()))
            print(f"✅ 成功加载断点缓存！已存在 {len(store_dict)} 个父文档。")
        except Exception as e:
            print(f"⚠️ 无法加载 docstore.pkl，将从头开始: {e}")

    child_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=30)
    
    retriever = ParentDocumentRetriever(
        vectorstore=vectorstore,
        docstore=store,
        child_splitter=child_splitter,
    )
    
    # 步骤 5: 断点续传灌入数据
    print("正在计算 Embedding 并灌入数据...")
    
    docs_to_add = []
    ids_to_add = []
    
    for doc in parent_documents:
        # 使用文档内容的 MD5 作为唯一 ID
        doc_hash = hashlib.md5(doc.page_content.encode('utf-8')).hexdigest()
        
        # 检查是否已经在 docstore 中
        if store.mget([doc_hash])[0] is not None:
            continue
            
        docs_to_add.append(doc)
        ids_to_add.append(doc_hash)
        
    if not docs_to_add:
        print("所有文档都已在数据库中，无需新增 Embedding！")
        return
        
    print(f"发现 {len(docs_to_add)} 个新文档需要进行 Embedding。")
    
    # 分批次写入，每 50 个父文档保存一次断点
    batch_size = 50
    total_batches = (len(docs_to_add) + batch_size - 1) // batch_size
    
    for i in range(total_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, len(docs_to_add))
        
        batch_docs = docs_to_add[start_idx:end_idx]
        batch_ids = ids_to_add[start_idx:end_idx]
        
        print(f"  -> 正在处理第 {i+1}/{total_batches} 批次 (文档 {start_idx+1} 到 {end_idx})...")
        retriever.add_documents(batch_docs, ids=batch_ids)
        
        # 每次批次处理完，持久化一次 docstore.pkl
        with open(STORE_PATH, "wb") as f:
            store_dict = {k: store.mget([k])[0] for k in store.yield_keys()}
            pickle.dump(store_dict, f)
            
    print(f"✅ 向量数据库及 Parent-Child 映射已成功构建并保存在: {CHROMA_DB_PATH}")

if __name__ == "__main__":
    build_parent_child_store()