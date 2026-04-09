# 📖 Claude Code (泄露版) 源码学习与架构精解

本文档用于持续记录对 Anthropic 官方闭源工具 **Claude Code** (基于 NPM 包反编译/泄露代码) 的源码阅读心得、架构拆解，以及对当前 TongAgent 的演进启发。

> ⚠️ **核心原则与视角**：
> 遵循我们的约定，所有从 Claude Code 中提炼出的学习点，都必须严格区分两个视角：
> 1. **【工程化角度】**：关注系统架构、性能、并发、状态隔离、安全性设计、交互体验等。
> 2. **【Agent 角度】**：关注大模型驱动策略、Prompt 设计、上下文管理（如折叠机制）、意图解析、工具调用边界等。

---

## 🌟 1. 为什么学习 Claude Code？
如果说 OpenHands 是开源界为了搭建“微服务/云端沙箱”的架构教科书，那么 Claude Code 则是**“本地单体 CLI Agent”**的巅峰之作。
它运行在用户真实的电脑环境中，因此它在：
*   **极限 Token 压榨与上下文折叠 (Context Folding)**
*   **终端极致交互与人类在环 (Human-in-the-Loop)**
*   **系统级安全防爆破机制**
*   **Prompt 编写艺术**
等方面，做到了业界的极致。它是我们 TongAgent 最直接的对标产品。

---

## 🏗️ 2. 源码准备与背景
Claude Code (及其顶级平替 OpenClaw) 是由 TypeScript / Node.js 编写的大型工程。我们直接剖析了其原版（TypeScript版）的源码仓库结构。

### 2.1 整体目录结构速览
整个工程极其庞大，涵盖了从 CLI 终端、Web UI 到跨平台集成的完整生态：
*   `src/`: 核心业务逻辑代码，整个系统的“发动机”。
*   `docs/`: 极其详尽的文档（包括给人类看的，以及给 Agent 读的 Markdown 规则）。
*   `skills/` & `extensions/`: 第三方集成插件（如 Slack, Notion, Github 的接入）。
*   `apps/` & `ui/`: 跨平台应用代码（iOS/Android 客户端，以及 Web 控制台的 React 代码）。
*   `CLAUDE.md` & `AGENTS.md`: 根目录下的“宪法级”系统提示词。

### 2.2 🤖 核心的“Agent 大脑”藏在哪里？
如果我们在 TongAgent 中只想学习大模型的**意图编排**、**任务执行**和**上下文管理**，我们只需要死磕 `src/` 目录下的这几个核心文件夹：

1.  **`src/agents/` (Agent 控制中枢)**
    *   *作用*：这里是 Agent 的灵魂所在地。
    *   *核心文件*：`identity.ts` (定义 Agent 的名字、人设、回复语气)、`context.ts` (定义如何折叠历史对话、如何管理 Context Window)、`skills.ts` (定义它能调用哪些工具)。
2.  **`src/acp/` (Agent Client Protocol - 无头通信协议)**
    *   *作用*：取代传统的“看终端输出”模式。
    *   *核心文件*：`client.ts` 和 `server.ts`。这里实现了一套 JSON 结构化协议，让大模型直接通过 RPC 接口和底层沙箱（如执行 Bash）通信，极大提高了稳定性和速度。
3.  **`src/flows/` (工作流与 Plan Mode)**
    *   *作用*：实现“宏引擎”与任务编排。
    *   *核心逻辑*：把多个基础工具组合成一个标准作业程序 (SOP)。这是高级 Agent 在写代码前强制进行“思考->规划->执行”的核心引擎。
4.  **`src/cli/` (人类交互入口)**
    *   *作用*：拦截用户的终端输入，进行安全校验后，把问题抛给 Agent。包含 `acp-cli.ts`, `sandbox-cli.ts` 等。

---

## 🧠 4. 深入大脑腹地：核心模块源码解析
我们按照目录顺序，深入剖析 `src/` 下的核心机制，并将其转化为 TongAgent 可复用的设计。

### 4.1 `src/acp` (Agent Client Protocol): 抛弃终端输出，拥抱结构化通信
这是该项目最具革命性的架构设计。传统 Agent（包括早期的 TongAgent）在执行终端命令时，通常是靠 `subprocess` 拿到终端打印的字符串（通常还带有各种乱码和颜色 ANSI 码），然后强行塞给大模型去“读屏幕”。这极易导致大模型上下文混乱。

