# TongAgent RAG 优化与未来演进路线图

本文档旨在规划 TongAgent 中 RAG（检索增强生成）模块的优化路径，以及项目最终迈向“**人人可用的在线 Agent 服务**”的长期演进目标。

## 🏁 当前状态 (Current Status)
**已完成核心 MVP (Minimum Viable Product)**：
- **架构**：Contextual Hybrid RAG (上下文感知混合检索)。
- **检索器**：EnsembleRetriever (BM25 关键词 + Chroma 向量检索)。
- **预处理**：PDF 解析 -> 语义分块 -> DeepSeek 生成上下文摘要 -> 向量化 (BGE-Large)。
- **环境**：独立的 Python 虚拟环境 (`.venv`)，解决了依赖冲突。
- **验证**：通过 `test_rag_tool.py` 验证了检索准确性。

---

## 🚀 第一阶段：RAG 核心性能优化 (Core RAG Optimization)
*目标：让检索更准、更全，解决“找不到”或“找错”的问题。*

### 1. 引入重排序 (Reranking) ⭐ **(高优先级)**
- **现状**：仅依赖向量相似度和关键词匹配的加权分数。
- **改进**：
    - 在检索回 Top 50 个文档后，引入 **Cross-Encoder (如 BGE-Reranker)** 模型。
    - 对这 50 个文档进行精细的语义打分，只将得分最高的 Top 5-10 提供给 LLM。
- **价值**：大幅提升 Precision（精确率），减少 LLM 的幻觉。

### 2. 元数据增强与过滤 (Metadata Filtering)
- **现状**：简单的文件路径元数据。
- **改进**：
    - 在预处理阶段提取更多结构化信息：`适用版本` (如 TongWeb 7.0), `组件模块` (如 Session, JDBC), `操作系统` (Linux/Windows)。
    - **Self-Querying**：让 Agent 在检索前自动生成过滤器（例如用户问“Linux 下怎么配”，自动过滤 `OS=Linux` 的文档）。

### 3. 语义分块策略 (Semantic Chunking)
- **现状**：固定字符数分块 (Fixed-size chunking)。
- **改进**：
    - 使用 LLM 或 NLP 工具识别段落、章节边界，按语义完整性切分。
    - 保证一个 Chunk 包含一个完整的知识点，避免上下文断裂。

### 4. 建立评估体系 (Evaluation)
- **现状**：人工肉眼检查。
- **改进**：
    - 集成 **RAGAS** 或 **DeepEval** 框架。
    - 自动化测试指标：`Context Recall` (召回率), `Context Precision` (精确率), `Faithfulness` (忠实度)。

---

## 🛠️ 第二阶段：系统架构升级 (Architecture Upgrade)
*目标：处理复杂问题，提升系统的鲁棒性。*

### 1. 查询转换 (Query Transformation)
- **HyDE (Hypothetical Document Embeddings)**：针对用户模糊的问题，先生成一个“假设答案”，用假设答案去检索。
- **多路查询 (Multi-Query)**：将复杂问题拆解为多个子问题并行检索，汇总结果。

### 2. GraphRAG (知识图谱增强)
- **场景**：回答跨文档的全局性问题（如“总结所有版本之间的区别”）。
- **方案**：构建实体（Entity）和关系（Relation）的知识图谱，结合图遍历进行检索。

### 3. 向量数据库升级
- **现状**：本地文件版 Chroma (Local Persistence)。
- **改进**：迁移到 **Chroma Server** 或 **Milvus/PGVector**，支持更高并发和海量数据。

---

## 🌐 第三阶段：生产化与在线服务 (Production & Deployment)
*目标：实现“每个人都可以使用 Agent”的愿景。*

### 1. 服务化 (API First)
- **Backend**：使用 **FastAPI** 或 **Flask** 将 Agent 封装为 RESTful API。
- **协议**：支持 SSE (Server-Sent Events) 流式输出，让用户像用 ChatGPT 一样看到字一个个蹦出来。
- **并发**：引入 **Celery/Redis** 队列处理耗时任务，支持多用户同时提问。

### 2. 用户界面 (Frontend)
- **Web UI**：开发一个现代化的聊天界面 (React/Vue/Next.js)。
- **功能**：
    - 多会话管理 (Chat History)。
    - 文件上传与解析进度展示。
    - 引用来源高亮 (点击角标跳转到 PDF 原文)。

### 3. 多用户与安全 (Multi-Tenancy & Security)
- **认证**：集成 **Auth0** 或 **JWT** 登录系统。
- **隔离**：确保用户 A 只能看到自己上传的私有知识库（如果支持用户上传）。
- **防护**：
    - **Prompt Injection 防护**：防止用户诱导 Agent 说出违规内容。
    - **Rate Limiting**：限制 API 调用频率，防止滥用。

### 4. 部署与运维 (DevOps)
- **Docker 化**：将 API、数据库、Agent 逻辑打包成 Docker 镜像。
- **云部署**：部署到 AWS/阿里云/腾讯云 (K8s 或 Serverless)。
- **监控**：
    - **LangFuse/LangSmith**：生产环境全链路追踪，分析 Token 消耗和延迟。
    - **Sentry**：错误日志监控。

---

## 📅 下一步行动建议 (Immediate Next Steps)

1. **代码归位**：将 `rag_tool_v2.py` 正式集成到主 Agent (`rag_agent`) 中。
2. **API 化尝试**：写一个简单的 FastAPI 接口，让本地可以通过 HTTP 请求调用 Agent。
3. **前端原型**：使用 **Streamlit** 或 **Gradio** 快速搭建一个可交互的 Web Demo，方便分享给他人测试。
