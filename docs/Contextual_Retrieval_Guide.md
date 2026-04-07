# Anthropic Contextual Retrieval 技术解析

本文档基于 Anthropic 的工程博客 [Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)，解析三种提升 RAG (Retrieval-Augmented Generation) 性能的核心技术：上下文嵌入 (Contextual Embeddings)、上下文 BM25 (Contextual BM25) 与重排序 (Reranking)。

## 1. 核心问题：切片导致的上下文丢失

在传统的 RAG 流程中，长文档被切分成小的 Chunk（切片）进行索引。这会导致**上下文丢失**问题。

**举例**：
*   **原始文档**：“ACME 公司的财务状况在 2023 年第二季度表现强劲，收入增长了 20%。”
*   **切片 Chunk**：“收入增长了 20%。”
*   **问题**：当用户问“ACME 公司的收入情况如何？”时，检索系统找不到这个 Chunk，因为它只包含“收入增长”，却丢失了“ACME 公司”这个关键主语。

## 2. 三大核心技术

### 2.1 Contextual Embeddings (上下文嵌入)

**原理**：
在对每个 Chunk 进行 Embedding（向量化）之前，先利用 LLM 为该 Chunk 生成一段简短的**上下文说明**，并将其拼接到 Chunk 前面。

**流程**：
1.  输入整个文档到 LLM。
2.  LLM 为每个 Chunk 生成一段解释性前缀（例如：“这是关于 ACME 公司 2023 Q2 财务报告的片段”）。
3.  **Contextualized Chunk = 上下文前缀 + 原始 Chunk**。
4.  对 Contextualized Chunk 进行 Embedding 存入向量库。

**优势**：
*   解决了代词指代不清（“它”、“该公司”）的问题。
*   即使 Chunk 本身没有关键词，也能通过上下文前缀被检索到。

### 2.2 Contextual BM25 (上下文 BM25)

**原理**：
BM25 是一种基于关键词匹配的传统检索算法。Contextual BM25 将上述生成的“上下文前缀”也加入到 BM25 的索引中。

**优势**：
*   **精确匹配增强**：当用户搜索特定专有名词（如“ACME”）时，即使该词不在原始 Chunk 中（而在上下文前缀里），BM25 也能通过前缀匹配到该 Chunk。
*   **互补性**：BM25 擅长精确匹配，Embedding 擅长语义匹配。两者结合（Hybrid Search）效果最佳。

### 2.3 Reranking (重排序)

**原理**：
在检索阶段，先通过 Embedding + BM25 检索出大量的候选 Chunk（比如 Top 150），然后使用一个专门的 **Rerank Model** 对这些结果进行精细打分和重新排序，只取前几名（Top 5-10）给 LLM。

**优势**：
*   **大幅提升准确率**：Rerank 模型比 Embedding 模型更重、更精准，它能理解 Query 和 Chunk 之间的细微逻辑关系。
*   **减少幻觉**：过滤掉不相关的噪音数据，让 LLM 专注于高质量上下文。

## 3. 技术组合与性能提升

根据 Anthropic 的实验数据：

| 检索策略 | 性能表现 |
| :--- | :--- |
| Standard RAG (传统向量检索) | 基准线 |
| + Contextual Embeddings | 显著提升 (解决上下文丢失) |
| + Contextual BM25 (Hybrid) | 进一步提升 (结合精确匹配) |
| **+ Reranking (全套组合)** | **最佳性能 (降低 50% 检索失败率)** |

## 4. 如何在当前 Agent 中实现？

我们将在接下来的步骤中，逐步引导你在 `TongAgent` 中实现这套架构。

### 实现路线图

1.  **Contextual Pre-processing**: 创建一个新的预处理脚本，使用 LLM 为现有文档生成上下文前缀。
2.  **Hybrid Retrieval**: 改造 `rag_tool.py`，引入 BM25Retriever 并与 ChromaRetriever 进行 Ensemble（混合）。
3.  **Reranking**: 引入 Rerank 模型（如 BGE-Reranker 或 Cohere），对混合检索的结果进行重排序。
