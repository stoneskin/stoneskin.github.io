# DeepSeek《Super-agent 设计探索》详细摘要：五大模块、实验数据与局限

> 来源（一手原文）：DeepSeek Harness 团队《Super-agent 设计探索：迈向更自主的 Agent 系统》，DeepSeek 官方微信公众号（"DeepSeek 产品部"），2026-10-31 晚。全文转贴：https://www.uied.cn/posts/922127 ；另一转贴：http://www.uml.org.cn/ai/202611023.asp?artid=27640 。英文讲解（带原图）：https://agentspulse.github.io/tutorials/deepseek-super-agent-architecture/
> 导读见 [deepseek-super-agent-guide.md](./deepseek-super-agent-guide.md)。本篇是详细摘要——论点、五大模块、实验数据、局限、原型档案，写到不看原文也能学到精髓。
> 原文开篇声明：这是一篇面向工程实践的架构思路探讨，并非对 DeepSeek Harness 现有产品功能的介绍。作者：Yujia Qiao（系统实现与写作）。

## 1. 核心论点：多任务的上限是人的注意力

- 单任务 Agent 已经证明：模型能用工具解决复杂问题，需要的人盯越来越少；跨会话的多 Agent 协调也正在变得可行。人在低层执行里的参与下降，人的角色上移到更高层的决策与验收。
- 但主流 Agent 仍以**一个 Session 为基本单位**，会话之间互相独立。用户并行推几个任务，必须手动切换会话、记住每个会话的上下文。**"据我们观察，一个人通常只能同时跟进 3 到 5 个活跃 Session。"**
- **"在这种设计下，单任务的上限取决于模型能力，多任务的上限取决于人的注意力。"**
- 只给本地单会话 Agent 加 CLI/MCP/外部连接器，解决不了问题：同步单会话阻塞、多任务上下文混淆、"设备离线 = Agent 停摆"，仍需大量人工维护。
- 解法：打破 Agent 与单次手动会话的绑定，做成一个**跨会话保持上下文、并行推进多个复杂任务而不互相干扰的连续实体**，叫 Super-agent。四性：
  - **连续**：一个 Agent 横跨 IM、GitHub 评论等渠道；在 IM 里定的计划 A，到 PR 评论里变成计划 B，系统认得是同一个任务。
  - **高效**：交互快、多个复杂任务并行、新指令不用等上一个跑完就能接。
  - **主动**：盯着环境事件，该推进的推进，不该说话时安静。
  - **持久**：一直在线、直连真实工作环境、异常自愈。
- 一个 ReAct Loop 交付不了这四性，得靠模型之外的系统。文章明确说没提新理论——是把经典计算机系统思想（调度、缓存、存算分离、外部看门狗）应用到 Agent 上。

## 2. 五大模块

### 2.1 Router + Worker 两层架构

