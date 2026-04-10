# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2026-04-10

### Major Architecture Overhaul (v2.0)

在本次深度重构中，我们将系统从 `liuagent-master` 全面升级为当前的单体 Agentic RAG 架构。新旧版本最核心的差异体现在以下几个维度：

#### 1. 废除 Map-Reduce 架构，拥抱单体自治
- **旧版 (`liuagent-master`)**：依赖传统的 Map-Reduce 架构。由 Planner 分发任务，各个子 Agent（Worker）并行执行然后汇总。这种模式虽然并发高，但在处理跨组件复杂问题时，各个 Worker 之间缺乏全局视野，容易丢失上下文。
- **新版重构**：全面升级为对标 Claude Code 的“单脑自治架构 (Autonomous Single-Agent)”。由一个强大的主干 Agent 统揽全局，利用 `update_todo_list` 物理外挂（Context Compaction）实现“边探索、边做笔记、边调整计划”的闭环，彻底解决了长线任务中的“记忆漂移”。

#### 2. 回答生成：从“蛮力堆砌”到“边做笔记边总结”
- **旧版 (`liuagent-master`)**：回答问题靠的是“蛮力”。在最终生成答案时，它会将前面各个子 Agent 查到的所有零散文本片段、以及漫长的思考过程，全部一股脑地强行塞给最后的 `generate_response` 节点。这种做法不仅极度消耗 Token，而且经常超出了大模型的上下文处理极限，导致回答丢失细节。
- **新版重构**：全面抛弃了最后的“蛮力堆砌”节点。主干 Agent 通过 `update_todo_list` 工具，在探索的过程中就实时地将关键线索压缩成“工作笔记”。当达到交卷条件时，大模型只需看着自己精炼过的笔记，就能轻松、从容地总结出最终的自然语言解答，实现了极高的信息密度和逻辑连贯性。

#### 3. 节点大整合：更内聚的心智模型
- **旧版 (`liuagent-master`)**：图的结构非常冗长，包含了 `classifier`（分类节点）、`planner`（规划节点）以及用于防止大模型发疯的 `generate_response`（历史清洗节点）。
- **新版重构**：
  - **删除了分类节点 (Classifier)**，不再区分任务的简单或复杂，所有任务统一通过 Agentic 循环处理。
  - **将 Planner 整合进了 Intent Parse 节点**，由主干 Agent 自己完成任务的拆解和 TODO 列表的维护。
  - **赋予了主干 Agent 主动交卷权**，并在达到 50 步极限时通过“三重强制打断”在单一节点内驯服大模型，成功去掉了专职负责“擦屁股”的 `generate_response` 节点。
