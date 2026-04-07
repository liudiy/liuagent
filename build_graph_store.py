import os
import pickle
import hashlib
import json
import time
import concurrent.futures
import threading
from tqdm import tqdm
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer

# 兼容不同版本的 langchain 导入
from langchain_neo4j import Neo4jGraph

# 加载环境变量
load_dotenv()

CHECKPOINT_FILE = "graph_checkpoint.json"

def get_md5(text: str, source: str = "") -> str:
    """计算文本和来源的联合 MD5 值，用于断点续传。加入 source 防止不同产品文档中相同内容的段落被误杀"""
    combined_str = f"{source}_{text}"
    return hashlib.md5(combined_str.encode('utf-8')).hexdigest()

def load_checkpoint() -> set:
    """加载已处理的文档块 MD5 集合"""
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
            try:
                return set(json.load(f))
            except Exception:
                return set()
    return set()

def save_checkpoint(processed_md5s: set):
    """保存断点记录"""
    with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(processed_md5s), f)

def main():
    print("🔌 正在连接到本地 Neo4j 数据库...")
    try:
        graph = Neo4jGraph(
            url="bolt://localhost:7687", 
            username="neo4j", 
            password="password"
        )
        print("✅ 成功连接到 Neo4j！")
    except Exception as e:
        print(f"❌ 连接 Neo4j 失败，请检查数据库是否正常启动: {e}")
        return

    print("\n📦 正在加载之前切分好的文档数据 (llm_chunks_final.pkl)...")
    pkl_path = "llm_chunks_final.pkl"
    if not os.path.exists(pkl_path):
        print(f"❌ 找不到文件: {pkl_path}")
        return
        
    with open(pkl_path, 'rb') as f:
        all_chunks = pickle.load(f)
        
    # 过滤：提取 THS6, TongWEB7, TongWEB8, TongRDS2 的相关文档
    # 不再限制版本或排除特定词汇，只要是这几个产品线的统统吸纳
    target_products = ["THS", "TongWEB", "TongRDS"]
    target_chunks = []
    
    for chunk in all_chunks:
        source = chunk.metadata.get("source", "")
        # 只要文件路径中包含目标产品关键字之一，就加入待处理列表
        if any(prod in source for prod in target_products):
            target_chunks.append(chunk)
            
    print(f"🎯 过滤完毕，共有 {len(target_chunks)} 个目标产品文档块。")
    
    processed_md5s = load_checkpoint()
    print(f"🔍 读取断点记录，发现已处理过的块: {len(processed_md5s)} 个。")

    print("\n🤖 正在初始化大模型和图谱抽取器...")
    llm = ChatOpenAI(
        model="qwen-plus", 
        api_key=os.environ.get("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.1
    )
    
    # 仅使用通用的中间件实体类型，不特意偏袒 JDBC 或 SQL
    allowed_nodes = [
        "Product", "Component", "ConfigurationItem", 
        "LogFile", "Concept", "Error", "Operation", "Parameter"
    ]
    
    llm_transformer = LLMGraphTransformer(
        llm=llm,
        allowed_nodes=allowed_nodes,
        # 不限制 allowed_relationships，让大模型自由发现“依赖”、“导致”、“配置于”等关系
    )
    
    import concurrent.futures

    # 批量处理参数
    batch_size = 5
    max_workers = 5  # 阿里云并发限制
    total_processed_this_run = 0
    
    print("\n🚀 开始执行图谱抽取与增量入库...")
    
    # 过滤出真正需要处理的块（未存在于断点中的块），并且在此处进行去重，避免处理相同内容的块
    pending_chunks = []
    seen_in_this_run = set()
    
    # 统计有多少个块是因为 MD5 重复（相同内容）被跳过的，有多少是因为已处理被跳过的
    duplicate_count = 0
    already_processed_count = 0
    
    for doc in target_chunks:
        # 使用内容 + 文件来源 计算联合 MD5，这样不同文档里相同的句子（比如免责声明）也会被分别提取并关联到正确的文档来源
        doc_md5 = get_md5(doc.page_content, doc.metadata.get("source", ""))
        if doc_md5 in processed_md5s:
            already_processed_count += 1
        elif doc_md5 in seen_in_this_run:
            duplicate_count += 1
        else:
            pending_chunks.append(doc)
            seen_in_this_run.add(doc_md5)
            
    print(f"📦 分析完成：已处理 {already_processed_count} 个，本次去重丢弃 {duplicate_count} 个完全重复的块。")
    print(f"📦 本次共有 {len(pending_chunks)} 个全新的文档块需要处理。")
    
    if not pending_chunks:
        print("🎉 所有文档都已处理完毕，无需重复提取！")
        return

    # 定义 Neo4j 写入锁，防止并发写入导致死锁
    neo4j_lock = threading.Lock()
    
    def process_graph_batch(batch_tuple):
        i, batch_docs = batch_tuple
        batch_md5s = [get_md5(d.page_content, d.metadata.get("source", "")) for d in batch_docs]
        
        try:
            # 1. 耗时的 LLM 抽取操作（不加锁，允许高并发）
            graph_documents = llm_transformer.convert_to_graph_documents(batch_docs)
            
            # 2. 快速的 Neo4j 写入操作（加锁，防止并发写冲突）
            with neo4j_lock:
                graph.add_graph_documents(graph_documents, baseEntityLabel=True, include_source=True)
                
                # 重新读取并更新断点（防止多线程写文件冲突）
                current_md5s = set()
                if os.path.exists(CHECKPOINT_FILE):
                    with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
                        try:
                            current_md5s = set(json.load(f))
                        except Exception:
                            pass
                current_md5s.update(batch_md5s)
                with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
                    json.dump(list(current_md5s), f)
                    
            return True, i, len(batch_docs), None
        except Exception as e:
            return False, i, 0, str(e)

    # 准备批次数据
    batches = []
    for i in range(0, len(pending_chunks), batch_size):
        batches.append((i, pending_chunks[i:i+batch_size]))

    # 使用多线程执行图谱抽取
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_graph_batch, b) for b in batches]
        
        with tqdm(total=len(pending_chunks), desc="多线程图谱抽取进度", unit="块") as pbar:
            for future in concurrent.futures.as_completed(futures):
                success, i, processed_count, err_msg = future.result()
                if success:
                    total_processed_this_run += processed_count
                    pbar.update(processed_count)
                else:
                    pbar.write(f"    [图谱错误] 批次写入失败: {err_msg}")
                    time.sleep(2)
    print(f"\n🎉 运行结束！本次共新处理并入库了 {total_processed_this_run} 个文档块。")

if __name__ == "__main__":
    main()