- **取舍**：一个事件一个会话 = 连续性最好，但串行 ReAct 循环、完成时间长、吞吐低、任务细节混在一起拉低结果；一个事件一个全新会话 = 并发最好，但结果碎片化、没有全局上下文、多个会话同时回用户 = 混乱。
- **拆分**：**Router 层**（常驻）管全局连续性——所有人机交互、全局协调、全局时序点 / 协调点 / 记忆；**Worker 层**是上下文隔离的会话，并发执行具体任务。
- **Router 只做**：接收各入口的交互、汇总跨任务信息与决策、分派任务。**Router 不做**：执行具体任务；它甚至不需要 Bash 工具。活比看起来简单——**轻量模型往往就够**，速度 + 质量都占。
- **Router ≠ Agent Team 的队长**：队长是把一个复杂任务拆开、高频协调成员（重推理负载）；Router 只处理任务之间的高层关系与分派，绝不拆解单个任务内部。（反过来，一个主会话被 prompt 约束为永不执行、只分派的 Agent Team，也可以算这种两层架构。）
- **Router 扩容**：实现为单个常驻 LLM 会话；没那么容易成瓶颈——一轮推理中到达的 Trigger 会排队、下一轮一起处理，即**批处理**（见 §4）。规模再大：Router 内部多层过滤，或**横向分片**成多个会话——分片越细吞吐越高，但跨分片的记忆/连续性越低。当前规模下一个 Router 会话够用。
- **Worker**：每个 Worker 会话上下文隔离、挂满**完整执行工具**、专注**单个任务**；Worker 会话直接决定任务结果/代码质量，所以**通常用最强模型**。Worker **绝不直接跟人说话**——它的推理/工具调用不输出到外部渠道；它向 Router 汇报状态，由 Router 统一回复。Worker 之间通常不直接通信；冲突（比如同一个 PR）通常靠双方订阅同一个 Thread、看到同一批事件来解决；极少数跨任务协调走 Router。Worker 内部可以再建 subagent 或 Agent Team——对 Router 透明。编码场景（并行复现 bug、PR 评审、功能开发）与个人助手场景（前面一个聊天 UI，后面一个话题一个 Worker）都适用。
- **Session 只是实现细节**：用户面对的应该是一个 Super-agent；手动管理会话是"从底层 LLM API 继承来的设计惯性"。产品层面的项目/任务管理与底层会话解耦，成为独立的产品问题（§8.2）。

### 2.2 事件驱动 + 订阅直通

- **Trigger**：驱动不再是人敲的 prompt，而是**半结构化的环境事件**——群聊消息、邮件/日历提醒、代码评审评论、CI 结果。
- **两级过滤（Fast Path / Slow Path）**：真实事件流高噪声、低触发率。LLM 判断是灵活但昂贵的 Slow Path；确定性代码是便宜的 Fast Path。
  - *程序层（Fast Path）*：按来源、群范围、用户/bot 白名单做确定性准入——比如按来源定"只响应明确请求" / "作为候选" / "直接忽略"——大部分噪声在进模型前就滤掉了。
  - *语义层（Slow Path）*：通过程序层的候选交给 LLM，按 prompt 写好的策略 + 上下文判断要不要行动；语义层也是自然语言扩展点（用 prompt 开关/新增策略）。
- **订阅直通（事件路由）**：Router 只管新任务冷启动 + 跨任务协调。Router 根据某 Thread 的初始事件创建一个 Worker 后，该 Worker **直接订阅这个 Thread**；同一 Thread 的后续事件由**程序代码直送订阅的 Worker，不再经 Router 转发**。
  - *Thread*：一个 GitHub PR 下、一轮 IM 话题里、一条邮件链里连续的事件。
  - *已订阅（Fast Path）*：同一 Thread 的后续事件直达 Worker。新事件超出范围时，Worker 可以退订或交回 Router 重新分派。
  - *未订阅（Slow Path）*：Router 仍观察全部事件以维护全局状态，但只判断/分派未订阅的新事件。
  - **订阅是多对多**：一个 Worker 可以订阅多个 Thread；一个 Thread 可以被多个 Worker 订阅——同一个 PR 上的协作者都收到它的事件，不用点对点消息就能发现/解决冲突。输出侧：Worker 仍向 Router 汇报关键结论，由 Router 统一回复、同步全局记忆。
  - **实测效果（§7.1）**：去掉直通机制，完成时间基本不变，但 **Router 决策量多约 30%**，缓存读取 Token 从 **23.23M 涨到 31.77M（+约 37%）**。直通不提升速度/质量；它省的是 Router 的 Token 与推理量。
