# Google Harness² 总结

[← 返回目录](index.md)

> 来源：@AISuperDomain 推文（2026-10-18）https://x.com/AISuperDomain/status/2111642569654378716
> 补充：@shao__meng 深度解读（2026-10-18）https://x.com/shao__meng/status/2111730826308452600 —— 补了 harnessing 级递归细节、parallel/sequential 模式、组件功能分组、实证发现
> 仓库：https://github.com/google-research/harness2（刚开源，10 star 起步）
> 一句话：不改模型权重，只靠自动重构外围工程系统，Agent 基准最高提升 11.8 个百分点。

## 核心论点

**Agent 遇新任务失效，瓶颈往往不在模型，而在写死的提示词、工具和编排逻辑。**

Harness² 把这套外围系统（Harness）变成了**可递归自优化的变量**——模型是常量，harness 是变量，优化变量就能涨分。

## 三个机制

### 1. 无答案自博弈（Propose–Probe–Compose）

- **提议**：生成对 harness 的候选改动
- **探测**：对比不同改动的执行行为（不是对比答案对错）
- **合成**：合成出新系统
- 关键：**无需标准答案反馈**——靠行为对比而非 ground truth
- 任务结束后沉淀经验，更新底层系统（经验复利）

### 2. 8 个可编辑组件（按作用分组，@shao__meng 补充）

- **上下文构建**（每次调用都生效）：System Prompt、Guardrails、Memory
- **工具接口**：Tool Guidance、Skills（Skills 按需加载，不占成本）
- **编排**：Subagents（**唯一会增加推理上下文**的组件）
- **脚本**：Scripts（新确定性能力，执行而非推理）
- **插件**：Plugins（TypeScript 中间件——"在工具环内**强制**一种行为，而非**指令**它"；enforce vs instruct）

### 3. Harnessing 级递归：持久库设计（@shao__meng 补充，核心新增）

任务级 Propose-Probe-Compose 之上还有第二层递归——持续改进的 improvement harness：

- 每个任务结束后，对完整改进记录做反思，把被采纳的 harness 和有证据支持的教训写入**按领域组织的持久库**
- **教训只有在执行对比支持时才保留**——单次选出好输出 ≠ 可迁移
- 库里存的是**可执行的组件文件**，不是散文式摘要，配一份 EXPERIENCE.md 记录适用场景和证据
- 下一个任务仍从**公共基础 harness** 出发（执行 harness 不继承），但 Propose/Probe/Compose 由更新后的库引导
- "Harness²"的双重含义：**改进 harness 的那个 harness 本身也在被改进**
- 消融验证：去掉 library，WorkBuddy-Bench 掉 3.1 分；库可跨基准迁移（JobBench 的库迁到 WorkBuddy-Bench 仍有 +0.6~+2.9）

### 4. 两种扩展模式（@shao__meng 补充）

- **parallel**：同时探测 k 组候选，k 个独立组合会话
- **sequential**：k 步链式精炼，逐步携带累积证据
- k=1 到 5 均单调提升

### 5. 实测收益（官方报告 + @shao__meng 补充的实证发现）

单步递归即可让 GLM-5 和 Gemini 3.5 Flash：
- WorkBuddy-Bench：最高 +11.5 分
- JobBench：+4.5 分
- LAB：+11.8 个百分点

**更值得注意的发现**（@shao__meng 整理）：
- **越弱的执行模型获益越大**：GLM-5 换上改进后的 harness 反超了 Gemini 的基础分数——"换 harness"在某些场景下顶得上"换模型"
- **跨模型迁移**：为 Gemini 精炼的 harness，给 GLM-5 在 Code 子集带来 +17.3；也胜过 Claude Code、Codex 的固定生产 harness 4.6–5.8 分
- **自编辑也涨**：执行器和编辑器用同一个模型也能涨（GLM-5 自编辑在 LAB 上 +13.7），不依赖更强的"老师"模型

## 与三个项目的咬合

