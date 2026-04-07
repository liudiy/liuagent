# TongAgent vs. Deer Flow: 状态图与核心逻辑对比

本文详细对比了 TongAgent (`graph.py`) 与 Deer Flow Lead Agent (`agent.py`) 的架构差异。

## 1. 核心架构模式 (Pattern)

| 特性 | TongAgent (你的) | Deer Flow (参考) | 差异分析 |
| :--- | :--- | :--- | :--- |
| **构建方式** | **显式图 (Explicit Graph)** <br> 手动添加 Node (intent, tool_exec, reflection) 并定义 Edge。 | **LangChain Agent + Middleware** <br> 使用 `create_agent` 高级 API，通过 Middleware 注入逻辑。 | Deer Flow 封装程度更高，逻辑隐藏在 Middleware 中；TongAgent 逻辑更直观，便于学习底层原理。 |
| **状态管理** | **自定义 State (TypedDict)** <br> 包含 `messages`, `retry_count`, `next_action` 等显式字段。 | **ThreadState (继承 AgentState)** <br> 包含 `sandbox`, `artifacts`, `viewed_images` 等高级上下文。 | Deer Flow 的状态更丰富，原生支持沙盒和多媒体。 |
| **工具调用** | **手动执行节点 (tool_exec_node)** <br> 自己写代码解析 tool_calls 并调用函数。 | **LangGraph Prebuilt ToolNode** <br> 使用 LangGraph 内置的 `ToolNode` (虽然代码里没显式写，但 `create_agent` 内部使用了它)。 | 你手动实现了 ToolNode，这很好，能让你完全掌控执行过程。 |
| **反思机制** | **独立节点 (reflection_node)** <br> 显式的 LLM 调用进行反思。 | **Middleware + System Prompt** <br> 通过 `ClarificationMiddleware` 和 `ToolErrorHandlingMiddleware` 隐式处理错误和反思。 | TongAgent 的反思是"显性"的流程步骤；Deer Flow 的反思融入了 Prompt 和中间件拦截。 |

---

## 2. 状态定义对比 (State Schema)

### TongAgent (`AgentState`)
你主要关注**控制流**字段：
```python
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    retry_count: int                  # 重试计数
    next_action: Literal[...]         # 下一步动作
    reflection: Optional[str]         # 反思内容
    retrieved_memories: Optional[str] # 长期记忆
```

### Deer Flow (`ThreadState`)
它主要关注**资源与环境**字段：
```python
class ThreadState(AgentState):
    sandbox: SandboxState             # 沙盒 ID
    thread_data: ThreadDataState      # 文件路径 (workspace, uploads)
    uploaded_files: list[dict]        # 用户上传的文件
    viewed_images: dict               # 看过的图片
    todos: list                       # 待办事项 (由 TodoMiddleware 管理)
```

**💡 启示**：你的 State 偏向"流程控制"，Deer Flow 的 State 偏向"环境上下文"。未来你可以给 `AgentState` 增加 `workspace_path` 或 `sandbox_id`。

---

## 3. 关键逻辑实现对比

### A. 记忆 (Memory)
*   **TongAgent**: 
    *   **显式节点**: `retrieve_memory_node` 和 `save_memory_node`。
    *   **流程**: Start -> Retrieve -> ... -> Save -> End。
    *   **优点**: 逻辑非常清晰，一眼就能看出记忆在哪一步起作用。
*   **Deer Flow**:
    *   **Middleware**: `MemoryMiddleware`。
    *   **机制**: 在 `after_agent` 钩子中，异步将对话推入队列，由后台任务处理摘要和存储。
    *   **优点**: 不阻塞主流程，用户体验更流畅。

### B. 错误处理与重试
*   **TongAgent**:
    *   **显式循环**: `reflection` -> `retry_logic` -> `intent_parse`。
    *   **逻辑**: LLM 决定是否重试。
*   **Deer Flow**:
    *   **Middleware**: `ToolErrorHandlingMiddleware`。
    *   **逻辑**: 捕获工具异常 -> 转换成 ToolMessage (Status=Error) -> 让 LLM 在下一次 Token 预测时看到错误并自我纠正。

### C. 任务拆解
*   **TongAgent**:
    *   **单步执行**: 主要是"想 -> 做 -> 反思"的循环。
*   **Deer Flow**:
    *   **Sub-agents**: 通过 System Prompt (`prompt.py`) 引导模型将任务拆解为 `task` 工具调用。
    *   **并行执行**: 限制并发数 (`SubagentLimitMiddleware`)，支持一次性调用多个 Sub-agent。

---

## 4. 你的代码中有趣的发现 (DeepSeek 适配)
在 `graph.py` 中，你专门处理了 DeepSeek 模型的一个行为：
```python
if "<｜DSML｜invoke" in content or "<tool_code>" in content:
    # 强制转换为 reselect_tool 动作
```
这是非常实战的经验！Deer Flow 也有类似的适配代码（在 `models/patched_deepseek.py` 中），说明大家都在与模型的"个性"做斗争。

## 5. 总结与建议

**你的 TongAgent 架构非常清晰，且符合 LangGraph 的标准范式 (Nodes + Edges)。** 
相比之下，Deer Flow 采用了更复杂的 **Middleware** 模式，这让代码解耦了，但也增加了阅读难度。

**你可以借鉴的 "积木"：**

1.  **State 增强**:
    *   给 `AgentState` 增加 `files` 或 `workspace` 字段，为将来引入文件操作做准备。
2.  **Middleware 思想**:
    *   虽然你不用完全重写成 Middleware，但可以参考它的 `ClarificationMiddleware`（澄清中间件）。当用户指令模糊时（比如"部署应用"但不说是哪台服务器），主动暂停并询问用户，而不是瞎猜。
3.  **Prompt 工程**:
    *   阅读 `prompt.py`，特别是它如何通过 `<thinking_style>` 标签强制模型先思考再行动。你可以把这部分 Prompt 抄到你的 `INTENT_PARSE_NODE_INSTRUCTION` 中。

---
*文档生成时间: 2026-03-14*