- **上下文当缓存——Inline 与 Spill、Chain of Recall**：塞太多，窗口拥挤、注意力稀释；塞太少，模型烧步骤去调工具读。**"浪费上下文窗口就是浪费模型智能。"**
  - *Inline*：把可能用到的信息直接放进上下文（省一次工具往返）。*Spill*：把超预算/低频的完整内容放窗口外，只留引用/摘要，按需读取。
  - 做法：(1) 从最小信息起步——对象 ID + 摘要；(2) 按局部性 Inline——关系密切的对象 ID，再是时空相邻的内容，比如内容前 50 字、相邻 IM 消息 + 被回复的那条消息、评审串里的相邻评论；(3) 超出一个小长度上限就 Spill——截断 + 一个"读更多"入口，模型需要时调工具读全文。
  - *Chain of Recall*：把 Inline 与 Spill 统一用到 Trigger、Thread、Worker Session 上——每个对象一个唯一 ID，注入的内容内联关系密切对象的 ID，形成引用图谱；每次工具取回的结果本身也遵循 Inline 与 Spill，内联下一跳的摘要 + ID，于是模型可以从当前消息 → 它的 Thread → 相关的 Worker Session → 那个 Worker 的另一条评审 Thread，一跳一跳按需取回。这缓解了 Router 长跑后丢失早期信息的问题。
- **推测执行**：在不知道结果会不会被用之前，先在后台行动，花额外的后台算力省人的等待/干预；有价值的结果送达，没价值的丢弃。个人助手例子：收到会议邀请邮件，先查日历冲突、搜背景、起草回复等用户确认。研发例子：DeepSeek 内部 Harness 用户群跑 **"静默复现并修复"** 策略——有人报问题/讨论改动时，Agent 在后台悄悄复现 + 找修复，只在确认了问题、找到了简单修复时才说话（比如群里还在讨论波浪线被渲染成删除线的 bug 时，Super-agent 已经开了修复 PR）。

### 2.3 全双工与多渠道适配

- **异步 ReAct Loop（全双工）**：经典 ReAct 在同步 `run()` 工具调用上阻塞，直到工具返回——期间会话无法响应新输入。改法：把长命令/子任务工具改成异步 **`start()` 与 `stop()`**。`start()` 立即返回 **"已启动"**；循环不再等待；后台工具完成时，系统把最终结果作为**一条新事件消息**送进会话；模型可以调 `stop()` 杀掉过长/无关的后台命令。前台对话与后台执行解耦：新输入在**当前推理步骤之后**处理，不用等后台工具。**"这一异步任务机制已经在 DeepSeek Harness 中实现，但尚未默认开启。"**
- **多渠道**：不同渠道信息密度/习惯不同；把单用户终端的长推理 + 密集工具调用原样倒进群聊会造成过载。两层设计已经把长推理/工具调用隔离在 Worker 会话里；Router 做对外沟通，按渠道定 prompt 规范：
  - *IM / 即时消息*：低打扰、轻量、像人类同事——**只在需要决策或验收时通知，只问直接问题，给简短结论。硬规则：单次回复不超过 100 词。**（注意：是 100 词，不是 100 字。）
  - *GitHub、邮件、文档（异步渠道）*：结构化、高信息密度异步交付——比如创建/更新 PR 时，按项目惯例写完整背景、改动说明与验证结果；个人助手场景里直接起草结构化邮件/文档摘要。

### 2.4 计算、状态、环境彻底解耦

- 本地 Agent 默认把三样东西绑在一台设备上：推进 Agent Loop 的**计算**、必须持久的**状态**（会话）、**环境**（代码仓库、本地工具链）。设备休眠/离线 = Agent 停摆，其他设备的环境也够不着。
- **第一步——计算/状态分离**：Agent Loop 的计算是无状态的 → 放进**无状态弹性云容器**；会话状态进**数据库**。容器可以横向扩容、重启或替换；连续性由持久存储保证。Agent 摆脱单台机器的生命周期，在云端持续在线。
- **第二步——计算/环境分离**：不把环境复制/同步到云端（真实环境里有未提交的改动、私有凭证、内网依赖、特定硬件/工具链——同步成本高且有损），也不强迫用户迁移到云端。Agent Loop 在云端跑，重状态的执行环境**留在原地**；只在端侧部署一个**不存会话状态的轻量守护进程**——它只执行命令、返回结果；Agent 按需通过它读环境上下文。
- 这与 Anthropic 的"脑/手"解耦一致（无状态 harness、会话日志在 harness 外、环境走统一接口）。区别：Anthropic 的文章讲的是托管服务（按需沙箱、客户 VPC 资源）；DeepSeek 的设计针对用户**日常的、可能间歇在线的个人机器**，带着未提交改动与本地凭证。
- **BYOM（Bring Your Own Machine）**：把开发者的日常机器或个人电脑接进云端 Agent；也支持云端托管机器或按需算力。一个 Agent 可以在执行设备间切换、按任务选环境、支持间歇在线的设备——比如用户设备重新上线时，云端 Agent 自动触发、完成需要那台设备的工作。