### thinktank
- **8 组件审计**：System Prompt✓（panel/judge prompts）、Guardrails✓（contracts.py）、Memory△（member-state 只有模型分数，没有 prompt/编排经验）、Tool Guidance✓（skill manifests）、Subagents✓（panel members）、Skills✓（auto-skill）、Scripts△（tt/*.py 散装）、Plugins✗（缺）
- **可采用**：Propose-Probe-Compose 用于 judge prompt 优化——在 golden cases 上提议 prompt 变体、探测行为差异、合成最优版；member-state 从"记模型分数"扩展到"记 harness 改动效果"（经验沉淀）——直接对标 Harness² 的持久库设计：存可执行的 prompt/配置版本 + EXPERIENCE.md 式适用场景记录，教训只保留有执行对比支持的

### opencode-fuse
- **可采用**：8 组件作为 plugin 的配置面——用户可调的不只是选哪个模型，而是整套 harness；三档路由的调优走 Propose-Probe-Compose（提议路由规则→在真实任务探测→合成更优路由），这就是 /better 机制的工程化
- D19 候选：harness 版本化 + A/B 对比

### open-memex
- **定位**：Harness² 的 Memory 组件——open-memex 就是给 harness 用的记忆层
- **可采用**："任务结束沉淀经验更新底层"正是 open-memex capture/recall 的用武之地；V2 的跨 session 经验复用直接对上

## 论文原文的关键设计原则（primary source，2026-10-19 扒 arXiv:2610.14224）

**"ALWAYS-ON PROSE IS THE EXPENSIVE OPTION"**（Appendix H，editor prompt 原文）：
- 每次调用都生效的文字（system prompt、guardrails、memory），每个词都在和 agent 的输出预算竞争
- 最昂贵的失败就是"推理到预算耗尽、什么都没产出"——加 prose 让这种失败**更可能**，而不是更少
- 加 always-on 文字时，必须从别处**砍掉**等量的东西来"付账"

**组件成本层级**（按推荐顺序）：
1. **SKILL**（默认选项）：可识别触发器的新指令，on-demand 加载，调用前零成本
2. **SCRIPT**：确定性操作，runs 手写且写错/写慢了的
3. **SUBAGENT**：有界调查，输入大、答案小；输出和输入一样大时是亏本买卖
4. **PLUGIN**：工具环内机械性问题的唯一解——"prose 可以被跳过读，hook 不可以"；且不占 always-on 预算
5. **ALWAYS-ON TEXT**（最后手段）：只给真正每 run 都适用的短规则

**"A named component usually beats prose"**：skill/script/subagent 是下一个任务能调用或复制的东西；埋在 always-on 文字里的一段话，每次运行都要付费，且"travels badly"（跨任务迁移性差）。

**"WRITE THE FACT ITSELF"**：把验证过的事实本身写进组件，而不是"如何重新发现它"的流程。"告诉 agent 如何找 mapping 的规则，把最难的一步留给了 agent；mapping 本身则消除了这一步。"猜的事实比没有更糟。

**"Every edit must trace to a moment in a trajectory"**：每个改动必须能指着某次运行的某个时刻说"就是这里"。指不出来就是 speculation，白占 context。

**对 open-memex 的直接启示**：我们 session start 注入 8+5 条记忆走的正是"最贵的那条路"（always-on）。按这套理论，记忆应该尽量做成 on-demand（skill/工具调用时加载），常驻的只留真正每 turn 都需要的。这和 Stone"都是重要的，可以忍"的判断不冲突，但给出了优化方向：**把"重要但不是每 turn 需要"的往 on-demand 挪**。

**其他论文细节**：
- ReasoningBank（只做检索、不改 harness）在 coding 任务上比 base harness **低 6.6 分**——往 context 里塞策略可能起反作用，给"记忆污染"的担忧提供了实证
- 改进后的 harness 往往**步数更少**（WorkBuddy 上 Gemini 从 25.4 步降到 21.9 步）——好的 harness 更高效，不只是更准
- Harness Scaling（只花推理预算改、不跨任务带状态）在 12 个配置里 7 个不如 base——验证了"状态沉淀"的必要性
- 相关工作：RRSI（Regularized Recursive Self-Improvement，2026-10-04）专门解决 harness 优化的过拟合问题，值得跟进

## 方法论互文

- "harness 是变量"= build-the-lever 的学术版：先造能调 harness 的工具，而不是手调 prompt
- "无需标准答案"= golden cases 的反面：golden 测"答案对不对"，Harness² 测"行为有没有变好"
- 8 组件清单 = Lauren Tan 信任金字塔的展开：她的第 1 层（改代码库本身）细化成 8 个可调旋钮
- 与 FDE-Gym 呼应：FDE-Gym 说"挖隐性约束是最大断崖"，Harness² 说"瓶颈在外围系统不在模型"——都是"别只盯着模型"

## 注意事项

- 刚开源（10 star），代码成熟度未知，先读论文/报告再决定跟进深度
- 11.8 个百分点是官方报告数字，独立复现前打折扣听（explain-the-number：瓶颈先说清楚）
- GLM-5 和 Gemini 3.5 Flash 是 Google 自家生态，跨模型泛化性待验证
