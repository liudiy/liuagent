# RAG 系统开发实战：从零构建混合检索 (Hybrid Search)

本文档总结了我们在 TongAgent 项目中构建高级 RAG (Retrieval-Augmented Generation) 系统的完整过程。我们从最基础的向量检索，一步步升级为包含上下文增强 (Contextual Embeddings) 和混合检索 (Hybrid Search) 的企业级方案。

## 1. 核心概念

在开始写代码之前，我们需要理解几个核心概念：

*   **Embedding (向量化)**: 将文字转化为计算机能理解的数字列表（向量）。语义相近的词，向量距离也近（如“苹果”和“香蕉”）。
*   **Contextual Retrieval (上下文检索)**: 解决文档切片丢失上下文的问题。例如，一个切片里只有“它支持高并发”，如果不结合上下文，谁知道“它”是指 TongWeb 还是 TongGW？
*   **Hybrid Search (混合检索)**: 结合 **语义检索 (Vector)** 和 **关键词检索 (BM25)** 的优点。
    *   **Vector**: 懂语义（搜“水果”能找到“苹果”）。
    *   **BM25**: 懂字面（搜错误码 `ERROR-1024` 能精准定位）。

---

## 2. 第一阶段：数据预处理 (Preprocessing)

**目标**: 将 PDF 文档切片，并为每个切片生成“上下文说明”，解决指代不清的问题。

**脚本**: `preprocess_docs.py`

### 关键步骤：
1.  **加载 PDF**: 使用 `PyPDFLoader` 递归扫描目录。
2.  **切分文档**: 使用 `RecursiveCharacterTextSplitter` 将长文档切成 800 字左右的小块 (Chunk)。
3.  **生成上下文 (Contextualizing)**:
    *   使用 LLM (DeepSeek) 为每个 Chunk 生成一段解释性文字。
    *   Prompt: `请简要描述这段内容在整篇文档中的上下文背景...`
    *   **拼接**: 将生成的上下文拼接到原始文本前面：`[Context] \n\n Original Text: \n [Content]`。
4.  **保存**: 将处理好的 Chunk 列表保存为 `contextualized_chunks.pkl`。

---

## 3. 第二阶段：构建向量数据库 (Indexing)

**目标**: 将预处理好的文本转化为向量，并存入 Chroma 数据库。

**脚本**: `build_vector_store.py`

### 关键步骤：
1.  **加载数据**: 读取 `contextualized_chunks.pkl`。
2.  **初始化 Embedding 模型**:
    *   使用 `BAAI/bge-large-zh-v1.5` (中文领域顶尖模型)。
    *   注意：这里需要 `sentence-transformers` 库。
3.  **构建数据库**:
    *   使用 `Chroma.from_documents()`。
    *   这一步会将文本转化为向量，并持久化保存到磁盘 (`chroma_db_tongdata_v2`)。

---

## 4. 第三阶段：构建检索工具 (Retrieval Tool)

**目标**: 编写 Agent 可调用的工具，实现混合检索逻辑。

**脚本**: `rag_tool_v2.py`

### 架构设计 (Multi-Stage Retrieval)

我们采用了 **多路召回 + 加权合并** 的策略：

```mermaid
graph TD
    A[用户 Query] --> B(Vector Retriever)
    A --> C(BM25 Retriever)
    B -->|语义相似度| D[结果列表 A]
    C -->|关键词匹配| E[结果列表 B]
    D & E --> F{Ensemble Retriever}
    F -->|加权合并 (0.6/0.4)| G[最终候选集]
```

### 核心代码拆解

#### A. 加载向量检索器 (Vector)
```python
def get_vectorstore():
    # 1. 初始化模型 (必须与构建时一致)
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-large-zh-v1.5")
    # 2. 加载数据库
    vectorstore = Chroma(embedding_function=embeddings, persist_directory=DB_PATH)
    return vectorstore
```

#### B. 构建关键词检索器 (BM25)
*   **难点**: Chroma 不支持 BM25，需要把所有文本“捞”出来现场构建索引。
```python
def get_bm25_retriever(vectorstore):
    # 1. 取出所有文档
    all_data = vectorstore.get()
    # 2. 转换为 Document 对象
    docs = [Document(page_content=t, metadata=m) for t, m in zip(all_data['documents'], all_data['metadatas'])]
    # 3. 构建索引
    return BM25Retriever.from_documents(docs)
```

#### C. 混合与封装 (Ensemble & Tool)
```python
def get_hybrid_retriever():
    vs = get_vectorstore()
    vector_retriever = vs.as_retriever(search_kwargs={"k": 5})
    bm25_retriever = get_bm25_retriever(vs)
    
    # 混合！Vector 权重 0.6, BM25 权重 0.4
    return EnsembleRetriever(
        retrievers=[vector_retriever, bm25_retriever],
        weights=[0.6, 0.4]
    )

@tool
def retrieve_docs(query: str):
    # 全局缓存检索器，避免重复加载
    global _cached_retriever
    if not _cached_retriever:
        _cached_retriever = get_hybrid_retriever()
    
    docs = _cached_retriever.invoke(query)
    return format_docs(docs)
```

---

## 5. 常见问题与坑 (Troubleshooting)

1.  **路径问题**: `FileNotFoundError`。
    *   **教训**: 脚本运行目录和文件所在目录可能不一致。**推荐使用 `os.path.join(os.path.dirname(__file__), ...)` 绝对定位。**
2.  **依赖缺失**: `ImportError: sentence_transformers`。
    *   **解决**: `pip install sentence-transformers rank_bm25`。
3.  **模型重复加载**: 每次调用 Tool 都重新加载 1.2GB 模型，导致极慢。
    *   **解决**: 使用全局变量 `_cached_retriever` 进行缓存（单例模式）。
4.  **BM25 初始化失败**: 如果数据库为空，`from_documents([])` 会报错。
    *   **解决**: 加判断 `if not docs: return None`，并在混合时做降级处理（只用 Vector）。

---

## 6. 未来优化方向

1.  **Rerank (重排序)**: 在混合检索之后，引入 Cross-Encoder (如 `bge-reranker`) 对前 10 个结果进行精细打分，进一步提升准确率。
2.  **元数据过滤 (Metadata Filtering)**: 允许 Agent 指定只搜“TongWeb”相关的文档，通过 `filter={"source": "TongWeb..."}` 过滤。
