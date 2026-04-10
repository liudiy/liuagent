# TongAgent_langgraph

TongAgent_langgraph 是一个基于 [LangGraph](https://python.langchain.com/docs/langgraph/) 构建的企业级多智能体（Multi-Agent）系统，专为解决复杂中间件架构规划和深层次技术文档检索而设计。

它采用了对标 Claude Code / OpenHands 的 **单体自治架构 (Autonomous Single-Agent)** 和 **Agentic RAG 文件系统检索范式**，能够像资深架构师一样，自主使用系统级 TODO 工具规划任务、利用强大的工具链深度查阅资料、并经过督导节点 QA 评估后生成高质量的落地答案。

## 🌟 新旧版本架构对比与核心优势 (Why the New Architecture?)

在老版本（即桌面上的 `liuagent-master`）中，系统依赖于传统的串行流水线、Map-Reduce 多智能体分发，以及硬暴力的节点隔离（如专门的 `generate_response` 节点来切断上下文）。虽然这保证了输出的稳定性，但在处理超大规模架构文档时显得僵化、极度消耗 Token 且容易丢失全局上下文。

新版本的 `TongAgent_langgraph` 全面重构为现代的单体 Agentic RAG 架构，带来了以下核心优势：

## 🌟 核心特性

- **Agentic RAG (文件系统检索)**：摒弃了传统的 ChromaDB 向量库，直接使用 `list_directory`, `search_file_content`, `read_file_content` 工具，像人类程序员一样进行“渐进式揭露”，避免了传统 RAG 容易出现的跨段落上下文截断问题。
- **自治单体架构 (Autonomous Single-Agent)**：废弃了臃肿的 Planner-Worker Map-Reduce 架构。现在由一个强大的主干 Agent (`intent_parse`) 统揽全局。它利用 `update_todo_list` 工具将任务状态强行注入系统底层，实现了“边探索、边做笔记、边调整计划”的高度自治闭环。
- **并行工具调用 (Parallel Tool Calling)**：虽然是单体大脑，但在执行层充分利用了大模型的原生 Parallel Function Calling 能力。Agent 可以在一轮思考中同时发起对多个文件的 `read` 或 `grep`，极大地提升了检索效率。
- **多重反馈机制 (ReAct & Evaluator)**：内置异常捕获防卡死机制和专门的 QA Evaluator 节点。如果生成的答案缺乏文档依据，评估员会将其驳回，给出具体指导要求 Agent 重新搜索（渐进式纠偏）。
- **记忆与摘要管理 (Mem0)**：支持通过 `mem0` 进行长期偏好记忆存储，并内置了对话超长时的自动摘要与历史修剪机制。
- **企业级工程化结构**：模块化的节点拆分、集中的配置管理、基于 Markdown 的 Prompt 管理和标准的 Logging 日志追踪。

## 📜 近期深度重构与架构优化日志
详细的新旧架构对比（如 Map-Reduce 的废弃、单脑自治的引入、动态检索的实现等），请查阅专门的 [CHANGELOG.md](./CHANGELOG.md) 更新日志。

## 📂 项目结构

项目遵循大厂的 Clean Architecture 规范进行重构：

```text
TongAgent_langgraph/
 ├── tong_agent/
 │   ├── config/                  # 核心：集中配置管理
 │   │   ├── __init__.py
 │   │   └── settings.py          # 使用 Pydantic 或 os.environ 管理环境变量
 │   ├── core/                    # 核心：图的基础设施
 │   │   ├── __init__.py
 │   │   ├── state.py             # AgentState 和各类 TypedDict/Pydantic 结构体定义
 │   │   ├── llm_factory.py       # 统一的模型初始化工厂 (带超时和重试机制)
 │   │   ├── logger.py            # 统一的日志配置
 │   │   └── tools_registry.py    # 统一管理工具列表和映射
 │   ├── nodes/                   # 核心：图的节点拆分 (每个 Node 一个独立文件)
 │   │   ├── intent_parse.py      # 单体核心思考节点 (主干 Agent，负责规划、执行、总结交卷)
 │   │   ├── tool_exec.py         # 工具执行节点
 │   │   ├── evaluator.py         # 质量检查与验收节点 (督导 Agent)
 │   │   ├── memory.py            # 长期记忆的检索与异步保存
 │   │   └── summarize.py         # 历史对话超长压缩节点
 │   ├── prompts/                 # 核心：提示词集中管理
 │   │   ├── intent_parse.md      # 主干 Agent 核心指令与行为边界
 │   │   ├── evaluator.md         # 质检员标准与纠偏法则
 │   │   └── summarization.md     # 摘要压缩指令
 │   ├── tools/                   # 核心：工具链包
 │   │   ├── __init__.py
 │   │   ├── file_tools.py        # 包含 ls, grep, read 等文件系统探索工具
 │   │   ├── notebook_tools.py    # 包含 update_todo_list 状态注入工具
 │   │   ├── server_tools.py      # 服务器库存及部署工具
 │   │   ├── aliyun_web_search.py # 联网搜索工具
 │   │   └── code_interpreter_tool.py # 代码沙箱工具
 │   ├── graph.py                 # 核心：图组装车间 (Graph Builder)，定义单体架构循环与兜底逻辑
 │   └── mem0_client.py           # 记忆库客户端封装
 ├── clean_md_files.py            # 辅助脚本：PDF转MD后的文本断行与格式清洗
 ├── test_agentic_rag.py          # 核心测试入口：基于本地 MD 目录的 Agentic RAG
 ├── agent_run.log                # 运行时详细日志输出
 ├── CHANGELOG.md                 # 重构与架构演进日志
 └── README.md                    # 本说明文档
```

## 🛠️ 快速开始

### 1. 环境准备

确保你安装了 Python 3.11+，并在虚拟环境中安装依赖。

```bash
# 创建并激活虚拟环境
python -m venv .venv
source .venv/Scripts/activate  # Windows
# source .venv/bin/activate    # Linux/Mac

# 安装核心依赖 (示例，具体请参考实际的 requirements.txt)
pip install langgraph langchain-openai langchain-core pydantic mem0ai
```

### 2. 配置环境变量

你需要提供相关的模型 API Key，可以直接在终端中设置：

```bash
# Windows (PowerShell)
$env:DEEPSEEK_API_KEY="your_deepseek_api_key_here"
$env:DASHSCOPE_API_KEY="your_dashscope_api_key_here"
$env:DISABLE_MEM0="true"  # 如果不想连接远端 Mem0 数据库，可将其禁用
```

### 3. 运行测试

使用根目录的 `test_agentic_rag.py` 作为入口启动测试：

```bash
python test_agentic_rag.py
```

你也可以使用 `pytest` 运行（如果配置了相关的断言测试）。

## 🧠 工作流 (Workflow) 简述

1. **输入层**：用户发起提问，系统首先调用 `retrieve_memory_node` 加载历史偏好（若启用）。
2. **初始化与规划 (Context Compaction)**：主干 Agent (`intent_parse_node`) 接收任务后，被强制要求调用 `update_todo_list` 工具。它会将任务拆解为具体的 TODO 步骤，并持久化在 System Prompt 的顶部。
3. **探索与执行循环 (ReAct Engine)**：
   - `intent_parse_node` 利用 `list_directory`, `search_file_content`, `read_file_content` 等文件系统工具，在文档目录中进行深度的“渐进式揭露”搜索。
   - `tool_exec_node` 并发执行工具调用并返回原始结果。
   - 每次获得关键线索后，Agent 都会再次调用 `update_todo_list`，将新发现压缩进工作笔记 (notes) 中，防止历史对话折叠导致失忆。
4. **自治交卷 (Autonomous Synthesis)**：当 TODO 列表完成，或者达到 50 步的探索极限时，主干 Agent 会利用其积累的工作笔记，主动输出最终的自然语言解答。
5. **质检与纠偏层 (Evaluator)**：`evaluator_node` 作为督导员，对主干 Agent 提交的答案进行逻辑和证据审核。
   - 若发现遗漏或无证据的编造，则将其打回，给出具体的修改建议（渐进式纠偏）。
   - 若答案完美，则放行。
6. **记忆层**：最后，后台异步线程会将本次有价值的交互信息通过 LLM 提炼后存入长程记忆库。
