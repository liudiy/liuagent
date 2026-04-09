# 📖 OpenClaw / OpenClaudeCode (Python版) 源码学习与架构精解

本文档用于持续记录对 Python 版本的 Claude Code 替代品 **OpenClaw (OpenClaudeCode)** 的源码阅读心得、架构拆解，以及对当前 TongAgent 的演进启发。

> ⚠️ **核心原则与视角（根据 Core Memory 自动记录规则）**：
> 遵循我们在阅读 OpenHands 时确立的严格规则，所有从该项目中提炼出的启发和学习点，都必须严格区分以下两个视角进行总结：
> 1. **【工程化角度】**：关注系统架构、性能、并发、解耦、安全性设计、交互体验等。
> 2. **【Agent 角度】**：关注大模型驱动策略、Prompt 设计、上下文管理（如折叠机制）、意图解析、工具调用边界、任务拆解与子 Agent 编排等。

---

## 🌟 1. 为什么学习 Python 版的 Claude Code？
因为我们的 TongAgent 本身就是基于 Python 和 LangGraph 构建的。官方原版 Claude Code 是一整坨几十万行的 Node.js / TypeScript 混淆代码（`cli.mjs`），我们只能从中学习“灵魂”（如 Prompt 设计）。
而 **OpenClaw (OpenClaudeCode)** 则是用 Python 对其进行了“骨肉级”的复刻。学习它，意味着我们可以直接“抄代码”！
它带来的最大价值在于：
*   **Plan Mode (计划模式)**：学习如何强制 AI 在写代码前先进行思考、分析和制定 Spec。
*   **AgentFlow (意图编排)**：学习如何将大任务拆解并分发给多个子 Agent（如搜索 Agent、执行 Agent）。
*   **纯净版底层工具链**：学习它是如何用 Python 优雅地封装 `Read`、`Bash` 和 `Grep` 的。

---

## 🏗️ 2. 源码准备与核心目录结构拆解
我们克隆了 `OpenClaudeCode` 的源码进行剖析，其核心目录结构非常清爽，典型的轻量级 Python 架构：
*   `main.py`: CLI 的入口，负责解析命令行参数并调度核心执行逻辑。
*   `core/`:
    *   `registry.py`: 工具注册中心（Tool Registry）。
    *   `tool.py`: 工具的基类定义（Tool Interface）。
*   `tools/`: 核心的四大工具实现。
    *   `bash_tool.py`: 负责执行终端命令。
    *   `file_read_tool.py`: 负责读取文件。
    *   `grep_tool.py`: 负责正则表达式搜索。
    *   `task_tool.py`: 负责子任务分发。
*   `agents/`:
    *   `manager.py`: 子 Agent（如架构师、测试编写者等）的编排与调度器。

---

## 🔍 3. 核心机制精解：Tool 与 Agent 的协同

### 3.1 【工程化角度】轻量级的依赖注入与注册表 (Tool Registry)
在 `main.py` 的初始化中，OpenClaudeCode 采用了一种极简的注册表模式：
```python
def setup_tools(self):
    tool_registry.register_tool(FileReadTool())
    tool_registry.register_tool(BashTool())
    tool_registry.register_tool(GrepTool())
    tool_registry.register_tool(TaskTool())
```
**启发**：
比起 OpenHands 复杂的动态类加载，这种显式的单例注册表非常适合初创 Agent 框架。TongAgent 目前在 `tools.py` 中直接暴露函数数组给 LangGraph，未来如果要做到插件化，可以参考引入一个全局的 `ToolRegistry`。

### 3.2 【工程化角度】BashTool 的沙箱逃逸防御与异步超时
查看 `tools/bash_tool.py`，它对终端命令执行做了非常好的防护：
1. **危险命令黑名单**：拦截了诸如 `rm -rf`, `chmod 777`, `:(){:|:&};:` (Fork 炸弹) 等极具破坏性的命令。
2. **安全参数转义**：使用 `shlex.quote(command)` 对命令进行转义，防止 Bash 注入。
3. **异步超时控制**：
```python
stdout, stderr = await asyncio.wait_for(
    process.communicate(),
    timeout=timeout_ms / 1000.0
)
```
这保证了大模型如果写了一个会死循环的代码（比如 `while True: pass`），系统会在设定时间后自动 `kill` 进程，防止服务器资源被耗尽。
**启发**：TongAgent 在实现代码执行工具时，必须强制引入 `asyncio.wait_for` 和 `shlex.quote` 这两道安全门。

### 3.3 【Agent 角度】多角色子 Agent 的编排设计 (Agent Manager)
在 `agents/manager.py` 中，作者定义了 4 种经典的子 Agent 角色：
1. `general-purpose` (通用助手): Temperature 0.7
2. `code-reviewer` (代码审查员): Temperature 0.3 (低温度保证严谨)
3. `architect` (架构师): Temperature 0.8 (高温度激发创造力)
4. `test-writer` (测试编写员): Temperature 0.5

**启发**：
大模型在扮演不同角色时，所需的参数（如 Temperature）和工具权限是不同的。
*   写测试的 Agent 必须拥有 `Bash` 权限去跑单测；
*   做代码审查的 Agent 只需要 `Read` 和 `Grep` 权限，防止它乱改代码；
*   架构师的温度要调高，让它发散思维。
这种**“按需分配角色、参数与工具权限”**的策略，是高级 Agent 意图编排（AgentFlow）的灵魂。

---

> 💡 *注：我们将继续深入挖掘其 TaskTool 的子任务拆解逻辑，并实时更新至本文档。*
