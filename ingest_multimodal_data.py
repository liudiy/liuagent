import os
import hashlib
import pickle
import json
import fitz  # PyMuPDF
import concurrent.futures
import threading
from tqdm import tqdm
from dotenv import load_dotenv
from langchain_core.documents import Document

# 导入您现有的工具
from tong_agent.sub_agents.rag_agent.vlm_pdf_parser import pdf_page_to_base64_image, parse_image_to_markdown_with_vlm
from tong_agent.sub_agents.rag_agent.llm_chunking_strategy import chunk_text_with_llm
from langchain_openai import ChatOpenAI

# 向量库
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.storage import InMemoryStore
from langchain.retrievers import ParentDocumentRetriever
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 图数据库
from langchain_neo4j import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "Tongdata")

# 向量库路径
CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db_tongdata_v4_parent_child")
STORE_PATH = os.path.join(CHROMA_DB_PATH, "docstore.pkl")

# 断点续传记录
VLM_CHECKPOINT = os.path.join(BASE_DIR, "vlm_processed_pages.json")
CHUNKING_CHECKPOINT = os.path.join(BASE_DIR, "vlm_chunking_cache.pkl")

def get_file_md5(file_path):
    """计算文件的 MD5 值用于全局去重"""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def scan_and_dedup_pdfs():
    """扫描目标目录并对 TongWEB7 进行全局去重"""
    target_products = ['TongWeb7', 'TongWeb8', 'TongRDS2', 'THS6']
    pdf_files = []
    tongweb7_hashes = set()
    
    print("🔍 开始扫描文档并进行去重...")
    for root, _, files in os.walk(DOCS_DIR):
        root_lower = root.lower()
        product_name = next((p for p in target_products if p.lower() in root_lower), None)
        
        if not product_name:
            continue
            
        for filename in files:
            if filename.lower().endswith('.pdf'):
                file_path = os.path.join(root, filename)
                
                # 针对 TongWeb7 进行全局去重
                if product_name == 'TongWeb7':
                    file_hash = get_file_md5(file_path)
                    if file_hash in tongweb7_hashes:
                        print(f"  [去重跳过] 发现重复的 TongWeb7 文件: {filename}")
                        continue
                    tongweb7_hashes.add(file_hash)
                    
                pdf_files.append((product_name, file_path))
                
    print(f"✅ 扫描完毕！共找到 {len(pdf_files)} 个有效 PDF 文件（已对 TongWeb7 去重）。")
    return pdf_files

def page_contains_graphics_or_tables(page):
    """
    启发式判断：页面是否可能包含图片或表格。
    通过检测是否有图片、或者有大量直线（绘制的表格）来决定是否调用 VLM。
    如果全是大段纯文本，可以跳过以节省 API 费用。
    """
    # 1. 检测是否有图片
    if page.get_images():
        return True
    
    # 2. 检测是否有矢量绘图（通常是表格的边框线）
    drawings = page.get_drawings()
    if len(drawings) > 5: # 如果页面上有超过5条线/矩形，极有可能是表格
        return True
        
    return False

