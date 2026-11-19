# AI 学习资料目录

[← 返回首页](../../index.html)


*整理：2026-11-19 · 共 60 份（基础 19 + 专题 41）*
*文件名链到本地总结，原文链到出处；下表 79 行：总纲 1 行、基础十九篇 19 行（无本地文件、原文直链）、其余 59 行；清单 60 份里 58 份有行（#35、#54 只在清单；#23、#27、#28 各占导读 + 摘要两行），其余为站内补充（非清单，不编号）；本站 .md 文件现为 59 个；编号 = 清单编号（第 N 份）；推荐度按对 AI Solutions Architect 目标的重要性与价值打分（中立，不按个人喜好）：★★★★★ 核心必读、★★★★☆ 值得精读、★★★☆☆ 值得一读、★★☆☆☆ 查阅参考、★☆☆☆☆ 了解即可，总纲行不打分；基础十九篇推荐度按分级折算（对照正文 ★★★★☆、摘要 ★★★☆☆、摘要（低优先）★★☆☆☆、概念即可 ★☆☆☆☆）*


---

## 一、总纲（1）

| 编号 | 本地总结 | 原文 | 说明 | 推荐度 |
|---|---|---|---|---|

| — | [ai-learning-resources.md](./ai-learning-resources.html) | —（自建清单） | **总清单**：共 60 份（基础 19 + 专题 41），分级标注，专题按 7 组归类；与私仓清单同步。 | — |

## 二、基础十九篇（19）

systemdesign.one 19 篇深度文章（@0xSilver_Time 2026-10-14 推文串），库里无本地文件、只读原文；推荐度按分级折算（见页顶说明）。

