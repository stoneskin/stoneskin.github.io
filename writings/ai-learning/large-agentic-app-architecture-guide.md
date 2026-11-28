# Gaurav Pandey《大型 agentic AI 应用的架构草图》导读

[← 返回学习清单目录](./index.md)

> **原文**：Gaurav Pandey，LinkedIn 帖子，2026-11-26，[lnkd.in/p/eDSgKe-b](https://lnkd.in/p/eDSgKe-b)
> **分级**：【摘要即可】——本页已把 9 层写到能独立成立，只看本页、跳过原文
> **编号**：第 70 份（组三 Harness 与课程）

## 导读层

### 一句话结论

模型只是一个框。大型 agentic 应用能不能在生产里跑，取决于模型周围的 8 层东西：入口网关、编排、工具、记忆、异步骨干、信任层、CI/CD——这篇就是一张一页纸的"生产系统需要什么"的检查清单。

### 为什么值得看

市面上大多数架构图都是"用户 → LLM → 回答"，这篇直接画了生产版：9 层，每层一句话 + 工具选型。它不是一篇教你怎么搭的教程，而是一张对照表——拿着它去对你自己的系统，一眼就能看出缺了哪层。

对 Stone 来说，价值在对照不在学习：AI Gateway 对上 PingPilot 的入口设计，信任层对上 Verifier + human on the loop，eval 门禁对上刚合进 main 的 eval 方法论。里面有两项是你的设计里有、但没单拎出来写死过的——kill switch（不用重新部署就能停掉任何 agent）和 agent 身份（每个 agent 有自己的身份）。这两项值得进 PingPilot/WorkBuddy 的设计清单。

### 叙事主线

作者的逻辑是一条线：先接用户（渠道），再过一道统一的门（AI Gateway），然后 supervisor 分工（编排），模型按需升级（小模型先行），所有外部系统走 MCP（工具），记忆分短期长期（知识），长任务别用 HTTP（异步骨干），最后信任层把所有层包起来，CI/CD 用 eval 门禁和金丝雀守住上线。越往后越是"生产"和"demo"的区别所在。

### 怎么读

摘要即可。本页精读层已把 9 层逐层写全。原文只有帖子正文 + 一张附图（附图未细读，9 层以正文为准），255 条评论未读。

## 精读层

### 1. 渠道（Channels）

Web、移动端、Teams、Slack、API——入口不止一个。含义：agent 系统从第一天起就是多入口的，渠道层要统一接进来，而不是每个渠道各搭一套。

### 2. AI Gateway

鉴权、限流、成本追踪、缓存、模型路由，集中在一个地方。工具：Azure API Management、LiteLLM、Kong。

这是整篇最值得单拎出来的一层：模型调用不该散落在各处，网关一把管住谁能调、调多少、花多少钱、有没有缓存、走哪个模型。对 PingPilot 的对照：入口设计里缺的就是这样一个显式的网关层。

### 3. 编排（Orchestration）

supervisor agent 做规划，分给 specialist agent 干活；checkpoint 让长任务能暂停、能续跑。工具：LangGraph、Microsoft Agent Framework。

Checkpoint 是关键：长任务不是一口气跑完的，能断点续跑才叫生产级。这点和南晚 12 条里的"断点续跑"、DeepSeek Super-agent 的异步设计是同一条线。

### 4. 模型（Models）

小模型先行，不够再上大模型。工具：Azure OpenAI、Gemini、Claude、vLLM 上跑的开源模型。

核心是路由不是选型：不是"选哪个模型最好"，而是"每个请求配哪个模型最划算"。这和 Iron Giant #61 里"Jev 决策便宜化"、ByteByteGo 成本优化 #52 是同一个省钱逻辑的不同落点。

### 5. 工具（Tools）

agent 碰的每个外部系统都走 MCP；高风险动作等人工批准。

两条纪律：统一协议（MCP）+ 人工审批卡在高风险动作上。后者直接对上 PingPilot 的 L1/L2/L3 和 human on the loop。

### 6. 知识与记忆（Knowledge and memory）

RAG、GraphRAG、短期状态、长期记忆。工具：Azure AI Search 或 Qdrant、Neo4j、Redis、Postgres。

四件套分得干净：检索（RAG/GraphRAG）+ 短期状态 + 长期记忆。open-memex 的三层区（Hot/Warm/Cold）正好是长期记忆这一格的实现。

### 7. 异步骨干（Async backbone）

长任务走事件，别用会超时的 HTTP。工具：Kafka、AKS 上的 worker。

一句话点破一个常见死法：HTTP 调 agent，任务跑 10 分钟，调用方早超时了。事件驱动 + worker 才是长任务的正确形状。

### 8. 信任层（Trust layer），包住所有层

- 每次输入输出都过 guardrail
- fallback：模型挂了换模型，agent 挂了转交或转人工
- kill switch：不用重新部署，立刻停掉任何 agent
- 每个动作都有 eval、tracing、审计日志
- 每个 agent 有自己的身份

工具：NeMo Guardrails、Ragas、Langfuse、OpenTelemetry。

这是全篇最硬的一层，也是和 Stone 现有设计咬合最深的一层：guardrail + fallback + 审计日志 ≈ PingPilot 的 Verifier + 决策日志；但 kill switch 和 agent 身份是新增项——你的设计里有"停"的能力（L 级别、人工介入），但没有写死成"一键停、不重新部署"；agent 身份（谁干的、算谁的账）在审计日志里是隐含的，没单列成设计要素。

### 9. 云上 CI/CD

提交 → 构建 → eval 门禁 → 5% 金丝雀 → 全量。质量或成本掉下来自动回滚。prompt 和 agent 配置像代码一样版本化部署。工具：GitHub Actions 或 Azure DevOps、Docker、Helm、ArgoCD。

关键两点：eval 是上线门禁不是事后复盘（对上 PingPilot eval 方法论里"Verifier 一致率达标才毕业到 L3"）；回滚触发条件是质量或成本掉下来——成本进回滚条件，这点少见，值得记。

### 小沐的分析与判断

**这篇的真正价值是"缺层检查表"，不是"怎么搭"。** 9 层里，Stone 的系统（PingPilot + WorkBuddy + open-memex + thinktank）大头都有了：编排、工具、记忆、人工审批、eval。缺口在三处：

1. **AI Gateway 没有显式的一层**——鉴权、限流、成本、缓存、路由现在散在各处，值得在 PingPilot 设计里单列。
2. **kill switch 没有写死**——"能停"是有的，"一键停、不用重新部署"是没写死的，补进设计清单。
3. **agent 身份没有单列**——审计日志记了动作，没把"哪个 agent 干的"当成一等公民。

**和清单里其他材料的分工**：#59 Anthropic《Harness design》讲的是 harness 内部的 evaluator 与拆分纪律，#61 Iron Giant 讲的是四层分工与成本，#64 Ethan《Agentic SDLC》讲的是交付流程的瓶颈转移——这篇补的是"生产系统的分层全景"，和它们互补不重复。读的时候按这个分工对，不用从头学。

### 证据不支持什么

- 这是 LinkedIn 帖子，一张草图 + 9 条清单，**没有实现细节、没有失败故事、没有数字**——别把它当成实战记录引用。
- 工具选型是 Azure 重的（APIM、AKS、Azure AI Search、Azure DevOps），和 Stone 的栈（AWS 为主）不一样；收的是分层本身，不是照搬工具。
- 附图未细读，9 层以帖子正文为准；255 条评论未读，评论区可能有补充和反驳，没核。
- 作者没给任何"这套架构跑了多大流量"的证据——分层的合理性靠常识支撑，不靠实测背书。
