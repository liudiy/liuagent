# LiuAgent (TongAgent) 当前能力总结与架构分析

## 一、 系统架构与核心框架
目前项目基于 **LangGraph** 构建了一个状态机驱动（StateGraph）的智能 Agent 架构。系统采用类似 Cursor/Devin 的多节点控制流设计，具备以下核心特性：

1. **多模型协同调度**：
   - 核心决策与对话模型：**DeepSeek V3 / DeepSeek Chat**（主节点）
   - 任务分类与轻量级任务：**Qwen-Turbo**（Classifier Node / Query Rewriting）
   - 复杂任务规划：**Qwen-Plus**（Planner Node）
2. **状态流转机制 (AgentState)**：
   - 包含消息历史、编辑器/环境上下文、意图与执行状态、反思控制流（重试次数、下一步动作）以及长期记忆。
3. **自适应规划 (Adaptive Planning)**：
   - **Classifier Node**：根据用户输入判断任务是“简单(SIMPLE)”还是“复杂(COMPLEX)”。
   - **Planner Node**：对于复杂任务，将其拆解为多个子任务（Plan），并逐个执行（通过 `continue_logic` 节点循环流转）。

## 二、 核心功能模块

### 1. 混合增强检索增强生成 (Advanced RAG)
系统集成了一个高级的中间件文档检索工具（`retrieve_middleware_docs`），采用了多重优化策略：
*   **HyDE 查询重写 (Query Rewriting)**：使用 LLM 根据用户问题生成“假设性官方文档片段”，增强向量检索的语义命中率。
*   **关键词提取 (Keyword Extraction)**：提取核心术语，增强字面检索能力。
*   **双路混合检索**：
    *   **Vector Retrieval**：基于 HuggingFace `bge-large-zh-v1.5` 的密集向量检索（ChromaDB）。
    *   **BM25 Retrieval**：基于词频的稀疏检索（持久化到本地 `.pkl`）。
*   **RRF 融合 (Reciprocal Rank Fusion)**：手动实现的重排算法，将双路召回的结果进行科学融合（权重 Vector:0.6, BM25:0.4）。

### 2. 代码解释器与沙箱环境 (Code Interpreter)
提供了一个安全的云端 Python 执行环境（基于 E2B Sandbox），并在工具层进行了深度定制：
*   **状态保持 (Stateful Execution)**：沙箱实例在全局保持存活（设定超时时间），Agent 可以分步执行代码（如第一步加载数据，第二步处理，变量不丢失）。
*   **文件系统映射**：在沙箱初始化时，自动将本地 `data` 目录下的文件同步挂载到沙箱的 `/home/user/` 目录中，允许 Agent 直接读取并分析本地数据。
*   **多模态输出支持**：除了捕获标准输出 (stdout)，还会自动拦截代码生成的图表（如 Matplotlib 生成的 `.png`、`.jpeg`），将其解码并保存到本地 `output` 目录，同时将本地路径反馈给 Agent。

### 3. 长期记忆与个性化 (Long-term Memory)
集成了 **Mem0** 记忆管理库：
*   **异步记忆保存 (`save_memory_node`)**：在后台线程中提取用户和 AI 的最新一轮交互并存入记忆库，不阻塞主对话流。
*   **记忆检索 (`retrieve_memory_node`)**：在对话开始前，根据用户当前问题检索历史记忆，并作为上下文注入到后续的 Prompt 中。

### 4. 自动反思与自我修正 (Self-Correction)
*   **Reflection Node**：工具执行后，如果发生错误或未达到预期，系统会进入反思节点。
*   **结构化评估**：要求 LLM 输出 JSON 格式的评估报告（包含 analysis, feedback, next_action）。
*   **控制流干预**：根据反思结果决定是 `retry`（原样重试）、`reselect_tool`（更换工具/策略）、`continue`（继续下一步）还是 `ask_user`（询问用户）。

### 5. 其他辅助工具
*   **Web Search**：接入了 `aliyun_web_search`，用于获取实时互联网信息。
*   **File Tools**：提供了 `list_data_files` 和 `get_data_file_path`，帮助 Agent 感知本地可用的数据文件。

---

## 三、 存在的问题与进一步改进建议

在阅读完现有代码并修复 E2B 代码解释器工具后，我发现系统目前存在以下可进一步优化的点：

### 1. 架构流转与错误处理
*   **问题**：在 `graph.py` 中，`route_tool_exec` 的判断逻辑比较简单（仅仅通过字符串中是否包含 "Error" 或 "Exception" 来判断失败）。对于 RAG 查不到内容或者代码执行返回逻辑错误（不带 Error 关键字），系统可能误认为成功而跳过反思。
*   **改进**：建议工具返回值采用结构化设计（如包含 `status: "success" | "failure"`），或者在 `ToolExec` 之后统一走一次轻量级的 LLM 验证节点，以决定是否需要反思。

### 2. E2B 代码解释器的高级交互
*   **问题**：虽然目前已经将本地的 `data` 目录上传到了 E2B 沙箱中，但如果是用户临时通过 UI 上传的日志文件，可能无法实时同步到全局的 Sandbox 中。
*   **改进**：在 Streamlit 前端 (`app.py`) 增加文件上传组件，并在触发工具调用前，提供一个专门的 `upload_file_to_sandbox` 内部逻辑或工具，让 Agent 能够动态推送新文件。

### 3. RAG 检索的性能瓶颈
*   **问题**：`rag_tool_v2.py` 中虽然注释掉了 CPU 的 Reranker（因为速度慢），但 HyDE 查询重写和关键词提取在每次检索时都要串行调用两次大模型（Qwen-Turbo）。这会导致工具调用的整体延迟偏高（通常在 3-5 秒以上）。
*   **改进**：可以使用 `asyncio.gather` 将“查询重写”和“关键词提取”这两个独立的 LLM 调用并行化，甚至与底层的向量检索并行执行，大幅缩短 RAG 工具的响应时间。

### 4. 流式输出体验 (Streaming UI)
*   **问题**：`app.py` 中使用了 `requests.get(..., stream=True)` 来接收 SSE 事件，但目前 LangGraph 抛出的 `on_chat_model_stream` 会被前端直接拼接到 `full_response`。在复杂的工具调用和多步 Plan 执行期间，前端页面会长时间卡在“正在调用工具”，且工具的中间输出（如反思过程）对用户不可见。
*   **改进**：可以在 Streamlit 界面引入 LangChain 官方的 `StreamlitCallbackHandler` 或优化后端的 SSE 数据结构，将 Agent 的“思考过程 (Thought)”、“反思日志 (Reflection)”和“最终回复 (Final Answer)”在 UI 上分区块展示（类似 DeepSeek/ChatGPT 的折叠思考框）。

### 5. 记忆管理的冗余
*   **问题**：`save_memory_node` 仅仅是简单地把 `User: xxx \n AI: yyy` 直接塞给 Mem0。随着对话变长，记忆库会产生大量冗余对话记录，而不是提炼后的“知识”或“偏好”。
*   **改进**：在保存前，使用一个轻量级 Prompt 让 LLM 提取**“值得记忆的核心事实或用户偏好”**（例如：用户习惯用 Python、用户关注某个特定报错），只将提炼后的精华存入 Mem0。