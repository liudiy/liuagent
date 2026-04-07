# RAG 3.0 Chunk 合并策略问题汇总与改进建议

## 1. 核心痛点 (Core Pain Points)

当前 `MERGE_SYSTEM_PROMPT` 主要存在以下四个方面的工程落地风险：

### A. 合并逻辑模糊 (Ambiguous Merging Logic)
*   **现象**: Prompt 中提及“逻辑分块”和“层级递归分块”，但未定义具体的合并边界条件。
*   **风险**: LLM 可能随机合并无关内容，导致语义断裂。例如：
    *   **图文分离**: 图片 (`layout: image`) 与其描述文本 (`layout: text`) 被分到不同 Chunk，导致多模态检索失败。
    *   **跨层级错误**: 小标题 (`layout: title`) 被错误地合并到前一个段落，而不是作为新段落的开始。
*   **建议**: 明确优先级规则，如“图文强绑定”、“同一小节文本累积”、“遇一级标题强制截断”。

### B. JSON 语法与解析风险 (Syntax & Parsing Risks)
*   **现象**: 示例 Output 中的 `imageUrls` 包含非标准的 Markdown 反引号格式 (`` `https://...` ``)。
*   **风险**: 下游 JSON 解析器 (如 Python `json.loads`) 可能报错，或导致前端渲染图片链接失效。
*   **建议**: 移除示例中的反引号，确保输出为标准 JSON 字符串格式。

### C. 上下文缺失 (Context Loss)
*   **现象**: Prompt 要求“继承父级路径”，但 Output 结构中缺失 `path` 或 `breadcrumb` 字段。
*   **风险**: RAG 检索召回该 Chunk 时，模型无法知晓其所属章节（如“第一章 > 核心观点”），降低回答准确度。
*   **建议**: 在 Output 对象中显式增加 `metadata` 字段，包含层级路径信息。

### D. 幻觉与过度清洗 (Hallucination & Over-Cleaning)
*   **现象**: Prompt 指令为“修复断词”、“合并非自然断句”。
*   **风险**: LLM 可能过度发挥，错误修改专有名词、公式或数值（如将 "GPT-4" 修复为 "GPT-40"）。
*   **建议**: 增加约束指令：“仅修复格式错误（如单词内换行），严禁修改任何数值、公式或专有名词”。

---

## 2. 改进后的 Prompt 策略示例

建议将 Prompt 的核心逻辑部分调整为：

```python
1. Core Merging Strategy (核心合并策略) - IMPORTANT
   a. **图文强绑定**: 检测到 `layout: image/table` 时，必须与其紧邻的上下文 `text` 合并。
   b. **语义完整性**: 在 <1000 Tokens 限制下，优先合并同一层级的 `text` 对象。
   c. **标题截断**: `layout: title` 应作为新 Chunk 的起始点。
```

## 3. 工程化建议 (Engineering Action Items)

1.  **Token 计数**: 在 Python 代码层进行 Token 二次检查，避免 LLM 输出超长 Chunk。
2.  **JSON 容错**: 使用 `json_repair` 库处理 LLM 输出的非标准 JSON。
3.  **元数据增强**: 确保合并后的 Chunk 保留原始文档的 `source_url`, `page_number` 等关键元数据。
