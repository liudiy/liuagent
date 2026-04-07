# TongAgent 状态机图逻辑结构详解

本文档详细描述了 TongAgent 基于 LangGraph 构建的状态机（State Graph）的逻辑结构。Agent 的执行流程本质上是一个有向图，节点（Nodes）代表具体的执行动作，边（Edges）代表节点间的流转逻辑。特别是**条件边（Conditional Edges）**，决定了 Agent 如何根据当前状态动态选择下一步。

## 1. 整体架构概览

TongAgent 的图结构分为“快速通道（Fast Path）”和“慢速反思通道（Slow Path）”。

**核心节点列表：**
*   `retrieve_memory_node`: 并行提取 Mem0 长期记忆。
*   `context_update_node`: 并行更新系统时间、服务器状态等环境上下文。
*   `summarize_conversation_node`: 压缩历史对话，防止 Token 溢出。
*   `intent_parse_node`: 核心路由节点，识别用户意图并决定调用哪个工具。
*   `tool_exec_node`: 工具执行节点（如 RAG、联网搜索、代码执行）。
*   `reflection_node`: 结果反思节点，评估工具执行结果。
*   `reselect_logic_node` / `continue_logic_node`: 辅助逻辑节点。
*   `generate_response_node`: 最终回复生成节点。
*   `save_memory_node`: 保存重要信息到长期记忆。

---

## 2. 执行流程与条件触发详解

以下是 Agent 从接收用户输入到生成回复的完整路径拆解。

### 阶段 1：上下文准备 (Context Preparation)

当用户输入一个新的 Query 时，图的执行从 `START` 开始。

*   **节点执行**：
    1.  `START` -> `retrieve_memory`
    2.  `START` -> `context_update`
    3.  `START` -> `summarize_conversation`
*   **说明**：这三个节点是**并行执行**的。它们负责为 LLM 准备充足的上下文（包括过去的记忆、当前的系统状态、以及压缩后的历史对话）。

### 阶段 2：意图识别与路由 (Intent Parsing & Routing)

准备好上下文后，流程汇总到意图解析节点。

*   **执行节点**：`intent_parse`
*   **动作**：LLM（DeepSeek/OpenAI）阅读用户问题和上下文，决定是直接回答，还是需要调用工具。

#### ⚡ 条件边 1：`route_intent`
此条件边位于 `intent_parse` 节点之后，决定接下来的走向。

*   **触发条件与流向**：
    *   **条件 A: `intent == "tool_call"`**
        *   **触发场景**：LLM 认为必须使用工具才能回答（例如，它输出了一个调用 `aliyun_web_search` 的指令）。
        *   **流向**：`-> tool_exec` (去执行工具)。
        *   **例子**：用户问“今天杭州天气如何？”，LLM 发现自己不知道，决定调用搜索工具。
    *   **条件 B: `intent != "tool_call"` (通常是 "conversation")**
        *   **触发场景**：LLM 认为仅凭自己的知识或现有的上下文就能回答，不需要外部工具。
        *   **流向**：`-> reflection` (直接去生成回复的通道)。
        *   **例子**：用户问“你好，你叫什么名字？”，LLM 可以直接回答。

### 阶段 3：工具执行与“快慢通道” (Tool Execution & Fast/Slow Path)

如果进入了 `tool_exec` 节点，Python 代码将实际执行被选中的工具（如查询数据库、搜索网络）。执行完毕后，迎来了**最关键的性能分水岭**。

#### ⚡ 条件边 2：`route_tool_exec`
此条件边位于 `tool_exec` 节点之后，决定是走“极速生成”还是“反思重试”。

*   **触发条件与流向**：
    *   **条件 A: `all_success == True` (快速通道 - Fast Path)**
        *   **触发场景**：工具执行完毕，且返回的结果中没有包含明确的 `Error` 或 `Exception` 报错信息。
        *   **流向**：`-> generate_response` (跳过反思，直接生成答案)。
        *   **例子**：RAG 工具成功检索到了 5 个相关的文档片段，将其拼接为字符串返回。系统认为执行成功，直接将这 5 个片段喂给生成节点回答用户。
    *   **条件 B: `all_success == False` (慢速通道 - Slow Path)**
        *   **触发场景**：工具执行崩溃，或者返回了网络超时等明确的错误信息。
        *   **流向**：`-> reflection` (进入反思节点分析错误原因)。
        *   **例子**：`execute_python_code` 工具因为语法错误抛出了 `SyntaxError`，系统将其导向反思节点，让 LLM 看看错在哪了。

### 阶段 4：反思与纠错 (Reflection & Retry)

只有在工具报错，或者不需要调用工具（纯聊天）时，才会进入 `reflection` 节点。

#### ⚡ 条件边 3：`route_reflection`
此条件边位于 `reflection` 节点之后。反思节点会输出一个 JSON 格式的决定 (`next_action`)。

*   **触发条件与流向**：
    *   **条件 A: `next_action == "reselect_tool"`**
        *   **触发场景**：反思节点认为当前工具不适用，或者参数给错了，需要换个思路。
        *   **流向**：`-> reselect_logic -> intent_parse` (回到起点重新选工具)。
        *   **例子**：第一次用 RAG 查不到关于“特朗普最新推文”的信息，反思节点建议改用 `aliyun_web_search` 重新尝试。
    *   **条件 B: `next_action == "retry"`**
        *   **触发场景**：工具执行因为临时网络问题失败，反思节点认为再试一次可能成功。
        *   **流向**：`-> continue_logic -> tool_exec` (直接重新执行工具)。
    *   **条件 C: `next_action == "finish"` 或其他**
        *   **触发场景**：不需要工具（纯聊天），或者虽然之前工具报错但反思节点认为不需要再试了。
        *   **流向**：`-> generate_response` (去生成最终回答)。

### 阶段 5：生成与记忆 (Generation & Memory)

无论经历了怎样的波折，最终流程都会来到 `generate_response`。

*   **执行节点**：`generate_response`
*   **动作**：LLM 根据收集到的所有信息（历史对话、环境、检索结果），生成最终的自然语言回复发给用户。

*   **执行节点**：`save_memory`
*   **动作**：在回答用户后，最后一步是分析这轮对话中是否有值得长期保存的偏好或事实（例如用户说“我讨厌看长文”），如果有，则写入 Mem0。

*   **流向**：`save_memory -> END` (本次图执行结束，等待用户的下一条消息)。

---

## 3. 为什么“复杂问题”现在无法像 Trae 那样先规划？

当前的逻辑是偏向于 **Reactive (反应式)** 的：遇到问题 -> 找工具 -> 找工具 -> 拿到结果就回答。这在 90% 的简单场景（查资料、看状态）下速度极快。

但如果是 **“帮我分析当前 CPU 占用最高的前三个进程，并杀掉它们”** 这种复杂任务，当前的图结构会显得笨拙，因为它可能需要反复在 `intent_parse -> tool_exec -> reflection -> intent_parse` 这个循环里绕圈子。

**Trae 的做法 (Adaptive Planning)**：
Trae 或高级 Agent 会在图的最开始加入一个 **Classifier (分类器)** 节点。
*   如果是简单查询：走现在的 Fast Path 图。
*   如果是复杂指令：走 Planner Path。Planner 会先生成一个明确的 Todo List：
    1. 查 CPU。
    2. 解析结果找前三。
    3. 循环杀进程。
    然后让 Agent 严格按照 Todo List 步进执行，而不是靠盲目的 Reflection 来碰运气。

如果未来需要提升复杂任务处理能力，我们需要在图的起点引入这种 Planner 架构。