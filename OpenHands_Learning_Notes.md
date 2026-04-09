# 📖 OpenHands (原 OpenDevin) 源码学习与架构精解

本文档用于持续记录对顶尖开源 Agent 框架 **OpenHands** 的源码阅读心得、架构拆解，以及对当前 TongAgent 的演进启发。

---

## 🌟 1. 为什么学习 OpenHands？
OpenHands 是目前开源界最强、最接近 Devin 的全自动软件工程师 Agent。它不仅仅是一个算法脚本，而是一个集成了前端 Web、后端微服务、Docker 编排、CI/CD 自动化测试的**超级工程**。通过阅读它的源码，我们可以学习到最顶级的上下文管理、事件驱动架构以及微内核设计模式。

---

## 🏗️ 2. 核心目录结构拆解 (微内核操作系统)
OpenHands 采用高度解耦的模块化设计，宛如一个运转高效的公司：

*   **`controller/` & `core/` (大脑与总指挥)**：包含 Agent 的主循环 (思考->执行->观察) 和底层基础设施。它不直接操作文件，而是发出指令。
*   **`events/` (神经系统/事件总线)**：所有模块通过“事件”沟通（如 `Action` 和 `Observation`），彻底取代了传统的“聊天记录拼接”。
*   **`runtime/` (干活的手脚/沙箱)**：最硬核的模块。通过 Docker 容器提供隔离的执行环境，大模型在这里安全地跑代码、装依赖，相当于“无尘车间”。
*   **`llm/` & `mcp/` (外交部与接口)**：统一封装各种大模型 API，并支持最新的 MCP (Model Context Protocol) 标准协议。
*   **`critic/` & `security/` (质检与安保)**：负责评估大模型的输出质量，并拦截诸如 `rm -rf /` 的恶意指令或提示词注入。
*   **`server/` & `frontend/` (前台接待)**：提供 FastAPI 接口与 React 前端界面，实现实时的终端与对话流展示。

---

## 🧠 3. 上下文管理 (Context Management) 降维打击
对比 TongAgent 的单轨上下文，OpenHands 采用了**多层级、多轨道的上下文生命周期管理**：

1.  **多轨记忆 (Multi-track)**：
    *   **瞬时观察 (Track A)**：执行 `ls` 或读取文件的结果只在当前轮次可见，随后立刻释放，0 垃圾残留。
    *   **暂存便签 (Track B - Scratchpad)**：Agent 拥有主动记笔记的工具，将关键信息提取到便签本中，贯穿整个任务生命周期。
    *   **长期契约 (Track C)**：系统规则与守则 (如 `AGENTS.md` / System Prompt)，享受 Prompt Caching。
2.  **交互式视窗 (Interactive Viewport)**：
    *   Agent 读取大文件时，面对的是一个“虚拟终端屏幕”。它可以发送 `page_down` 翻页或进行 `search`，而不是把几千行文本生硬地塞进 Prompt。这极大地节省了 Token 并降低了幻觉。
3.  **严格的状态隔离 (State Scoping)**：
    *   使用强类型的 `State` 对象传递上下文。在处理子任务时，子 Agent 拥有完全独立的作用域，完成后只向上级提交结构化汇报 (Report)，彻底杜绝了复杂任务中的“状态串线 (State Bleeding)”。

---

## 🚀 4. 对 TongAgent 的演进启发
1.  **引入显式便签工具 (`take_note`)**：取代隐式的思维提取，增强长程记忆。
2.  **重构事件流驱动**：将单纯的 `messages` 列表升级为 `Action -> Observation` 的事件总线，为后续的 WebUI 和多端监听做准备。
3.  **隔离沙箱环境**：未来若需执行代码验证（验证即真理），必须引入类似 `runtime/` 的轻量级容器隔离机制。

---

## 📚 5. 源码精读系列：第一课 (Event-Driven Architecture)
**阅读路径**：`openhands/events/` 目录。
**核心理念**：Agent 不在“聊天”，而是在“发报”。

在传统 RAG（如早期的 TongAgent）中，大模型的输出和工具的返回，都是以 `AIMessage` 或 `ToolMessage` 的形式追加到一个 Python List 里。这在单机脚本里没问题，但如果在复杂的 Web 系统中（需要把大模型的思考实时推送到前端网页，同时存入数据库，还要让 Docker 沙箱去执行），这种基于 List 的强耦合设计就会崩溃。

