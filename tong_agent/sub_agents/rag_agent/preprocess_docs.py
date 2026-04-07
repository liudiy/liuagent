import os
import pickle
from dotenv import load_dotenv
from langchain_core.documents import Document

# 设置 HuggingFace 镜像，防止国内网络连接超时
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def load_pdf_docs(directory_path, limit=9999):
    """
    加载指定目录下的所有 PDF 文件。
    参数: directory_path (str) - PDF 文件所在的文件夹路径
    返回: documents (list) - 包含所有 PDF 内容的文档列表
    """
    documents=[]
    count = 0
    # 我们只需要加载这四个核心产品线
    target_products = ['TongWeb7', 'TongWeb8', 'TongRDS2', 'THS6'] # 注意大小写，最好忽略大小写匹配
    
    for root,dirs,files in os.walk(directory_path):
        # 检查当前路径是否包含目标产品线名称 (忽略大小写进行匹配，防止漏掉 TongWEB7 等不同命名)
        root_lower = root.lower()
        if not any(product.lower() in root_lower for product in target_products):
            continue
            
        for filename in files:
            # 移除硬编码的过滤条件，加载目标目录下所有的 PDF 文档
            if filename.lower().endswith('.pdf'):
                if count >= limit:
                    print(f"🛑 已达到测试限制 ({limit} 个文件)，停止加载更多。")
                    return documents
                file_path = os.path.join(root, filename)
                print(f"📄 [{count+1}/{limit}] 正在使用 PyPDFLoader 加载: {filename} ...") 
                try:
                    loader = PyPDFLoader(file_path)
                    docs = loader.load()
                    documents.extend(docs)
                    count += 1
                except Exception as e:
                    print(f"加载文件 {file_path} 时出错: {e}")
    return documents
    
# 导入刚刚写的 llm_chunking_strategy
from llm_chunking_strategy import process_documents_with_llm_chunking

def chunk_docs(documents):
    """
    使用我们最新的 LLM 提纲式切分方案 (Semantic Chunking with LLM)。
    这种方法能极大地保证上下文的连贯性，并生成 title。
    """
    print(f"开始进行基于 LLM 的提纲式切分，共 {len(documents)} 页文档。")
    # 直接调用新写的逻辑，支持断点续传
    all_chunks = process_documents_with_llm_chunking(documents, save_path="llm_chunks_final.pkl", cache_path="llm_chunking_cache.pkl")
    
    print(f"切分全部完成！原始文档数: {len(documents)}, 切分后高质量片段总数: {len(all_chunks)}")
    return all_chunks