def extract_with_vlm(pdf_files):
    """使用 VLM 提取 PDF 中的表格和图片页面（多线程版）"""
    processed_pages = {}
    if os.path.exists(VLM_CHECKPOINT):
        with open(VLM_CHECKPOINT, 'r', encoding='utf-8') as f:
            processed_pages = json.load(f)
            
    vlm_documents = []
    tasks = []
    
    print("\n� 正在扫描所有文档以筛选包含图表的页面...")
    
    # 1. 快速单线程扫描，找出需要提取的页面
    for product_name, pdf_path in tqdm(pdf_files, desc="预扫描 PDF"):
        doc_name = os.path.basename(pdf_path)
        doc = fitz.open(pdf_path)
        
        for page_num in range(len(doc)):
            page_id = f"{doc_name}_page_{page_num}"
            
            # 断点续传：已处理过的直接跳过
            if page_id in processed_pages:
                if processed_pages[page_id]: # 如果有内容
                    vlm_documents.append(Document(
                        page_content=processed_pages[page_id],
                        metadata={"source": doc_name, "page": page_num, "product": product_name, "type": "vlm_extracted"}
                    ))
                continue
                
            page = doc.load_page(page_num)
            
            # 仅处理包含图片或表格（直线）的页面
            if page_contains_graphics_or_tables(page):
                tasks.append((product_name, pdf_path, doc_name, page_num, page_id))
            else:
                processed_pages[page_id] = "" # 标记为空跳过
                
        doc.close()
        
    # 保存一次基础扫描结果
    with open(VLM_CHECKPOINT, 'w', encoding='utf-8') as f:
        json.dump(processed_pages, f, ensure_ascii=False)
        
    if not tasks:
        print(f"✅ VLM 解析已全部完成！(历史提取了 {len(vlm_documents)} 个包含图表的文档)")
        return vlm_documents
        
    print(f"\n🚀 开始多线程并发调用 VLM 解析 {len(tasks)} 个包含图表的页面...")
    
    def process_page_task(task_args):
        p_name, p_path, d_name, p_num, p_id = task_args
        # 在线程内单独读取文件并转换，避免 PyMuPDF 线程安全问题
        base64_img = pdf_page_to_base64_image(p_path, p_num)
        md_text = parse_image_to_markdown_with_vlm(base64_img)
        return p_id, md_text, p_name, d_name, p_num
        
    max_workers = 8 # 阿里云并发限制较宽松，8个线程速度直接起飞
    completed_count = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_page_task, task): task for task in tasks}
        
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(tasks), desc="VLM 并发解析进度"):
            try:
                p_id, md_text, p_name, d_name, p_num = future.result()
                processed_pages[p_id] = md_text
                
                if md_text:
                    vlm_documents.append(Document(
                        page_content=md_text,
                        metadata={"source": d_name, "page": p_num, "product": p_name, "type": "vlm_extracted"}
                    ))
                    
                # 动态保存断点
                completed_count += 1
                if completed_count % 10 == 0:
                    with open(VLM_CHECKPOINT, 'w', encoding='utf-8') as f:
                        json.dump(processed_pages, f, ensure_ascii=False)
                        
            except Exception as e:
                tqdm.write(f"❌ 解析某页面失败: {e}")
                
    # 最终保存
    with open(VLM_CHECKPOINT, 'w', encoding='utf-8') as f:
        json.dump(processed_pages, f, ensure_ascii=False)
        
    print(f"✅ VLM 并发解析完成！共提取了 {len(vlm_documents)} 个包含表格/图片的富文本文档。")
    return vlm_documents

def ingest_to_vector_store(documents):
    """将提取的高质量 Document 存入 Chroma 向量库"""
    if not documents:
        return
        
    print("\n💾 开始将 VLM 提取的内容切分并灌入向量数据库...")
    
    # 尝试加载切分缓存
    final_chunks = []
    if os.path.exists(CHUNKING_CHECKPOINT):
        try:
            with open(CHUNKING_CHECKPOINT, 'rb') as f:
                final_chunks = pickle.load(f)
            print(f"📦 发现本地切分缓存，成功加载 {len(final_chunks)} 个 Chunk，跳过 LLM 切分步骤！")
        except Exception as e:
            print(f"⚠️ 读取切分缓存失败，将重新开始切分: {e}")
            
    if not final_chunks:
        # 1. 结构化切分 (多线程加速)
        llm = ChatOpenAI(
            model="deepseek-chat",
            api_key=os.environ.get("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com",
            temperature=0
        )
        
        print("  -> 正在进行 LLM 提纲式切分 (多线程并发)...")
        
        def chunk_doc_task(doc):
            return chunk_text_with_llm(doc.page_content, doc.metadata, llm)
            
        # DeepSeek 接口控制并发数防止 429
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(chunk_doc_task, doc): doc for doc in documents}
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(documents), desc="切分进度"):
                try:
                    chunks = future.result()
                    if chunks:
                        final_chunks.extend(chunks)
                except Exception as e:
                    tqdm.write(f"❌ 切分失败: {e}")
                    
        # 保存切分结果到本地缓存
        with open(CHUNKING_CHECKPOINT, 'wb') as f:
            pickle.dump(final_chunks, f)
        print("💾 切分结果已缓存至本地。")
        
    # 2. 连接现有的向量库
    local_model_path = os.path.join(BASE_DIR, "bge-m3")
    embeddings = HuggingFaceEmbeddings(model_name=local_model_path, model_kwargs={'device': 'cpu'})
    vectorstore = Chroma(collection_name="tongdata_children", embedding_function=embeddings, persist_directory=CHROMA_DB_PATH)
    store = InMemoryStore()
    
    if os.path.exists(STORE_PATH):
        with open(STORE_PATH, "rb") as f:
            store_dict = pickle.load(f)
            store.mset(list(store_dict.items()))
            
    child_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=30)
    retriever = ParentDocumentRetriever(vectorstore=vectorstore, docstore=store, child_splitter=child_splitter)
    
    # 3. 增量写入
    docs_to_add = []
    ids_to_add = []
    for chunk in final_chunks:
        doc_hash = hashlib.md5(chunk.page_content.encode('utf-8')).hexdigest()
        if store.mget([doc_hash])[0] is None:
            docs_to_add.append(chunk)
            ids_to_add.append(doc_hash)
            
    if docs_to_add:
        print(f"  -> 正在追加 {len(docs_to_add)} 个新向量到 Chroma...")
        
        # 修复 ChromaDB max batch size 限制问题
        # ChromaDB 默认最大批次通常在 5461 左右，我们将批次设置得更小以确保安全
        batch_size = 1000
        for i in range(0, len(docs_to_add), batch_size):
            batch_docs = docs_to_add[i:i + batch_size]
            batch_ids = ids_to_add[i:i + batch_size]
            tqdm.write(f"    [Chroma 写入] 正在处理批次 {i//batch_size + 1}, 大小: {len(batch_docs)}")
            retriever.add_documents(batch_docs, ids=batch_ids)
            
        with open(STORE_PATH, "wb") as f:
            store_dict = {k: store.mget([k])[0] for k in store.yield_keys()}
            pickle.dump(store_dict, f)
        print("✅ 向量库追加完成！")
    else:
        print("  -> 所有向量已存在，无需重复追加。")
        
    return final_chunks

