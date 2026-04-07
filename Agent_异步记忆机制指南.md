# 异步记忆保存实现指南 (Async Memory Save Guide)

你已经成功优化了摘要阈值（`>50`），也修正了图的串行逻辑（避免了重复触发）。现在，只差最后一步就能让 Agent 响应速度"起飞"：**异步保存记忆**。

## 1. 为什么要异步？
目前的流程：
`Generate Response` (3s) -> `Save Memory` (2s) -> `END` (用户看到回复)
**用户总等待：5s**

异步后的流程：
`Generate Response` (3s) -> 启动后台线程保存 -> `END` (用户看到回复)
**用户总等待：3s** (瞬间快了 40%)

---

## 2. 代码实现指南

请修改 `tong_agent/graph.py` 中的 `save_memory_node` 函数。

### 第一步：导入线程模块
在文件头部导入 `threading`：
```python
import threading
```

### 第二步：定义后台任务函数
把原来 `save_memory_node` 里的核心逻辑（连接 Mem0、保存数据）抽离出来，变成一个独立的函数 `save_memory_task`。

```python
def save_memory_task(user_msg: str, ai_msg: str):
    """
    后台线程执行的保存任务，不阻塞主流程。
    """
    if not user_msg or not ai_msg:
        return

    try:
        print(f"--- [Async Background] 开始保存记忆... ---")
        m = get_mem0_client()
        interaction = f"User: {user_msg}\nAI: {ai_msg}"
        m.add(interaction, user_id="user_123")
        print(f"--- [Async Background] 记忆保存成功 ---")
    except Exception as e:
        print(f"--- [Async Background] 保存失败: {e} ---")
```

### 第三步：修改 Node 函数
让 Node 函数只负责"启动线程"，然后立刻返回。

```python
def save_memory_node(state: AgentState):
    """
    启动异步线程保存记忆，自身立即返回。
    """
    print("--- [Node: Save Memory] 启动异步保存任务 ---")
    messages = state["messages"]
    
    # 提取最近的一轮对话 (逻辑不变)
    user_msg = ""
    ai_msg = ""
    
    for m in reversed(messages):
        if isinstance(m, AIMessage) and not ai_msg:
            ai_msg = m.content
        if isinstance(m, HumanMessage) and not user_msg and ai_msg: 
            user_msg = m.content
        if user_msg and ai_msg:
            break
            
    # 启动线程 (Fire-and-Forget)
    if user_msg and ai_msg:
        t = threading.Thread(target=save_memory_task, args=(user_msg, ai_msg))
        t.start()
    else:
        print("DEBUG: No complete interaction found to save.")
            
    return {} # 立即返回，不等待线程结束
```

---

## 3. 为什么优化后还是感觉慢？(Troubleshooting)

如果你做完这一步，还是觉得慢，可能还有以下原因：

1.  **流式传输 (Streaming)**：你的 Web UI 或终端支持流式输出吗？
    *   如果不支持流式，用户必须等整个回复生成完才能看到第一个字。这会让人感觉很慢。
    *   *检查点*：你的 `get_model` 已经开启了 `streaming=True`，但这只意味着模型支持。你的前端（Streamlit）是否正确接收了 Chunk？

2.  **网络延迟**：
    *   连接 DeepSeek API 本身可能有延迟。
    *   连接 Mem0 (如果是在云端) 可能有延迟。

3.  **Trace 耗时**：
    *   LangFuse 的 Callback 可能会增加微小的网络开销，但通常是异步的，影响不大。

**下一步建议**：
先把这个异步保存加上，这是目前性价比最高的优化。如果还慢，我们就去查 Streamlit 前端的流式显示问题。
