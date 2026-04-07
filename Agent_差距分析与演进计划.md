# Agent 差距分析与行动指南 (Gap Analysis & Action Plan)

这是一份基于最初 RAG 路线图 (`RAG_ROADMAP.md`) 与当前系统现状的深度对比分析。
**目标**：明确指出目前的 Agent 与“理想形态”之间的具体差距，并提供可执行的代码积木。

## 📊 总体差距概览

| 模块 | 理想形态 (Ideal) | 当前现状 (Current) | 差距 (Gap) | 优先级 |
| :--- | :--- | :--- | :--- | :--- |
| **检索精度** | 混合检索 + 重排序 + **元数据过滤** + **语义分块** | 混合检索 + 重排序 | 缺少元数据增强与语义分块，长文档检索容易断章取义 | 🔥 High |
| **查询理解** | **Query Rewrite (多路/HyDE)** + 意图识别 | 仅原始问题检索 | 用户提问模糊时（如“它多少钱”），检索完全失效 | 🔥 High |
| **记忆能力** | **多租户隔离** + 记忆清洗 | 单用户 + 全量保存 | 无法区分用户，长期运行会积累垃圾记忆，拖慢速度 | 🔥 High |
| **知识深度** | **GraphRAG (知识图谱)** | 纯文本切片 | 无法回答跨文档的全局总结性问题（如“对比A和B的区别”） | Medium |
| **评估体系** | **自动化 CI/CD 评分** | 人工肉眼看 | 每次改代码不知道效果是变好了还是变差了 | Medium |

---

## 🛠️ 行动指南：如何缩小差距 (Action Plan)

### 1. 攻克“检索精度”：语义分块 (Semantic Chunking)
**现状问题**：目前的切分是“每 1000 字切一刀”，不管话题有没有结束。导致检索时可能只搜到半截话。
**解决方案**：使用 Embedding 模型判断语义突变点进行切分。

#### 🧱 代码积木 (File: `preprocess_docs.py`)
> 请替换原有的 `chunk_docs` 函数。

```python
from langchain_experimental.text_splitters import SemanticChunker
from langchain_openai import OpenAIEmbeddings 

def chunk_docs(documents):
    # 使用语义模型来判断哪里该切分，而不是数格子
    # 注意：需要配置 OPENAI_API_KEY 或兼容的 Embedding 服务
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    text_splitter = SemanticChunker(
        embeddings,
        breakpoint_threshold_type="percentile", 
        breakpoint_threshold_amount=95
    )
    
    print(f"正在进行语义切分...")
    chunks = text_splitter.split_documents(documents)
    return chunks
```

### 2. 攻克“查询理解”：查询重写 (Query Rewrite)
**现状问题**：用户问“它怎么配置？”，Agent 直接拿“它怎么配置”去搜数据库，结果搜不到任何东西（因为数据库里没有“它”）。
**解决方案**：在检索前增加一步 LLM 处理，把问题改写清楚。

#### 🧱 代码积木 (File: `tong_agent/graph.py`)
> 需要在 Graph 中新增一个 `rewrite_query` 节点，插在 `retrieve_memory` 和 `tool_exec` 之间。

```python
# 1. 定义 Rewrite 节点
def rewrite_query_node(state: AgentState, config: RunnableConfig):
    messages = state["messages"]
    last_message = messages[-1].content
    
    # 简单的 Prompt 让 LLM 改写问题
    prompt = f"""
    你是一个查询优化专家。请将用户的以下问题改写为更适合搜索引擎的完整查询语句。
    补充缺失的主语（根据上下文），去除口语化词汇。
    
    用户原话: "{last_message}"
    
    只输出改写后的查询语句，不要输出其他内容。
    """
    
    model = get_model(config)
    response = model.invoke([HumanMessage(content=prompt)])
    rewritten_query = response.content
    
    print(f"DEBUG: Query Rewritten: '{last_message}' -> '{rewritten_query}'")
    
    # 将改写后的查询存入 state，或者直接替换最后一条消息（视架构而定）
    # 这里我们选择更新 state 中的 current_intent 或新增字段
    return {"current_intent_query": rewritten_query}

# 2. 在 build_graph 时添加该节点
# workflow.add_node("rewrite_query", rewrite_query_node)
# workflow.add_edge("intent_parse", "rewrite_query") ...
```

### 3. 攻克“记忆能力”：多租户隔离 (Multi-Tenancy)
**现状问题**：`user_id="user_123"` 写死，所有人共用一个大脑。
**解决方案**：从前端透传 `user_id`。

#### 🧱 代码积木 (File: `tong_agent/graph.py`)
> 修改 `retrieve_memory_node` 和 `save_memory_node`。

```python
def retrieve_memory_node(state: AgentState, config: RunnableConfig):
    # 从 config 中动态获取 user_id
    user_id = config.get("configurable", {}).get("user_id", "default_user")
    
    m = get_mem0_client()
    memories = m.search(last_human_message, user_id=user_id) # 使用动态 ID
    # ...
```

---

## 📅 推荐执行顺序

1.  **立刻执行**：**语义分块**。这是提升 RAG 质量最底层的基石，改动成本小，收益大。
2.  **紧接着做**：**查询重写**。这能瞬间让 Agent 变“聪明”，听得懂省略句。
3.  **最后做**：**多租户记忆**。这属于工程完善，确保多人使用时不串台。
