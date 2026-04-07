import os
import pickle
import json
from dotenv import load_dotenv
from typing import List

# 设置 HuggingFace 镜像
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
load_dotenv()

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

# --- 1. 定义 Pydantic 结构 ---
class Chunk(BaseModel):
    title: str = Field(description="这个知识块的简短标题，必须能概括核心内容，比如 '配置数据库连接池' 或 '解决 JDBC Connection 报错'")
    content: str = Field(description="完整的段落内容，确保不要遗漏任何原文细节")
    hypothetical_questions: List[str] = Field(description="生成 3-5 个用户可能会如何提问来寻找这段内容的自然语言问题。例如：'TongWeb 怎么配置最大连接数？'")
    category: str = Field(description="对该段内容的分类。可选值：'配置说明', '故障排查', '架构原理', '安装部署', '其他'")
    
class ChunkResult(BaseModel):
    chunks: List[Chunk] = Field(description="切分后的知识块列表")

# --- 2. 基于 LLM 的提纲式切分逻辑 ---
def chunk_text_with_llm(text: str, doc_metadata: dict, llm) -> List[Document]:
    """
    使用 LLM 和 Pydantic 将长文本切分为带有 Title、假设性问题和分类的独立逻辑块。
    返回 LangChain Document 列表。
    """
    prompt = ChatPromptTemplate.from_template(
        """
        你是一个专业的中间件（TongWeb）文档结构化与 RAG 优化专家。
        请阅读以下长文本，并根据其内在逻辑、语义连贯性将其拆分为多个独立的知识块。
        
        要求：
        1. 确保每个知识块都是一个完整的逻辑单元。
        2. 绝对不要遗漏原文的任何细节，代码、表格内容等必须完整保留在 content 中。
        3. 必须为每个知识块起一个准确的 title。
        4. 必须为每个知识块生成 3-5 个假设性问题 (hypothetical_questions)，模拟用户的真实口语化提问。
        5. 为该知识块打上分类标签 (category)。
        
        待切分文本：
        {text_chunk}
        """
    )
    
    # 绑定结构化输出
    structured_llm = llm.with_structured_output(ChunkResult)
    chain = prompt | structured_llm
    
    # 增加重试机制，应对 JSON 解析错误 (如包含非法的转义字符)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            # 清理文本中的非法转义字符，防止 LLM 生成错误的 JSON 导致 pydantic 解析失败
            clean_text = text.replace('\\', '\\\\')
            result: ChunkResult = chain.invoke({"text_chunk": clean_text})
            
            documents = []
            for chunk in result.chunks:
                # 提取原始 metadata 的信息
                source_file = doc_metadata.get("source", "unknown_source")
                
                # 提取产品线和版本号 (假设你的文件路径或文件名里包含这些信息，比如 TongWeb7.0_Manual.pdf)
                # 这是一个简单的启发式提取，你也可以让 LLM 去提取
                product = "Unknown"
                if "tongweb7" in source_file.lower() or "tongweb_v7" in source_file.lower(): product = "TongWeb7"
                elif "tongweb8" in source_file.lower() or "tongweb_v8" in source_file.lower(): product = "TongWeb8"
                elif "ths" in source_file.lower(): product = "THS"
                elif "rds" in source_file.lower(): product = "TongRDS"
                
                # 组装新的 metadata
                new_metadata = doc_metadata.copy()
                new_metadata.update({
                    "title": chunk.title,
                    "category": chunk.category,
                    "product": product,
                    "hypothetical_questions": " | ".join(chunk.hypothetical_questions) # 将列表转为字符串存储
                })
                
                # 为了让检索时能被命中，我们将假设性问题拼接在 content 的前面或后面
                # 这样即使用户问得很口语化，也能通过假设性问题命中这段文本
                enhanced_content = (
                    f"【可能的问题】：\n"
                    f"{chr(10).join(['- ' + q for q in chunk.hypothetical_questions])}\n\n"
                    f"【正文内容】：\n{chunk.content}"
                )
                
                doc = Document(
                    page_content=enhanced_content,
                    metadata=new_metadata
                )
                documents.append(doc)
            return documents
            
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"⚠️ LLM 切分解析失败，正在重试 ({attempt + 1}/{max_retries})... 错误: {str(e)[:100]}")
                continue
            else:
                print(f"❌ LLM 切分彻底失败 (重试 {max_retries} 次): {e}")
                # 降级处理
                fallback_metadata = doc_metadata.copy()
                fallback_metadata["title"] = "未分类片段"
                return [Document(page_content=text, metadata=fallback_metadata)]

