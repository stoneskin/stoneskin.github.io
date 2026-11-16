# AI 工程学习资源清单

[← 返回目录](index.html)

> 共 58 份（基础 19 篇 + 专题 39 条）。编号按清单呈现顺序：第一编 1–19，第二编按组顺序（组一 20–24、组二 25–28、组三 29–35、组四 36–39、组五 40–42、组六 43–45、组七 46–57）。2026-11-14 Stone 定重排，旧流水号作废；新增取下一个号（58、59…）。
> 分级：【对照正文】重要，对照原文读；【摘要即可】摘要已写到能独立成立，只看摘要、跳过原文（旧版导读的精读层同此标准）；【查阅型】工具书，按需翻；【概念即可】知道概念为止。
> 重心（Stone 定）：全部涉猎、FDE 与 Agent 为重点；深度押三处——FDE 落地方法、Agent 跑稳（Ops）、Evals 体系。
> 本站：导读与摘要见本目录各文件，学习笔记见 ../learning-notes/。编号与外部引用（站点计数）保持一致。
> 总索引（按编号找文件）：见 [站内目录](./index.html)——每表首列即编号；基础十九篇原文链接见目录第二节。
> 库内自足（Stone 2026-10-31 定）：重要资料的摘要写到不依赖原文站点也能学到精髓——库里有足够的学习内容及概要，不只留链接；旧资料缺摘要的，学习时补。

## 总目录

- **第一编 · 基础十九篇**（systemdesign.one）：对照正文 6 篇——#2 Patterns、#3 Multi-Agent、#5 Memory、#9 MCP、#13 Context Engineering、#16 Evaluation；其余摘要或概念即可。
- **第二编 · 专题进阶**（按主题组合）：
  - 组一 路由与编排：Router/调度（kafkaup）、Thin Orchestrator（Meta）、决策模型与 Jev、DeepSeek《Super-agent 设计探索》（第 23 份）、Anthropic《When to fold subagents into your main agent loop》（第 24 份）
  - 组二 记忆与检索进阶：Agentic RAG、Generative Agents、Karpathy《LLM Wiki》（第 27 份）、SAG2《无 embedding 多跳检索》（第 28 份，Jev 实战首例）
  - 组三 Harness 与课程：MIT 6.S950 Lec 5、MIT 6.S950 课程全景、UMich AASE、walkinglabs《Learn Harness Engineering》（第 32 份，动手搭完整 harness）、namiai《从零手写 Agent》（第 33 份，动手从零写 Agent + 拆解主流 Agent）、Microsoft《AI Agents for Beginners》（第 34 份，查阅型，只标 4 课）、xiaonancs《Codex 与同类对比》（第 35 份）、OpenAI《Harness engineering》（第 58 份）
  - 组四 框架与平台：Pi、Strands、Bedrock AgentCore、阿里云 AI Agent Handbook
  - 组五 教材与路线：Gulli《Agentic Design Patterns》、Sharma 12 步路线图、龙井《2 小时从零看懂 AI》
  - 组六 交付与职业：FDE-Gym + OpenAI FDE、码良面试题单、Karpathy 理解漏斗
  - 组七 FDE 深挖 / Agent Ops / 安全与治理（第 46–57 份）：FDE 深挖（Pragmatic Engineer、PostHog、RevenueBrew）、Agent Ops（Databricks、Temporal、Cresta、ByteByteGo 成本优化六策（第 52 份）、晓辉博士《Skill 自迭代能力改造指南》（第 53 份）、南晚《构建自己的 Agent 至少需要完成这些》（第 54 份））、安全与治理（OWASP ASI、NIST AI RMF、欧盟 GPAI Code）
- **附**：评价与缺口状态（2026-10-16 评价原文 + 2026-10-24 缺口状态更新）
- **变更记录**：按日期记每次增补与重整。

---

## 第一编：基础十九篇

> 来源：https://x.com/0xSilver_Time/status/2110546705838117326 （19 篇 systemdesign.one 深度文章）

## Agent 核心