### 2.5 独立 Watchdog

- 持久化光靠 §2.4 不够：长期运行的分布式系统不能只靠主系统内部逻辑；需要在主系统之外设一个**外部控制循环**。
- 传统的进程存活探针/监控脚本**不够**：很多故障不是进程崩溃——模型陷入**无效循环**或**偏离目标**。长期运行的 Agent 系统必须监控**任务进展本身**，不只监控基础设施存活。
- 设计：主系统之外一个独立的 **Watchdog Session**，由**定时消息**驱动，形成外部 Control Loop。它处理基础设施故障（API 报错、状态恢复失败），**还用模型判断每个 Worker 是不是在取得实质进展、方向有没有偏离总体目标**。发现异常：及时干预修复；外部瞬时故障：持续复查直到恢复。
- 因为 Watchdog 本身也是一个带全套工具的 Agent Session，维护者可以用自然语言问它为什么失败，还能让它**在线修正主系统的行为**——比如增删 prompt、调整触发规则。

## 3. 实验（第 7 节，合成负载，初步参考）

文章明确说明：实验基于合成负载与简化环境，部分设置还可以更严谨，**以下结果仅作为初步参考**。

### 3.1 消融实验（端到端）

- 设置：群聊 + GitHub CI 消息流同时驱动**四种方案**。**每轮约 300 条消息，其中约 20 条是工作请求**；其余是闲聊、跟进、停止请求与 CI 消息。**编码工作被替换成一个只消耗时间的工具**——实验测的是**调度/协调能力，不是单任务执行能力**。**每种方案重复 5 次。**消息间隔与工作时长按 **1/4 缩放**；模型调用延迟是真实的。任务完成时间 = 从工作请求到结果消息。
- 四种方案：(1) Super-agent；(2) Super-agent **去掉直通**；(3) 单 Session + Subagent 工具，**中性 prompt**（"适当时用 subagent 处理一部分工作……"）；(4) 单 Session + Subagent 工具，**优先委派 prompt**（"聊天里的每条消息都会到你这儿，所以自己跑的工作总会被新消息打断。优先把每件工作交给各自的 subagent，自己只做小事……"）。

| 方案 | 任务完成 p50 / p95（分钟） | 每轮缓存读取 Token（全部会话） |
|---|---|---|
| Super-agent | **12.4 / 15.7** | 23.23M |
| Super-agent，去掉直通 | 12.6 / 15.5 | 31.77M |
| 单 Session + Subagent，中性 prompt | 20.4 / **29.5** | 6.05M |
| 单 Session + Subagent，优先委派 | 13.8 / 29.0 | 10.82M |

- 单会话为什么输：它依赖 prompt 工程 + 模型当时的判断。中性 prompt：**5 轮里模型一次也没调过 Subagent**——所有工作都留在主会话里，不断被新消息打断，p95 29.5 分钟。优先委派：5 轮里 4 轮委派了，但剩下一轮它判断工作"小"、自己干了，造出长尾（p95 29.0）。两层设计在系统层面修了这个问题：Router 永不执行，Worker 只收到它订阅的 Thread 的消息。
- Token 取舍：Super-agent 用**更多 Token 换更短、更稳定的完成时间**——23.23M 对 6.05M（约 3.8 倍）和 10.82M（约 2.1 倍）。去掉直通：完成时间基本不变，但 Router 决策量 **+约 30%**，缓存读取 Token **23.23M → 31.77M（+约 37%）**。
- **没测的东西：真实编码质量**（编码是计时工具）。没有独立基准；自报的合成负载。