**OpenHands 的破局之道（事件总线）：**
1.  **万物皆事件 (Event)**：它抽象出了一个基础类 `Event`。
2.  **两极分化**：所有的事件分为两大类：
    *   `Action`（动作）：代表**“我想要做什么”**。比如 `CmdRunAction`（请求运行命令），它包含了要执行的命令 `command` 和大模型的思考 `thought`。
    *   `Observation`（观察）：代表**“我看到了什么”**。比如 `CmdOutputObservation`（终端命令执行完毕后的输出结果）。
3.  **Pub/Sub 订阅机制 (`stream.py`)**：它实现了一个 `EventStream`（事件流）。
    *   大模型（Agent）只是往这个流里丢入一个 `CmdRunAction`。
    *   底层的 Docker 沙箱（Runtime）**订阅**了这个流。它一旦监听到有人发出了 `CmdRunAction`，就会自动去执行代码，执行完后，往流里扔回一个 `CmdOutputObservation`。
    *   前端网页（Server）也**订阅**了这个流。一旦有新的 Action，前端就会在界面上打字显示；一旦有新的 Observation，前端的虚拟终端里就会打印出绿色的代码输出。

**对工程化的启示**：
这是解耦的最高境界。大模型根本不知道 Docker 的存在，Docker 也不知道大模型的存在。它们只对着一个“事件流”说话。这就是为什么 Devin 的界面能够如此丝滑地实时渲染终端输出的原因。

---

## 📚 6. 源码精读系列：第二课 (Controller 目录全解)
**阅读路径**：`openhands/controller/` 目录。
**核心理念**：Controller 是 Agent 的经纪人，负责管钱、防死循环、管理状态。

我们逐一拆解了该目录下的 9 个核心文件，它们完美地展示了什么是“防御性编程”：

1.  **`agent.py` (员工基类与面向接口编程)**：
    *   **代码位置**：`class Agent(ABC):`
    *   **深度解析：为什么需要继承一个看似“毫无作用”的 ABC（抽象基类）？**
        *   **痛点**：在大型开源项目中，有几百个开发者在同时写不同的 Agent（比如写代码的 Agent、查网页的 Agent）。如果不用基类约束，张三可能把思考方法命名为 `run()`，李四命名为 `think()`，王五命名为 `execute()`。一旦主程序（Controller）去调用它们，瞬间就会因为找不到方法名而全盘崩溃。
        *   **ABC 的作用 (强制契约)**：**注意，Python 自带的 `abc.ABC` 源码里确实没有规定必须叫 `step`**。`ABC` 只是一个“执法者” (工具)。真正的“法律条文”是由 OpenHands 框架的作者在 `agent.py` 里自己定义的：
            ```python
            from abc import ABC, abstractmethod
            class Agent(ABC):
                @abstractmethod
                def step(self, state: 'State') -> 'Action':
                    pass
            ```
            `ABC` 配合 `@abstractmethod` 装饰器，构成了一份**强制合同**。它规定了：**任何想成为 OpenHands 员工（继承 `Agent` 子类）的人，都必须自己实现一个名字叫 `step` 的方法。**
        *   **拦截于未然**：如果某个粗心的开发者写了一个新 Agent，但他忘了写 `step` 方法，或者名字拼错了。有了 `ABC` 这个执法者，他在敲下 `MyAgent()` 尝试实例化的那一瞬间，Python 就会直接抛出报错，**阻止这个半成品进入运行阶段**。这就是高级架构中极度推崇的“面向接口编程（Interface-Oriented Programming）”。它用极其严格的规则，换取了系统在复杂协作下的绝对稳定。
        *   **对 TongAgent 的启发**：
            *   **【工程化角度】依赖注入 (Dependency Injection)**：`Agent` 的 `__init__` 不自己创建 LLM，而是从外面传进来一个 `llm: LLM` 和 `config: AgentConfig`。这就把“Agent 怎么思考”和“Agent 用什么脑子思考”彻底解耦了。随时可以把 GPT-4 换成 Claude 或 Llama，而不需要改 Agent 内部哪怕一行代码。
            *   **【工程化角度】提示词与代码分离 (Prompt Manager)**：Agent 启动时会初始化一个 `PromptManager`，它通过读取文件夹（`prompt_dir`）把系统提示词加载进内存，而不是把大段的字符串硬编码在 `.py` 文件里。这使得提示词的迭代和代码逻辑的迭代互不干扰。
            *   **【Agent 角度】万物皆事件 (SystemMessageAction)**：在 `get_system_message` 方法中，连 System Prompt 和 Tools 都被打包成了一个 `SystemMessageAction` 事件扔进消息流。这让系统初始化的过程也融入了整个“事件总线”架构，非常优雅统一。
