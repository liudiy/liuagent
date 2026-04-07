# AI/Agent 开发通用面试题库

这份文档补充了除了 `TongAgent` 项目细节之外，面试官可能会问到的**通用技术问题**。掌握这些能够证明你的基础扎实，不仅仅是一个“调包侠”。

## 1. LLM 基础理论 (Fundamentals)

*   **Q: 什么是 Tokenization？为什么 LLM 算数不好？**
    *   **A**: Tokenization 是将文本转换为模型可处理的数字序列的过程（如 BPE 算法）。LLM 算数不好是因为数字通常被切分成不直观的 Token（例如 "1024" 可能被切成 "10" 和 "24"），破坏了数字的语义连贯性。
*   **Q: 解释一下 Temperature 和 Top-P 的区别？**
    *   **A**: `Temperature` 控制概率分布的平滑程度（越高越随机，越低越确定）；`Top-P` (Nucleus Sampling) 是截断累积概率（只从概率最高的 P% 词表中采样）。通常建议调整其中一个即可。
*   **Q: 什么是 Context Window（上下文窗口）？如果输入超过了怎么办？**
    *   **A**: 模型一次能处理的最大 Token 数。超长处理策略：
        1.  **截断/滑动窗口**：丢弃旧信息。
        2.  **摘要 (Map-Reduce)**：分段总结后再合并。
        3.  **RAG**：只检索相关片段放入窗口。

## 2. RAG (检索增强生成) 进阶

*   **Q: 你的 RAG 检索效果不好，怎么优化？（经典题）**
    *   **A**:
        1.  **预检索 (Pre-retrieval)**: 优化分块策略（Chunking），增加重叠（Overlap），清洗数据。
        2.  **检索中 (Retrieval)**:
            *   **混合检索 (Hybrid Search)**: 结合 关键词检索 (BM25) 和 向量检索 (Dense)。
            *   **元数据过滤**: 先按时间/作者过滤，再搜索。
        3.  **后检索 (Post-retrieval)**:
            *   **重排序 (Re-ranking)**: 使用 Cross-Encoder 对召回的 Top-50 进行精细排序，选出 Top-5。
            *   **上下文压缩**: 去除无关内容。
*   **Q: 什么时候用 RAG，什么时候用微调 (Fine-tuning)？**
    *   **A**:
        *   **RAG**: 需要外部实时知识、私有数据，且要求低幻觉、可解释性强。
        *   **Fine-tuning**: 需要改变模型的说话风格、格式指令跟随能力，或者领域专业术语非常生僻（RAG 检索不到）。
        *   *最佳实践*: RAG + 轻量微调。

## 3. 向量数据库 (Vector DB)

*   **Q: 向量数据库的索引原理是什么？(HNSW)**
    *   **A**: 大多使用 **HNSW (Hierarchical Navigable Small World)**。它像一张分层的地图，上层是高速公路（跳跃大），下层是街道（精细搜索），能在海量数据中实现毫秒级近似最近邻搜索 (ANN)。
*   **Q: 相似度计算有哪些方法？**
    *   **A**: 余弦相似度 (Cosine，关注方向，最常用)、欧氏距离 (Euclidean，关注距离)、点积 (Dot Product)。

## 4. Agent 框架与设计

*   **Q: 介绍一下 ReAct 模式？**
    *   **A**: **Reason + Act**。模型先进行思考 (Thought)，决定调用什么工具 (Action)，观察工具的输出 (Observation)，然后再思考，直到得出结论。这是 Agent 的基本工作原理。
*   **Q: 什么是 CoT (Chain of Thought)？**
    *   **A**: 思维链。通过让模型 "Let's think step by step"，诱导其生成中间推理步骤，显著提高复杂逻辑问题的准确率。
*   **Q: LangChain 和 LangGraph 的区别？**
    *   **A**: LangChain 是**DAG (有向无环图)**，适合单向流水线；LangGraph 是**循环图 (Cyclic Graph)**，引入了 State 和 Loop，适合需要重试、人机交互、多轮循环的复杂 Agent。

## 5. Python 工程与并发

*   **Q: 你的 Agent 如何支持高并发？(Asyncio)**
    *   **A**: 使用 Python 的 `asyncio` 和 `aiohttp`。LLM API 调用是 IO 密集型任务，使用异步可以避免阻塞主线程，同时处理成百上千个请求。
*   **Q: 什么是生成器 (Generator)？在 LLM 中有什么用？**
    *   **A**: 使用 `yield` 的函数。在 LLM 中用于 **流式输出 (Streaming)**，即模型生成一个 Token 就推给前端一个，提升用户体验（首字延迟低）。

## 6. 场景设计题 (System Design)

*   **Q: 设计一个法律合同审查 Agent，你会怎么做？**
    *   **A**:
        1.  **数据处理**: OCR 识别文档，按条款 (Clause) 进行 Chunking。
        2.  **检索**: 使用 RAG 检索相关法律条文和过往案例。
        3.  **检查**: 设计多个 Prompt 分别检查“风险条款”、“合规性”。
        4.  **输出**: 生成 Markdown 报告，并在原文高亮风险点。
        5.  **人工介入 (Human-in-the-loop)**: 律师确认后才最终通过。

---

**💡 备考建议**:
*   把上面的 RAG 优化点（混合检索、重排序）结合到你的 `TongAgent` 项目里去说，比如：“虽然我目前项目主要用了向量检索，但我了解如果在生产环境，我会加上 Re-ranking...” 这样显得你视野很宽。