OpenClaw 引入了 **ACP (Agent Client Protocol)**：
*   **【工程化角度】无头 RPC 通信**：它把底层的操作系统封装成了一个 Server，大模型是一个 Client。大模型想执行命令时，不再是“敲键盘”，而是发送一个标准的 JSON-RPC 请求。执行结果也会被解析成干净的 JSON 返回。
*   **【工程化角度】权限分级拦截 (`approval-classifier.ts`)**：在 `client.ts` 中，我们看到了它极其完善的拦截机制。在把命令交给底层执行前，会经过 `classifyAcpToolApproval`。它把命令分成了 `readonly_scoped` (安全)、`readonly_search` (安全) 和危险命令。危险命令会强制挂起，通过终端 `readline` 要求人类输入 `y/N` 确认（Human-in-the-loop）。

**启发**：
我们的 TongAgent 在调用工具时（比如 LangGraph 的 Tool Node），不应该把原始的、几万字的控制台输出直接返回给大模型。我们应该在中间加一层“清洗与结构化拦截器”，像 ACP 协议一样，只返回大模型真正需要的结构化结果，并在遇到高危操作时，暂停当前 Graph，等待人类输入 `y`。
### 4.2 `src/agents`: 庞大的控制中枢 (The Brain)
当我们点开 `src/agents` 目录时，会被里面成百上千个文件震惊。但经过剥丝抽茧，我们发现这其实是一个**“披着大模型外衣的现代分布式系统”**。

在 TongAgent 现有的 LangGraph 架构中，我们通常只有简单的 `invoke_model` 和 `execute_tool` 节点。而顶级 Agent 架构将其细分为了极其专业的子系统：

#### 核心子系统拆解 (附 Python 思想复刻版与裂变分析)：

为了更好地对标业界标准的 Agent 架构，我们将这些底层机制归类到 Agent 的四大核心模块中：**大模型执行引擎 (LLM Engine)**、**工作记忆管理 (Working Memory)**、**工具与环境交互 (Tool & Action Space)**、**配置与安全中心 (Profile & Security)**。

---

##### 🧠 模块一：大模型执行引擎 (LLM Engine)
此模块负责模型调用、网络通信、故障转移以及参数修正，是 Agent 的“心脏”。