2.  **`agent_controller.py` (项目经理)**：这是整个文件夹的大脑。它负责拉起 Agent、执行循环、扣除预算（Token/金钱）、处理人类审批（Confirmation Mode），以及拉起子 Agent（Delegation）。
    *   **第一部分：类的声明与大管家的武器库**
        *   **具体代码**：
            ```python
            class AgentController:
                event_stream: EventStream
                parent: 'AgentController | None' = None
                delegate: 'AgentController | None' = None
                _pending_action_info: tuple[Action, float] | None = None
            ```
        *   **代码作用**：声明了控制器运行所需的核心资源。`event_stream` 是全局的事件流管道；`parent/delegate` 指针用于指向父级或子级 Agent；`_pending_action_info` 用于暂存需要人类审批的危险动作。
        *   **对 TongAgent 的启发**：
            *   **【工程化角度】微服务解耦**：TongAgent 目前用 `messages` 列表存聊天记录，前后端强耦合。未来应引入 `EventStream`，让大模型只负责“往流里扔事件”，前端和沙箱只负责“监听流”，彻底解耦。
            *   **【Agent 角度】多智能体外包 (Delegation)**：为 TongAgent 引入 `delegate` 指针，遇到复杂任务（如搜索资料）时，主 Agent 可挂起，拉起一个专用的 `SearchAgent`（小弟）去干活，干完再收回结果。
            *   **【工程化角度】人类在环 (HITL)**：TongAgent 接入终端命令等高危工具时，必须引入 `_pending_action_info` 机制，遇到危险命令先挂起，等待用户点击确认后再执行。
    *   **第二部分：初始化方法与状态订阅**
        *   **具体代码**：
            ```python
            def __init__(self, agent: Agent, event_stream: EventStream, ...):
                # ...
                if not self.is_delegate:
                    self.event_stream.subscribe(
                        EventStreamSubscriber.AGENT_CONTROLLER, self.on_event, self.id
                    )
                self.state_tracker = StateTracker(sid, file_store, user_id)
                self._stuck_detector = StuckDetector(self.state)
            ```
        *   **对 TongAgent 的启发**：
            *   **【工程化角度】异步响应式编程**：TongAgent 在等待工具执行时，可以用事件订阅机制取代死循环等待，极大节省服务器资源。
            *   **【工程化角度】多租户状态隔离**：通过 `sid` (Session ID) 和 `StateTracker`，把不同用户的对话状态持久化到本地文件或 Redis，解决多用户并发时的“状态串线 (State Bleeding)”问题。
            
        *   **深度解析（通俗版）**：
            这里有两项最顶级的架构设计：**事件订阅 (`subscribe`)** 和 **状态追踪 (`StateTracker`)**。我们用最通俗的话来解释它们解决了什么痛点：
            
            **1. `event_stream.subscribe` (异步响应式编程 vs 死循环等待)**
            *   **传统做法 (比如早期的 Python 脚本)**：大模型决定执行一个耗时 5 分钟的 Python 脚本。主程序只能 `while True:` 傻傻地等，每隔 1 秒去问一次沙箱：“你跑完了没？” 这 5 分钟里，主程序的 CPU 和内存一直被占着，什么别的也干不了（也就是被“阻塞”了）。
            *   **OpenHands 的做法 (事件订阅)**：`AgentController` 说：“沙箱你去跑吧，我不等你了。我先去休息了。**但是，我在这里（事件流）挂了一个铃铛（`subscribe`），并且留下了我的联系方式（`on_event` 方法）。**” 等 5 分钟后沙箱跑完，沙箱往事件流里丢一个“代码执行完毕”的事件，这个事件就像敲响了铃铛，自动把 `AgentController` 唤醒，并把执行结果塞进 `on_event` 方法里让它继续处理。这就叫“异步响应式编程”，它能让一台普通的服务器同时处理成百上千个 Agent 请求而不卡死。

            **2. `StateTracker` (多租户隔离 vs 状态串线)**
            *   **传统做法 (比如你的本地单机测试)**：你可能在 Python 里用了一个全局变量 `messages = []` 来存聊天记录。你自己一个人用没问题。但是上线后，张三问：“怎么配置 Nginx？”，李四问：“怎么配 Redis？” 如果没有隔离，大模型可能会把 Nginx 的配置发给李四。这就叫**状态串线 (State Bleeding)**。更有甚者，几万个用户的聊天记录全堆在内存里，服务器直接 OOM（内存溢出）崩溃。
            *   **OpenHands 的做法 (无状态服务)**：每一次对话都有一个唯一的身份证号 `sid`（Session ID）。当请求来临时，`StateTracker` 用这个 `sid` 去本地磁盘（`file_store`）或者 Redis 里，把只属于张三的那一份记忆（状态）捞出来，装载到内存里；张三的问题回答完后，马上再存回硬盘，然后把内存清空！这样，Agent 本身就像一个没有记忆的计算器（无状态 Stateless），谁来用，就临时加载谁的记忆。这就是解决“多用户并发”和“内存爆炸”的工业级标准答案。
            
            **3. 硬核源码拆解：事件流到底是怎么跑起来的？**
            为了彻底搞懂 `event_stream`、`subscribe`、`on_event` 和 `Observation` 这四个词的运作机制，我们深入看了 `openhands/events/stream.py`。
            
            *   **第一步：挂铃铛 (`subscribe`)**
                在 `AgentController` 初始化时：
                ```python
                # AgentController 告诉 EventStream：
                # “我是 AGENT_CONTROLLER，如果有新事件，请调用我的 on_event 方法”
                self.event_stream.subscribe(EventStreamSubscriber.AGENT_CONTROLLER, self.on_event, self.id)
                ```
                在 `EventStream` 的底层，它把你的名字和回调函数存到了一个字典里，并且**为你单独开了一个线程池**：
                ```python
                # stream.py 的底层逻辑
                self._subscribers[subscriber_id][callback_id] = callback
                self._thread_pools[subscriber_id][callback_id] = ThreadPoolExecutor()
                ```
            *   **第二步：别人丢事件进来 (`add_event`)**
                假设 Docker 沙箱把一段 Python 代码跑完了，它会创建一个 `Observation` (观察结果，比如终端输出了 "hello world")，然后把它丢进流里：
                ```python
                # Docker 沙箱执行：
                self.event_stream.add_event(observation, EventSource.RUNTIME)
                ```
                在底层，这个事件被放进了一个**队列 (Queue)** 中：
                ```python
                # stream.py 的底层逻辑
                self._queue.put(event)
                ```
            *   **第三步：自动唤醒 (`on_event`)**
                `EventStream` 后台有一个永远在跑的线程（相当于餐厅的服务员），它看到队列里有新事件了，就会去查字典，找出所有挂了铃铛的人，把事件塞给他们：
                ```python
                # stream.py 里的后台服务员
                event = self._queue.get()
                for subscriber in self._subscribers:
                    callback = callbacks[subscriber] # 也就是拿到了 AgentController 的 on_event
                    pool.submit(callback, event)     # 异步执行！
                ```
                于是，`AgentController` 的 `on_event(event)` 突然被触发了！它一看传进来的是一个 `Observation`，就知道“哦，刚才大模型交代的代码跑完了，结果在这呢，我可以去唤醒大模型进行下一步思考了！”
                
                > **这就是 Pub/Sub (发布/订阅) 模式的最经典实现。它彻底消灭了 `while True` 的死循环等待！**
                
            **4. 为什么要这么设计？(强耦合 vs 事件松耦合的通俗比喻)**
            *   **场景**：假设家里有 4 个人：爸爸 (AI)、妈妈 (执行器)、爷爷 (日志系统)、奶奶 (前端界面)。现在爸爸让妈妈去倒垃圾。
            *   **不用事件订阅 (传统点对点调用，会乱套)**：
                爸爸必须直接喊妈妈（`mom.take_out_trash()`）。妈妈干完活，必须分别去告诉爸爸（`dad.notify()`）、爷爷（`logger.record()`）、奶奶（`frontend.show()`）。
                这就导致所有人互相绑定死了。想换掉妈妈？不行，所有人代码都要改。想加个新角色？所有人都要改。代码最后变成一团蜘蛛网，这叫**强耦合**。
            *   **用事件订阅 (OpenHands 的解耦架构)**：
                家里中间放一个**喇叭 (event_stream)**。规则只有一条：谁有事就对着喇叭喊，谁想听就监听喇叭。
                爸爸对着喇叭喊：“倒垃圾”。妈妈早就**订阅 (`subscribe`)** 了家务指令，听到后自动去倒。倒完后，妈妈对着喇叭喊：“倒完了 (`Observation`)”。爸爸听到后继续思考，爷爷听到后记录，奶奶听到后展示。
                **精髓在于：谁都不认识谁！** 爸爸不知道妈妈存在，妈妈也不知道爷爷奶奶存在。大家只和“喇叭”打交道。这就叫**彻底解耦**。

            **5. 职场科普：这些高并发/事件流架构在工作中由谁负责？**
            *   **【纯 Agent 算法工程师 (AI Engineer)】**：他们不管事件流、不管 Docker、不管多租户。他们的日常工作是写 Prompt（调教大模型脾气）、写 Tools（比如爬虫脚本）、调优 RAG（向量检索）、微调模型（SFT）。他们的交付物通常就是一个 `test.py`（单机脚本）。
            *   **【纯 后端工程师 (Backend Engineer)】**：他们不懂大模型的 Context Window 是什么，不懂怎么写 System Prompt。他们负责搭 FastAPI、写 Redis 状态隔离、写 WebSocket 和前端通信。
            *   **【AI 架构师 / AI Infra 工程师 (The Builder)】**：**这就是 OpenHands 的作者，也是你目前正在学习的角色！** 这是一个极度稀缺的复合型岗位。他需要把 AI 工程师的“单机脚本”包装成一个能扛住上万人并发的“工业级系统”。他需要懂大模型（才知道为什么要用 `Observation` 喂给模型），也需要懂高并发后端（才知道要用 `EventStream` 防阻塞）。

     *   **第三部分：安全门禁拦截**
         *   **具体代码**：
            ```python
            async def _handle_security_analyzer(self, action: Action) -> None:
                if self.security_analyzer:
                    action.security_risk = await self.security_analyzer.security_risk(action)
                else:
                    action.security_risk = ActionSecurityRisk.UNKNOWN
            ```
        *   **代码作用**：在动作执行前，调用安全分析器评估风险级别。如果没有配置安全分析器，则默认将风险设为 `UNKNOWN`（最高警戒级别）。
        *   **对 TongAgent 的启发**：**默认不信任原则 (Fail-Safe Default)**。在安全架构中，宁可错杀不可放过（白名单机制）。未来 TongAgent 在执行任何底层操作时，都必须经过一层“安保拦截器”。
