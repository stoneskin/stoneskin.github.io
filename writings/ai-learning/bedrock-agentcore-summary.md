# Amazon Bedrock AgentCore 导读：Agent 的托管基础设施，九件可组合取用

> 官方文档：AWS 官方 FAQ https://aws.amazon.com/bedrock/agentcore/faqs/ （GA 于 2025-10）
> 读法：对照官方文档；与 Strands Agents SDK 配套读

---

## 一句话

Bedrock 的 agent 托管基础设施：Runtime / Memory / Gateway / Identity / Observability / Evaluations / Policy / Browser / Code Interpreter，九件可组合取用。Pi 故意不做的企业件，AWS 在这里做成了服务——Strands 是框架层，AgentCore 是它下面的基础设施层。

## 重点看的三件

- **Policy（新出）**：专管 agent 行为边界。读的时候要问：它能不能表达「写操作先审批」「只许访问白名单工具」这类规则？表达能力的边界，就是它能不能进生产的关键
- **Identity**：管 agent 以谁的身份跨 AWS 与第三方行动，与企业 IdP 对接是关键——身份问题不解决，agent 在企业里走不远
- **Observability**：走 OpenTelemetry 直进 CloudWatch（会话数、延迟、token、错误率 + 推理轨迹），是原生实现，不用自建适配层

## 其余组件一句话

- **Gateway**：把现有 API / Lambda / MCP server 统一成 agent 工具入口
- **Runtime**：框架无关，Strands、LangGraph、CrewAI 等都能跑；模型经 Bedrock 目录（Claude、Nova、GPT、Gemini 等）
- **Memory / Evaluations / Browser / Code Interpreter**：按需取用，不用全套照单全收

## 三个关键问题

1. **Policy 的表达能力与成本模型**：哪些组件可单用、迁出成本多大？锁定程度要先算清楚再上量
2. **Evaluations 的评测口径**：它的评测与多模型陪审团的 judge 审计有何异同？同一任务两种评法，差在哪？
3. **与 Pi 对照**：Pi 不做的九件事，AgentCore 一件件做成服务——每一件的代价（成本、锁定、复杂度）分别是什么？

## 跟其他材料的咬合

- **Strands Agents SDK**：框架 + 基础设施，两份合起来才是 AWS 路线的全貌；部署靶子就是 AgentCore Runtime
- **UMich AASE L09/L11**：停止条件与审批门，是验收 Policy 组件的清单
- **企业治理与安全材料**：Policy / Identity 这两件，正是企业场景最常见的缺口，读的时候对照着看