**【机制一：容灾与重试保护伞 (`attempt.*` 和 `failover-*`)】**
*   **功能思想**：绝对不能裸调大模型 API。每一次调用都是一次 "Attempt" (尝试)，必须套上防弹衣。如果主模型 (Claude) 网络不通或被限流，系统必须能无缝切换到备用模型 (如 OpenAI)；如果大模型输出的 JSON 参数少了个逗号，不要崩溃，而是自动修补。
*   **Python 伪代码复刻**：
    ```python
    def invoke_model_with_failover(messages, max_retries=3):
        models = ["claude-3-5-sonnet", "gpt-4o", "gemini-pro"] # 主备模型列表
        for attempt in range(max_retries):
            for model_name in models:
                try:
                    return call_api(model_name, messages) # 尝试调用
                except RateLimitError:
                    print(f"{model_name} 被限流，无缝切换到下一个备用模型...")
                    continue # 触发 Failover 降级
                except JsonDecodeError as e:
                    messages = auto_repair_json(e.raw_text) # 触发自动修补
        raise Exception("API 余额耗尽或死循环，触发 retry-limit 熔断！")
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * 在上面的 Python 脚本里，重试只是一层 `try...except` 循环。
       * 但在企业级产品中，你需要记录每一次重试的状态（是哪种错误引发的？重试了几次？）。于是裂变出了 `attempt.ts` (主控循环) 和 `failover-observation.ts` (专门收集每次降级时的监控指标数据)。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * Python 里我们直接写死 `models = ["claude", "gpt-4o"]`。
       * 企业级 Agent 支持数十种模型和自定义端点，于是裂变出了 `failover-policy.ts`。它作为“指挥官”，动态决定如果 Claude 报 429 限流错，下一步该切哪个模型；如果是报 500 内部错，该怎么切。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * 简单的 API 调用在遇到坏 JSON 时直接崩溃。
       * 工业级必须有兜底。于是裂变出了 `attempt.tool-call-argument-repair.ts` (专门修补大模型吐出的坏 JSON)，以及 `retry-limit.ts` (防止修补逻辑陷入死循环的最终熔断器)。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * 上述所有策略和修补逻辑，都配有极其严密的 `*.test.ts` 文件（如 `failover-policy.test.ts`），文件数量直接翻倍。

---

##### 🗂️ 模块二：工作记忆与上下文管理 (Working Memory & Context)
此模块负责防止大模型的“脑容量（Context Window）”被撑爆，它等同于高级 RAG 中对历史记录的摘要机制。

**【机制二：神级优化——上下文折叠引擎 (`compaction-*`)】**
*   **功能思想**：这是解决长上下文 (Token 爆炸) 最牛的手段。当对话历史太长时，它会把前几轮的对话抽出来，交给一个小模型去总结：“前 10 轮对话，用户查了 5 个文件，结论是 bug 在 a.py 里”。然后用这段总结，替换掉原来几万字的历史。
*   **Python 伪代码复刻**：
    ```python
    def compact_history(messages, max_tokens=80000):
        if count_tokens(messages) < max_tokens:
            return messages # 还没满，不用管
        
        # 抽出前 10 轮废话
        old_messages = messages[:10] 
        recent_messages = messages[10:]
        
        # 召唤一个小模型（便宜的）来写总结，并加入超时防死锁机制
        try:
            summary = run_with_timeout(
                call_api("gpt-4o-mini", "把以下过程压缩成结论：\n" + str(old_messages)), 
                timeout=10
            )
        except TimeoutError:
            return recent_messages # 兜底：如果小模型卡死，直接丢弃老消息
            
        # 狸猫换太子：用简短的总结替换掉几万字的废话
        return [{"role": "system", "content": f"之前的历史摘要: {summary}"}] + recent_messages
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * Python 阶段只是简单切片 `messages[:10]` 抽出老消息。
       * 企业级裂变出了 `session-manager-cache.ts` (管理并发情况下的内存一致性) 和 `runs.ts` (专门追踪当前压缩任务的生命周期)。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * Python 里写死 `if tokens > 80000`。
       * 企业级裂变出了 `compact-reasons.ts` (动态判断何时该压缩) 和 `model-context-tokens.ts` (维护各模型 Context Window 字典)。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * 裂变出 `compaction-timeout.ts` 和 `compaction-retry-aggregate-timeout.ts`。如果用来写总结的小模型卡死了，系统必须强制中断它，防止整个 Agent 陪葬。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * 压缩逻辑和截断边界的各类异常情况，都有对应的 `.test.ts` 保驾护航。

**【机制六：多模态视觉记忆修剪 (`history-image-prune.ts`)】**
*   **功能思想**：Agent 能够读取图片（如屏幕截图或 UI 设计图）。但图片极其消耗 Token，历史对话中的旧图片必须被智能修剪，否则几轮对话就会让 API 账单和显存双双爆炸。
*   **Python 伪代码复刻 (图像生命周期管理)**：
    ```python
    def prune_history_images(messages, max_images=3):
        # 1. 状态与数据解耦：只针对含有图片的节点进行处理
        image_nodes = find_all_images(messages)
        
        if len(image_nodes) <= max_images:
            return messages
            
        # 2. 策略引擎：优先保留最新的图片，旧图片退化为文本描述
        nodes_to_prune = image_nodes[:-max_images]
        for node in nodes_to_prune:
            # 3. 兜底与副作用隔离：用文本占位符替换掉庞大的 Base64 数据
            node.content = "[系统提示: 用户曾经上传过一张图片，由于内存限制已被移除]"
            
        return messages
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * Python 里只是简单的列表替换。企业级裂变出了 `images.ts`，专门负责图片 Base64 的编码、解码和在内存中的状态管理。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * 裂变出 `history-image-prune.ts`，它作为清理策略官，决定哪些对话节点里的图片可以被安全移除而不影响接下来的逻辑推理。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * 如果图片被错误裁剪，大模型会报出“图片引用丢失”的严重错误。因此在修剪时，必须注入特殊的占位符（如“User attached an image here”），防止下文的 Prompt 失去逻辑连贯性。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * 伴随有大量的 `history-image-prune.test.ts`，测试多图连续上传、长文本混排图片等极端情况下的裁剪正确性。

**【机制七：平行时间线与撤销引擎 (`lanes.ts` 和 `replay-history.ts`)】**
*   **功能思想**：Agent 在执行任务时经常走错路。用户大喊一声“停！撤销你刚才那两步操作”。这要求系统必须具备类似 Git 分支（Lanes）的撤销和回放能力。
*   **Python 伪代码复刻 (版本控制架构)**：
    ```python
    class ChatLane:
        def __init__(self):
            self.commits = [] # 1. 状态与数据解耦：把对话变成 Commit 历史
            
        def undo_last_action(self):
            # 2. 策略引擎：判断哪些节点是可以安全回退的
            if not self.commits:
                return "无可撤销"
            last_commit = self.commits.pop()
            
            # 3. 副作用隔离：回放历史，恢复系统状态
            replay_history(self.commits)
            return "已为您回退到上一个状态。"
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * Python 里是简单的列表。企业级裂变出了 `lanes.ts`，把整个会话历史抽象成了多条可平行切换的“时间线（Lanes）”，支持用户在不同的推理分支之间跳跃。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * 裂变出 `replay-history.ts`，当用户要求撤销时，系统不仅要删掉聊天记录，还要决定如何撤销大模型刚刚创建的文件（与沙箱结合的策略）。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * 撤销大模型正在执行的流式任务极其危险，容易引发内存泄漏。`incomplete-turn.ts` 就是专门兜底这种因为被中途打断而产生的“残缺回合”，确保下次对话正常开始。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * 对应 `lanes.test.ts`，确保在深层分支回退时，Context 不会产生脏读。