3.  **`stuck.py` (死循环探测器)**：这是一个极具启发的防爆破文件。里面的 `StuckDetector` 会检查历史记录，如果发现 Agent 连续 4 次执行了同样的 Action 并得到了同样的报错（如 `SyntaxError`），它会判定 Agent 卡死了，直接中断任务，防止无限烧钱。
4.  **`action_parser.py` (意图解析器)**：当大模型输出一长串 Markdown 文本时，这个文件负责将文本中的 XML/JSON 解析成标准的 `Action` 事件对象（对应 TongAgent 中的意图解析节点）。
5.  **`replay.py` (时光机)**：用于在测试或 Debug 时，根据历史的事件日志，把 Agent 曾经做过的事情一模一样地重新执行一遍，是极佳的调试工具。
6.  **`state/state.py` (状态快照)**：定义了 Agent 当前时刻看到的所有世界信息（历史事件、当前任务、迭代步数）。
7.  **`state/state_tracker.py` (记忆存储器)**：负责把 `state.py` 中的快照持久化到本地文件或云端。基于 `sid`（Session ID）实现多租户隔离。
8.  **`state/control_flags.py` (中断标志位)**：非常轻量级的文件，定义了系统级的信号灯（比如“用户要求立刻停止”、“余额不足强制熔断”）。
9.  **`__init__.py`**：Python 模块的标准导出文件，把上面的类暴露给外部使用。

