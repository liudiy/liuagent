# DeepEval 核心功能速查表

## 一、DeepEval：LLM 单元测试框架 (Evaluation & Testing)

**一句话定位**：LLM 界的 `pytest`。专门用来给 Agent 跑分、找 Bug、测幻觉。

### 1. 核心功能 (Core Features)

#### 1.1 Metrics (评测指标) - **最核心**
*   **功能**：提供了一堆现成的“尺子”来量化 Agent 的表现。
*   **核心指标 (RAG 必备)**：
    *   **Faithfulness (忠实度)**：回答是否忠于检索到的文档？（测幻觉）
    *   **Answer Relevancy (相关性)**：回答是否切题？
    *   **Contextual Precision (检索精度)**：检索到的文档里有多少是有用的？
    *   **Contextual Recall (检索召回)**：该找到的文档都找到了吗？
*   **其他指标**：毒性 (Toxicity)、偏见 (Bias)、JSON 格式正确性。

#### 1.2 Synthetic Data Generation (合成数据生成)
*   **功能**：给你一篇文档，自动生成 100 个“问题-答案”对。
*   **价值**：冷启动时没有测试数据？用这个功能一键生成，不用自己编。

#### 1.3 Unit Testing (单元测试集成)
*   **功能**：完美集成 `pytest`。
*   **价值**：可以把 Agent 评测写进 CI/CD 流水线。`git push` 时自动跑测试，分数低于 80 分禁止合并代码。

#### 1.4 Confident AI (云端平台)
*   **功能**：DeepEval 的云端版，提供可视化报告、历史趋势图。
*   **价值**：非技术人员（产品/测试）也可以在上面看评测结果。

### 2. 为什么用 DeepEval？
*   **专业**：指标算法是基于最新论文实现的（如 G-Eval），比自己写的 Prompt 评测更准。
*   **RAG 专精**：针对 RAG 场景（检索+生成）有全套的评测方案。
*   **CI/CD 友好**：完全符合程序员的测试习惯。