---

##### 🛠️ 模块三：工具调用与环境交互 (Tool Use & Action Space)
此模块负责 Agent 与外部物理世界（终端、文件系统）的安全边界控制，确保大模型不会被庞大的工具输出压垮。

**【机制三：结果智能截断 (`tool-result-truncation.ts`)】**
*   **功能思想**：防止单个工具的返回结果直接把上下文撑爆。
*   **Python 伪代码复刻**：
    ```python
    def truncate_tool_output(tool_name, output_str, max_tokens=2000):
        # 1. 预估 Token 而不是行数，防止压缩代码爆内存
        if count_tokens(output_str) <= max_tokens:
            return output_str
            
        lines = output_str.split("\n")
        
        # 2. 根据不同工具执行动态策略
        if tool_name == "ls":
            # 目录太长：保留头尾
            head = "\n".join(lines[:100])
            tail = "\n".join(lines[-100:])
            return f"{head}\n\n...[TRUNCATED]...\n\n{tail}"
        elif tool_name == "grep":
            # 搜代码：绝对不能从中间截断，只能丢弃尾部
            return "\n".join(lines[:200]) + "\n\n...[TRUNCATED]"
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * Python 里直接对返回的字符串做 `split('\n')`。
       * 在企业级中，长输出可能被缓存在本地，所以截断的结果必须和原数据产生映射关系。裂变出了 `tool-result-context-guard.ts`，确保被截断的数据进入 Context 时有明确的标识。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * Python 里写死了“头尾保留 100 行”。
       * 但不同的工具特性不同。于是裂变出了 `tool-result-truncation.ts`。如果工具是 `ls`，头尾截断没问题；如果是 `grep` (搜索代码)，中间截断可能漏掉关键信息。所以策略必须根据被调用的 `tool-name` 动态变化。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * 简单的行数截断遇到“压缩过的一行 10 万字 JS 代码”会失效。
       * 于是裂变出了 `tool-result-char-estimator.ts`。作为兜底机制，它不按行数，而是通过分词器精确计算返回结果的 Token 数，如果 Token 超标，强制从中间硬生生切断，保全大模型的命。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * 每一种奇怪的输出情况（空行、单行巨长文本、乱码），都有对应的 `tool-result-truncation.test.ts` 来保证截断算法不会把内存吃光。

**【机制八：独立执行沙箱的孵化 (`attempt.spawn-workspace.*`)】**
*   **功能思想**：为了防止大模型的危险操作污染用户的真实电脑（宿主机），Agent 尝试运行代码或执行未知命令时，必须“孵化”一个轻量级的独立 Workspace（沙箱）。
*   **Python 伪代码复刻 (沙箱隔离机制)**：
    ```python
    def spawn_workspace(command):
        # 1. 状态与数据解耦：创建一次性的隔离环境
        workspace = Sandbox(id=generate_uuid(), isolation_level="high")
        
        try:
            # 2. 策略引擎：在沙箱内安全执行，并在超时前返回
            return workspace.run(command, timeout=30)
        except Exception as e:
            # 3. 兜底与副作用隔离：无论如何，执行完必须销毁沙箱
            workspace.destroy()
            raise RuntimeError(f"沙箱内执行失败: {e}")
        finally:
            workspace.destroy()
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * Python 中我们通过简单的 `subprocess` 执行。企业级裂变出了 `attempt.spawn-workspace.sessions-spawn.ts`，专门管理与沙箱宿主建立通信隧道（如 WebSocket）的状态。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * 裂变出了 `attempt.spawn-workspace.context-injection.ts`，它决定了哪些环境变量、上下文和工具权限可以被注入到这具刚孵化出来的沙箱躯壳中。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * 沙箱最容易出现僵尸进程。裂变出了 `context-engine-maintenance.ts` 和 `attempt.subscription-cleanup.ts`，它们就像环卫工人，负责定期清扫被遗弃的沙箱、关闭断掉的 WebSocket 连接，绝不允许污染宿主机的内存。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * 对应的大量 `spawn-workspace.*.test.ts` 确保了即使沙箱内部发生死锁或崩溃，也不会将宿主进程拖垮。