### 3.2 Router 批处理压力测试

- Router 调真实模型，Worker 用 mock 模型。需要决策的 Trigger 到达率从**约 1/分钟提到约 40/分钟**；测平均批大小、单请求延迟、每次决策的摊销推理时间。
- 结果：平均批大小 **1.0 → 2.8**；单请求延迟只从 **2.5 秒 → 3.9 秒**（涨得比批大小慢，因为成批的 Trigger 在 Prefill 阶段并行计算）；每次决策摊销推理时间 **6.4 秒 → 1.6 秒**。突发下 Router 自动合并积压事件、提高有效吞吐——这也解释了为什么 §3.1 里去掉直通（Router 峰值负载更高）仍没撞上单 Router 的吞吐瓶颈。当前团队规模下，不需要分片 Router 而牺牲全局上下文连续性。

## 4. 原文自述的局限（第 8–9 节）

- **架构探索，不是产品功能**（开篇声明）；**"本文的部分设计已在 dsh-superagent-prototype 中实现……该插件只是一种为了验证技术路线而提供的原型，并非 DeepSeek 的正式产品"**——只有部分设计在原型里实现了。
- **合成/初步实验**（第 7 节引言）：合成负载、简化环境、编码是模拟的、每种方案 5 轮、时间按 1/4 缩放——"仅作为初步参考"。
- **多任务并行的 Token 成本**：多个独立会话意味着更高的缓存读取 Token 消耗（每轮 23.23M 对 6.05M/10.82M）——更短/更稳定的完成时间是用更多 Token 买的。
- **安全/隐私（§8.4）——最尖锐的一节**：事件驱动设计增加了不可信输入的暴露面；不解决安全/隐私，Super-agent"只有在一个很小且可信的范围才能工作"。云端 loop + 端侧守护进程的设计假设云端与端侧互相信任。但云端 loop 持续摄入外部环境事件，而端侧握着私有代码、敏感数据与本地凭证：**如果云端 Agent Loop 被服务器入侵或提示词注入攻破，每个接进来的端侧都面临被控制的风险**。即使没有攻破，如果端侧的凭证进了模型上下文，正常执行中也可能泄露——还需要一种机制，让 Agent **用凭证而不 ever 碰到凭证**。更广的应用要一边解决这个、一边从多样环境里取回上下文。
- **§8.1 两层设计的扩容**："单个常驻 Router Session + 订阅直通 + Worker 之间不直接通信"这套组合是覆盖当前多数日常任务的简化，工程成本低。任务规模/耦合度超出一个 Router 会话时，内部结构还没定——何时分片 Router、分片粒度、Worker 何时需要直接通信、用何种拓扑——还得在更多场景里测。模型/系统协同设计（给 Router 的事件判别、批量分派、上下文取回做专门训练）是未来方向。**长期记忆是主要扩容瓶颈**：跑上几个月后，常驻 Router + Chain of Recall 只解决近期任务/按需取回。
- **§8.2 会话藏起来之后的交互**：藏起多会话管理会带来新问题——怎么呈现任务、提供自然的交互/项目管理。以聊天窗口为中心的交互部分是路径依赖；交互可能移到领域专属界面（比如直接在 GitHub Issue/PR 里工作）；一个 UI 会话不必 1:1 对应一个执行会话。还没解决的：任务进行中的人参与——后台执行继续时，用户怎么实时干预/接管/协作；最终形态很可能按领域/个人风格高度定制。
- **§8.3 上下文边界与 A2A**：文章只设计单个 Super-agent 实例，假设所有在范围内的信息汇聚在一个全局上下文里。扩到更大组织要决定上下文共享与隔离的边界（共享范围 = 一个实例；隔离范围 = 各自的实例）。隔离实例之间的跨边界协作（比如每个成员的个人助手 vs 团队共用的 Super-agent）是不同权限边界下的 agent 间通信（A2A，不是某个具体协议）——怎么做才安全/可靠，还待探索。
- **§9 结论**：没有新理论——经典计算机系统工程思想应用到 Agent 上；实现会演进，但系统设计的思考据称有更长期的价值。