> 💡 *启发：工业级的 Agent 系统，其 80% 的代码都在写“异常处理”和“防呆机制”，而真正调大模型 API 的代码只占极小部分。*

---

## ⚖️ 7. 源码学习抉择：Claude Code (泄露版) vs OpenHands
当面临“该读哪一个”的十字路口时，作为架构师应有如下清醒的认知：

*   **Claude Code (商业闭源泄露版) —— 适合学“产品与奇技淫巧”**：
    *   **优点**：代表了 Anthropic 官方的极限 Token 压榨技术、最顶级的 System Prompt 编写艺术，以及极致的 CLI 终端交互体验。
    *   **缺点**：它是用 TypeScript/Node.js 写的（并非 Python），且经过了混淆或压缩，没有注释，没有工程化目录，完全是一个“黑盒”。它不具备通用性，深度绑定了 Claude 模型。
*   **OpenHands (开源社区王者) —— 适合学“软件工程与微内核架构”**：
    *   **优点**：纯正的 Python 企业级项目。拥有教科书般的目录拆分、事件总线设计、Docker 沙箱机制、完善的 CI/CD 测试流以及依赖注入模式。
    *   **结论**：如果你的目标是**提升 Python 代码的工程化能力、学习如何搭建一个能上线的 SaaS 级 Agent 平台**，OpenHands 是唯一且最佳的教材。