---

##### 🛂 模块四：配置与安全中心 (Profile & Security)
此模块处理 Agent 的人设、访问权限以及密钥生命周期管理。

**【机制四：身份与权限管理的裂变 (`auth-profiles`)】**
*   **功能思想**：它是 Agent 访问外部世界（大模型 API、GitHub 仓库、数据库）的通行证管家和保安。解决“多身份隔离、凭证过期自动续期、现代 OAuth 授权”三个痛点。
*   **Python 伪代码复刻**：
    ```python
    def get_valid_token(provider_name):
        # 1. 解耦状态：从本地 Keychain 而非写死的环境加载
        token = load_from_keychain(provider_name)
        
        # 2. 如果 Token 过期，不崩溃，而是静默刷新
        if not token or is_expired(token):
            print(f"{provider_name} 凭证失效，正在后台静默刷新...")
            try:
                # 3. 执行刷新策略
                token = perform_oauth_refresh(provider_name)
                save_to_keychain(provider_name, token)
            except RefreshFailedError:
                # 4. 副作用兜底：挂起 Agent，要求人类扫码
                print("⚠️ 刷新失败，请点击链接重新扫码登录：https://...")
                wait_for_human_login()
                return get_valid_token(provider_name)
                
        return token
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * **Python 阶段**：获取身份就是一句 `api_key = os.getenv("OPENAI_API_KEY")`。
       * **企业级裂变**：一个 Agent 往往有多个身份（比如既要代表系统管理员，又要代表普通用户）。于是裂变出了 `credential-state.ts` 和 `identity.ts`。它们把单纯的字符串变成了具有生命周期（比如会过期、需要刷新）的凭证对象，并从本地的安全存储 `store.ts` 中解耦加载。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * **Python 阶段**：不管是哪个大模型或者哪个工具，都共用一套鉴权逻辑。
       * **企业级裂变**：不同服务（如 OpenAI、GitHub、本地沙箱）的鉴权方式截然不同（有的用 Token，有的用 OAuth）。于是裂变出了 `policy.ts`，作为决策中心，它根据当前 Agent 的任务和目标服务，动态下发对应的鉴权策略。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * **Python 阶段**：如果没有环境变量或者 Token 过期，直接抛出 `KeyError` 或 `401 Unauthorized`，程序崩溃。
       * **企业级裂变**：为了防止断连，裂变出了 `oauth.ts`（负责 OAuth 刷新流）、`repair.ts`（当发现身份状态损坏时自动尝试修复，比如提示用户重新扫码）以及 `doctor.ts`（全局的健康检查医生，防患于未然）。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * 针对各种身份过期、并发覆盖、OAuth 刷新失败等边缘场景，每个模块都配备了如 `credential-state.test.ts`、`oauth.test.ts` 这样的严密测试，确保鉴权机制坚如磐石。

---

##### ⚡ 模块五：多模型适配与性能优化 (Model Abstraction & Performance)
此模块负责屏蔽底层各个大模型（Claude, GPT-4, Gemini）的 API 差异，并将 Prompt 缓存等高级特性压榨到极致。

**【机制五：Prompt 缓存与流式适配器 (`prompt-cache.*` 和 `*-stream-wrappers`)】**
*   **功能思想**：
    1. **缓存压榨**：在使用长上下文（如 RAG 或长历史对话）时，每次发送相同的 Prefix（前缀）极其昂贵。必须通过精准的缓存控制来省钱。
    2. **多模型适配**：OpenAI 吐出的是 `choices[0].delta`，Anthropic 吐出的是 `content_block_delta`，Gemini 又不一样。系统不能把这种脏活漏给上层，必须在底层抹平差异。
*   **Python 伪代码复刻 (模型适配层架构)**：
    ```python
    def call_any_model_stream(model_provider, messages):
        # 1. 状态与数据解耦：打上 Cache 标记
        optimized_messages = apply_prompt_cache_markers(messages)
        
        # 2. 策略分发：根据不同厂商调用不同的 Wrapper
        if model_provider == "anthropic":
            raw_stream = anthropic_client.chat(optimized_messages)
            return AnthropicStreamWrapper(raw_stream) # 统一转化标准格式
        elif model_provider == "openai":
            raw_stream = openai_client.chat(optimized_messages)
            return OpenAIStreamWrapper(raw_stream)
        
        # 3. 兜底逻辑：如果 API 卡死，超时熔断
        raise TimeoutError()
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * **Python 阶段**：发给模型的 `messages` 就是一个普通的字典列表。
       * **企业级裂变**：裂变出了 `prompt-cache-retention.ts` 和 `anthropic-cache-control-payload.ts`。它们负责在发请求前，精确计算哪些消息块是“长期不变的”（比如 System Prompt 或巨型代码库 Context），并悄悄给它们打上 `cache_control` 标记，把缓存命中率从抽象的动作变成了可量化的数据状态。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * **Python 阶段**：一坨巨大的 `if-else` 来处理各家 API 的返回格式。
       * **企业级裂变**：裂变出了海量的 Wrapper 策略文件：`openai-stream-wrappers.ts`, `bedrock-stream-wrappers.ts`, `moonshot-stream-wrappers.ts`。无论底层是哪家厂商的乱七八糟的 JSON 流，经过这些 Wrapper 后，上层引擎拿到的永远是干净、统一的 `AsyncGenerator<StandardEvent>`。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * **Python 阶段**：如果模型厂商突然改了返回格式，程序直接崩溃。
       * **企业级裂变**：裂变出了 `model.provider-normalization.ts` 和 `model.forward-compat.ts`（向前兼容模块）。如果用户强行配置了一个未知的新模型，它会尝试用最基础的通用格式（Fallback）去解析，绝不轻易崩溃。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * `prompt-cache-observability.test.ts` 专门用来测试“这笔 API 调用到底有没有成功命中缓存？有没有为用户省下钱？”。各种厂商的 Wrapper 也都有对应的 `.test.ts` 确保格式解析万无一失。