## 5. 原型档案：dsh-superagent-prototype

- **地址**：https://github.com/deepseek-ai/dsh-superagent-prototype
- **定位**：一个主动式编码 Agent，服务于**一个 GitHub 仓库**，打包成 DeepSeek Harness 的一个 bundle。监听 GitHub、可选飞书；允许的人提出工作时，它开一个工作项、在自己的 Agent 会话与目录里干活、在原对话里作答（比如提 PR）；网页面板只显示需要人处理的事。
- **状态（README 原话）**："Research prototype for reference only, not an official DeepSeek product." "Treat it as research code, not production-ready software. It may still contain bugs, and its coding style and engineering practices may be inconsistent. Review and adapt it before using it in your own environment." "We have adapted it for publication, so it is not identical to our internal version or the implementation described in *Exploring Super-agent Design*… Some designs discussed in the article are directions for future development and are not implemented in this prototype." 大量工程由 coding agent 完成，源自团队日常开发。
- **数据（2026-11-02 11:34 UTC）**：创建于 2026-10-31T09:32:46Z；1 个 commit；11,088 stars、1,134 forks；MIT；0 release。
- **内容**：`docs/`（000 Philosophy → 008 Cookbook）、`examples/`、`locale/`、`prompts/`、`scripts/`、`skills/`、`src/`、`tests/`、`SETUP.md`、`cordis.patch.yml`、`package.json`。
- **已实现的部分（按它自己的文档）**：Router = 主 Session，preset `dsh-superagent-router`（工具集较小；shell/job 等待上限几秒）；Worker = Executor Session `worker-<ticket id>`，preset `dsh-superagent-worker`，每个 Ticket 一个目录（`git worktree` 准备，10 分钟上限）；前台 shell 命令 5 秒后转后台，Worker 能在下一步收到新消息；Worker 槽位有并发上限 + **1 个额外槽位留给人的消息/状态请求**，新工作永远饿不死人的跟进；后台工作每轮上限 30 分钟；持久化 SQLite + outbox/effects 队列；接受模式 `off` / `observe`（默认） / `auto`；主动工作从只记录模式起步；自动合并默认关闭。
- **没 claims 的部分**：README 没列哪些文章设计未实现。在读过的原型文档里**没找到 Watchdog 组件**（二次报道说外部 Watchdog、存算分离、完整异步 ReAct 超出当前原型——按未核实处理，不当 README 的说法）。Worker 以**操作系统的用户身份无审批执行命令**——没有沙箱边界；屏蔽命令的 wrapper 只是默认值、不是安全边界（Worker 仍可用绝对路径执行）。只支持 github.com（据二次报道，不支持 GitHub Enterprise Server）。飞书可选，据一份二次报道默认在 `cordis.patch.yml` 里禁用。
- **部署（按 SETUP.md 的多份一致二次报道）**：Agent 驱动——"Read SETUP.md in this repository and set up dsh-superagent with me." 前置：Node.js 22.19+ 或 24+、pnpm、git 2.32+、tmux、Python 3.8+、GitHub CLI 2.48+、DeepSeek Harness 本体 + 配好的模型 provider、一个专用的 GitHub 账号（被邀进目标仓库）、飞书用 `lark-cli`。以专用的 Harness profile 运行（据报道端口 3082，分支前缀 `agent/`，接受模式 `observe`）。

## 6. 与 deepseek-harness（dsh）/ Cordis 的关系

