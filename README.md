# TongAgent_langgraph

TongAgent_langgraph 是一个基于 [LangGraph](https://python.langchain.com/docs/langgraph/) 构建的企业级多智能体（Multi-Agent）系统，专为解决复杂中间件架构规划和深层次技术文档检索而设计。

它采用了 **Map-Reduce 并发架构** 和 **Agentic RAG 文件系统检索范式**，能够像资深架构师一样，自主拆解任务、并发查阅资料、并经过严格的 QA 评估后生成高质量的落地答案。

## 🌟 核心特性

- **Agentic RAG (文件系统检索)**：摒弃了传统的 ChromaDB 向量库，直接使用 `list_directory`, `search_file_content`, `read_file_content` 工具，避免了传统 RAG 容易出现的上下文截断问题。
- **并发工作流 (Map-Reduce)**：通过 Planner-Worker 架构，针对多组件问题自动拆解子任务，并利用 Python 的 asyncio 机制并发执行检索，大幅提升响应速度。
- **多重反馈机制 (ReAct & Evaluator)**：内置意图解析防泥潭机制和专门的 QA Evaluator 节点。如果生成的线索不足，评估员会将其驳回，要求 Agent 重新搜索。
- **记忆与摘要管理 (Mem0)**：支持通过 `mem0` 进行长期偏好记忆存储，并内置了对话超长时的自动摘要与历史修剪机制。
- **企业级工程化结构**：模块化的节点拆分、集中的配置管理、基于 Markdown 的 Prompt 管理和标准的 Logging 日志追踪。

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
 │   │   ├── llm_factory.py       # 统一的模型初始化工厂 (DeepSeek/Qwen)
 │   │   ├── logger.py            # 统一的日志配置 (RotatingFileHandler)
 │   │   └── tools_registry.py    # 统一管理工具列表和映射
 │   ├── nodes/                   # 核心：图的节点拆分 (每个 Node 一个独立文件)
 │   │   ├── __init__.py
 │   │   ├── classifier.py        # 意图分类节点
 │   │   ├── planner.py           # 复杂任务拆解节点
 │   │   ├── parallel_worker.py   # 并行执行子任务节点
 │   │   ├── intent_parse.py      # 单体核心思考节点 (ReAct 循环引擎)
 │   │   ├── tool_exec.py         # 工具执行节点
 │   │   ├── evaluator.py         # 质量检查与验收节点
 │   │   ├── generate_response.py # 最终回答生成节点
 │   │   ├── memory.py            # 长期记忆的检索与异步保存
 │   │   └── summarize.py         # 历史对话超长压缩节点
 │   ├── prompts/                 # 核心：提示词集中管理
 │   │   ├── __init__.py          # 负责将所有 Prompt 作为字符串变量导出
 │   │   ├── intent_parse.md      # ReAct Agent 核心指令
 │   │   ├── evaluator.md         # 质检员标准
 │   │   ├── generate_response.md # 回答生成规范
 │   │   └── summarization.md     # 摘要压缩指令
 │   ├── tools/                   # 核心：工具链包
 │   │   ├── __init__.py
 │   │   ├── file_tools.py        # 包含 ls, grep, read 等强大的文件探索工具
 │   │   └── ...                  # 其他网络或沙箱工具
 │   ├── graph.py                 # 核心：图组装车间 (Graph Builder)，纯粹定义连线和路由
 │   └── mem0_client.py           # 记忆库客户端封装
 ├── test_agentic_rag.py          # 测试入口文件
 ├── agent_run.log                # 运行时详细日志输出
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

1. **输入层**：用户发起提问，系统首先调用 `retrieve_memory_node` 加载历史偏好。
2. **分类层**：`classifier_node` 快速判断任务复杂度（SIMPLE/COMPLEX）。
3. **分发层 (如果复杂)**：`planner_node` 将大任务拆解为多个 JSON 描述的子任务。
4. **并发层**：`parallel_worker_node` 使用 `asyncio.gather` 并发拉起多个子 Agent，在知识库中疯狂查阅资料。
5. **单体层 (如果简单或子任务打回)**：`intent_parse_node` 和 `tool_exec_node` 构成 ReAct 循环，使用文件工具深度探索。
6. **质检层**：`evaluator_node` 根据用户需求和收集到的线索进行交叉验证。如果有缺失，则打回重做。
7. **输出层**：`generate_response_node` 遵循“零幻觉”原则输出带有文档引用的高质量 Markdown 回答。
8. **记忆层**：最后，后台异步线程会将本次有价值的交互信息通过 LLM 提炼后存入长程记忆库。