**【工程化角度启示】**：**【机制五：多源凭证链与高并发安全锁 (`auth-profiles` 深水区)】**
*   **功能思想**：Agent 的权限不仅来自于用户手动扫码（OAuth），还可能“借用”系统里已有的 CLI 工具（比如 AWS CLI）。同时，如果 5 个 Agent 线程同时发现 Token 过期，它们不能同时去抢着刷新（会导致覆盖或风暴），必须加锁排队，并且精确统计额度消耗。
*   **Python 伪代码复刻**：
    ```python
    def resolve_token_safely(provider_name):
        # 1. 责任链模式：如果本地钱包没有，尝试去其他 CLI (如 AWS CLI/GitHub CLI) “偷”一个
        token = load_from_keychain(provider_name) or sync_from_external_cli(provider_name)
        
        if not token or is_expired(token):
            # 2. 高并发防数据踩踏：获取全局文件锁
            with acquire_file_lock(f"{provider_name}_refresh.lock"):
                
                # 3. 双重检查 (Double-check)，防止在排队等待锁的期间，别人已经刷新完了
                token = load_from_keychain(provider_name)
                if not token or is_expired(token):
                    token = perform_oauth_refresh(provider_name)
                    save_to_keychain(provider_name, token)
                    
        # 4. 记录额度消耗
        record_token_usage(provider_name) 
        return token
    ```