1. **Agent vs ChatGPT 的区别**【摘要】 — agent 把 LLM 接上工具，形成"行动→观察→重试"循环；ChatGPT 是单轮问答，agent 是能自己调工具、看结果、调策略的多步任务系统 [原文](https://newsletter.systemdesign.one/p/ai-agents-explained)
2. **9 种 Agentic Patterns**【对照正文】 — reflection（自我检查）、tool use、planning、ReAct（边想边干）等 9 种模式，搭 agent 时的"设计模式手册" [原文](https://newsletter.systemdesign.one/p/agentic-design-patterns)
3. **Multi-Agent 架构**【对照正文】 — supervisor/worker、串行 pipeline、并行 fan-out、辩论共识；thinktank 的 panel+judge 就是 supervisor 模式的一种 [原文](https://newsletter.systemdesign.one/p/multi-agent-system)
4. **从零搭 Incident Response Agent 的血泪史**【摘要】 — 实战：工具怎么选、规划策略（ReAct vs 先规划后执行）、记忆怎么管、guardrails 怎么设 [原文](https://newsletter.systemdesign.one/p/how-do-ai-agents-work)

## 记忆与状态

5. **Agent State / Memory / Consistency**【对照正文】 — 短期记忆（context 内）vs 长期记忆（跨 session）；多步任务怎么保证 agent 不"失忆"不自相矛盾；open-memex 解的就是长期记忆这块 [原文](https://newsletter.systemdesign.one/p/ai-agent-memory)

## 检索与 RAG

6. **RAG Deep Dive**【摘要 · 与 Agentic RAG 合读】 — 查询时先检索外部文档拼进 prompt；解决知识截止+私有数据问题；关键在切分、检索、重排 [原文](https://newsletter.systemdesign.one/p/how-rag-works)
7. **Vector Database Deep Dive**【摘要】 — 存 embedding 做语义检索；选型（Pinecone/Milvus/Qdrant/pgvector）；什么时候该用什么时候不该用 [原文](https://newsletter.systemdesign.one/p/what-is-a-vector-database)
8. **HNSW 十亿向量毫秒检索**【摘要】 — 分层图索引，不用全量扫描；理解向量库底层的必看 [原文](https://newsletter.systemdesign.one/p/hnsw-vector-search-explained)

## 协议

9. **MCP Deep Dive**【对照正文】 — Anthropic 的开放协议，统一模型接工具/数据的接口；一次适配，到处可用 [原文](https://newsletter.systemdesign.one/p/how-mcp-works)
10. **A2A Protocol**【摘要】 — 不同厂商 agent 之间怎么通信协作；MCP 是 agent 接工具，A2A 是 agent 接 agent [原文](https://newsletter.systemdesign.one/p/agent-to-agent-protocol)
11. **用 MCP 搭 Research Agent**【摘要】 — 实战端到端：规划研究问题→搜索资料→综合结论 [原文](https://newsletter.systemdesign.one/p/how-to-build-an-ai-research-agent-with-mcp)

## LLM 基础

12. **LLM 到底怎么工作**【摘要】 — token、embedding、attention、context window；理解模型怎么"看"字，才能写好 prompt [原文](https://newsletter.systemdesign.one/p/llm-concepts)
13. **Context Engineering 101**【对照正文】 — 窗口里放什么怎么放：system prompt、示例、检索结果、历史、工具定义；核心是取舍 [原文](https://newsletter.systemdesign.one/p/what-is-context-engineering)
14. **垂直领域小模型**【摘要】 — 特定任务上小模型+好数据能打败大模型；成本低延迟低可本地部署 [原文](https://newsletter.systemdesign.one/p/fine-tuning-small-language-models)

## 生产与评估

15. **AI App 扩到 100 万用户**【摘要】 — 缓存、batch、小模型处理简单任务大模型只处理复杂；跟 router 三层架构一个思路 [原文](https://newsletter.systemdesign.one/p/llm-inference-cost-optimization)
16. **29 个 LLM 评测概念**【对照正文】 — 测试集、打分标准、LLM-as-judge（跟 thinktank judge 同思路）、人工评估 [原文](https://newsletter.systemdesign.one/p/llm-evals)
17. **设计个人 AI 助手**【摘要 · 低优先】 — 流式输出、会话历史、检索增强；偏产品向 [原文](https://newsletter.systemdesign.one/p/ai-chat-assistant)

## 训练

18. **Fine Tuning Deep Dive**【概念即可】 — 领域数据微调提准确率；什么时候该微调 vs RAG/prompt 就够（多数情况后者就够） [原文](https://newsletter.systemdesign.one/p/llm-fine-tuning-guide-with-lora-and-qlora)
19. **21 个强化学习概念**【概念即可】 — agent 在环境里行动靠 reward 调策略；RLHF 就是 RL 的一种应用 [原文](https://newsletter.systemdesign.one/p/what-is-reinforcement-learning)

---

## 第二编：专题进阶（按主题分类）

### 路由与编排

- **Router/调度**【摘要即可】 — router 是 AI 产品的"调度台"——决定请求进哪个能力、花多少成本；信息不足或高风险时追问/降级/拒绝/转人工。 [原文](https://x.com/kafkaup/status/2110500904868757542) [导读](./router-scheduling-summary.html)
- **Meta《The Thin Orchestrator》**【摘要即可】 — Meta 数据列接入系统的 Agent 架构复盘：第一版"全知单 agent"上生产幻觉（概念互相污染），重构成 1,300 行薄编排器 + 14 个隔离上下文的专家子 agent。 [原文](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/) [导读](./thin-orchestrator-summary.html)
- **决策模型（Decision Models）与 Jev**【摘要即可】 — 2026 年 9 月起的新品类——模型不写文本，只输出概率/选项/分数，当 LLM-as-a-Judge 的替代。Jev（TypeSafe，9/15）开创，一个月内 14 个跟进（Perplexity Decider、Cloudflare Clef、OpenAI Decisions API、Microsoft Decision-1 等），多数是小开源模型后训练的"打分头"。 [原文](https://hamel.dev) [导读](./decision-models-and-jev-summary.html)
- **DeepSeek《Super-agent 设计探索》**【摘要即可】 — 多任务的上限是人的注意力（3–5 会话）；Router + Worker 两层、事件订阅直通、异步全双工、存算分离、独立 Watchdog；实验 p50 12.4 分钟对单会话 p95 29.5 分钟，代价是 Token 近 4 倍；安全 §8.4 最尖锐。 [原文转贴](https://www.uied.cn/posts/922127) [原型](https://github.com/deepseek-ai/dsh-superagent-prototype) [导读](./deepseek-super-agent-guide.html) [摘要](./deepseek-super-agent-summary.html)
- **Anthropic《When to fold subagents into your main agent loop》**【摘要即可】 — 单 Agent + Skills 在多家企业部署对比中经常打赢"一 prompt 包打天下"与"多 subagent"两种设计，质量更高、成本与延迟更低；subagent 只留三处（上下文膨胀致可测量下降、可并行即弃的新鲜窗口、选工具困难或指令冲突）；迁移凭任务完成 eval、一次折一个；与 DeepSeek Super-agent 互补——Claude 讲一个任务内部怎么精简，DSH 讲一组任务长期并行怎么组织。 [原文](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop) [迁移 kit](https://github.com/anthropics/single-agent-loop-kit) [导读](./claude-fold-subagents-guide.html)

### 记忆与检索进阶

- **Agentic RAG**【摘要即可】 — 标准 RAG 的病在中间没人验货；Agentic RAG 把"检索→生成"的直线改成"检索→评估→决定回答还是重试"的循环。 [原文](https://blog.bytebytego.com/p/how-agentic-rag-works) [导读](./agentic-rag-summary.html)
- **Generative Agents / Smallville 论文**【摘要即可】 — Agent 记忆系统的开山之作。25 个 agent 在 Smallville 小镇里生活两天， emergent 出传派对邀请、约会、协调到场等社会行为。 [原文](https://arxiv.org/abs/2304.03442) [导读](./generative-agents-summary.html)
- **Karpathy《LLM Wiki》**【摘要即可】 — RAG 每次都从头找答案、不积累；LLM Wiki 让 LLM 把知识一次编译进持久 wiki，越用越富；摘要含 Graphify 实现。 [原文](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) [导读](./karpathy-llm-wiki-guide.html) [摘要](./karpathy-llm-wiki-summary.html)
- **SAG2《Embedding-Free Multi-Hop Retrieval with BM25 and JEV》**【摘要即可】 — 无 embedding 多跳检索：本地只剩 SQLite + BM25 索引，Jev（TypeSafe 决策模型，Noul 是非题 → 0–1 概率）在查询时逐段判“是不是必需证据”，好段供词扩下一轮，最多两轮；MuSiQue Recall@10 86.62%、2WikiMultiHopQA 97.43%、HotpotQA 99.00%，三项第一，索引 11,656 段 2.36 秒、25.87 MiB、离线零模型调用；但语义类企业题只有 58.40%、四跳完整覆盖率 28.31%，且判断走 hosted Jev、非完全离线。 [原文](https://arxiv.org/abs/2610.22588) [评测代码](https://github.com/Zleap-AI/SAG-Benchmark) [导读](./sag2-guide.html) [摘要](./sag2-summary.html)

### Harness 与课程

- **MIT 6.S950 Lecture 5《The Harness》**【对照正文】 — Agent = LLM + Harness；这一讲不教新机制，教三件事——怎么看清它（可观测性）、怎么管住它（可控性）、到底需要多少它（无通用最优），且每条做法都追到几十年前的系统原则。 [原文](https://agencyai.mit.edu/w5/) [导读](./mit-6s950-harness-lecture-summary.html)
- **MIT 6.S950《Agency with AI》课程全景**【对照正文】 — 整门课只教一件事——Agency，即"什么该委托、什么该验证、什么该留给自己做"的判断力；第 29 份是其中 Lec 5 一讲，本份是全景地图。 [原文](https://agencyai.mit.edu/) [导读](./mit-6s950-course-panorama-guide.html)
- **UMich EECS 498 AASE《Applied Agentic Software Engineering》**【分讲分级】 — 把"指挥 agent 写代码"当工程学科教的大学课程——先学开（Aider），再拆真 harness（Claude Code / Codex / Aider 的 loop、skills、guardrails、subagents、compaction），最后在现成 harness 上做东西。与 MIT 6.S950（第 30 份）互补：MIT 偏原理，这门偏工程实践与拆解。 [原文](https://github.com/eecs498-aase/materials) [导读](./umich-aase-summary.html)
- **walkinglabs《Learn Harness Engineering》**【分讲分级】 — 清单里第一份“从零亲手搭一个完整 harness”的动手课程——同一个 Electron 知识库应用，从纯 prompt 一步步走到完整 harness，每步测弱 harness vs 强 harness 的实测差。 [原文](https://github.com/walkinglabs/learn-harness-engineering) [导读](./learn-harness-engineering-summary.html)
- **namiai《从零手写 Agent》**【分课分级】 — 中文动手系列——从 100 行循环亲手搭出一个完整 Agent，配可运行代码（到 EP11 共 49 个测试），再拿 11 个零件当尺子拆 7 个主流 Agent；Gulli 那本是模式教材，这份是“亲手搭一遍”的对照。 [原文](https://namiai.tech/agent/?v=1) [导读](./namiai-agent-summary.html)
- **Microsoft《AI Agents for Beginners》**【查阅型】 — 微软的 18 课入门课程（文字 + 短视频 + Python 代码，简体中文译本齐全）；七成内容是清单已有材料的入门版（设计模式、RAG、记忆、多 Agent 均有更深的在册版本），只标 4 课值得看：第 14 课 Microsoft Agent Framework（清单里唯一的微软 Agent 栈）、第 15 课 Computer Use Agents（补 Sharma 路线图缺口 03 操作电脑界面）、第 17 课本地 Agent、第 9 课元认知；代码示例须 Azure 账号 + Microsoft Foundry 才能跑全。 [原文](https://github.com/microsoft/ai-agents-for-beginners)
- **xiaonancs《Codex 与同类对比》**【摘要即可】 — Codex/Claude Code/Opencode 七维架构对比（《OpenAI Codex 源码深度研究》第 24 章）：governance 层位是根本差异（内核沙箱 vs 26 种 hook vs HTTP 后端）；Codex 协议中枢 app-server + 双轨持久化是真优势，Hook 运行时只有 AfterAgent 是最大债；附任务矩阵与"入口对象→主循环→安全边界"三步评估法。注意：全系列 AI 写作，数字为 2026 年 5 月快照，Codex 行号未逐条核验。 [原文](https://github.com/xiaonancs/codex-source-analysis/blob/main/Part%20III%20Comparative%20Analysis/24-Codex%E4%B8%8E%E5%90%8C%E7%B1%BB%E5%AF%B9%E6%AF%94.md)
- **OpenAI《Harness engineering：leveraging Codex in an agent-first world》**【摘要即可】（第 58 份，Stone 2026-11-15 批入） — 5 个月、0 行手写代码、约 100 万行、约 1,500 PR 的 agent-first 实战记录；“harness engineering”这个词推成主流的那篇（词是 2025-11-04 Dex Horthy 先造，Anthropic 2025-11-26 先出成体系做法）；核心：AGENTS.md 当目录、docs/ 当 system of record、enforce invariants 不 micromanage、golden principles + 定期清理当垃圾回收；人 steering、agent 执行，稀缺资源是人的时间注意力。 [原文](https://openai.com/index/harness-engineering/) [导读](./openai-harness-engineering-guide.html)

### 框架与平台

- **Pi（Pi Coding Agent）**【对照正文】 — 把 agent harness 做到最薄的开源样本——内核只留工具循环 + 状态管理，plan mode、子智能体、权限系统全不内置，想要自己以 package 形式装。 [原文](https://x.com/xaiwind/status/2113084544375304503) [导读](./pi-coding-agent-summary.html)
- **Strands Agents SDK**【对照正文】 — AWS 的开源 agent 框架——「是库不是平台」：Agent 对象 + @tool 装饰器，模型默认 Bedrock、一行可换；现分两层：harness（create_harness 一行整装）与 SDK（自己拼 loop）。 [原文](https://strandsagents.com/) [导读](./strands-agents-sdk-summary.html)
- **Amazon Bedrock AgentCore**【对照正文】 — Bedrock 的 agent 托管基础设施：Runtime / Memory / Gateway / Identity / Observability / Evaluations / Policy / Browser / Code Interpreter 可组合取用——Pi 故意不做的企业件，AWS 做成了服务。 [原文](https://aws.amazon.com/bedrock/agentcore/faqs/) [导读](./bedrock-agentcore-summary.html)
- **阿里云 AI Agent Handbook**【查阅型】 — 企业级 AI Agent 全生命周期实战指南——30 章 + 2026 Agent 开发者调研；从"怎么搭"转向工程化/规模化/组织化三大挑战。 [原文](https://github.com/aliyun/ai-agent-handbook) [导读](./aliyun-ai-agent-handbook-summary.html)

### 教材与路线

- **Antonio Gulli《Agentic Design Patterns》**【查阅型】 — Google Antonio Gulli 写的开源教材，21 章 + 7 个附录，每章配可运行的 Jupyter Notebook。版税全部捐给 Save the Children。 [原文](https://github.com/evoiz/Agentic-Design-Patterns) [导读](./agentic-design-patterns-summary.html) [摘要](./agentic-design-patterns-summary.html)
- **Suraj Sharma《AI Agent 工程师 12 步学习路线图》**【摘要即可】 — 12 步学习路线，每步三列（学什么 / 练手项目 / 为什么）。核心观点：Demo 和生产系统的分水岭是稳定运行、安全执行、故障恢复、交付客户。 [原文](https://x.com/suraj_sharma14/status/2111789399176335412) [导读](./sharma-agent-roadmap-summary.html)
- **龙井《2小时从零看懂AI》**【摘要即可】 — 8000元/小时企业内训同款公开版——大模型通识→提示词方法→Agent入门→Agent实操，四段式AI认知体系。 [原文](https://x.com/long_jingai/status/2111356255889723723) [导读](./longjing-ai-primer-summary.html)

### 交付与职业

- **FDE-Gym / AI 交付最后一公里**【对照正文】 — 会写代码 ≠ 会交付——在 Terminal-Bench 拿 88% 的模型，真实客户交付只能拿 0.56 分；FDE 的核心（挖隐性约束、把事实变成贴合组织的系统）正是 AI 最弱、人类最强的部分。 [原文](https://arxiv.org/abs/2610.22350) [导读](./fde-gym-paper-summary.html)
- **码良《Agent 高频面试题单》**【查阅型 · 自测】 — 从牛客网 343 篇 Agent 岗面经（180 作者、~80 家公司，8/18–10/18）统计出的 29 道高频题，每道带作者数、场次数、公司/轮次分布、原帖例问和牛客链接。另有算法岗、低频题、面试结构、月度趋势、方法论/局限性章节。 [原文](https://x.com/cxjwin/status/2111644503341953409) [导读](./maliang-interview-questions-summary.html)
- **Karpathy "AI 理解漏斗"**【摘要即可】 — 你眼里的 AI 和别人眼里的不是同一个东西——差距不再是"两拨人各说各话"，而是一个四层漏斗，而且在变陡。 [原文](https://x.com/karpathy/status/2109361) [导读](./karpathy-ai-funnel-summary.html)
> 三路各补最硬的 3 份，均逐条验过 URL 与原文；验货时删掉三处未核实说法（见各条备注），不硬凑。FDE、Agent Ops、安全与治理三组角度不重叠。


### FDE 深挖

- **Pragmatic Engineer《What are Forward Deployed Engineers, and why are they so in demand?》**【对照正文】 — 采访了 OpenAI 的 FDE 负责人、Ramp 的 FDE 负责人和一位 7 年 Palantir FDE，把起源、日常、三段工作法和两个真实案例都讲透了。 [原文](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers) [导读](./pragmatic-engineer-fde-summary.html)
- **PostHog《WTF is a forward deployed engineer?》**【摘要即可】 — FDE 与普通工程师的对照表、"什么时候该用 FDE"的判断条件讲得最清楚。 [原文](https://posthog.com/blog/forward-deployed-engineer) [导读](./posthog-fde-summary.html)
- **RevenueBrew《What it's like to work in tech's hottest new role》**【摘要即可】 — Superhuman 的 Thomas Baucom，讲 FDE 一天之内在完全不同客户之间切换、以及"把线从头 carry 到尾"是什么意思。 [原文](https://www.revenuebrew.com/stories/forward-deployed-engineer-role) [导读](./revenuebrew-fde-summary.html)

### Agent Ops

- **Databricks《AgentOps on Databricks: Operating Production AI Agents》**【对照正文】 — 评估门禁 + 可观测性闭环 + 提示词版本化 + 治理，是一张完整的 Agent Ops 全图。 [原文](https://community.databricks.com/t5/technical-blog/agentops-on-databricks-operating-production-ai-agents/ba-p/163602) [导读](./databricks-agentops-summary.html)
- **AWS Builders《Orchestrating Our Agents SDLC on Temporal》**【对照正文】 — 把人工 prompt-by-prompt 的 AI 编码流水线改成 Temporal 编排的持久化 SDLC 后踩过的坑——确定性、载荷、重试、心跳、成本、观测——以及每个坑的 fix。 [原文](https://dev.to/aws-builders/orchestrating-our-agents-sdlc-on-temporal-the-hard-parts-nobody-warns-you-about-1mgc) [导读](./temporal-agents-sdlc-summary.html)
- **Cresta《Observability for AI Agents: Tracing Multi-Service LLM Pipelines with Langfuse》**【摘要即可】 — 一家真实跑多服务 agent 管线的公司，讲它怎么用自托管 Langfuse 把跨服务的 LLM 追踪、租户隔离与故障回放落到生产——正好补上前两份没展开的一角。 [原文](https://cresta.com/blog/observability-for-ai-agents-tracing-multi-service-llm-pipelines-with-langfuse) [导读](./cresta-agent-observability-summary.html)
- **ByteByteGo《Top 6 Cost Optimization Strategies in AI Systems》**【摘要即可】 — 一张信息图讲透 AI 系统六种省钱打法：提示词缓存、模型路由、批量接口、语义缓存、精简上下文、用小模型；每条一句话效果。原图与矢量重绘见导读页。 [原文](https://x.com/alexxubyte/status/2117302471156781430) [导读](./cost-optimization-strategies-guide.html)
- **晓辉博士《Skill 自迭代能力改造指南》**【摘要即可】 — 先验证再迭代：约 30% 的时间花在验收上（“验证税”），skill 达不到 100% 交付标准就放手自迭代只会批量生产垃圾；纠错五层里最强的是黄金样例与脚本检查，规则/skill/偏好没法验证；Verification Skill 两件套（feature map + CLI 工具）；八步改造法（验收标准、工具化、结构化、反馈日志、小步迭代、评估集、验收机制）与“看起来完成了”的回归样例；与 yetone Agent Loop 直接咬合，poteto 与 Addy Osmani 是两个新名字。 [原文](https://x.com/xiaohuiyuan/status/2118496773706797338) [导读](./xiaohui-verification-skill-summary.html)
- **南晚《构建自己的 Agent 至少需要完成这些》**【摘要即可】 — 生产 Agent 的 12 条 checklist：确定性边界、轻量路由、上下文隔离、主动取上下文、工具接口、结构化报错、显式状态、并发与过期拦截、循环上限与预算、人工审批、断点续跑、沙箱隔离；结论是 demo 惊艳不等于生产能跑。 [原文](https://x.com/snwiki238337/status/2119414637842305149)

### 安全与治理

- **OWASP《Top 10 for Agentic Applications 2026》**【对照正文】 — 每条配真实攻击场景与可落地的缓解措施，是目前最贴合"会自己调工具、多步执行"的 Agent 安全基线。 [原文](https://genai.owasp.org) [导读](./owasp-agentic-top10-summary.html)
- **NIST《AI Risk Management Framework 1.0》+ Playbook + 生成式 AI Profile**【摘要即可】 — 美国官方的 AI 风险管理框架：自愿性、跨行业，用 Govern / Map / Measure / Manage 四个职能 + Playbook 建议动作，把"可信 AI"变成可执行的管理循环。 [原文](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) [导读](./nist-ai-rmf-summary.html)
- **欧盟《通用人工智能行为准则》最终版（GPAI Code of Practice）+ EU AI Act 部署者义务**【摘要即可】 — 欧盟 AI 法案下通用模型合规的操作化文件：自愿签署、换取合规推定与较低行政负担；三章结构，GPAI 义务 2025 年 8 月 2 日生效。 [原文](https://digital-strategy.ec.europa.eu/en/news/general-purpose-ai-code-practice-now-available) [导读](./eu-gpai-code-summary.html)

---

## 附：评价与缺口状态

## 评价与补充（2026-10-16）

> 状态（2026-10-31）：本节是 2026-10-16 的评价原文，"缺的东西"所列 5 个缺口已于 2026-10-24 全部补上——Prompt Engineering→龙井第二部分；安全→阿里云治理篇 + OWASP/NIST/EU；可观测性→阿里云 13 章 + MIT Lec 5 + Cresta/Databricks；Human-in-the-loop→阿里云 6 章 + AASE L09/L11；Router→kafkaup 篇 + 决策模型/Jev。详见本节末"缺口补足完成"与末尾变更记录。优点、"不太值的几篇"、"如果只读 5 篇"、学习方法建议仍有效。

### 优点

覆盖面全：agent、RAG、协议、LLM 原理、生产、评测、训练一条线；systemdesign.one 质量靠谱，适合系统性补课。

### 缺的东西（2026-10-16 原文，现已全部补足）

1. **Prompt Engineering 没有**：有 context engineering 但没有专门的 prompt 工程，对做 agent 的人这是地基
2. **安全只字未提**：prompt injection、jailbreak、工具调用的数据外泄——生产级 agent 必修，完全缺席
3. **Agent 可观测性没有**：tracing、日志、debug（LangSmith 这类），出问题怎么查
4. **Human-in-the-loop 没有**：审批流、人工接管，生产 agent 标配
5. **Router/调度没有**：多能力产品怎么做三层路由——可直接用 @kafkaup 那篇补上（https://x.com/kafkaup/status/2110500904868757542）

### 不太值的几篇（可跳过）

- **#18 Fine-tuning、#19 RL**：architect 不训模型，知道概念就行
- **#17 个人助手设计**：偏产品向，优先级低

### 如果只读 5 篇

1. **#2 Agentic Patterns**（地基）
2. **#3 Multi-Agent**（thinktank 理论对照）
3. **#5 Memory**（open-memex 对照）
4. **#13 Context Engineering**（prompt 和 judge 设计天天用）
5. **#16 LLM Evaluation**（jury 评测方法论对照）
+ kafkaup 的 router 文章

### 学习方法建议

Stone 是动手型学习者，这 19 篇全是文章、没有动手项。建议别按顺序读，而是对照项目读：
- 读 #3 时对照 thinktank 的 panel+judge，看人家的 multi-agent 分类、自己的属于哪种
- 读 #5 时对照 open-memex 的三层检索，看缺了哪块
- 读 #16 时对照 capability-scores，看人家的 eval 怎么做 calibration
三个项目本身就是最好的 lab，清单是理论对照不是作业。

---

### 缺口状态（2026-10-24 更新）

上面点的 5 个缺口已全部补上：Prompt Engineering → 龙井 primer 第二部分；安全 → 阿里云手册治理篇（13–16 章）；可观测性 → 阿里云 13 章 + MIT Lec 5；Human-in-the-loop → 阿里云 6 章 + AASE 的 L09/L11；Router → kafkaup 篇 + 阿里云 Jev 专题。当前短板不在输入在转化：新材料默认轻处理，唯一观察项 = 企业 AI 治理/合规。

### 缺口补足完成（2026-10-24 晚更新）

2026-10-24 晚，FDE 深挖、Agent Ops、安全与治理三组 9 份（新号第 46–51、55–57 份）已并入。企业 AI 治理/合规观察项至此有 NIST + EU 两份可讲的材料与 OWASP 安全基线支撑，"唯一观察项"状态更新为：治理从"知道"升到"能讲"已有材料，待 Stone 读后验收。当前短板仍在转化不在输入。

---

## 变更记录
- **2026-11-15**：同步私仓清单，补第 58 份 OpenAI《Harness engineering》（组三）+ 导读页；新增后清单共 58 份（基础 19 + 专题 39）。
- **2026-11-14**：补全第一编 19 篇原文链接（原帖逐条核对，newsletter.systemdesign.one）；站内目录重整——加编号列、第二节新增基础十九篇 19 行（原文直链），总纲行 49 份旧注修正，各节计数核对。
- **2026-11-14**：同步私仓清单，补 8 份——#23 DeepSeek《Super-agent 设计探索》（2026-11-02 批入）、#24 Anthropic《When to fold subagents into your main agent loop》（2026-11-03 批入）、#28 SAG2《Embedding-Free Multi-Hop Retrieval with BM25 and JEV》（2026-11-09 批入）、#34 Microsoft《AI Agents for Beginners》（2026-11-03 批入）、#35 xiaonancs《Codex 与同类对比》（2026-11-08 批入）、#52 ByteByteGo《Top 6 Cost Optimization Strategies in AI Systems》（2026-11-03 批入）、#53 晓辉博士《Skill 自迭代能力改造指南》（2026-11-07 批入）、#54 南晚《构建自己的 Agent 至少需要完成这些》（2026-11-08 批入）。同日编号按新表重排（旧流水号作废，新旧对照见私仓清单变更记录）。新增后清单共 57 份（基础 19 + 专题 38）。
- **2026-10-31**：补第 49 份 Karpathy《LLM Wiki》（组二，Stone 批入——X 帖 @awe0_io 推 Graphify 时提到 Karpathy 的三层知识库文章，Stone 让找原文、要原理与实现思路）。三层编译式知识库：raw（不可改原文）/ wiki（LLM 写的 markdown）/ schema（纪律文件）；三操作 ingest / query / lint；index.md + log.md 规模化到 ~100 份资料。用途三处：open-memex（编译式记忆）、本地文件组织、WorkBuddy harness。**结构升级：学习资料分三部分——导读 + 摘要（写到不看原文能学到精髓）+ 学习笔记；新资料按三部分走，旧资料的导读已含精读层、暂不拆。** 新增后清单共 49 份（基础 19 + 专题 30）。同日补：摘要加第 10 节 Graphify 实现（代码库上的编译式知识图谱）；并立新规矩——以后重要资料都要有详细摘要，库内自足、不依赖原文站点；旧资料缺摘要的，学习时补。

- **2026-10-15/16**：清单初建（基础 19 篇 systemdesign.one + 专题补编起步）。
- **2026-10-24**：按新标准重整——每份材料标分级（对照正文 / 摘要即可 / 查阅型 / 概念即可）；MIT 6.S950 Lec 5 重复收录并为一份；主题相邻条目互标合读关系；重心定为全部涉猎、FDE 与 Agent 为重点，深度押 FDE 落地、Agent 跑稳（Ops）、Evals 三处；安全与治理从"知道"升到"能讲"。缺口补足完成（FDE、Agent Ops、安全与治理三组各补最硬的 3 份，第 33–41 份，均逐条验过 URL 与原文）。
- **2026-10-25**：补第 42 份 walkinglabs《Learn Harness Engineering》（组三）。
- **2026-10-29**：补第 48 份 namiai《从零手写 Agent》（组三，Stone 批入）。此前动手线只有 walkinglabs 一份（搭 harness），这份补"搭 Agent 本体 + 拆解对照"：18 课已完结、配可运行代码，EP03/EP05/EP11/EP18 对照正文、其余摘要即可。新增后清单共 48 份（基础 19 + 补编 29）。Gulli《Agentic Design Patterns》仍未读完，晚间提醒优先接着推其未读章节，第 48 份排在其后。
- **2026-10-31**：第三编 18 条详解各拆为单独文件，目录第二编 29 条全部链到导读文件；"补"字标签退役——"专题补编"改名"专题进阶"，按 7 个主题组归类（路由与编排 / 记忆与检索 / Harness 与课程 / 框架与平台 / 教材与路线 / 交付与职业 / FDE·Agent Ops·安全治理），不再按"后补的"分；流水号（第 N 份）保留在总目录与变更记录里。
- **2026-10-31**：附"评价与补充（2026-10-16）"标注为历史原文——"缺的东西" 5 个缺口已于 2026-10-24 全部补上（各缺口的补法见该节顶状态注），优点、"不太值的几篇"、"如果只读 5 篇"、学习方法建议仍有效。
- **2026-10-31**：重写本文件为干净目录——目录（第一、二编）只留每份一行 + 导读链接；无单独导读文件的条目详解移入第三编；变更记录集中到本节。内容一字未删，只搬了位置。
