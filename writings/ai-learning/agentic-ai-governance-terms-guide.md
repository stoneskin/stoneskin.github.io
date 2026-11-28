# Soheib Kiani《12 个 Agentic AI 治理词》导读

[← 返回学习清单目录](./index.md)

> **原文**：Soheib Kiani，LinkedIn 帖子，2026-11-26，[lnkd.in/p/e8DVhcqC](https://lnkd.in/p/e8DVhcqC)
> **分级**：［摘要即可］——本页已把 12 个词按三阶段写到能独立成立，只看本页、跳过原文
> **编号**：第 74 份（组三 Harness 与课程）

## 导读层

### 一句话结论

当 AI 从"只回答问题"变成"能动手"（发邮件、改数据、花钱），治理就从管内容变成管控制——这篇是 12 个治理词的三阶段检查表。

### 为什么值得看

与 #70 的信任层、#71 的评测工具互补：#70 讲架构里信任层长什么样，#71 给评测工具箱，这篇给治理词表。三份一起读，才是"生产 agent 需要什么"的完整拼图。

对 Stone 来说，价值在对号入座：Agent Identity 与 Kill Switch 正是 #70 点过的值得补进 PingPilot 的两项；L0–L3 就是 Risk Tiering，human on the loop 就是 Human in the Loop——你的设计里这些东西都有了，这篇是帮你把它们叫出标准名字、排进三阶段。对 AI SA 面试：治理题的标准词表，问"agent 上生产怎么管"就按这三阶段答。

### 叙事主线

先立前提——只会回答的 AI，治理管的是内容；会动手脚的 AI，治理管的是控制。再按 agent 的生命周期摊开 12 个词：跑前 4 个、每次行动 4 个、事后持续 4 个。最后收到 day-one 最小集：最小权限 + 人工批准 + 审计轨迹，这三样 cover 了第一天的大部分风险。

### 怎么读

只看下面的三阶段表就够了。审自己的系统时，按三阶段逐项打勾；不需要现在审，记住 day-one 最小集那三样就够了。

## 精读层

### 1. 跑前（Before the agent runs）

- **Risk Tiering（风险分级）**：按影响给每个 agent 定级，风险越高、控制越严，思路同 EU AI Act 给 AI 系统分组。
- **Agent Identity（Agent 身份）**：每个 agent 有自己的身份与凭证，绝不用共享的人类登录——这样才知道是哪一个 agent 干了什么。
- **Least Privilege（最小权限）**：只给 agent 完成任务真正需要的工具、数据与权限，多一点都不给。
- **Policy as Code（策略即代码）**：规则（能做什么、能访问什么、能花多少）写成代码，自动强制执行，不躺在 PDF 里。

### 2. 每次行动（During every action）

- **Guardrails（护栏）**：输入与输出上的检查，挡住不安全、跑题或泄漏数据的回答。
- **Human in the Loop（人在回路里）**：高影响动作（付款、删除）发生前，先有人批准。
- **Budget Limits（预算上限）**：每个任务的 token、花费、步数、工具调用数设硬上限，死循环的 agent 烧不掉你的预算。
- **Kill Switch（紧急停止开关）**：agent 失控时能立刻停掉它。

### 3. 事后与持续（After, and continuously）

- **Audit Trail（审计轨迹）**：每次提示词、决策、工具调用的防篡改记录。
- **Observability（可观测性）**：追踪与指标，看得见 agent 干了什么、为什么这么干。
- **Continuous Evals（持续评测）**：上线后定期用真实案例测质量、安全与漂移，不是一次性的事。
- **Red Teaming（红队）**：先自己攻击自己的 agent——提示词注入、数据窃取、滥用——在别人动手之前。

### 附：原文给的三个资源

- **NIST AI Risk Management Framework**：管 AI 风险用得最广的框架。
- **OWASP Gen AI Security Project**：LLM 应用与 agent 的主要风险及缓解办法。
- **EU AI Act Explorer**：可读的、持续更新的 EU AI Act 与风险分级指南。

### 小沐的分析与判断

- 三阶段对应 agent 的生命周期：跑前定规矩、行动中设卡、事后留证据——PingPilot 的 L0–L3 + Verifier + human on the loop 正好是这套的实例。
- day-one 最小集（最小权限 + 人工批准 + 审计轨迹）与 PingPilot 的 L1/L2/L3 + Verifier 证据链对得上。
- Policy as Code 是 WorkBuddy 合规基线 §1.2 的方向：规则写死成确定性信号，不靠人每次记得。
- Budget Limits 对上智囊团的评测费用熔断思路：上限要写死，不能靠自觉。
- 注意：这 12 个词是治理词表，不是实施手册——每个词落到具体系统里怎么做，原文没展开。

### 证据不支持什么

- 12 个词都是一行定义，无实现细节、无工具选型，不能直接当搭建教程。
- 三个资源链接（NIST AI RMF、OWASP Gen AI、EU AI Act Explorer）目的地未验证——NIST 与 OWASP 是公开标准可信，lnkd.in 短链未点开核对。
- 原文没给任何数字与案例，"cover 大部分风险"是作者的判断，不是实测结论。
