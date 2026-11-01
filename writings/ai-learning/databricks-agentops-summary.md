# Databricks《AgentOps on Databricks: Operating Production AI Agents》

[← 返回目录](index.md)

分级：【对照正文】（只读方法论部分，跳过 Databricks 产品细节）——把 MLOps 的 deploy-code 模式搬到 agent 世界的一张完整全图。

> 原文：https://community.databricks.com/t5/technical-blog/agentops-on-databricks-operating-production-ai-agents/ba-p/163602（Databricks 社区技术博客，2026-07-23）
> 一句话：评估门禁 + 可观测性闭环 + 提示词版本化 + 治理，是一张完整的 Agent Ops 全图。

- 核心论点：agent 是概率性的，严谨性从"上线前验一次"变成持续循环：评估度量质量、评估卡发布、追踪看生产流量、学到的东西喂回下一轮。
- 三环境流水线：一个 Git 仓、三个工作区（dev / staging / prod）。开发环境内循环：追踪 → 筛选 → 再评估；staging 跑单元测试 + 集成测试 + AgentOps 特有的评估门禁（更大评估集打分，全部 scorer 过阈值才放行，相当于 agent 世界的 champion/challenger）；release 后持续部署到生产，同时服务批量和实时流量。
- 可观测性闭环：追踪每一次请求（LLM 调用、工具调用、检索、延迟、成本）→ 线上用同一批 scorer 和 LLM judge 监控生产流量（质量、正确性、安全性）→ 人工反馈流回评估数据集，"今天的生产故障就是明天的测试用例"。
- 提示词按制品走发布：agent 大多是代码 + 提示词 + 工具，没有可发布的权重制品；可发布的是"配方"（配置分别部署到各环境）。提示词是唯一按制品式发布的组件：版本化资产、按别名（alias）提升。
- 治理变难不只是变大：传统 ML 治理"谁能碰模型/数据"；agent 还要治理"它被允许做什么"——运行时调用哪些工具、碰哪些数据、在什么策略下。工具、提示词、追踪、评估数据集放在同一个血缘和权限模型下管，人处在"定边界"的 on-the-loop 位置，而非每步审批的 in-the-loop 位置。
- 追踪必须是 OTel 原生的：同一份遥测既能进自家平台，也能双导出到 Datadog、Grafana；工程细节：MLflow 单个实验默认上限 10 万条 trace，上量后要把 trace 存进统一 catalog 才能长期保留。

### 跟你的咬合

- 评估门禁 + 线上同批 judge + 人工反馈回流，正是 thinktank judge/panel 机制放大到生产的样子。
- "人定边界而非每步审批"与"人是纠偏位不是瓶颈"同构。