*   **企业级四步裂变分析**：
    1. **裂变第一步：状态与数据的解耦 (State Management)**
       * **Python 阶段**：Token 只是个字符串，没啥附加状态。
       * **企业级裂变**：裂变出了 `usage.ts`（专门追踪当前 Profile 花了多少钱/Token，把计费状态从凭证中解耦出来）和 `session-override.ts`（支持只在当前对话有效、不存盘的一次性临时凭证）。
    2. **裂变第二步：策略与执行的解耦 (Policy Pattern)**
       * **Python 阶段**：写死按顺序找。
       * **企业级裂变**：裂变出了 `order.ts`（决定先读本地环境，还是先读 AWS CLI 的优先级策略）和 `external-cli-sync.ts`（专门执行从其他第三方工具“偷取”合法身份的执行器）。
    3. **裂变第三步：副作用隔离与兜底 (Side-effects)**
       * **Python 阶段**：不考虑多线程，并发一刷新，数据必乱。
       * **企业级裂变**：为了防止并发导致的 Token 覆盖，裂变出了核心的 `upsert-with-lock.ts`（它通过文件锁机制，保证同一时刻全系统只有一个线程在修改 Token 数据库）。为了防止 API 调用时才发现 Token 是坏的，又裂变出了 `doctor.ts`（它在 Agent 启动前就会去给所有凭证做体检，坏的提前修复）。
    4. **裂变第四步：极致的测试驱动开发 (TDD)**
       * `upsert-with-lock.test.ts` 专门测试并发死锁，`external-oauth.test.ts` 专门测试如果系统里装了奇怪版本的 CLI 会不会导致解析失败，保证系统极端健壮。

**【工程化角度启示】**：
在构建 TongAgent 时，早期版本完全可以像我们的 Python 伪代码一样，用一个 `agent_core.py` 搞定所有机制。**但当系统需要支持多模型、多端状态、流式输出并面临严苛的稳定性要求时，必须按照上述逻辑将“策略、状态、执行、异常处理”拆分到不同的模块中。**

### 3.1 【工程化角度】多级降级配置 (Fallback Hierarchy)
在阅读 `identity.ts` 时，我们发现顶级 Agent 在处理用户配置（如 Agent 的名字、回复的前缀、使用的 Emoji）时，采用了一种极其严谨的**四级降级策略 (L1 -> L4)**：
1. **L1: Channel Account Level (渠道账号级)**：比如用户在特定微信/Slack账号下设置的专属前缀。
2. **L2: Channel Level (渠道级)**：整个 Slack 渠道的通用配置。
3. **L3: Global Level (全局级)**：用户在 `config.json` 里全局设置的默认值。
4. **L4: Fallback (代码兜底)**：如果全都没设，代码里硬编码的 `[openclaw]` 或默认 Emoji `👀`。

**启发**：
TongAgent 在未来支持多用户或多端（如微信端、终端、网页端）时，配置管理绝不能是简单的 `config.get("name")`，而必须实现这种 `Context-Aware (上下文感知)` 的多级降级加载机制，保证系统的健壮性。

### 3.2 【Agent 角度】系统提示词的“宪法级”约束 (AGENTS.md)
顶级项目不仅在代码里写 Prompt，他们甚至在根目录下放了一个 `AGENTS.md`，这就是大模型的“宪法”。
我们从其规范中提炼出了几条极具杀伤力的 Prompt 设计哲学：
1. **“禁止绝对路径”法则**：明确要求 Agent `In chat replies, file references must be repo-root relative only`（回复时必须使用相对路径），防止大模型在不同系统间产生路径幻觉。
2. **“安全红线”法则**：明确警告 Agent `Do not edit files covered by security-focused CODEOWNERS rules`（禁止修改安全核心文件），从 Prompt 层面进行物理隔离。
3. **“确定性排序”法则**：在组装工具列表或目录树给大模型时，要求 `must make ordering deterministic`（必须进行确定性排序，如按字母排序），这能极大提高 Prompt Cache 的命中率，节省海量 Token 费用。

**启发**：
不要把 System Prompt 写成简单的“你是一个有用的助手”。真正的 System Prompt 应该像一份**员工入职手册**，明确规定它的输出格式、禁区、甚至是为了省钱（命中 Cache）而必须遵守的排序规则。我们要把这些规则立刻加入 TongAgent 的 `system_prompt` 中！
