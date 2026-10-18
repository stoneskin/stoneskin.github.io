# Google Harness² 总结

> 来源：@AISuperDomain 推文（2026-10-18）https://x.com/AISuperDomain/status/2111642569654378716
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

### 2. 8 个可编辑组件

动态调整：System Prompt、Guardrails、Memory、Tool Guidance、Subagents、Skills、Scripts、Plugins

### 3. 实测收益（官方报告）

单步递归即可让 GLM-5 和 Gemini 3.5 Flash：
- WorkBuddy-Bench：最高 +11.5 分
- JobBench：+4.5 分
- LAB：+11.8 个百分点

## 与三个项目的咬合

### thinktank
- **8 组件审计**：System Prompt✓（panel/judge prompts）、Guardrails✓（contracts.py）、Memory△（member-state 只有模型分数，没有 prompt/编排经验）、Tool Guidance✓（skill manifests）、Subagents✓（panel members）、Skills✓（auto-skill）、Scripts△（tt/*.py 散装）、Plugins✗（缺）
- **可采用**：Propose-Probe-Compose 用于 judge prompt 优化——在 golden cases 上提议 prompt 变体、探测行为差异、合成最优版；member-state 从"记模型分数"扩展到"记 harness 改动效果"（经验沉淀）

### opencode-fuse
- **可采用**：8 组件作为 plugin 的配置面——用户可调的不只是选哪个模型，而是整套 harness；三档路由的调优走 Propose-Probe-Compose（提议路由规则→在真实任务探测→合成更优路由），这就是 /better 机制的工程化
- D19 候选：harness 版本化 + A/B 对比

### open-memex
- **定位**：Harness² 的 Memory 组件——open-memex 就是给 harness 用的记忆层
- **可采用**："任务结束沉淀经验更新底层"正是 open-memex capture/recall 的用武之地；V2 的跨 session 经验复用直接对上

## 方法论互文

- "harness 是变量"= build-the-lever 的学术版：先造能调 harness 的工具，而不是手调 prompt
- "无需标准答案"= golden cases 的反面：golden 测"答案对不对"，Harness² 测"行为有没有变好"
- 8 组件清单 = Lauren Tan 信任金字塔的展开：她的第 1 层（改代码库本身）细化成 8 个可调旋钮
- 与 FDE-Gym 呼应：FDE-Gym 说"挖隐性约束是最大断崖"，Harness² 说"瓶颈在外围系统不在模型"——都是"别只盯着模型"

## 注意事项

- 刚开源（10 star），代码成熟度未知，先读论文/报告再决定跟进深度
- 11.8 个百分点是官方报告数字，独立复现前打折扣听（explain-the-number：瓶颈先说清楚）
- GLM-5 和 Gemini 3.5 Flash 是 Google 自家生态，跨模型泛化性待验证
