# AI 学习资料目录

[← 返回首页](../../index.md)


*整理：2026-11-01 · 共 49 条*
*文件名链到本地总结，原文链到出处；49 条 = 下表条目数，也是学习清单总数（基础 19 + 专题 30）的口径，本站 .md 文件现为 49 个*


---

## 一、总纲（1）

| 本地总结 | 原文 | 说明 |
|---|---|---|

| [ai-learning-resources.md](./ai-learning-resources.md) | —（自建清单） | **总清单**：共 49 份（基础 19 + 专题 30），分级标注，专题按 7 组归类。本文件是旧版快照（只有基础 19 篇 + 补节），49 份完整版待下一步同步更新。 |


## 二、论文 / 长文详解（15）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [fde-gym-paper-summary.md](./fde-gym-paper-summary.md) | [arXiv 论文](https://arxiv.org/abs/2610.22350) · [解读帖](https://x.com/Xudong07452910/status/2111306709318951189) | FDE-Gym 论文详解：95 个真实交付任务测 AI 能不能干 FDE 的活；最好模型 0.56 分；文摘中文翻译 + 五个发现 + 对职业发展的 5 点启示 |
| [hedy-fde-knowledge-base-retrospective-work-notes.md](./hedy-fde-knowledge-base-retrospective-work-notes.md) | [X 长文](https://x.com/xiaomanhedy/status/2113174733344673956) | Hedy Zhang（一线 FDE）企业知识库复盘·工作版要点：知识库死于交付后无人运营、不死于检索；立项八步链路、答错先验源头、人工答过的问题五步回流、建设/维护/知识运营/新增需求四分报价；与 FDE-Gym 同为 FDE 主题，一个讲人怎么做、一个测 AI 能不能做 |
| [aliyun-ai-agent-handbook-summary.md](./aliyun-ai-agent-handbook-summary.md) | [GitHub 仓库](https://github.com/aliyun/ai-agent-handbook) | 阿里云《AI Agent Handbook》总结：30 章企业级 Agent 全生命周期指南；章节结构 + 核心观点 + 和你三个项目的咬合 |
| [longjing-ai-primer-summary.md](./longjing-ai-primer-summary.md) | [X 长文](https://x.com/long_jingai/status/2111356255889723723) | 龙井《2小时从零看懂AI》总结：2.5 万字企业内训稿；大模型通识 + 提示词六技巧 + Agent 三维度评估 + WorkBuddy 实操 |
| [opensre-summary.md](./opensre-summary.md) | [GitHub 仓库](https://github.com/Tracer-Cloud/opensre) | OpenSRE 总结：开源 AI SRE agent 工具包（"让 AI 值夜班"）；告警→拉取证据→脱敏→诊断→推 Slack 六步工作流；60+ 工具集成；咬合 Ping 割接 on-call、5070 本地 LLM、incident-to-eval |
| [generative-agents-summary.md](./generative-agents-summary.md) | [arXiv 论文](https://arxiv.org/abs/2304.03442) | Generative Agents / Smallville：Agent 记忆开山之作；Memory Stream 三维检索（recency/importance/relevance）+ Reflection 触发 + Planning 递归分解；Hot/Warm/Cold 是其显式分区版 |
| [harness2-summary.md](./harness2-summary.md) | [GitHub 仓库](https://github.com/google-research/harness2) · [推文](https://x.com/AISuperDomain/status/2111642569654378716) | Google Harness² 总结：不改模型权重、只优化外围系统，Agent 基准最高 +11.8pp；Propose-Probe-Compose 自博弈；8 个可编辑组件；三个项目咬合点 |
| [thin-orchestrator-summary.md](./thin-orchestrator-summary.md) | [Meta Engineering 博客](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/) | Meta《The Thin Orchestrator》：1,300 行确定性编排器 + 14 个隔离上下文专家子 agent；新用例只写 workflow template 不造新 agent；12 步缺口 01 状态机的生产级样本 |
| [decision-models-and-jev-summary.md](./decision-models-and-jev-summary.md) | [Hamel 博客](https://hamel.dev) · [推荐推](https://x.com/dongxi_nlp/status/2112652766997103016) | 决策模型与 Jev：输出概率不写文本的新品类；Hamel 阈值调优/Pareto 选型/校准验证方法论；Jev 三题型与独立实测；冷静派选型纪律 + thinktank judge 层咬合 |
| [agentic-rag-summary.md](./agentic-rag-summary.md) | [ByteByteGo 原文](https://blog.bytebytego.com/p/how-agentic-rag-works) · [X 图帖](https://x.com/alexxubyte/status/2112204626921762987) | Agentic RAG 总结：标准 RAG 三种死法（歧义/证据分散/虚假自信）与 agentic 三能力（路由/改写/自评）一一对应；光谱不是开关；评估者悖论与过度纠正；选型三问；open-memex 升级路径 + thinktank 咬合 |
| [posthog-fde-summary.md](./posthog-fde-summary.md) | [PostHog 博客](https://posthog.com/blog/what-is-a-forward-deployed-engineer) | PostHog《WTF is a forward deployed engineer?》：一家自己也在招 FDE 的公司写的最佳速查地图 |
| [pragmatic-engineer-fde-summary.md](./pragmatic-engineer-fde-summary.md) | [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/what-are-forward-deployed-engineers) | Pragmatic Engineer《What are Forward Deployed Engineers?》：关于 FDE 最扎实的一手深挖，定义、日常、方法、案例、反哺五件套齐全 |
| [revenuebrew-fde-summary.md](./revenuebrew-fde-summary.md) | [RevenueBrew](https://revenuebrew.com) | RevenueBrew《What it's like to work in tech's hottest new role》：唯一一份在职 FDE 本人出镜讲日常的报道 |
| [karpathy-llm-wiki-guide.md](./karpathy-llm-wiki-guide.md) | [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Karpathy《LLM Wiki》导读（第 49 份）：把知识一次编译进 wiki，而不是每次重算；三层架构 + 三个操作 |
| [karpathy-llm-wiki-summary.md](./karpathy-llm-wiki-summary.md) | [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Karpathy《LLM Wiki》详细摘要：三层架构与三个操作，写到不看原文能学到精髓；含 Graphify 实现 |

## 三、方法论文档（15，X 帖提炼）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [skill-trigger-hit-rate-methodology.md](./skill-trigger-hit-rate-methodology.md) | [X 原帖](https://x.com/kafkaup/status/2110964963284033978) | kafkaup：skill 触发命中率五方向（路由架构/匹配召回/样例库/边界/评估） |
| [anthropic-code-review-methodology.md](./anthropic-code-review-methodology.md) | [X 原帖](https://x.com/dongxi_nlp/status/2111202933849178210) | Anthropic 代码评审六实践；四条已入 AGENTS.md（互审≤3轮/失败变考题/谁拍板/换眼睛） |
| [tool-skill-mcp-methodology.md](./tool-skill-mcp-methodology.md) | [X 原帖](https://x.com/kafkaup/status/2111063860757057677) | kafkaup：Tool / Skill / MCP 三分法与选型 |
| [spec-driven-vibe-coding-summary.md](./spec-driven-vibe-coding-summary.md) | Google Drive（Lee Boonstra，Google，2026-05） | Spec-Driven 论文总结：spec 是 source of truth；tests 抓回归、evaluation 抓漂移；approval fatigue |
| [prompt-framework-and-agent-migration.md](./prompt-framework-and-agent-migration.md) | —（AIExplorerTim 帖 + 10-13 方法论） | Prompt 框架与 Agent 迁移手册 |
| [second-brain-deleted-summary.md](./second-brain-deleted-summary.md) | [原文](https://westenberg.beehiiv.com/p/i-deleted-my-second-brain) | Westenberg 删光第二大脑："forget on purpose"；curation > capture；open-memex 红队（该忘什么是—等公民） |
| [maliang-interview-questions-summary.md](./maliang-interview-questions-summary.md) | [X 长文](https://x.com/cxjwin/status/2111644503341953409) | 码良《Agent 高频面试题单》：343 篇牛客面经统计的 29 道高频题；RAG/AI Coding 工具/Skill-MCP 边界/Agent 评测/Harness；能力对标清单 |
| [sharma-agent-roadmap-summary.md](./sharma-agent-roadmap-summary.md) | [英文原帖](https://x.com/suraj_sharma14/status/2111789399176335412) · [中文解读](https://x.com/UPing123zzz/status/2112157681729564861) | Suraj Sharma《AI Agent 工程师 12 步学习路线图》：12 步（学什么/练手/为什么）；已做 8 步，缺口 03 操作电脑界面、06 沙箱执行 |
| [agentic-design-patterns-notes.md](../learning-notes/agentic-design-patterns-notes.md) | [GitHub](https://github.com/evoiz/Agentic-Design-Patterns) · [推荐帖](https://x.com/Huahuazo/status/2112037776044749145) | Antonio Gulli《Agentic Design Patterns》：21 章 + 7 附录开源教材，每章可运行 Jupyter；Prompt Chain/路由/反思、多 Agent/记忆/RAG、安全护栏；清单里第一本系统教材，当"查漏"的底；第 12–17 章学习笔记：异常恢复、Human-in-the-Loop、RAG、Agent 间通信、资源优化、推理技术 |
| [router-scheduling-summary.md](./router-scheduling-summary.md) | [X 原帖](https://x.com/kafkaup/status/2110500904868757542) | Router/调度：router 是 AI 产品的“调度台”，级联三层、决策四问、降级触发、评估五指标 |
| [karpathy-ai-funnel-summary.md](./karpathy-ai-funnel-summary.md) | [Karpathy](https://karpathy.ai) | Karpathy“AI 理解漏斗”：四层漏斗与三个成因 |
| [owasp-agentic-top10-summary.md](./owasp-agentic-top10-summary.md) | [OWASP](https://owasp.org) | OWASP《Top 10 for Agentic Applications 2026》：Agent 专用的十大风险分类 |
| [nist-ai-rmf-summary.md](./nist-ai-rmf-summary.md) | [NIST](https://www.nist.gov/itl/ai-risk-management-framework) | NIST《AI Risk Management Framework 1.0》+ Playbook + 生成式 AI Profile |
| [eu-gpai-code-summary.md](./eu-gpai-code-summary.md) | [欧盟](https://digital-strategy.ec.europa.eu/en/news/general-purpose-ai-code-practice-now-available) | 欧盟《通用人工智能行为准则》最终版 + EU AI Act 部署者义务 |
| [agentic-design-patterns-summary.md](./agentic-design-patterns-summary.md) | [GitHub](https://github.com/evoiz/Agentic-Design-Patterns) | Antonio Gulli《Agentic Design Patterns》导读（全书 21 章）：模式教材，学习笔记见 learning-notes |

## 四、工程原则与习惯（4）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [pstack-24-principles-zh.md](./pstack-24-principles-zh.md) | [GitHub cursor/plugins](https://github.com/cursor/plugins) | pstack 24 条工程原则（中英对照，Uncle Bob：把经典工程智慧重编码给 AI agent） |
| [ai-habits-as-institution-design.md](./ai-habits-as-institution-design.md) | —（小沐整理） | 把 AI 使用习惯做成可迁移的制度（含"白盒生产，黑盒交付"） |
| [agent-skill-writing-checklist-zh.md](./agent-skill-writing-checklist-zh.md) | mattpocock/skills（writing-for-agents） | 给 Agent 写文档的检查清单（译自原文） |
| [agents-md-portable-v02.md](./agents-md-portable-v02.md) | —（自建） | AGENTS.md 便携版 v0.2（最新；v0.1 为冻结快照） |

## 五、阅读筛选（1）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [x-worthwhile-reads-2026-10-16.md](./x-worthwhile-reads-2026-10-16.md) | —（小沐筛选） | 值得读的 X 帖子（只收对你有增量的，每篇一句话价值 + 核心观点 + 咬合点） |

## 六、项目方法论（4）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [open-memex-boundary-audit-2026-10-16.md](./open-memex-boundary-audit-2026-10-16.md) | —（小沐审计） | open-memex 边界审计：tool description 瘦身、pipeline tools 定位、企业版约束 |
| [ai-memory-summary.md](./ai-memory-summary.md) | [GitHub akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | akitaonrails/ai-memory（10k star，Rust）：跨 agent handoff 杀手功能、20+ harness 集成、零 LLM 记忆老化（access-weighted retention 正是三区换入换出策略的工程答案） |
| [mit-6s950-harness-lecture-summary.md](./mit-6s950-harness-lecture-summary.md)（附海报 mit-6s950-harness-lecture-poster.jpg） | [MIT 讲义原文](https://agencyai.mit.edu/w5/) · [shao__meng 介绍推](https://x.com/shao__meng/status/2112821429121204275) | MIT 6.S950 Lecture 5《The Harness》导读（第 27 份）：Baby Anigans 300 行教学 Agent；可观测性五维检查与厂商封存（正补清单自评缺口）；可控性三原则的经典谱系（1965/1968/1972/1975）；无通用最优 harness 与校准数据（±2%~±5%、成本 2 倍）——Harness² 的反面教材 |
| [mit-6s950-course-panorama-guide.md](./mit-6s950-course-panorama-guide.md) | [课程官网原文](https://agencyai.mit.edu/) · [shao__meng 全景导读](https://x.com/shao__meng/status/2103461095566676365) | MIT 6.S950《Agency with AI》课程全景（第 28 份，原文 + 导读成对）：Agency = 委托/验证/保留的判断力；官网明列 spec-driven development；Lec 4 "Specs before prompts"；评测即实验设计、审计产出物与评判者；导读 Lec 3–12 解读含作者推断，已标注——与第 27 份配套 |

## 七、框架与课程（9）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [pi-coding-agent-summary.md](./pi-coding-agent-summary.md) | [教程](https://x.com/xaiwind/status/2113084544375304503) · [仓库](https://github.com/earendil-works/pi) | Pi Coding Agent 导读（第 29 份）：把 harness 做到最薄的开源样本——内核只留工具循环 + 状态管理；分包、会话树、扩展点四种模型；无权限 / 审计是设计决定 |
| [strands-agents-sdk-summary.md](./strands-agents-sdk-summary.md) | [官方文档](https://strandsagents.com/) · [仓库](https://github.com/strands-agents/harness-sdk) | Strands Agents SDK 导读（第 30 份）：AWS 开源 agent 框架，「是库不是平台」；hooks 拦截 loop、guardrails 与 context 管理内置；与 AgentCore 配套 |
| [bedrock-agentcore-summary.md](./bedrock-agentcore-summary.md) | [AWS 官方 FAQ](https://aws.amazon.com/bedrock/agentcore/faqs/) | Bedrock AgentCore 导读（第 31 份）：agent 托管基础设施九件可组合取用；重点看 Policy / Identity / Observability 三件 |
| [umich-aase-summary.md](./umich-aase-summary.md) | [仓库](https://github.com/eecs498-aase/materials) · [课程站](https://eecs498-aase.github.io) | UMich EECS 498 AASE 导读（第 32 份）：把「指挥 agent 写代码」当工程学科教；分讲分级（6 讲对照正文）；Big Three、停止条件、EGM 五个 skill |
| [databricks-agentops-summary.md](./databricks-agentops-summary.md) | [Databricks](https://www.databricks.com) | Databricks《AgentOps on Databricks》：把 MLOps 的 deploy-code 模式搬到 agent 世界的一张完整全图 |
| [temporal-agents-sdlc-summary.md](./temporal-agents-sdlc-summary.md) | [AWS Builders](https://aws.amazon.com/blogs/) | AWS Builders《Orchestrating Our Agents SDLC on Temporal》：三份 Agent Ops 里最值得细读的一篇，纯实战 |
| [cresta-agent-observability-summary.md](./cresta-agent-observability-summary.md) | [Cresta](https://cresta.com) | Cresta《Observability for AI Agents》：trace 跨服务、多租户隔离、故障回放 |
| [learn-harness-engineering-summary.md](./learn-harness-engineering-summary.md) | [GitHub](https://github.com/walkinglabs/learn-harness-engineering) | walkinglabs《Learn Harness Engineering》（第 42 份）：从零亲手搭一个完整 harness 的动手课程 |
| [namiai-agent-summary.md](./namiai-agent-summary.md) | [namiai](https://namiai.tech/agent/?v=1) | namiai《从零手写 Agent》（第 48 份）：中文动手系列，从 100 行循环亲手搭出完整 Agent，再拆 7 个主流 Agent |

---

*注：随笔（人与 AI 的关系 part4 等）见 [human-ai-relationship-notes-part4.md](../human-ai-relationship-notes-part4.md)，另计。*
*以后新增 AI 资料时同步更新此目录。*