- **上面的一层，不是 fork、不是 dsh 的一部分**。原型是 DeepSeek Harness 的一个 **bundle/plugin**：Harness 是开源 Agent 运行时；原型把 Super-agent 行为打包成 Harness bundle。它在自己的仓库（`deepseek-ai/dsh-superagent-prototype`），Harness 在自己的仓库（`github.com/deepseek-ai/deepseek-harness`，见 https://www.deepseek.com/en/harness/）。
- **Harness 本体**：DeepSeek 的开源 Agent harness，基于 **Cordis** "everything is a plugin" 元框架（模型、工具、技能、会话、沙箱、存储、Agent 循环、调度、UI 全是插件）。**公开预览**（harness 页面："now in public preview worldwide and open source"）；2026-08-13 以 developer preview 发布；安装 `npx @deepseek-ai/dsh web`（默认 UI 127.0.0.1:3080）。二次报道：developer preview，兼容性破坏变更在预期内，无安全审计，沙箱/审批控制不保证隔离。
- **Super-agent 从 Harness 拿了什么**：会话管理、工具执行、插件集成、（已实现但默认关闭的）异步任务机制、subagent/preset。原型的 Router/Worker preset（`dsh-superagent-router`、`dsh-superagent-worker`，Worker 的 subagent 用 Harness 的 `standard` preset）都是 Harness preset。
- **Super-agent 不是什么**：不是 Harness 的产品功能、不能在 Harness 里一键开启——文章说它的设计是架构探索，不是现有 Harness 功能。内部 Super-agent 实例是"基于这一思路与 DeepSeek Harness"搭建的——即**用** Harness 搭建，不是**在** Harness 里。

## 7. 可直接借鉴的实现细节

**调度/分派**
- 两层拆分：一个常驻 Router（轻模型、不需要 Bash、长输入/短输出的步骤）+ N 个隔离 Worker（最强模型、全套工具、一个任务一个）。绝不让 Router 执行；绝不让 Worker 直接回用户。
- Router 批处理是白送的：推理中到达的 Trigger 排队、合并进下一轮 LLM 调用；Prefill 并行算它们，于是每决策成本随负载下降（实测到达率 1 → 40/分钟，6.4 秒 → 1.6 秒）。批的上限看上下文长度与模型一轮能准确处理多少 Trigger。
- Worker 槽位：原型限制并发 Worker；留 **+1 槽位给人的消息/状态请求**，新工作永远饿不死人对已有 Ticket 的跟进；其他输入（比如 CI）等普通槽位。

**消息/事件格式与路由**
- 事件 = **Trigger**：一个不可变事件，带来源元数据 + 行为者；属于 1 个以上 **Thread**（时间有序的事件流：一个 PR、一个 IM 话题、一条邮件链）。来源把 Trigger 翻译成 Thread + 回复 **Channel**；来源持有自己的读位置，自己的 bot 消息在进入领域前丢掉（重启不能重放事件——靠已存的 Trigger 做幂等）。
- **Eval = 门控 + 评估**：确定性门控（白名单/准入表 → 强度 explicit/inferred/not-admitted），再由模型按 prompt 写好的规则评估；输出是 **Decision**：accept / stop / ignore / unavailable。一个 Thread 一次一个 Eval；期间到达的 Trigger 合并进下一批。Eval 过期：重排两次，第三次过期判 `unavailable`。
- **Ticket + Mandate**：接受后建一个 Ticket，带不可变的 **Mandate**（Policy 版本、范围、强度、匹配的规则、发送者身份、Trigger 是怎么收到的）。范围更宽 = 新 Ticket。只撤回 Mandate 的人才算停；Policy 变化不立即撤销 live Mandate（改为通知）。结束的 Ticket 保留 Mandate，人在它的 Thread 上发消息时恢复（按当前 Policy 重新验证）——bot/CI 不恢复它。
- **订阅扇出**：多对多 Ticket↔Thread；匹配的 Trigger 扇出给每个 live 的订阅 Ticket，不过门控、不授新权；人的消息到达某个 Ticket 归那个 Ticket（Executor 决定，超出范围交回）。纯上下文订阅只送消息，不授权限、没有恢复能力。
- **接受模式**（原型）：`off`（推断出的都不成候选）、`observe`（默认——推断出的候选被评估，阳性评估记为"会接受"，什么都不接受）、`auto`（阳性评估即接受）。明确请求在任何模式下都有效。从 `observe` 起步，看过记录的 Decision 后再切 `auto`。