| 编号 | 本地总结 | 原文 | 说明 | 推荐度 |
|---|---|---|---|---|
| 1 | — | [What Makes an AI Agent Different From ChatGPT?](https://newsletter.systemdesign.one/p/ai-agents-explained) | Agent vs ChatGPT 的区别：agent 把 LLM 接上工具形成“行动→观察→重试”循环，ChatGPT 是单轮问答 | ★★★☆☆ |
| 2 | — | [9 Agentic Patterns, Simply Explained](https://newsletter.systemdesign.one/p/agentic-design-patterns) | 9 种 Agentic Patterns：reflection、tool use、planning、ReAct 等 9 种模式，搭 agent 时的“设计模式手册” | ★★★★☆ |
| 3 | — | [Multi-Agent Architectures, Clearly Explained](https://newsletter.systemdesign.one/p/multi-agent-system) | Multi-Agent 架构：supervisor/worker、串行 pipeline、并行 fan-out、辩论共识 | ★★★★☆ |
| 4 | — | [I struggled with AI agents until I built an incident response agent](https://newsletter.systemdesign.one/p/how-do-ai-agents-work) | 从零搭 Incident Response Agent 的血泪史：实战——工具怎么选、规划策略、记忆怎么管、guardrails 怎么设 | ★★★☆☆ |
| 5 | — | [AI Agents: State, Memory, Consistency - A Deep Dive](https://newsletter.systemdesign.one/p/ai-agent-memory) | Agent State / Memory / Consistency：短期记忆 vs 长期记忆；多步任务怎么保证 agent 不“失忆”不自相矛盾 | ★★★★☆ |
| 6 | — | [RAG - A Deep Dive](https://newsletter.systemdesign.one/p/how-rag-works) | RAG Deep Dive：查询时先检索外部文档拼进 prompt；关键在切分、检索、重排 | ★★★☆☆ |
| 7 | — | [Vector Database - A Deep Dive](https://newsletter.systemdesign.one/p/what-is-a-vector-database) | Vector Database Deep Dive：存 embedding 做语义检索；选型与什么时候该用、什么时候不该用 | ★★★☆☆ |
| 8 | — | [How Vector Database Search Billions of Vectors in Milliseconds](https://newsletter.systemdesign.one/p/hnsw-vector-search-explained) | HNSW 十亿向量毫秒检索：分层图索引，不用全量扫描；理解向量库底层的必看 | ★★★☆☆ |
| 9 | — | [MCP - A Deep Dive](https://newsletter.systemdesign.one/p/how-mcp-works) | MCP Deep Dive：Anthropic 的开放协议，统一模型接工具/数据的接口；一次适配，到处可用 | ★★★★☆ |
| 10 | — | [A2A Protocol - Deep Dive](https://newsletter.systemdesign.one/p/agent-to-agent-protocol) | A2A Protocol：不同厂商 agent 之间怎么通信协作；MCP 是 agent 接工具，A2A 是 agent 接 agent | ★★★☆☆ |
| 11 | — | [How to Build an AI Research Agent](https://newsletter.systemdesign.one/p/how-to-build-an-ai-research-agent-with-mcp) | 用 MCP 搭 Research Agent：实战端到端——规划研究问题→搜索资料→综合结论 | ★★★☆☆ |
| 12 | — | [Everything You Need to Know to Understand How LLMs Like ChatGPT Actually Work](https://newsletter.systemdesign.one/p/llm-concepts) | LLM 到底怎么工作：token、embedding、attention、context window；理解模型怎么“看”字 | ★★★☆☆ |
| 13 | — | [Context Engineering 101: How ChatGPT Stays on Track](https://newsletter.systemdesign.one/p/what-is-context-engineering) | Context Engineering 101：窗口里放什么、怎么放；核心是取舍 | ★★★★☆ |
| 14 | — | [Vertical Small LLMs: A Deep Dive](https://newsletter.systemdesign.one/p/fine-tuning-small-language-models) | 垂直领域小模型：特定任务上小模型 + 好数据能打败大模型；成本低、延迟低、可本地部署 | ★★★☆☆ |
| 15 | — | [How to Scale an “AI App” to 1 Million Users in Production](https://newsletter.systemdesign.one/p/llm-inference-cost-optimization) | AI App 扩到 100 万用户：缓存、batch、小模型处理简单任务、大模型只处理复杂任务 | ★★★☆☆ |
| 16 | — | [29 LLM Evaluation Concepts Every Engineer Needs to Know](https://newsletter.systemdesign.one/p/llm-evals) | 29 个 LLM 评测概念：测试集、打分标准、LLM-as-judge、人工评估 | ★★★★☆ |
| 17 | — | [Design a personal AI chat assistant](https://newsletter.systemdesign.one/p/ai-chat-assistant) | 设计个人 AI 助手：流式输出、会话历史、检索增强；偏产品向 | ★★☆☆☆ |
| 18 | — | [Fine Tuning: A Deep Dive](https://newsletter.systemdesign.one/p/llm-fine-tuning-guide-with-lora-and-qlora) | Fine Tuning Deep Dive：领域数据微调提准确率；什么时候该微调 vs RAG/prompt 就够 | ★☆☆☆☆ |
| 19 | — | [21 Reinforcement Learning (RL) Concepts Explained Simply](https://newsletter.systemdesign.one/p/what-is-reinforcement-learning) | 21 个强化学习概念：agent 在环境里行动、靠 reward 调策略；RLHF 就是 RL 的一种应用 | ★☆☆☆☆ |

## 三、论文 / 长文详解（22）

| 编号 | 本地总结 | 原文 | 说明 | 推荐度 |
|---|---|---|---|---|
| 43 | [fde-gym-paper-summary.md](./fde-gym-paper-summary.html) | [arXiv 论文](https://arxiv.org/abs/2610.22350) · [解读帖](https://x.com/Xudong07452910/status/2111306709318951189) | FDE-Gym 论文详解：95 个真实交付任务测 AI 能不能干 FDE 的活；最好模型 0.56 分；文摘中文翻译 + 五个发现 + 对职业发展的 5 点启示 | ★★★★★ |
| — | [hedy-fde-knowledge-base-retrospective-work-notes.md](./hedy-fde-knowledge-base-retrospective-work-notes.html) | [X 长文](https://x.com/xiaomanhedy/status/2113174733344673956) | Hedy Zhang（一线 FDE）企业知识库复盘·工作版要点：知识库死于交付后无人运营、不死于检索；立项八步链路、答错先验源头、人工答过的问题五步回流、建设/维护/知识运营/新增需求四分报价；与 FDE-Gym 同为 FDE 主题，一个讲人怎么做、一个测 AI 能不能做 | ★★★★☆ |
| 39 | [aliyun-ai-agent-handbook-summary.md](./aliyun-ai-agent-handbook-summary.html) | [GitHub 仓库](https://github.com/aliyun/ai-agent-handbook) | 阿里云《AI Agent Handbook》总结：30 章企业级 Agent 全生命周期指南；章节结构 + 核心观点 + 和你三个项目的咬合 | ★★★★☆ |
| 42 | [longjing-ai-primer-summary.md](./longjing-ai-primer-summary.html) | [X 长文](https://x.com/long_jingai/status/2111356255889723723) | 龙井《2小时从零看懂AI》总结：2.5 万字企业内训稿；大模型通识 + 提示词六技巧 + Agent 三维度评估 + WorkBuddy 实操 | ★★★★☆ |
| — | [opensre-summary.md](./opensre-summary.html) | [GitHub 仓库](https://github.com/Tracer-Cloud/opensre) | OpenSRE 总结：开源 AI SRE agent 工具包（"让 AI 值夜班"）；告警→拉取证据→脱敏→诊断→推 Slack 六步工作流；60+ 工具集成；咬合 Ping 割接 on-call、5070 本地 LLM、incident-to-eval | ★★★☆☆ |
| 26 | [generative-agents-summary.md](./generative-agents-summary.html) | [arXiv 论文](https://arxiv.org/abs/2304.03442) | Generative Agents / Smallville：Agent 记忆开山之作；Memory Stream 三维检索（recency/importance/relevance）+ Reflection 触发 + Planning 递归分解；Hot/Warm/Cold 是其显式分区版 | ★★★★☆ |
| — | [harness2-summary.md](./harness2-summary.html) | [GitHub 仓库](https://github.com/google-research/harness2) · [推文](https://x.com/AISuperDomain/status/2111642569654378716) | Google Harness² 总结：不改模型权重、只优化外围系统，Agent 基准最高 +11.8pp；Propose-Probe-Compose 自博弈；8 个可编辑组件；三个项目咬合点 | ★★★☆☆ |
| 21 | [thin-orchestrator-summary.md](./thin-orchestrator-summary.html) | [Meta Engineering 博客](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/) | Meta《The Thin Orchestrator》：1,300 行确定性编排器 + 14 个隔离上下文专家子 agent；新用例只写 workflow template 不造新 agent；12 步缺口 01 状态机的生产级样本 | ★★★★☆ |
| 22 | [decision-models-and-jev-summary.md](./decision-models-and-jev-summary.html) | [Hamel 博客](https://hamel.dev) · [推荐推](https://x.com/dongxi_nlp/status/2112652766997103016) | 决策模型与 Jev：输出概率不写文本的新品类；Hamel 阈值调优/Pareto 选型/校准验证方法论；Jev 三题型与独立实测；冷静派选型纪律 + thinktank judge 层咬合 | ★★★☆☆ |
| 25 | [agentic-rag-summary.md](./agentic-rag-summary.html) | [ByteByteGo 原文](https://blog.bytebytego.com/p/how-agentic-rag-works) · [X 图帖](https://x.com/alexxubyte/status/2112204626921762987) | Agentic RAG 总结：标准 RAG 三种死法（歧义/证据分散/虚假自信）与 agentic 三能力（路由/改写/自评）一一对应；光谱不是开关；评估者悖论与过度纠正；选型三问；open-memex 升级路径 + thinktank 咬合 | ★★★★☆ |
| 47 | [posthog-fde-summary.md](./posthog-fde-summary.html) | [PostHog 博客](https://posthog.com/blog/what-is-a-forward-deployed-engineer) | PostHog《WTF is a forward deployed engineer?》：一家自己也在招 FDE 的公司写的最佳速查地图 | ★★★☆☆ |
| 46 | [pragmatic-engineer-fde-summary.md](./pragmatic-engineer-fde-summary.html) | [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/what-are-forward-deployed-engineers) | Pragmatic Engineer《What are Forward Deployed Engineers?》：关于 FDE 最扎实的一手深挖，定义、日常、方法、案例、反哺五件套齐全 | ★★★★★ |
| 48 | [revenuebrew-fde-summary.md](./revenuebrew-fde-summary.html) | [RevenueBrew](https://revenuebrew.com) | RevenueBrew《What it's like to work in tech's hottest new role》：唯一一份在职 FDE 本人出镜讲日常的报道 | ★★★☆☆ |
| 27 | [karpathy-llm-wiki-guide.md](./karpathy-llm-wiki-guide.html) | [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Karpathy《LLM Wiki》导读：把知识一次编译进 wiki，而不是每次重算；三层架构 + 三个操作 | ★★★★☆ |
| 27 | [karpathy-llm-wiki-summary.md](./karpathy-llm-wiki-summary.html) | [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Karpathy《LLM Wiki》详细摘要：三层架构与三个操作，写到不看原文能学到精髓；含 Graphify 实现 | ★★★★☆ |
| 23 | [deepseek-super-agent-guide.md](./deepseek-super-agent-guide.html) | [全文转贴](https://www.uied.cn/posts/922127) · [原型](https://github.com/deepseek-ai/dsh-superagent-prototype) | DeepSeek《Super-agent 设计探索》导读：多任务的上限是人的注意力；Router + Worker、事件直通、Watchdog 五大模块 | ★★★★☆ |
| 23 | [deepseek-super-agent-summary.md](./deepseek-super-agent-summary.html) | [全文转贴](https://www.uied.cn/posts/922127) · [原型](https://github.com/deepseek-ai/dsh-superagent-prototype) | DeepSeek《Super-agent 设计探索》详细摘要：五大模块、实验数据（p50 12.4 分钟）、安全局限、原型档案；写到不看原文能学到精髓 | ★★★★☆ |
| 24 | [claude-fold-subagents-guide.md](./claude-fold-subagents-guide.html) | [原文](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop) · [迁移 kit](https://github.com/anthropics/single-agent-loop-kit) | Anthropic《When to fold subagents into your main agent loop》导读：单 Agent + Skills 常打赢多 subagent；subagent 只留三处；迁移凭任务完成 eval、一次折一个；与 DeepSeek Super-agent 互补（任务内精简 vs 任务间组织） | ★★★★★ |
| 28 | [sag2-guide.md](./sag2-guide.html) | [arXiv 论文](https://arxiv.org/abs/2610.22588) · [评测代码](https://github.com/Zleap-AI/SAG-Benchmark) | SAG2《无 embedding 多跳检索》导读：本地只剩 SQLite + BM25 索引，Jev 在查询时逐段判证据、供词扩下一轮；Jev 第一个公开实战用法 | ★★★★☆ |
| 28 | [sag2-summary.md](./sag2-summary.html) | [arXiv 论文](https://arxiv.org/abs/2610.22588) · [评测代码](https://github.com/Zleap-AI/SAG-Benchmark) | SAG2《无 embedding 多跳检索》详细摘要：三轮检索流程、Recall@10 三项第一（86.62% / 97.43% / 99.00%）、消融与成本、局限与二手文章纠正；写到不看原文能学到精髓 | ★★★★☆ |
| 58 | [openai-harness-engineering-guide.md](./openai-harness-engineering-guide.html) | [原文](https://openai.com/index/harness-engineering/) | OpenAI《Harness engineering》导读：5 个月、0 行手写代码的 agent-first 实战记录；“harness engineering”推成主流的那篇；纪律不在代码里，在脚手架里 | ★★★★☆ |
| 59 | [anthropic-harness-design-guide.md](./anthropic-harness-design-guide.html) | [原文](https://www.anthropic.com/research/harness-design-long-running-apps) | Anthropic《Harness design for long-running apps》导读：别让 agent 给自己打分；怀疑型 evaluator 与“模型一强就拆 harness” | ★★★★☆ |
| 60 | [ethan-rag-eval-guide.md](./ethan-rag-eval-guide.html) | [X 长文](https://x.com/UPing123zzz/status/2123245117930942775) | Ethan《RAG 评测》导读：答错先问错在哪一层——检索、忠实度还是旧版内容；评测是持续验证机制，不是仪表盘；直接对上 open-memex 0.11.0 的 rerank 与 memory_recall | ★★★★☆ |
## 四、方法论文档（17，X 帖提炼）

| 编号 | 本地总结 | 原文 | 说明 | 推荐度 |
|---|---|---|---|---|
| — | [skill-trigger-hit-rate-methodology.md](./skill-trigger-hit-rate-methodology.html) | [X 原帖](https://x.com/kafkaup/status/2110964963284033978) | kafkaup：skill 触发命中率五方向（路由架构/匹配召回/样例库/边界/评估） | ★★★☆☆ |
| — | [anthropic-code-review-methodology.md](./anthropic-code-review-methodology.html) | [X 原帖](https://x.com/dongxi_nlp/status/2111202933849178210) | Anthropic 代码评审六实践；四条已入 AGENTS.md（互审≤3轮/失败变考题/谁拍板/换眼睛） | ★★★★☆ |
| — | [tool-skill-mcp-methodology.md](./tool-skill-mcp-methodology.html) | [X 原帖](https://x.com/kafkaup/status/2111063860757057677) | kafkaup：Tool / Skill / MCP 三分法与选型 | ★★★☆☆ |
| — | [spec-driven-vibe-coding-summary.md](./spec-driven-vibe-coding-summary.html) | Google Drive（Lee Boonstra，Google，2026-05） | Spec-Driven 论文总结：spec 是 source of truth；tests 抓回归、evaluation 抓漂移；approval fatigue | ★★★★☆ |
| — | [prompt-framework-and-agent-migration.md](./prompt-framework-and-agent-migration.html) | —（AIExplorerTim 帖 + 10-13 方法论） | Prompt 框架与 Agent 迁移手册 | ★★★☆☆ |
| — | [second-brain-deleted-summary.md](./second-brain-deleted-summary.html) | [原文](https://westenberg.beehiiv.com/p/i-deleted-my-second-brain) | Westenberg 删光第二大脑："forget on purpose"；curation > capture；open-memex 红队（该忘什么是—等公民） | ★★★☆☆ |
| 44 | [maliang-interview-questions-summary.md](./maliang-interview-questions-summary.html) | [X 长文](https://x.com/cxjwin/status/2111644503341953409) | 码良《Agent 高频面试题单》：343 篇牛客面经统计的 29 道高频题；RAG/AI Coding 工具/Skill-MCP 边界/Agent 评测/Harness；能力对标清单 | ★★★☆☆ |
| 41 | [sharma-agent-roadmap-summary.md](./sharma-agent-roadmap-summary.html) | [英文原帖](https://x.com/suraj_sharma14/status/2111789399176335412) · [中文解读](https://x.com/UPing123zzz/status/2112157681729564861) | Suraj Sharma《AI Agent 工程师 12 步学习路线图》：12 步（学什么/练手/为什么）；已做 8 步，缺口 03 操作电脑界面、06 沙箱执行 | ★★★★☆ |
| 40 | [agentic-design-patterns-notes.md](../learning-notes/agentic-design-patterns-notes.html) | [GitHub](https://github.com/evoiz/Agentic-Design-Patterns) · [推荐帖](https://x.com/Huahuazo/status/2112037776044749145) | Antonio Gulli《Agentic Design Patterns》：21 章 + 7 附录开源教材，每章可运行 Jupyter；Prompt Chain/路由/反思、多 Agent/记忆/RAG、安全护栏；清单里第一本系统教材，当"查漏"的底；第 12–17 章学习笔记：异常恢复、Human-in-the-Loop、RAG、Agent 间通信、资源优化、推理技术 | ★★★★★ |
| 20 | [router-scheduling-summary.md](./router-scheduling-summary.html) | [X 原帖](https://x.com/kafkaup/status/2110500904868757542) | Router/调度：router 是 AI 产品的“调度台”，级联三层、决策四问、降级触发、评估五指标 | ★★★★☆ |
| 45 | [karpathy-ai-funnel-summary.md](./karpathy-ai-funnel-summary.html) | [Karpathy](https://karpathy.ai) | Karpathy“AI 理解漏斗”：四层漏斗与三个成因 | ★★★☆☆ |
| 55 | [owasp-agentic-top10-summary.md](./owasp-agentic-top10-summary.html) | [OWASP](https://owasp.org) | OWASP《Top 10 for Agentic Applications 2026》：Agent 专用的十大风险分类 | ★★★★☆ |
| 56 | [nist-ai-rmf-summary.md](./nist-ai-rmf-summary.html) | [NIST](https://www.nist.gov/itl/ai-risk-management-framework) | NIST《AI Risk Management Framework 1.0》+ Playbook + 生成式 AI Profile | ★★★☆☆ |
| 57 | [eu-gpai-code-summary.md](./eu-gpai-code-summary.html) | [欧盟](https://digital-strategy.ec.europa.eu/en/news/general-purpose-ai-code-practice-now-available) | 欧盟《通用人工智能行为准则》最终版 + EU AI Act 部署者义务 | ★★★☆☆ |
| 40 | [agentic-design-patterns-summary.md](./agentic-design-patterns-summary.html) | [GitHub](https://github.com/evoiz/Agentic-Design-Patterns) | Antonio Gulli《Agentic Design Patterns》导读（全书 21 章）：模式教材，学习笔记见 learning-notes | ★★★★★ |
| 52 | [cost-optimization-strategies-guide.md](./cost-optimization-strategies-guide.html) | [X 原帖](https://x.com/alexxubyte/status/2117302471156781430) | ByteByteGo《Top 6 Cost Optimization Strategies in AI Systems》导读：AI 系统成本优化六策——提示词缓存、模型路由、批量接口、语义缓存、精简上下文、用小模型；原图 GIF 已重绘为矢量图 | ★★★☆☆ |
| 53 | [xiaohui-verification-skill-summary.md](./xiaohui-verification-skill-summary.html) | [X 原帖](https://x.com/xiaohuiyuan/status/2118496773706797338) | 晓辉博士《Skill 自迭代能力改造指南》导读：先验证再迭代——黄金样例 + 脚本检查 + 反馈日志，skill 自迭代的操作手册；与 yetone Agent Loop 咬合 | ★★★★☆ |

## 五、工程原则与习惯（4）

| 编号 | 本地总结 | 原文 | 说明 | 推荐度 |
|---|---|---|---|---|
| — | [pstack-24-principles-zh.md](./pstack-24-principles-zh.html) | [GitHub cursor/plugins](https://github.com/cursor/plugins) | pstack 24 条工程原则（中英对照，Uncle Bob：把经典工程智慧重编码给 AI agent） | ★★★☆☆ |
| — | [ai-habits-as-institution-design.md](./ai-habits-as-institution-design.html) | —（小沐整理） | 把 AI 使用习惯做成可迁移的制度（含"白盒生产，黑盒交付"） | ★★★☆☆ |
| — | [agent-skill-writing-checklist-zh.md](./agent-skill-writing-checklist-zh.html) | mattpocock/skills（writing-for-agents） | 给 Agent 写文档的检查清单（译自原文） | ★★★☆☆ |
| — | [agents-md-portable-v02.md](./agents-md-portable-v02.html) | —（自建） | AGENTS.md 便携版 v0.2（最新；v0.1 为冻结快照） | ★★★☆☆ |

## 六、阅读筛选（1）

| 编号 | 本地总结 | 原文 | 说明 | 推荐度 |
|---|---|---|---|---|
| — | [x-worthwhile-reads-2026-10-16.md](./x-worthwhile-reads-2026-10-16.html) | —（小沐筛选） | 值得读的 X 帖子（只收对你有增量的，每篇一句话价值 + 核心观点 + 咬合点） | ★★☆☆☆ |

## 七、项目方法论（4）

| 编号 | 本地总结 | 原文 | 说明 | 推荐度 |
|---|---|---|---|---|
| — | [open-memex-boundary-audit-2026-10-16.md](./open-memex-boundary-audit-2026-10-16.html) | —（小沐审计） | open-memex 边界审计：tool description 瘦身、pipeline tools 定位、企业版约束 | ★★★☆☆ |
| — | [ai-memory-summary.md](./ai-memory-summary.html) | [GitHub akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | akitaonrails/ai-memory（10k star，Rust）：跨 agent handoff 杀手功能、20+ harness 集成、零 LLM 记忆老化（access-weighted retention 正是三区换入换出策略的工程答案） | ★★★☆☆ |
| 29 | [mit-6s950-harness-lecture-summary.md](./mit-6s950-harness-lecture-summary.html)（附海报 mit-6s950-harness-lecture-poster.jpg） | [MIT 讲义原文](https://agencyai.mit.edu/w5/) · [shao__meng 介绍推](https://x.com/shao__meng/status/2112821429121204275) | MIT 6.S950 Lecture 5《The Harness》导读：Baby Anigans 300 行教学 Agent；可观测性五维检查与厂商封存（正补清单自评缺口）；可控性三原则的经典谱系（1965/1968/1972/1975）；无通用最优 harness 与校准数据（±2%~±5%、成本 2 倍）——Harness² 的反面教材 | ★★★★★ |
| 30 | [mit-6s950-course-panorama-guide.md](./mit-6s950-course-panorama-guide.html) | [课程官网原文](https://agencyai.mit.edu/) · [shao__meng 全景导读](https://x.com/shao__meng/status/2103461095566676365) | MIT 6.S950《Agency with AI》课程全景（原文 + 导读成对）：Agency = 委托/验证/保留的判断力；官网明列 spec-driven development；Lec 4 "Specs before prompts"；评测即实验设计、审计产出物与评判者；导读 Lec 3–12 解读含作者推断，已标注——与第 29 份配套 | ★★★★☆ |

## 八、框架与课程（10）

| 编号 | 本地总结 | 原文 | 说明 | 推荐度 |
|---|---|---|---|---|
| 36 | [pi-coding-agent-summary.md](./pi-coding-agent-summary.html) | [教程](https://x.com/xaiwind/status/2113084544375304503) · [仓库](https://github.com/earendil-works/pi) | Pi Coding Agent 导读：把 harness 做到最薄的开源样本——内核只留工具循环 + 状态管理；分包、会话树、扩展点四种模型；无权限 / 审计是设计决定 | ★★★★☆ |
| 37 | [strands-agents-sdk-summary.md](./strands-agents-sdk-summary.html) | [官方文档](https://strandsagents.com/) · [仓库](https://github.com/strands-agents/harness-sdk) | Strands Agents SDK 导读：AWS 开源 agent 框架，「是库不是平台」；hooks 拦截 loop、guardrails 与 context 管理内置；与 AgentCore 配套 | ★★★★☆ |
| 38 | [bedrock-agentcore-summary.md](./bedrock-agentcore-summary.html) | [AWS 官方 FAQ](https://aws.amazon.com/bedrock/agentcore/faqs/) | Bedrock AgentCore 导读：agent 托管基础设施九件可组合取用；重点看 Policy / Identity / Observability 三件 | ★★★★☆ |
| 31 | [umich-aase-summary.md](./umich-aase-summary.html) | [仓库](https://github.com/eecs498-aase/materials) · [课程站](https://eecs498-aase.github.io) | UMich EECS 498 AASE 导读：把「指挥 agent 写代码」当工程学科教；分讲分级（6 讲对照正文）；Big Three、停止条件、EGM 五个 skill | ★★★★☆ |
| 49 | [databricks-agentops-summary.md](./databricks-agentops-summary.html) | [Databricks](https://www.databricks.com) | Databricks《AgentOps on Databricks》：把 MLOps 的 deploy-code 模式搬到 agent 世界的一张完整全图 | ★★★★☆ |
| 50 | [temporal-agents-sdlc-summary.md](./temporal-agents-sdlc-summary.html) | [AWS Builders](https://aws.amazon.com/blogs/) | AWS Builders《Orchestrating Our Agents SDLC on Temporal》：三份 Agent Ops 里最值得细读的一篇，纯实战 | ★★★★☆ |
| 51 | [cresta-agent-observability-summary.md](./cresta-agent-observability-summary.html) | [Cresta](https://cresta.com) | Cresta《Observability for AI Agents》：trace 跨服务、多租户隔离、故障回放 | ★★★☆☆ |
| 32 | [learn-harness-engineering-summary.md](./learn-harness-engineering-summary.html) | [GitHub](https://github.com/walkinglabs/learn-harness-engineering) | walkinglabs《Learn Harness Engineering》：从零亲手搭一个完整 harness 的动手课程 | ★★★★☆ |
| 33 | [namiai-agent-summary.md](./namiai-agent-summary.html) · [学习笔记](../learning-notes/namiai-agent-notes.html) | [namiai](https://namiai.tech/agent/?v=1) | namiai《从零手写 Agent》：中文动手系列，从 100 行循环亲手搭出完整 Agent，再拆 7 个主流 Agent | ★★★★☆ |
| 34 | — | [GitHub 仓库](https://github.com/microsoft/ai-agents-for-beginners) | Microsoft《AI Agents for Beginners》（查阅型）：18 课入门课程，七成内容与在册材料重复且更浅；只标 4 课值得看——第 14 课 Microsoft Agent Framework（清单里唯一的微软 Agent 栈）、第 15 课 Computer Use Agents（补 Sharma 路线图缺口 03 操作电脑界面）、第 17 课本地 Agent、第 9 课元认知；代码示例须 Azure 账号 + Microsoft Foundry 才能跑全 | ★★☆☆☆ |

---

*注：随笔（人与 AI 的关系等）见 [人与 AI 的关系目录](../human-ai-relationship/)，另计。*
*以后新增 AI 资料时同步更新此目录。*
