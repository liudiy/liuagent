# TongAgent 进阶开发路线图与《流畅的 Python》阅读指南

## 1. 核心目标 (Objective)
从“能跑的 Demo”进化为“生产级 Agent (Production-Grade Agent)”。
重点攻克：**混合检索 (Hybrid Search)**、**可观测性 (Observability)**、**持久化 (Persistence)**、**API 服务化 (Service)**。

---

## 2. 开发路线图 (Development Roadmap)

### Phase 1: RAG 内核增强 (Week 1-2)
**目标**：让 Agent “找得准”。
*   **任务 1.1: 混合检索 (Hybrid Search) 实现**
    *   引入 `BM25Retriever` (关键词检索)。
    *   引入 `Chroma` / `Qdrant` (向量检索)。
    *   实现 `EnsembleRetriever` (RRF 融合算法)。
    *   *验证*：对比纯向量检索和混合检索在“错误码查询”场景下的准确率。
*   **任务 1.2: 重排序 (Reranking) 引入**
    *   引入 `BGE-Reranker` 模型（通过 API 或本地）。
    *   对混合检索召回的 Top-50 结果进行精排，取 Top-5。

### Phase 2: 可观测性与调试 (Week 3)
**目标**：让 Agent “看得清”。
*   **任务 2.1: LangFuse 接入**
    *   本地部署 LangFuse (Docker)。
    *   在 `graph.py` 中全局注入 `CallbackHandler`。
    *   *验证*：在 LangFuse 后台看到每一轮对话的 Trace、Latency 和 Token 消耗。
*   **任务 2.2: 结构化日志**
    *   使用 `structlog` 替换 `print`，输出 JSON 格式日志，方便 ELK 分析。

### Phase 3: 工程化落地 (Week 4-5)
**目标**：让 Agent “用得上”。
*   **任务 3.1: FastAPI 服务化**
    *   重构 `run_agent.py`，移除 CLI 交互。
    *   实现 `POST /chat` 接口，支持 SSE (Server-Sent Events) 流式输出。
    *   实现 `GET /health` 健康检查接口。
*   **任务 3.2: 异步并发优化**
    *   将所有 IO 操作（检索、LLM 调用）严格改为 `async/await`。
    *   使用 `asyncio.gather` 并行执行多路检索（如同时查 Google 和 知识库）。

### Phase 4: 持久化与部署 (Week 6)
**目标**：让 Agent “忘不掉”。
*   **任务 4.1: Postgres 持久化**
    *   使用 `PostgresSaver` 替换内存 Checkpointer。
    *   验证服务重启后，对话状态（Graph State）依然存在。
*   **任务 4.2: Docker 编排**
    *   编写 `docker-compose.yml`，一键启动 Agent + Redis + Postgres + LangFuse。

---

## 3. 《流畅的 Python》实战阅读指南 (Reading Guide)

不要从头读！结合上述任务，按需阅读以下章节，**边做边读**效果最好。

### 配合 Phase 1 (RAG 增强)
*   **第 5 章：数据类构建器 (Data Class Builders)**
    *   *为什么读*：你会用到大量的 `Pydantic` 模型来定义检索结果结构、Rerank 输入输出。
    *   *重点*：`@dataclass` vs `pydantic.BaseModel` 的区别，类型提示 (`typing`) 的高级用法。
*   **第 2 章：序列构成的数组 (An Array of Sequences)**
    *   *为什么读*：处理检索回来的 `List[Document]`。
    *   *重点*：列表推导式 (List Comprehension)、生成器表达式 (Generator Expression)，学会高效处理数据列表。

### 配合 Phase 2 (可观测性)
*   **第 9 章：装饰器和闭包 (Decorators and Closures)**
    *   *为什么读*：LangChain/LangFuse 大量使用装饰器（如 `@traceable`）。
    *   *重点*：理解装饰器是如何在不修改函数代码的情况下，注入监控逻辑的。
*   **第 11 章：Python 风格的对象 (A Pythonic Object)**
    *   *为什么读*：理解 LangChain 的 `CallbackHandler` 是如何通过 `__call__` 等魔术方法工作的。

### 配合 Phase 3 (工程化与并发) —— **最重要**
*   **第 19 章：Python 并发编程 (Concurrency in Python)**
    *   *为什么读*：**这是 Agent 开发的核心内功**。FastAPI 和 LangGraph 全程依赖 `asyncio`。
    *   *重点*：`async def` / `await` 的本质，`Event Loop` (事件循环)，`asyncio.gather` (并行执行)。**必须读懂，否则你的 Agent 会很慢。**
*   **第 14-16 章：迭代器与生成器 (Iterators and Generators)**
    *   *为什么读*：实现 SSE 流式输出（打字机效果）。
    *   *重点*：`yield` 关键字，`yield from`，异步生成器 (`async for`)。

---

## 4. 行动建议 (Action Items)

1.  **本周 (Today)**: 按照 Phase 1，先跑通 **混合检索**。不要管界面，写个脚本 `test_hybrid_search.py`，能搜出东西就算赢。
2.  **阅读**: 今晚睡前读《流畅的 Python》**第 19 章 (并发)** 的开头部分，搞懂“协程”和“线程”的区别。
