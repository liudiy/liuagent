# TongAgent 进阶路线图 (Roadmap)

为了将 TongAgent 从一个“高分 Demo”进化为“企业级产品”，我们需要在以下四个维度进行深化。完成这些改造后，你的项目将具备真实的商业交付价值。

## 📅 第一阶段：服务化与并发 (Current Focus)
**目标**：摆脱脚本运行模式，支持多用户并发访问。
- [x] **API 封装**: 使用 `FastAPI` 将 Agent 封装为 RESTful 接口 (`POST /chat`)。
- [ ] **异步支持**: 确保 LangGraph 的 `ainvoke` 能够正确处理并发请求，不阻塞主线程。
- [ ] **API 文档**: 利用 FastAPI 自动生成 Swagger UI 文档。

## 📅 第二阶段：数据持久化 (Persistence)
**目标**：确保服务器重启后，用户的对话历史和长期记忆不丢失。
- [ ] **Redis Checkpointer**: 将 `MemorySaver` (内存) 替换为 `RedisSaver`。
    - *面试考点*: 为什么用 Redis？(速度快、支持 TTL、分布式锁)。
- [ ] **Postgres for Analytics**: 将对话日志写入 PostgreSQL，用于后续分析用户行为。

## 📅 第三阶段：可观测性 (Observability)
**目标**：打开 Agent 的“黑盒”，看清每一步的延迟和 Token 消耗。
- [ ] **接入 Langfuse**:
    - 记录完整的 Trace（意图识别 -> 检索 -> 工具调用 -> 反思）。
    - 统计 Token 成本和延迟。
    - *亮点*: 在面试中展示 Langfuse 的截图，证明你对系统内部了如指掌。

## 📅 第四阶段：微调与垂直领域优化 (SFT)
**目标**：在特定领域超越通用模型。
- [ ] **数据收集**: 利用 Langfuse 收集的用户真实对话数据。
- [ ] **模型微调**: 使用 LLaMA-Factory 对 Qwen-7B 进行 LoRA 微调，强化其对 "TongWeb" 报错日志的理解能力。

---
**🚀 今日行动**: 我们将立即完成 **第一阶段 (FastAPI 服务化)**，这是最显眼、最容易在简历上展示的成果。
