# Planner Node 实现指南：为 TongAgent 增加"规划大脑"

这份文档将指导你如何在 `TongAgent` 中实现类似 Deer Flow 的任务规划能力。我们将通过增加一个 `planner_node` 和更新 `AgentState` 来实现。

---

## 1. 目标
让 Agent 在执行复杂任务前，不再只是在 Prompt 里"嘴上说说"（输出 `<plan>` 文本），而是生成一个**结构化的 Todo List**，并强制按顺序执行。

## 2. 第一步：修改状态 (State)

在 `tong_agent/graph.py` 中，更新 `AgentState` 定义，增加 `todos` 字段。

```python
# tong_agent/graph.py

class AgentState(TypedDict):
    # ... (原有字段)
    messages: Annotated[list[BaseMessage], add_messages]
    
    # 新增字段：结构化计划列表
    # 格式示例：["搜索股价", "搜索财报", "计算比率", "生成报告"]
    todos: Optional[list[str]] 
    
    # ... (其他字段)
```

## 3. 第二步：定义 Planner Node 提示词

新建文件 `tong_agent/planner_node_prompt.py`。

```python
# tong_agent/planner_node_prompt.py

PLANNER_NODE_INSTRUCTION = """
你是一个高级任务规划师。你的目标是将用户的自然语言请求拆解为可执行的、线性的步骤列表。

### 输出格式要求
请直接输出一个 JSON 列表 (List[str])，不要包含任何 Markdown 代码块标记（如 ```json），也不要包含任何解释。

### 示例
用户输入："帮我对比一下阿里云和腾讯云的服务器价格，并写个报告"
输出：
[
    "搜索阿里云 ECS 服务器最新价格表",
    "搜索腾讯云 CVM 服务器最新价格表",
    "整理并对比两者的价格数据",
    "撰写对比报告"
]

### 任务
用户请求：{user_request}
请生成计划：
"""
```

## 4. 第三步：实现 Planner Node

在 `tong_agent/graph.py` 中添加 `planner_node` 函数。

```python
# tong_agent/graph.py

from tong_agent.planner_node_prompt import PLANNER_NODE_INSTRUCTION
import json

@observe()
def planner_node(state: AgentState, config: RunnableConfig):
    """
    Planner Node: 将复杂任务拆解为结构化 Todo List
    """
    print("--- [Node: Planner] 正在制定计划 ---")
    messages = state["messages"]
    
    # 获取用户最新的一条消息
    last_human_message = ""
    for m in reversed(messages):
        if isinstance(m, HumanMessage):
            last_human_message = m.content
            break
            
    if not last_human_message:
        return {}

    # 1. 准备 Prompt
    prompt = PLANNER_NODE_INSTRUCTION.format(user_request=last_human_message)
    
    # 2. 调用模型 (强制 JSON 模式)
    model = get_model(config)
    model_json = model.bind(response_format={"type": "json_object"})
    
    try:
        response = model_json.invoke([SystemMessage(content=prompt)])
        content = response.content
        
        # 3. 解析 JSON
        # 注意：有些模型可能会包裹在 key 中，这里假设是纯 list
        # 如果模型输出 {"steps": [...]}, 需要适配
        todos = json.loads(content)
        
        # 容错：如果输出是字典，尝试提取 list
        if isinstance(todos, dict):
            # 尝试找常见的 key
            for key in ["steps", "plan", "todos", "tasks"]:
                if key in todos and isinstance(todos[key], list):
                    todos = todos[key]
                    break
            else:
                # 找不到 list，就当做单步任务
                todos = [last_human_message]
                
        print(f"DEBUG: Generated Plan: {todos}")
        
        return {"todos": todos}
        
    except Exception as e:
        print(f"Error in planner node: {e}")
        return {"todos": []} # 失败则为空，回退到普通模式
```

## 5. 第四步：修改 Intent Parse Node (执行计划)

让 `intent_parse_node` 能感知并执行 `todos`。

```python
# tong_agent/graph.py - intent_parse_node

def intent_parse_node(state: AgentState, config: RunnableConfig):
    # ... (原有代码)
    
    # 获取当前的 todos
    todos = state.get("todos", [])
    
    # 如果有待办事项，取出第一个作为当前任务
    current_task = ""
    if todos and len(todos) > 0:
        current_task = todos[0]
        print(f"--- [Planner] 当前聚焦任务: {current_task} ---")
        
        # 将当前任务注入到 System Prompt 中，强制模型只关注这一步
        system_prompt += f"\n\n【当前任务锁定】\n你有一个正在执行的计划。当前必须专注完成这一步：'{current_task}'。\n请忽略后续步骤，只为这一步选择工具。"
    
    # ... (后续调用 LLM 的代码不变)
```

## 6. 第五步：更新图结构 (Graph)

修改 `get_graph` 函数，把 `planner_node` 加进去。

```python
# tong_agent/graph.py - get_graph

def get_graph(checkpointer=None):
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("planner", planner_node) # 新增
    # ... (其他节点)
    
    # 修改连线：Start -> Retrieve Memory -> Context Update -> Summarize -> PLANNER -> Intent Parse
    
    # 假设原来的连线是：
    # workflow.add_edge("summarize_conversation", "intent_parse")
    
    # 现在改为：
    workflow.add_edge("summarize_conversation", "planner")
    workflow.add_edge("planner", "intent_parse")
    
    # ... (其他连线不变)
```

## 7. (进阶) 如何完成一个 Todo？

你还需要一个机制来**移除**已完成的 Todo。
可以在 `reflection_node` 中判断：如果 `execution_result` 是 success，就从 `state["todos"]` 里 pop 掉第一个元素。

```python
# tong_agent/graph.py - reflection_node

def reflection_node(state: AgentState, config: RunnableConfig):
    # ... (原有反思逻辑)
    
    # 如果判断当前步骤成功完成
    if reflection.next_action == "continue" or reflection.next_action == "finish":
        todos = state.get("todos", [])
        if todos:
            completed_task = todos.pop(0) # 移除第一项
            print(f"--- [Planner] 任务完成: {completed_task} ---")
            
            # 如果还有剩余任务，强制 next_action = "continue" 以便循环回 intent_parse
            if todos:
                return {
                    "todos": todos,
                    "next_action": "continue",
                    "reflection": f"已完成 {completed_task}，继续下一步。"
                }
    
    # ...
```

---
**现在，你可以按照这个指南，自己动手去拼这个积木了！**
建议先从修改 `AgentState` 开始。