**上下文/状态持久化**
- 上下文窗口当**缓存**：Inline（可能用到的信息放窗口里）vs Spill（超预算内容放窗口外、只留引用/摘要）。从最小起步（ID + 摘要）；按局部性 Inline（相关 ID、前 50 字、相邻消息、被回复的消息、评审串里的相邻评论）；Spill 带截断 + 读更多入口。
- **Chain of Recall**：给 Trigger/Thread/Worker-Session 对象唯一 ID；每个注入对象内联相关对象的 ID → 引用图谱；每次取回结果内联下一跳的摘要 + ID，支持多跳按需取回，不用把全部历史塞进 Router。
- **持久化（原型，具体实现）**：一个 **SQLite 数据库**（`src/app/store.ts`），目录锁防第二个进程；trigger/thread/ticket/decision 的 repository；类型化 KV；设置/prompt 是带编号的版本；启动时 schema 迁移到 11。**Engine 是 Trigger/Thread/Decision/Ticket/Assignment 的唯一写者**；每个命令一个事务；端口在事务内把外部工作排队、提交后由 adapter 执行（`afterCommit`）。**Effects** = 持久化副作用队列（种类：assessment、launch、delivery、relay、notice、reply），指数退避（2 秒倍增到 60 秒；回复 5 秒倍增到 300 秒），每种有健康记录。**Outbox** 是回复收据的唯一写者；来源离线时消息等待，对话没了/没监听时丢弃。
- **Pass**：一次一个 pass，每 2 秒一次 + 按需——到期的 effect，然后 `Engine.evaluateDue`（一个 Thread 一个 Eval，到达的 Trigger 合并成一批）。
- **重启恢复**：中断的 Assignment 带着恢复说明重启（先查目录、git 历史、GitHub 再重复外部动作），最老的 Ticket 先来；Session、目录、订阅、待处理消息、每个 Executor 已读进历史的消息记录，重启后都在；未送达/未读的输入恰好重送一次（Session 里还等着的副本在新 Assignment 第一条消息前删掉）。

**异步/全双工**
- 阻塞 `run()` 改成 `start()`/`stop()`；`start()` 立即返回"已启动"；完成时作为新事件到达；`stop()` 杀掉过长的任务。原型具体化：前台 shell **5 秒**后转后台（两个 preset 都是）；后台工作每轮上限 **30 分钟**，然后杀掉任务、Ticket 报等待；subagent 可以继续。新输入在下一步处理，不等长命令。
- **渠道塑形**：IM = ≤100 词、只在需要决策/验收时通知、一次一个具体问题、结构化形式；GitHub/邮件/文档 = 结构化高密度交付（PR 背景/改动/验证，按项目惯例）。

**Watchdog（实现思路，文章层面）**
- 独立 Watchdog Session，由定时消息驱动（外部 Control Loop）。查：基础设施故障（API 报错、状态恢复失败）**加模型判断的进展/漂移**（每个 Worker 是不是在取得实质进展？方向有没有偏离总体目标？）。异常时干预/修复；外部瞬时故障持续复查直到恢复。给它全套工具，维护者可以用自然语言问失败原因，让它在线改 prompt/触发规则。（公开原型里没找到已验证的 Watchdog 实现——见 §5。）

**安全/注意力预算（原型哲学，可直接复用）**
- "花尽可能少的人类注意力，换尽可能多的价值。" 只在被问到或书面规则允许时行动；只在人必须行动或能用上结果时说话；确认一次，干活时安静，有结果/问题/失败时再写。先收窄（短白名单、主动工作只记录），看过之后再放宽。消息/输入不能改权限——只有版本化的 Policy 能改。自动合并默认关闭；Executor 以操作系统的用户身份无审批运行——用专用 OS 账号、只接一个仓库、每份 PR 都审。
