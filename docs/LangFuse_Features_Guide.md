# LangFuse 核心功能速查表

## 一、LangFuse：LLM 工程化与可观测性平台 (Observability & Engineering)

**一句话定位**：给你的 Agent 装上“行车记录仪”和“仪表盘”，让你看清每一次对话的内部细节、成本和延迟。

### 1. 核心功能 (Core Features)

#### 1.1 Tracing (全链路追踪) - **最核心**
*   **功能**：记录 Agent 执行的每一步（RAG 检索、LLM 调用、工具执行）。
*   **价值**：
    *   **可视化调试**：不再靠看 Log 文件瞎猜。在网页上看到一个漂亮的树状图，显示检索花了 2 秒，LLM 花了 5 秒。
    *   **Debug**：发现某个步骤报错了，直接点进去看输入输出是什么。

#### 1.2 Prompt Management (提示词管理)
*   **功能**：在 LangFuse 后台管理 Prompt 版本，而不是写死在代码里。
*   **价值**：
    *   **解耦**：产品经理可以在后台改 Prompt，不需要你重新部署代码。
    *   **版本控制**：回滚到昨天的 Prompt 版本。

#### 1.3 Analytics & Metrics (分析与指标)
*   **功能**：自动统计 Token 消耗、延迟 (Latency)、成本 (Cost)、用户数。
*   **价值**：
    *   **省钱**：发现哪个功能最费钱。
    *   **优化**：发现哪个步骤最慢。

#### 1.4 Datasets (数据集管理)
*   **功能**：在后台创建测试集（Input/Expected Output）。
*   **价值**：配合评测功能，每次发版前跑一遍回归测试。

#### 1.5 Evaluation (在线评测)
*   **功能**：基于 Trace 运行评测（如让 GPT-4 给刚才的回复打分）。
*   **价值**：持续监控线上效果。

### 2. 为什么用 LangFuse？
*   **开源 & 自托管**：数据不出域（Docker 部署），安全。
*   **集成方便**：原生支持 LangChain, LlamaIndex, OpenAI SDK。
*   **可视化强**：界面非常直观，适合给老板演示。

## 二、实战操作：如何查看你的第一个 Trace

当你运行了 `python run_check_task.py` 后，请按以下步骤操作：

1.  **打开控制台**：浏览器访问 `http://localhost:3000` (默认账号/密码通常在 docker-compose.yml 中配置，如 admin@langfuse.com / password)。
2.  **进入项目**：点击左上角项目名称（如果没有项目，创建一个名为 `default` 的项目）。
3.  **点击 "Traces"**：在左侧菜单栏找到 `Traces`（链路追踪）。
4.  **查看详情**：
    *   你应该能看到刚刚生成的记录，Name 通常显示为 `LangGraph` 或你的 Chain 名称。
    *   点击列表中的第一行，进入 **Trace Detail** 页面。
5.  **分析执行过程**：
    *   右侧展示了完整的 **树状图 (Tree View)**。
    *   **Root Span**：整个 Agent 的执行时间。
    *   **Generations (蓝色)**：代表 LLM 调用。点击它，可以看到 `Input` (Prompt) 和 `Output` (Response)。
    *   **Spans (绿色/黄色)**：代表工具调用或函数执行。
    *   **找重点**：找到 `execute_python_code` 这一行，点击它，查看 `Input` 中的 `code` 字段，确认 Python 代码是否正确生成。

### 常见 Debug 技巧
*   **Token 消耗**：在 Trace 列表页，查看 `Usage` 列，了解本次任务消耗了多少 Token（钱）。
*   **延迟分析**：在 Trace 详情页，观察 Timeline 上的长条，找出哪个步骤最慢（通常是 LLM 生成或网络请求）。
*   **错误定位**：如果执行失败，Trace 会显示红色的 Error 标记，点击即可看到完整的 Traceback 堆栈信息。