> 💡 *核心学习策略：用 Claude Code 的思想（如 Context Folding）武装大模型的大脑，用 OpenHands 的架构（如 Event Stream, Runtime Sandbox）搭建 Agent 的骨架。*

---

### 🛡️ 防线四：执行前与执行中（人类介入与兜底熔断）
当大模型遇到自己解决不了的问题，或者试图做出高危操作时，必须交出控制权。

*   **【工程化角度】异步挂起与人工审批 (HITL - Human-in-the-Loop)**：这是最难写的后端代码。当大模型决定调用 `DeleteFile` 时，系统立刻把这个执行线程**挂起 (Suspend)**。然后通过 WebSocket 给前端发个消息，前端弹出一个确认框：“Claude 试图执行高危命令”。只有人类点击“同意”，系统才会去唤醒那个挂起的线程并执行。
*   **【Agent 角度】显式的 `AskUser` 工具**：赋予大模型主动求助的权利。当大模型面临“用 Vue 还是 React”这种没有标准答案的问题时，它主动调用 `AskUser` 工具。此时流程也是挂起的，直到用户在终端里敲入回答，流程才继续。
*   **【工程化角度】全局 Token/预算熔断器 (Budget Circuit Breaker)**：Agent 启动时会被分配一个 `max_budget`（如 5 美元）。在底层的事件流中，每次调用后都会实时累加 Token 费用。一旦超标，强制抛出硬异常中断当前任务，防止死循环导致账单爆炸。

### 🛡️ 终极防线：隐藏在冰山下的高阶风控
除了常规的 4 个阶段，Claude Code 还隐藏了极其偏执的终极防御：
*   **【工程化角度】沙箱逃逸监控 (eBPF Syscall Monitor)**：在沙箱底层挂载系统级探针。如果大模型生成的代码试图修改 `/etc/shadow` 或发起反向 Shell，探针会瞬间捕获这些高危“系统调用 (Syscall)”并直接 `Kill -9` 杀掉进程。
*   **【Agent 角度】双模型审计 (Model-on-Model Evaluation)**：主模型写完代码后并不立刻执行，而是交给另一个独立的“审计模型”审查其是否存在破坏性或偏离用户意图。一旦审计失败，主模型行为被直接驳回（用 AI 防 AI）。
*   **【工程化角度】不可信记忆隔离 (Memory Poisoning Defense)**：在读取外部网页时，为防止网页中隐藏的“提示词注入（Prompt Injection）”，系统会在内存里开辟独立的“不可信沙盒区”，并临时降级大模型的工具执行权限。

---

## 🆚 9. 巅峰对决：Claude Code vs OpenHands

这两者代表了目前业界最顶尖的 Agent 水平，但因为“产品定位”完全不同，导致它们的架构呈现出巨大的差异。

### 1. 定位与基因的区别
*   **Claude Code：To C 的闭源商业软件 (偏执的保安)**
    *   它是在用户的真实电脑终端里跑的，一旦删错了用户文件，Anthropic 公司要惹大麻烦。
    *   因此，它的核心基因是**“极度受控、极度防御、成本极度敏感”**。
*   **OpenHands：To B/开发者的开源基建 (宏大的车间)**
    *   它是跑在云端 Docker 容器里的，跑崩了直接销毁容器重建即可，不怕搞坏系统。
    *   因此，它的核心基因是**“高度解耦、强扩展性、多租户并发支持”**。