from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def generate_contextualized_chunks(chunks, checkpoint_file="contextualized_chunks_checkpoint.pkl"):
    """
    为每个 Chunk 生成上下文解释，并拼接到原始内容前面。
    支持断点续传：会读取已处理的进度，跳过已处理的 Chunk，并每处理一定数量自动保存。
    """
    
    # 1. 尝试加载之前的断点进度
    processed_results = {}
    if os.path.exists(checkpoint_file):
        try:
            with open(checkpoint_file, 'rb') as f:
                processed_results = pickle.load(f)
            print(f"✅ 成功加载断点记录！已跳过 {len(processed_results)} 个已处理的 Chunk。")
        except Exception as e:
            print(f"⚠️ 无法加载断点文件，将从头开始: {e}")
            
    llm = ChatOpenAI(
        model="deepseek-chat", 
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
        temperature=0,
        request_timeout=30 # 增加请求超时限制，防止假死
    )

    prompt = ChatPromptTemplate.from_template(
        """
        <document_context>
        以下片段来自于文档："{doc_name}"。
        </document_context>
        
        <chunk>
        {chunk_content}
        </chunk>
        
        请简要描述这段内容在整篇文档中的上下文背景，以便于检索时能更好地匹配到它。
        请只输出简练的上下文描述，不要输出其他任何内容。
        """
    )

    chain = prompt | llm | StrOutputParser()
    
    def process_chunk(chunk_data):
        i, chunk = chunk_data
        
        # 如果已经处理过，直接返回之前的结果
        if i in processed_results:
            return i, processed_results[i], True
            
        doc_name = os.path.basename(chunk.metadata.get('source', 'Unknown'))
        
        # 增加重试机制，应对偶尔的网络抖动
        max_retries = 3
        for attempt in range(max_retries):
            try:
                context = chain.invoke({
                    "doc_name": doc_name,
                    "chunk_content": chunk.page_content
                })
                # 复制一个新 chunk 避免修改原始对象导致混乱
                import copy
                new_chunk = copy.deepcopy(chunk)
                new_chunk.page_content = f"{context}\n{new_chunk.page_content}"
                return i, new_chunk, True
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"  -> 处理第 {i+1} 个 Chunk (来自 {doc_name}) 失败 (重试{max_retries}次): {e}")
                    return i, chunk, False
                time.sleep(2) # 失败后稍微等一下再试

    # 过滤出还需要处理的索引
    total_chunks = len(chunks)
    remaining_chunks_data = [(i, chunk) for i, chunk in enumerate(chunks) if i not in processed_results]
    
    if not remaining_chunks_data:
        print("所有 Chunk 都已处理完毕，无需再次调用 API！")
        return [processed_results[i] for i in range(total_chunks)]
        
    print(f"开始为剩余的 {len(remaining_chunks_data)} 个 Chunk 生成上下文 (启用多线程加速)...")
    
    # 记录最新进度
    results = [processed_results.get(i) for i in range(total_chunks)]
    completed_in_this_run = 0
    save_interval = 100  # 每处理 100 个保存一次断点
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_chunk, data): data[0] for data in remaining_chunks_data}
        
        for future in as_completed(futures):
            i, new_chunk, success = future.result()
            results[i] = new_chunk
            processed_results[i] = new_chunk
            completed_in_this_run += 1
            
            # 进度打印
            if completed_in_this_run % 10 == 0 or completed_in_this_run == len(remaining_chunks_data):
                print(f"当前运行进度: {completed_in_this_run}/{len(remaining_chunks_data)} (总进度: {len(processed_results)}/{total_chunks}) Chunks 已处理...")
                
            # 定期保存断点
            if completed_in_this_run % save_interval == 0:
                try:
                    with open(checkpoint_file, 'wb') as f:
                        pickle.dump(processed_results, f)
                except Exception as e:
                    print(f"⚠️ 保存断点失败: {e}")
                    
    # 最终跑完再存一次完整的
    with open(checkpoint_file, 'wb') as f:
        pickle.dump(processed_results, f)
        
    # 按照原始顺序返回结果
    return [results[i] for i in range(total_chunks)]


if __name__ == "__main__":
    # 使用绝对路径，确保能找到项目根目录下的 Tongdata
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))
    pdf_dir = os.path.join(project_root, "Tongdata")
    
    # 定义缓存文件路径
    raw_chunks_cache = os.path.join(current_dir, "raw_chunks_cache.pkl")
    checkpoint_file = os.path.join(current_dir, "contextualized_chunks_checkpoint.pkl")
    final_cache_file = os.path.join(current_dir, "contextualized_chunks.pkl")
    
    # 尝试加载基础切分缓存
    if os.path.exists(raw_chunks_cache):
        print(f"📦 发现本地基础切分缓存 {raw_chunks_cache}，直接加载！无需重新计算 Embedding。")
        with open(raw_chunks_cache, 'rb') as f:
            chunks = pickle.load(f)
        print(f"成功加载 {len(chunks)} 个 Chunk。")
    else:
        # 1. 加载
        print(f"开始扫描目录: {pdf_dir}")
        raw_docs = load_pdf_docs(pdf_dir)
        
        # 2. 检查加载结果
        if not raw_docs:
            print("错误：未加载到任何文档！请检查目录路径或 PDF 文件。")
            exit(1)
            
        print(f"成功加载 {len(raw_docs)} 页文档，开始切分...")
        # 3. 切分
        chunks = chunk_docs(raw_docs)
        
        # 4. 立即保存基础切分结果
        print(f"💾 正在保存基础切分结果到 {raw_chunks_cache} (防切分重跑)...")
        with open(raw_chunks_cache, 'wb') as f:
            pickle.dump(chunks, f)
            
    # 5. 生成上下文（带断点续传）
    new_chunks = generate_contextualized_chunks(chunks, checkpoint_file)
    
    # 6. 最终保存
    print(f"✅ 正在保存最终处理后的数据到 {final_cache_file} ...")
    with open(final_cache_file, 'wb') as f:
        pickle.dump(new_chunks, f)
    
    # 7. 预览
    if new_chunks:
        print("\n=== 第一个片段预览 ===")
        print(new_chunks[0].page_content[:200] + "...")