# --- 3. 粗略切分与调度主逻辑 ---
def process_documents_with_llm_chunking(raw_documents: List[Document], save_path="llm_chunks.pkl", cache_path="llm_chunking_cache.pkl"):
    """
    1. 粗切 (用 RecursiveCharacterTextSplitter 优化边界)
    2. 细切 (用 LLM Structured Output)，并带本地断点续传缓存
    """
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    
    # 1. 粗切优化：按段落边界切分，给 LLM 提供更完整的上下文
    # 优先在双换行(段落)、单换行、句号处切分，避免在一句话中间腰斩
    rough_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        separators=["\n\n", "\n", "。", "！", "？", " ", ""]
    )
    
    print(f"正在进行第一阶段：粗略切分...")
    rough_chunks = rough_splitter.split_documents(raw_documents)
    print(f"第一阶段完成：共切出 {len(rough_chunks)} 个大块文本。")
    
    # 尝试加载缓存
    processed_cache = {}
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'rb') as f:
                processed_cache = pickle.load(f)
            print(f"📦 发现本地断点缓存，已跳过 {len(processed_cache)} 个已处理的大块。")
        except Exception as e:
            print(f"⚠️ 读取缓存失败，将从头开始: {e}")
            
    # 初始化大模型
    llm = ChatOpenAI(
        model="deepseek-chat",
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
        temperature=0,
        request_timeout=60 
    )
    
    final_documents = []
    
    print(f"正在进行第二阶段：LLM 提纲式切分 (共 {len(rough_chunks)} 个大块，启用多线程加速)...")
    
    import concurrent.futures
    import threading
    import hashlib
    
    lock = threading.Lock()
    processed_count = 0
    total_chunks = len(rough_chunks)
    
    def process_chunk_task(i, chunk):
        chunk_hash = hashlib.md5(chunk.page_content.encode('utf-8')).hexdigest()
        
        # 命中缓存
        if chunk_hash in processed_cache:
            return i, chunk_hash, processed_cache[chunk_hash], True
            
        print(f"  -> 正在处理第 {i+1}/{total_chunks} 块 (字数: {len(chunk.page_content)})...")
        # 调用 LLM 进行精细切分
        fine_docs = chunk_text_with_llm(chunk.page_content, chunk.metadata, llm)
        return i, chunk_hash, fine_docs, False

    # 我们预先分配好字典，最后按顺序合并
    results_dict = {}
    
    # 开启线程池，控制并发数在 10 左右比较安全，防止触发 DeepSeek API 频率限制 (429 Too Many Requests)
    max_workers = 10
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        future_to_index = {
            executor.submit(process_chunk_task, i, chunk): i 
            for i, chunk in enumerate(rough_chunks)
        }
        
        for future in concurrent.futures.as_completed(future_to_index):
            i = future_to_index[future]
            try:
                idx, chunk_hash, fine_docs, is_cached = future.result()
                
                with lock:
                    results_dict[idx] = fine_docs
                    processed_count += 1
                    
                    if not is_cached:
                        processed_cache[chunk_hash] = fine_docs
                        print(f"     ✅ 第 {idx+1} 块处理完成，切分为 {len(fine_docs)} 个逻辑单元。总进度: {processed_count}/{total_chunks}")
                        
                        # 每处理完一定数量保存一次断点，防止意外中断
                        if processed_count % 20 == 0:
                            with open(cache_path, 'wb') as f:
                                pickle.dump(processed_cache, f)
            except Exception as e:
                print(f"❌ 处理第 {i+1} 块时发生严重错误: {e}")
                results_dict[i] = [] # 失败则塞入空列表
                
    # 循环结束后做一次最终的缓存保存
    with open(cache_path, 'wb') as f:
        pickle.dump(processed_cache, f)
        
    # 按原始大块的顺序合并所有精细切分后的 Document
    for i in range(total_chunks):
        if i in results_dict:
            final_documents.extend(results_dict[i])
        
    print(f"全部切分完成！最终生成了 {len(final_documents)} 个高质量知识块。")
    
    # 预览第一个
    if final_documents:
        print("\n=== 切分结果预览 ===")
        print(f"标题 (Title): {final_documents[0].metadata.get('title')}")
        print(f"内容 (Content): {final_documents[0].page_content[:150]}...\n")
    
    # 保存结果，供 build_vector_store.py 使用
    with open(save_path, 'wb') as f:
        pickle.dump(final_documents, f)
    print(f"💾 数据已保存至 {save_path}")
    
    return final_documents

if __name__ == "__main__":
    # 为了测试，我们伪造一段需要切分的文档（实际应用中你应该调用 load_pdf_docs 加载真实文档）
    test_text = """
    第十三章 故障排查
    13.1 网络连接故障
    如果应用程序出现 Communications link failure，这通常意味着数据库端口不通或防火墙拦截。排查步骤如下：
    1. ping 数据库服务器 IP。
    2. telnet 数据库端口（如 3306）。
    
    13.2 SQL日志分析
    SQL日志记录了时间、执行的SQL语句等信息。通过分析SQL日志可以找出处理耗时多的SQL语句。
    展开管理控制台左侧的“诊断”节点，单击“SQL日志”，设置时间后可以查看。
    此页显示了由 TongWeb 中 JDBC 连接池生成的日志。
    """
    
    test_doc = Document(page_content=test_text, metadata={"source": "test_manual.pdf", "page": 13})
    
    # 执行流程
    process_documents_with_llm_chunking([test_doc], "test_llm_chunks.pkl")
