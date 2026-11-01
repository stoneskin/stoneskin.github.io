# Cresta《Observability for AI Agents: Tracing Multi-Service LLM Pipelines with Langfuse》

[← 返回目录](index.md)

分级：【摘要即可】——三份里唯一讲"trace 跨服务、多租户隔离、故障回放"的。

> 原文：https://cresta.com/blog/observability-for-ai-agents-tracing-multi-service-llm-pipelines-with-langfuse（Cresta 工程博客；页面未显示发布日期与作者署名，本条不写日期）
> 一句话：一家真实跑多服务 agent 管线的公司，讲它怎么用自托管 Langfuse 把跨服务的 LLM 追踪、租户隔离与故障回放落到生产——正好补上前两份没展开的一角。

- 起点判断：生产中的 agent 不是单次模型调用。一次面向客户的语音/文字回复背后，是意图检测、知识检索、工具执行、安全校验等多步、每步多个模型、各自不同的延迟画像与故障模式；表面结果看起来正常时，检索步可能已返回无关文档、guardrail 可能已静默改写输出。所以需要每步的 trace：输入是什么、输出是什么、花了多久、多少钱——先看清，才谈得上评估、改进与扩量。
- Trace 的结构（typed trace tree）：Langfuse 把一次 agent 执行组织成 trace 树，每个节点是 typed observation（LLM 生成、检索、工具调用各有其结构化字段）：生成节点记 prompt 与 completion，检索节点记文档数与相关性分，guardrail 节点记通过/失败。粒度带来的调试变化是质变：从"有点慢"变成"合成回复步骤用了 3 倍预期 token，因为检索返回了两种语言的政策文档"。因为 observation 是 typed 的，还能跨 trace 查询：找出所有 total_tokens > 2000 的生成、或按文档数过滤检索（太多或太少都有问题）。
- 自托管与数据主权：他们不用托管 SaaS，自托管 Langfuse。理由是硬性的：trace 里有客户对话内容，即使 PII 在记录前一律脱敏，trace 数据不出自家基建边界仍是硬要求。部署方式：每个 Kubernetes 集群一个 Langfuse 实例、与产 trace 的服务同集群——没有 trace 数据离开集群边界；同时直接掌握留存策略、备份计划与资源分配；追踪数据四周内自动删除。
- 多租户 trace 隔离：多租户环境下 trace 隔离是合规要求：不同客户的数据处理协议不同，即使 PII 脱敏后对话数据仍须严格分隔。做法：每客户一个 Langfuse organization、各有独立 API 凭证；trace 创建时，追踪库根据入站请求里的客户上下文（由 auth 中间件设定）自动解析对应凭证，服务开发者不直接碰 API key 或路由逻辑。于是客户 A 的 trace 与客户 B 物理分隔，即使同一批 pod 同时服务两者也不存在交叉污染可能。
- 跨服务 trace 传播：一次客户交互常跨多个服务（Go 的 agent 服务、Python 的 RAG 管线、独立的工具执行函数包），trace 必须跟随请求跨过去。他们经 gRPC metadata header 传播 trace 上下文，由各服务的 interceptor 注入与提取；下游服务加入已有 trace、无需手动设置；每个服务初始化自己的 root span、其下 observations 嵌套；各服务独立导出 span，Langfuse 按匹配的 trace 与 span ID 重建整棵树。工程师在 UI 里看到的是跨语言边界拼好的完整调用树，无需手动 threading ID 或对日志。
- 用 trace 调试 agent 链（真正的价值点）：看全 trace 不只为了延迟与成本分析，更是为了端到端调试 agent 管线。Agentic 管线是 LLM 调用链，前一步输出喂给下一步；最终回复错时，根因通常不是最后一次生成，而是早几步的一个误导性中间输出把整条链带偏。没有结构化 trace 时极难诊断：最终回复看起来错，但每步单独的日志看起来都合理——问题只有在按顺序看到整条 prompt 与 completion 链时才显形。沿 trace 树从根走到叶，能定位输出分叉的具体步骤；典型例子：意图检测把"服务取消"误判成"账单咨询"，之后检索、生成、工具选择每一步都忠实地跟随了这个错误信号。trace 让因果链显式化，不用再靠猜测加 debug 日志重跑管线。
- 故障回放（sandbox replay）：Langfuse 的 sandbox 让团队定位到有问题的生成后，能从该点重放整条链：换模型、生成参数、prompt，但冻结之前全部输入与上下文；改请求、重跑、立刻看到改动如何传导到链的其余部分。迭代周期从"部署改动、等一个相似请求"变成"用候选修复在几秒内重放这次确切故障"。
- 下一步（作者自述的探索方向，未落地）：trace 上挂评估分（相关性、忠实度、连贯性等自动质量分），收紧生产行为与离线评估的环；prompt 工程 co-pilot（给非技术用户起草与调优 prompt，用 trace、eval run、自然语言反馈作 grounding，但避免对单一指标过拟合）；跨 prompt 版本的回归检测（比较 prompt 改动前后的 trace 级指标，量化影响，而不只依赖离线评估）。
- 局限也要明说：篇幅短、偏"我们怎么搭"而非"踩过哪些坑"（没有 Temporal 篇那种故障实录），且未展开评估门禁与成本治理——所以只给"摘要即可"，不与前两份并列对照正文。
- 与 Temporal 篇的呼应：Temporal 篇讲编排面 + LLM 面难对齐，这篇讲 LLM 面内部如何跨服务拼成一棵树。