def ingest_to_graph_store(chunks):
    """将块写入 Neo4j 图数据库"""
    if not chunks:
        return
        
    print("\n🕸️ 开始将 VLM 提取的内容写入 Neo4j 图数据库...")
    try:
        graph = Neo4jGraph(url="bolt://localhost:7687", username="neo4j", password="password")
    except Exception as e:
        print(f"❌ 无法连接 Neo4j: {e}")
        return
        
    llm = ChatOpenAI(
        model="qwen-plus", 
        api_key=os.environ.get("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.1
    )
    
    allowed_nodes = ["Product", "Component", "ConfigurationItem", "LogFile", "Concept", "Error", "Operation", "Parameter"]
    llm_transformer = LLMGraphTransformer(llm=llm, allowed_nodes=allowed_nodes)
    
    # 图数据库的断点续传
    graph_checkpoint_file = os.path.join(BASE_DIR, "graph_vlm_checkpoint.json")
    processed_md5s = set()
    if os.path.exists(graph_checkpoint_file):
        with open(graph_checkpoint_file, 'r') as f:
            processed_md5s = set(json.load(f))
            
    docs_to_process = []
    for chunk in chunks:
        doc_md5 = hashlib.md5(chunk.page_content.encode('utf-8')).hexdigest()
        if doc_md5 not in processed_md5s:
            docs_to_process.append((doc_md5, chunk))
            
    if not docs_to_process:
        print("✅ 所有图节点已存在，无需重复抽取。")
        return
        
    print(f"  -> 需要抽取 {len(docs_to_process)} 个图谱块 (启用多线程加速)...")
    batch_size = 5
    
    # 定义 Neo4j 写入锁，防止并发写入导致死锁
    neo4j_lock = threading.Lock()
    
    def process_graph_batch(batch_tuple):
        i, batch = batch_tuple
        batch_docs = [b[1] for b in batch]
        batch_md5s = [b[0] for b in batch]
        
        try:
            # 1. 耗时的 LLM 抽取操作（不加锁，允许高并发）
            graph_documents = llm_transformer.convert_to_graph_documents(batch_docs)
            
            # 2. 快速的 Neo4j 写入操作（加锁，防止并发写冲突）
            with neo4j_lock:
                graph.add_graph_documents(graph_documents, baseEntityLabel=True, include_source=True)
                
                # 重新读取并更新断点（防止多线程写文件冲突）
                current_md5s = set()
                if os.path.exists(graph_checkpoint_file):
                    with open(graph_checkpoint_file, 'r') as f:
                        current_md5s = set(json.load(f))
                current_md5s.update(batch_md5s)
                with open(graph_checkpoint_file, 'w') as f:
                    json.dump(list(current_md5s), f)
                    
            return True, i
        except Exception as e:
            return False, e

    # 准备批次数据
    batches = []
    for i in range(0, len(docs_to_process), batch_size):
        batches.append((i, docs_to_process[i:i+batch_size]))

    # 使用多线程执行图谱抽取
    max_graph_workers = 5 # 阿里云并发限制
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_graph_workers) as executor:
        futures = [executor.submit(process_graph_batch, b) for b in batches]
        
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(batches), desc="多线程图谱抽取进度"):
            success, result = future.result()
            if success:
                tqdm.write(f"    [图谱进度] 成功写入批次 {result//batch_size + 1}")
            else:
                tqdm.write(f"    [图谱错误] 批次写入失败: {result}")

if __name__ == "__main__":
    print("🚀 开始多模态(表格/图片)增量建库流程...")
    # 1. 扫描并去重
    pdf_files = scan_and_dedup_pdfs()
    
    # 2. VLM 提取表格和图片
    vlm_docs = extract_with_vlm(pdf_files)
    
    # 3. 灌入向量库
    final_chunks = ingest_to_vector_store(vlm_docs)
    
    # 4. 灌入图数据库
    ingest_to_graph_store(final_chunks)
    
    print("\n🎉 全部多模态增量入库任务圆满完成！")