### 2. 【工程化角度】架构差异对比
| 对比维度 | Claude Code 泄露架构 | OpenHands 开源架构 | 为什么有这种差异？ |
| :--- | :--- | :--- | :--- |
| **开发语言** | TypeScript (Node.js) | Python | Node.js 天生适合写 CLI 命令行工具；Python 是开源 AI 社区的绝对主流，方便全世界贡献者接入。 |
| **底层通信** | 同步/轻量级队列 | EventStream (事件总线) + Redis | Claude 是单机 CLI 工具，自己一个人用；OpenHands 是为了上万人同时在网页上使用设计的，必须用微服务级别的 Pub/Sub 事件流来解耦前端、Agent 和沙箱。 |
| **执行环境** | **本地真机 (Host OS)** | **隔离沙箱 (Docker)** | Claude Code 为了丝滑体验，直接在你电脑上改代码（所以它需要极其变态的安全审批机制）；OpenHands 默认所有代码都在远端 Docker 里跑（所以它需要通过 SSH 或 WebSocket 和沙箱通信）。 |
| **状态存储** | 本地文件 (轻量化) | StateTracker (支持云端/Redis) | OpenHands 需要支持多租户隔离 (Session ID)，防止张三和李四的状态串线。 |

### 3. 【Agent 角度】大模型驱动策略对比
| 对比维度 | Claude Code 泄露架构 | OpenHands 开源架构 | 为什么有这种差异？ |
| :--- | :--- | :--- | :--- |
| **模型绑定** | **深度死绑 Claude 家族** | **模型无关 (LLM Agnostic)** | Claude Code 本质上是 Anthropic 卖自家 API 的“带货工具”，它深度利用了 Claude 特有的 Prompt Caching 和 XML 标签解析能力；OpenHands 则通过 `LLMProvider` 做了依赖注入，支持 GPT、Llama 等一切模型。 |
| **长文本处理** | **截断与折叠 (Context Folding)** | 完整保留 (视模型而定) | Claude 自己付不起无限增长的 Token 费，必须对历史记录进行无情的“折叠剪枝”；OpenHands 把 API Key 让用户自己填，用户自己承担费用。 |
| **死循环处理** | **智能审计与降级 (Self-Correction)** | 机械计数器 (`StuckDetector`) | Claude 会分析连续报错的“特征指纹”，并强制让模型输出求助信息；OpenHands 比较简单粗暴，连续同样的 Action 失败 3 次就直接 `raise Error` 掐断。 |

### 4. 【Agent 角度】设计哲学对比：“宽严度”的 Trade-off
我们在开发 Agent 时经常会遇到一个困境：**限制太严，Agent 沦为死板的脚本（无用）；限制太松，Agent 会越权甚至引发安全灾难（危险）。** 
Claude Code 和 OpenHands 在把握这个“度”上，给出了两种截然不同的流派：

| 宽严度 Trade-off | Claude Code 的哲学：【思考时极宽，执行时极严】 | OpenHands 的哲学：【全链路放权，靠沙箱兜底】 |
| :--- | :--- | :--- |
| **思考层面 (宽)** | 给予大模型一个 `<thinking>` 标签，让它在执行前自由推演、试错、自我否定。不限制它调用搜寻类工具（如 Glob/Grep）的顺序。 | 同样不限制模型的思考路径，甚至允许它拉起子 Agent（Delegation）来分包任务。 |
| **执行层面 (严)** | **极度独裁**。一旦涉及写文件或跑命令，强制经过双模型审计和人类审批（HITL）。一旦报错，强制模型自己修 Bug。 | **相对宽松**。大模型写错代码就让它直接在沙箱里跑，跑崩了把报错原样丢回给大模型。它相信大模型能在不断的“碰壁”中自己找到出路。 |
| **兜底策略** | 如果模型陷入死循环，强制篡改 Prompt，逼它停下来问用户 (`AskUser`)。 | 如果模型陷入死循环，`StuckDetector` 计数器满 3 次直接报错熔断，不给模型狡辩的机会。 |

### 总结：对 TongAgent 的终极启示
*   **如果你想做一个给无数人用的网页端 SaaS 平台**：照抄 **OpenHands** 的 `EventStream`、`Docker Runtime` 和 `StateTracker`。
*   **如果你想做一个在用户本地终端跑的、极度安全的智能助手**：照抄 **Claude Code** 的 `Context Folding`、`HITL 权限审批` 和 `XML 防注入约束`。

---

## 🔄 10. 源码精读系列：第三课 (AgentController 的核心循环)
**阅读路径**：`openhands/controller/agent_controller.py`。
**核心理念**：抛弃 `while True:`，拥抱事件驱动状态机 (Event-Driven State Machine)。

