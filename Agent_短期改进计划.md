# Agent 优化与未来路线图 (Agent Improvement Plan)

本文档专注于 **TongAgent 核心逻辑** 的功能完善与性能优化，已剔除前端、后端及运维部署相关内容，并根据当前代码库状态进行了校准。

## 1. 记忆系统 (Memory System) - `Priority: High`
目前 Agent 已通过 Mem0 实现了基础的长短期记忆，但仍需解决多租户和效率问题。
- **[Doing] 多租户隔离 (Multi-tenancy)**: 
  - 必须将 `user_id` 从硬编码的 `"user_123"` 改为动态传参。
  - 确保不同用户的记忆互不可见。
- **[Todo] 记忆过滤与优化 (Memory Filtering)**:
  - 增加“记忆门卫”机制，防止无意义的对话（如“你好”、“谢谢”）污染长期记忆。
  - 优化检索参数 (`limit`, `score_threshold`)，避免一次性召回过多低质量记忆干扰 Prompt。

## 2. RAG 检索增强 (RAG Enhancement) - `Priority: Medium`
代码审计显示，**你已经实现了混合检索 (Hybrid Search) 和重排序 (Reranking)**，因此这些不再列为 Todo。接下来的重点是提升检索质量的源头。
- **[Todo] 语义分块 (Semantic Chunking)**:
  - **现状**: 使用固定字符数 (`RecursiveCharacterTextSplitter`) 切分，容易切断逻辑。
  - **改进**: 使用 Embedding 模型基于语义相似度进行切分，确保每个 Chunk 是一个完整的语义单元。
- **[Todo] 问题重写 (Query Rewriting)**:
  - **现状**: 直接使用用户原始问题进行检索。如果用户问“它多少钱？”，检索会失败。
  - **改进**: 引入 Query Rewrite 节点，将用户问题改写为独立完整的查询句（“DeepSeek-V3 API 的价格是多少？”）再进行检索。

## 3. Agent 核心逻辑 (Core Logic) - `Priority: Medium`
- **[Todo] 鲁棒性提升 (Robustness)**:
  - 增强工具调用的错误处理（Error Handling）。当工具报错时，Agent 应能自动分析错误原因并尝试修正参数重试，而不是直接把报错抛给用户。
- **[Todo] 反思机制调优 (Reflection Tuning)**:
  - 目前的反思节点 (`reflection_node`) 逻辑较简单。可以引入更复杂的评判标准，甚至引入“批评家 Agent”来专门挑刺。

## 4. 评估体系 (Evaluation) - `Priority: Low (Long-term)`
- **[Todo] 持续评估流水线 (CI/CD for AI)**:
  - 每次代码提交后，自动运行 RAGAS/DeepEval 评估集，确保回答质量没有下降。
