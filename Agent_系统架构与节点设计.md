# TongAgent 系统架构说明书 (Architecture Specification)

## 1. 系统概述 (System Overview)
TongAgent 是一个基于 LangGraph 构建的智能中间件运维与问答 Agent。它融合了大型语言模型（DeepSeek）、高级检索增强生成（Advanced RAG）技术以及多层级的长短期记忆系统。该系统旨在为用户提供关于 TongWeb 等中间件的专业、准确、具有上下文连贯性的解答和操作建议。

---

## 2. 核心架构与工作流 (Core Architecture & Workflow)

系统整体采用 **有向图状态机 (State Graph)** 的设计模式，由以下核心节点组成：

### 2.1 任务分类器 (Complexity Classifier)
作为系统的入口，对用户的意图进行初步分析：
*   **SIMPLE 路径**：对于简单的闲聊、问候或直接的知识问答，直接进入 `generate_response_node`，快速响应，节省计算资源。
*   **COMPLEX 路径**：对于需要查阅文档、多步推理的复杂问题（如“如何安装并配置负载均衡？”），进入规划与执行循环。

### 2.2 复杂任务循环 (Complex Task Loop)
1.  **Planner Node (规划节点)**：将复杂任务拆解为可执行的子步骤（如：1. 查安装指南，2. 查并发参数）。
2.  **Intent Parse Node (意图解析与工具调用)**：根据当前的计划步骤，决定调用哪个具体工具（如 `retrieve_middleware_docs`、`aliyun_web_search`）。
3.  **Tool Execution**：执行工具并获取结果。
4.  **Reflection Node (反思节点)**：评估工具执行的结果是否满足当前计划的要求。如果失败或未找到，指导系统重试或切换策略。
5.  **Context Update**：循环结束后，收集所有步骤的工具结果（解决多步任务中的上下文截断问题）。

### 2.3 最终生成与记忆 (Generation & Memory)
*   **Generate Response Node**：基于用户问题、全量工具结果、长期记忆和通用知识，生成最终的专业回复。具备**兜底策略 (Fallback)**，当 RAG 缺失信息时，主动利用通用知识进行补充。
*   **Summarization Node**：对过长的对话历史进行精炼压缩，保留关键技术细节。
*   **Save Memory Node**：将会话中的关键事实、用户偏好持久化到长期记忆库中。

---

## 3. RAG 检索增强引擎 (Advanced RAG Engine)
知识检索是 Agent 的核心能力，目前已实现并计划引入以下高级特性：

### 3.1 混合检索 (Hybrid Search) [已实现]
结合了 **向量检索 (Vector Search)** 和 **关键词检索 (BM25)**，通过 `EnsembleRetriever` 进行倒数排序融合 (RRF)，确保语义理解和专有名词匹配的平衡。最后通过 **重排序 (Reranking)** 模型进一步提升准确率。

### 3.2 查询重写 (Query Rewriting / HyDE) [规划中]
*   **原理**：在检索前，引入一个轻量级 LLM 节点，将用户口语化的短问题转换为“假设性答案”或“标准查询语句”。
*   **优势**：扩大检索召回范围。例如，将“怎么调优？”重写为“TongWeb 性能调优参数及配置方法”，使向量空间距离更接近官方文档。

### 3.3 多路召回与关键词提取 (Keyword Extraction) [规划中]
*   **原理**：利用 LLM 提取用户问题中的核心实体（如特定文件名 `tongweb.xml`、报错码 `ERROR-001`）。
*   **优势**：构建专门的 `KeywordRetriever`，通过 Metadata 过滤或强化 BM25，弥补纯向量检索在面对专有名词时“懂意思但对不准字”的缺陷。

---

## 4. 记忆引擎分析 (Memory Engine - Mem0)

TongAgent 采用了 **Mem0** 作为其核心记忆管理组件，实现了跨会话的上下文连贯性。

### 4.1 为什么选择 Mem0？
在相关开源技术（如 Zep, Letta, Open Memory）中，Mem0 因其“向量 + 图谱”的架构脱颖而出。
*   **图数据库的优势**：传统的向量数据库擅长点对点匹配，但不擅长处理逻辑链条（多跳推理）和事实冲突更新。Mem0 的图存储通过实体映射（Entity Mapping）连接概念，当新事实与旧关系冲突时，能精准定位并更新关系边，保证知识图谱的实时性与一致性。

### 4.2 Mem0 的分层记忆架构
Mem0 将记忆按“生命周期与作用范围”分层存储：
1.  **Conversation Memory (对话回合记忆)**：单次回复内的临时状态，回合结束即消失。
2.  **Session Memory (会话记忆)**：关联 `session_id`，适用于一次排障或多步调试的短期上下文。
3.  **User Memory (用户长期记忆)**：关联 `user_id`，永久存储跨会话的偏好和长期事实（如“客户 A 正在使用 Linux 系统”）。
4.  **Organizational Memory (组织级记忆)**：关联 `agent_id`，存储全局共享的 FAQ 或统一政策。

### 4.3 记忆操作的生命周期
*   **Add (写入)**：默认使用 `infer=True`，Mem0 会调用 LLM 从消息中抽取“值得记住的事实”并自动进行去重和冲突处理。
*   **Search (检索)**：自然语言转 Embedding 后，在向量库中寻找相似记忆。支持按 `user_id`、`session_id` 等 Metadata 进行字段级过滤，防止数据串线。
*   **Update & Delete (更新与删除)**：支持单条或批量修正/删除记忆，以维护长期知识的正确性和合规性。

### 4.4 高级特性集成
*   **多用户隔离 (Multi-tenancy)**：TongAgent 通过在 API 层传递动态 `user_id` 至 Mem0，确保不同用户的记忆严格隔离。
*   **异步客户端 (Async Mode)**：支持非阻塞的读写操作，提升 Agent 的并发响应能力。
*   **多模态与结构化导出**：Mem0 支持处理图像/文档提取记忆，并可导出为结构化 JSON 数据。

---

## 5. 部署与运维 (Deployment & Operations)
*   **容器化 (Docker)**：前端 (Streamlit) 和后端 (FastAPI) 通过 `docker-compose` 编排，实现一键部署。
*   **跨平台依赖管理**：通过分离 `requirements_linux.txt` 解决环境依赖冲突，并放宽深度学习框架（PyTorch）的版本限制。
*   **本地化模型支持**：内嵌 HuggingFace Embedding 模型 (`bge-large-zh-v1.5`)，避免生产环境（如腾讯云服务器）的外部网络依赖问题。
