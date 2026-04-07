# TongAgent 深度优化全景指南 (Agent Optimization Guide)

基于当前版本（v2.0 - Docker部署/多步推理修复/Prompt泛化）的状态，以下是针对您的 Agent 系统接下来的**深度优化建议**。这些建议涵盖了**知识库质量**、**推理能力**、**系统架构**和**用户体验**四个维度。

## 1. RAG 知识库与检索增强 (Knowledge & Retrieval) - **最优先**
目前 Agent 的最大短板在于“知识盲区”（例如缺失并发调优参数）。

### 1.1 补全核心技术文档
*   **现状**：当前向量库主要包含《安装指南》，缺少深度运维文档。
*   **优化行动**：
    *   **上传《TongWeb技术白皮书》/《用户手册》**：补充关于线程池 (`maxThreads`)、JDBC连接池、JVM参数等核心配置的详细说明。
    *   **上传《性能调优指南》**：专门针对高并发场景的官方调优建议。
    *   **上传《常见报错与解决方案 (Troubleshooting)》**：覆盖 `OutOfMemoryError`、`ConnectionTimeout` 等常见运维问题的排查步骤。
    *   **操作**：将新 PDF 放入 `data/` 目录，重新运行 `preprocess_docs.py` 和 `build_vector_store.py`。

### 1.2 引入高级检索策略 (Advanced RAG)
*   **现状**：使用混合检索 (Hybrid Search) + 重排序 (Reranking)，但对用户模糊问题的理解仍有限。
*   **优化行动**：
    *   **查询重写 (Query Rewriting / HyDE)**：在检索前，先让 LLM 生成一个“假设性答案”或“标准查询语句”，用生成的文本去检索，而不是用用户口语化的问题去检索。
        *   *例子*：用户问“怎么调优？”，重写为“TongWeb 性能调优参数及配置方法”。
    *   **多路召回优化**：目前是 BM25 + Vector。可以加入 **关键词提取 (Keyword Extraction)** 召回，确保专有名词（如 `tongweb.xml`）不被忽略。

## 2. Agent 推理与执行能力 (Reasoning & Execution)
Agent 目前能“读文档”，但还不能“动手操作”或“深度分析”。

### 2.1 引入代码解释器 (Code Interpreter)
*   **场景**：用户上传一个 `server.log` 报错日志文件，让 Agent 分析。
*   **优化**：集成一个沙箱 Python 环境（如 E2B 或本地 Docker 容器），让 Agent 能写 Python 代码去**解析日志文件**、**统计错误频率**、**绘制性能曲线图**，而不仅仅是靠 LLM“读”日志（Token 限制）。

### 2.2 增加运维诊断工具 (Diagnostic Tools)
*   **场景**：用户问“我的服务器现在卡顿怎么办？”
*   **优化**：
    *   **SSH 远程执行工具**：(需授权) 允许 Agent 连接到目标服务器执行 `top`、`free -m`、`netstat` 等命令，实时获取系统状态。
    *   **配置文件检查工具**：编写 Python 脚本，自动读取 `tongweb.xml` 并检查关键参数是否符合最佳实践（如检查 `maxThreads < 200` 是否过小）。

## 3. 系统架构与生产级部署 (Architecture & Production)
现在的部署是 Docker 容器化的，但距离真正的“企业级 SaaS”还有差距。

### 3.1 Nginx 反向代理与 HTTPS
*   **现状**：直接暴露 `8501` 端口，使用 HTTP 协议，不安全且不专业。
*   **优化**：
    *   配置 Nginx 反向代理，将 `http://liuagent.cloud` (80/443) 转发到内部的 `8501`。
    *   申请免费 SSL 证书 (Let's Encrypt)，启用 **HTTPS**，保护用户数据安全。

### 3.2 监控与可观测性 (Observability)
*   **现状**：虽然集成了 LangFuse，但可能未深度使用。
*   **优化**：
    *   **全链路追踪**：确保每一个 `Graph Node`（规划、检索、生成）的耗时和 Token 消耗都在 LangFuse 中可视化。
    *   **成本监控**：设置 Token 使用量告警，防止 API 费用超支。
    *   **用户反馈闭环**：在前端增加“点赞/点踩”按钮，收集用户对回答的反馈（Bad Case），用于后续优化 Prompt 或知识库。

## 4. 前端交互体验 (User Experience)
Streamlit 适合快速原型，但交互上限较低。

### 4.1 界面升级
*   **现状**：Streamlit 原生界面，聊天气泡样式简单。
*   **优化**：
    *   **自定义 CSS**：美化 Streamlit 界面，使其更符合品牌调性。
    *   **迁移至 React/Next.js** (长期计划)：如果需要更复杂的交互（如拖拽上传日志、多窗口并行任务），建议前后端分离，后端保持 FastAPI，前端重构为现代 Web 应用。

### 4.2 引导式对话
*   **优化**：
    *   **预设问题 (Starter Questions)**：在对话开始时提供“如何安装？”、“性能调优？”等快捷按钮。
    *   **追问机制 (Follow-up Questions)**：Agent 回答完后，自动生成 3 个相关问题供用户点击（例如回答完安装后，自动推荐“如何配置 License？”）。

---

### 🚀 建议的实施路线图
1.  **本周 (P0)**：**补充知识库**（上传更多 PDF），解决“并发调优”等知识盲区。
2.  **下周 (P1)**：**配置 Nginx + HTTPS**，让 `liuagent.cloud` 域名正式可用。
3.  **下月 (P2)**：**集成 SSH/诊断工具**，让 Agent 从“咨询顾问”进化为“运维助手”。
