# 《Spec-Driven Production Grade Development in the Age of Vibe Coding》总结

*作者：Lee Boonstra（Google），2026 年 5 月。来源：Stone 的 Google Drive（Day_5_v3.pdf）。小沐总结 + 缺口分析，2026-10-16。*

## 一句话

Vibe coding 解决了写代码的速度，但把瓶颈推到了下游——review、测试、集成。这篇是 Google 给出的生产级答案：**spec 是唯一的 source of truth，code 是 disposable 的**。

## 核心框架

### 1. Spec-Driven Development（SDD）

- 开发者角色从 coder 变成 architect：主要时间写高质量 spec，code 可以反复重新生成
- 好 spec = Architectural North Star：防 context fragmentation（传话游戏式的信息衰减）
- BDD/Gherkin（Given/When/Then）是终极工具：逼 LLM 按 State > Action > Outcome 思考，消除猜测
- 指令分四层存放，各管各的：
  1. Chat（临时的，只做高层编排）
  2. `specs/` 文件夹（随 repo 进版本控制：技术设计、BDD 场景、API 契约）
  3. Agent Skills（可复用的触发式工作流）
  4. System Prompts（全局身份：AGENTS.md 是跨工具共享层，项目级 GEMINI.md 优先级最高）
- 注：AGENTS.md 被点名为生态标准——跨工具共享指令层

### 2. 四种执行模式（不同的 mindset）

- Architect（从零搭架子）：先出目录结构+技术栈确认，不许直接写代码
- Builder（现有代码加功能）：风格对齐，diff 必须人看
- Forensic（修 bug）：从 Symptom Prompting 转向 Evidence Prompting（贴日志证据），只修根因，不顺手"清理"
- Author / Librarian（文档 / 数据）：文档即 truth，文档代码不同步 AI 就开始幻觉

### 3. MCP：一次集成，到处用

"USB-C for AI"——一个 MCP server，任何兼容 agent 直接用，不用重复写集成。

### 4. 团队文化与流程

- PR 策略：AI 生成的变更摘要+风险评估、Conditional LGTM（测试过了自动合）、no-blame 文化
- 三档 review agent：Tier 1 现成的（SaaS）、Tier 2 自写 skill + CI 触发（多数团队起点）、Tier 3 全自研（graph + 向量 + 子 agent pipeline，百万行遗产代码重构从两周压到几小时）
- **Approval fatigue**：高频 AI 用户 burnout 率高 45%；对策是结构化边界而非逐个 micro-approval

### 5. Zero-Trust：安全网

- 真实事故：YOLO 模式下 browser agent 误发 50 封幻觉邮件——guardrail 不是可选的
- Sandboxing（终端沙箱/容器）、Human-in-the-Loop（高风险操作设检查点）
- **Tests vs Evaluation**："Tests catch deterministic regressions; evaluation catches behavioural drift." 评测用打分+容忍带，不用二值断言
- Policy Server：结构门禁（YAML 规则，快）+ 语义门禁（LLM 审意图，防 PII 泄漏）
- Context Hygiene：PII 打码、占位符注入，防 context hallucination 泄漏敏感信息

## 我们还缺什么（按价值排序）

### 缺口 1：Evaluation harness（最值得补）
- 现状：thinktank 有 judge 审结论，但没有** scored judgment + tolerance band** 的正式 eval——"行为漂移"抓不到
- 动作：给 agent 任务加 eval 层：LLM-as-judge 打 0-5 分，设容忍带，低于阈值告警。这是 thinktank Phase 3"Router 视角"的天然延伸

### 缺口 2：BDD 式 spec（低成本高回报）
- 现状：有设计文档（D-series、V2-DESIGN），但不是 Given/When/Then 结构
- 动作：新功能的设计文档加一节 BDD 场景——"Given 初始状态 / When 动作 / Then 可验证结果"。逼自己把验收标准写死，agent 就没法猜

### 缺口 3：Approval fatigue 的自觉
- 现状："去/go/👌 零确认轮次"是效率最优，但论文点名了风险—— reflexive approve
- 动作：不用改流程，但立一条：**连续三次无脑 approve 同一类动作后，强制看一次 diff**。防的是"我"变成橡皮图章

### 缺口 4：Policy as code（长期）
- 现状：靠 runtime 的 approval card，没有自己的 policy 层
- 动作：远期。真要搞，按论文的 hybrid 模式：deterministic YAML 规则 + LLM 语义审。现在优先级不高

### 已经覆盖的（不用动）
- AGENTS.md 跨工具共享层 ✓（论文点名肯定）
- Skills 可复用工作流 ✓（3 个本地 skill + checklist）
- Prove It Works / done-means-verified ✓（原则已收编）
- Fix Root Causes ✓（刚收编）
- 不可逆动作人工确认 ✓（现有 approval 规则）
- MCP ✓（open-memex 就是 MCP-first）
