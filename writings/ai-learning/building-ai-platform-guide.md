# Vishal Panchal《在 AWS 上建 AI 平台》导读

[← 返回学习清单目录](./index.md)

> **原文**：Vishal Panchal，LinkedIn 帖子，2026-11-27，[lnkd.in/p/enEEgx39](https://lnkd.in/p/enEEgx39)
> **分级**：［摘要即可］——本页已把 6 组选型写到能独立成立，只看本页、跳过原文
> **编号**：第 73 份（组四 框架与平台）

## 导读层

### 一句话结论

这是一张在 AWS 上建 AI 平台的选型图：ECS Fargate 跑服务、SQS + EventBridge 做异步、Bedrock + LangGraph + MCP 做 AI、RDS PostgreSQL Multi-AZ 存数据，安全与可观测性各有一套——#70 的 9 层在 AWS 上的落点。

### 为什么值得看

与 #70 互补：#70 讲 vendor-neutral 的 9 层，这篇讲每一层在 AWS 上对应哪个服务。拿着 #70 去对架构、拿着这篇去对选型，两份一起读才是完整的"架构 + 落地"。

对 Stone 来说，价值在对照不在学习：ECS Fargate + PostgreSQL + 异步事件就是 PingPilot 的真实栈，这篇等于一份现成的 AWS 选型对照——你的系统已经按这个形状在跑了。对 AI SA 面试：AWS 选型题的标准答案骨架，问"在 AWS 上怎么搭 AI 平台"就按这 6 组答。

### 叙事主线

按一层一层摊开：计算与扩展 → 事件驱动 → AI 工程 → 安全网络 → 高可用 → CI/CD 与可观测性。最后作者自己收了一句：这只是一种可能的做法，取舍看负载、规模和预算。

### 怎么读

只看下面的 6 组表就够了。需要做 AWS 选型时，按组去找对应服务；不需要现在选型，知道每层在 AWS 上叫什么就够了。

## 精读层

### 1. 计算与扩展（Compute & Scalability）

- **Amazon ECS on Fargate**：容器跑服务，不用管服务器。
- **Application Load Balancer**：入口分流，配 Fargate 一起扩。

### 2. 事件驱动架构（Event-Driven Architecture）

- **Amazon SQS**：异步队列，任务排队慢慢跑，不用 HTTP 死等。
- **EventBridge Scheduler**：定时与事件触发，跑异步流程。

### 3. AI 工程（AI Engineering）

- **Amazon Bedrock**：托管模型入口，多模型一处调。
- **LangGraph**：编排 agent 的图框架，状态机式流程。
- **MCP**：工具统一协议，模型调工具走同一套接口。
- **多 LLM 集成**：不锁一家模型，按任务换。

### 4. 安全与网络（Security & Networking）

- **Private Subnets**：服务放私有子网，不直接暴露。
- **VPC Endpoints**：不出公网调 AWS 服务。
- **AWS WAF**：入口挡恶意流量。
- **IAM**：身份与权限，每个服务最小权限。
- **Secrets Manager**：密钥集中管，不进代码。

### 5. 高可用（High Availability）

- **Amazon RDS PostgreSQL，Multi-AZ**：主库挂了备库顶上，数据层的高可用。

### 6. CI/CD 与可观测性（CI/CD & Observability）

- **GitLab CI**：持续集成与部署。
- **Amazon ECR**：容器镜像仓库。
- **CloudWatch**：日志与指标监控。
- **AWS X-Ray**：分布式追踪，看请求在哪一环慢了。

### 小沐的分析与判断

- Bedrock + LangGraph + MCP 多模型，对上 #70 的模型层（小模型先行、大模型升级）。
- SQS + EventBridge，对上 #70 的异步骨干（事件不用 HTTP）。
- Secrets Manager + IAM + 私有子网，对上 #70 信任层的安全面。
- RDS Multi-AZ，对上高可用；CloudWatch + X-Ray，对上可观测性。
- 这篇缺的东西：没提评测（对照 #71 的 20 个评测工具）、没提治理词表（对照 #74 的 12 个治理词）、没提成本数字与规模取舍——选型时这三块要另外补。

### 证据不支持什么

- 帖子是服务清单 + 图，无深度分析、无数字、无实现细节，不能直接当搭建教程。
- 附图（架构图）未细读，服务之间的连线关系以正文列出的 6 组为准。
- 作者自己也说了只是一种可能的做法，取舍看负载、规模和预算——别把这张图当唯一答案。