我们在编写简单的 Agent（如早期的 TongAgent 或 LangGraph 节点）时，最直觉的写法是一个死循环：
```python
while True:
    action = llm.think(messages)
    if action == "finish": break
    result = execute_tool(action)
    messages.append(result)
```
但 OpenHands 彻底摒弃了这种写法。它通过 `_step()` 和 `_on_event()` 两个方法的精妙配合，实现了一个完全异步、非阻塞的事件驱动循环。

### 第一部分：大脑下达指令 (`_step`)
*   **具体代码片段**：
    ```python
    async def _step(self) -> None:
        # 1. 检查状态和挂起动作
        if self.get_agent_state() != AgentState.RUNNING: return
        if self._pending_action: return
        
        # 2. 死循环探测与预算检查
        if self._is_stuck(): await self._react_to_exception(AgentStuckInLoopError(...))
        
        # 3. 呼叫大模型，获取动作
        action = self.agent.step(self.state)
        
        # 4. 将动作挂起，并扔进事件流
        self._pending_action = action
        self.event_stream.add_event(action, action._source)
    ```
*   **代码作用**：
    1. `_step` 每次只做一件事：问大模型“下一步干嘛？”，拿到 `action` 后，把它标记为**正在等待 (`_pending_action = action`)**。
    2. 然后它把 `action` 扔进 `event_stream`（事件总线），**然后 `_step` 函数就直接结束了（return）！它不等待工具执行！**
    3. 这种设计叫“非阻塞”。此时，CPU 被释放出来，Web 服务器可以去处理其他用户的请求，或者响应前端的 WebSocket。

### 第二部分：沙箱执行完毕，触发回调 (`_on_event`)
*   当底层的 Docker 沙箱（Runtime 模块）监听到事件流里有 `action` 时，它会去执行代码。执行完后，沙箱会把结果包装成 `Observation`（观察结果），再次扔回事件流。
*   **具体代码片段**：
    ```python
    async def _on_event(self, event: Event) -> None:
        # ...
        if isinstance(event, Observation):
            await self._handle_observation(event)
            
        # 决定是否要继续下一步
        if self.should_step(event):
            await self._step_with_exception_handling()

    async def _handle_observation(self, observation: Observation) -> None:
        # 完美闭环：如果收到的观察结果，正是我们在等待的那个动作的产物
        if self._pending_action and self._pending_action.id == observation.cause:
            # 清除挂起状态！
            self._pending_action = None
    ```
*   **代码作用**：
    1. `AgentController` 之前挂在事件流上的铃铛（`subscribe`）被敲响，触发了 `_on_event`。
    2. 它检查收到的 `Observation` 的 `cause`（起因 ID）是否等于刚才挂起的 `_pending_action.id`。如果是，说明“大模型交代的任务终于干完了”。
    3. 于是，它把 `_pending_action` 清空为 `None`。
    4. 最后，调用 `should_step(event)`，发现任务没结束，于是**再次调用 `_step()`**。循环继续！

### 第三部分：异常处理的降维打击
*   **具体代码片段**：
    ```python
    async def _step_with_exception_handling(self) -> None:
        try:
            await self._step()
        except (ContextWindowExceededError, BadRequestError) as e:
            if self.agent.config.enable_history_truncation:
                # 优雅地把“上下文超长”变成一个动作扔给大模型
                self.event_stream.add_event(CondensationRequestAction(), EventSource.AGENT)
            else:
                raise
    ```
*   **代码作用**：当大模型报“Context Window 超长”时，程序不崩溃，而是把这个报错包装成一个 `CondensationRequestAction`（记忆压缩请求动作）扔进事件流。大模型在下一轮就会收到这个事件，乖乖地去总结历史记录，腾出空间。

### 💡 对 TongAgent 的双视角启发
*   **【工程化角度】**：
    1. **告别死循环**：单体脚本向微服务演进的必经之路，是用事件队列（如 Redis Stream/Kafka 或内存 Queue）取代 `while True`。这样你的 Agent 随时可以被中断（如等待用户在网页上点击“同意执行”），且不会造成线程阻塞。
    2. **状态机转移**：`_pending_action` 就是一个极简的状态机。有值说明“在忙”，没值说明“空闲”。
*   **【Agent 角度】**：
    1. **异常即反馈**：不要把 API 报错（如 Token 溢出、工具参数拼错）直接 `raise` 抛给前端。而是把报错包装成 `ErrorObservation` 扔回给 Agent，让大模型自己看报错日志进行 Self-Correction（自我修正）。

---
> 💡 *注：此文档将随着我们后续的源码阅读与探讨，由 AI 助手自动持续更新与完善。*