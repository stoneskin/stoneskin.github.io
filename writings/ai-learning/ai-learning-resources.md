
# AI 工程学习资源（2026-10-16，来自 @0xSilver_Time 推文整理）

> 来源：https://x.com/0xSilver_Time/status/2110546705838117326
> 19 篇 systemdesign.one 深度文章，每篇一句话要点，不用点进去就知道讲什么

## Agent 核心

1. **Agent vs ChatGPT 的区别** — agent 把 LLM 接上工具，形成"行动→观察→重试"循环；ChatGPT 是单轮问答，agent 是能自己调工具、看结果、调策略的多步任务系统
2. **9 种 Agentic Patterns** — reflection（自我检查）、tool use、planning、ReAct（边想边干）等 9 种模式，搭 agent 时的"设计模式手册"
3. **Multi-Agent 架构** — supervisor/worker、串行 pipeline、并行 fan-out、辩论共识；thinktank 的 panel+judge 就是 supervisor 模式的一种
4. **从零搭 Incident Response Agent 的血泪史** — 实战：工具怎么选、规划策略（ReAct vs 先规划后执行）、记忆怎么管、guardrails 怎么设

## 记忆与状态

5. **Agent State / Memory / Consistency** — 短期记忆（context 内）vs 长期记忆（跨 session）；多步任务怎么保证 agent 不"失忆"不自相矛盾；open-memex 解的就是长期记忆这块

## 检索与 RAG

6. **RAG Deep Dive** — 查询时先检索外部文档拼进 prompt；解决知识截止+私有数据问题；关键在切分、检索、重排
7. **Vector Database Deep Dive** — 存 embedding 做语义检索；选型（Pinecone/Milvus/Qdrant/pgvector）；什么时候该用什么时候不该用
8. **HNSW 十亿向量毫秒检索** — 分层图索引，不用全量扫描；理解向量库底层的必看

## 协议

9. **MCP Deep Dive** — Anthropic 的开放协议，统一模型接工具/数据的接口；一次适配，到处可用
10. **A2A Protocol** — 不同厂商 agent 之间怎么通信协作；MCP 是 agent 接工具，A2A 是 agent 接 agent
11. **用 MCP 搭 Research Agent** — 实战端到端：规划研究问题→搜索资料→综合结论

## LLM 基础

12. **LLM 到底怎么工作** — token、embedding、attention、context window；理解模型怎么"看"字，才能写好 prompt
13. **Context Engineering 101** — 窗口里放什么怎么放：system prompt、示例、检索结果、历史、工具定义；核心是取舍
14. **垂直领域小模型** — 特定任务上小模型+好数据能打败大模型；成本低延迟低可本地部署

## 生产与评估

15. **AI App 扩到 100 万用户** — 缓存、batch、小模型处理简单任务大模型只处理复杂；跟 router 三层架构一个思路
16. **29 个 LLM 评测概念** — 测试集、打分标准、LLM-as-judge（跟 thinktank judge 同思路）、人工评估
17. **设计个人 AI 助手** — 流式输出、会话历史、检索增强；偏产品向

## 训练

18. **Fine Tuning Deep Dive** — 领域数据微调提准确率；什么时候该微调 vs RAG/prompt 就够（多数情况后者就够）
19. **21 个强化学习概念** — agent 在环境里行动靠 reward 调策略；RLHF 就是 RL 的一种应用

---

## 小沐的评价与补充（2026-10-16）

### 优点

覆盖面全：agent、RAG、协议、LLM 原理、生产、评测、训练一条线；systemdesign.one 质量靠谱，适合系统性补课。

### 缺的东西（按重要性）

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

## 补：Router/调度（@kafkaup，2026-10-16 补）

> 原文：https://x.com/kafkaup/status/2110500904868757542（2026-10-14，长帖）
> 一句话：router 是 AI 产品的"调度台"——决定请求进哪个能力、花多少成本；信息不足或高风险时追问/降级/拒绝/转人工。

### 三层级联（由便宜到贵，按确定性/置信度上浮）

1. **规则层**：确定性高的请求（按钮点击、文件上传、明确关键词）+ 安全拦截与权限判断前置。快、便宜、可解释。
2. **小模型层**：BERT/Embedding 做语义分类，处理规则抓不到但可归类的高频意图（例："整理成给领导看的材料"→报告生成）。
3. **大模型层**：多意图/混合意图、结合上下文判断、槽位（slots）抽取、是否追问、是否进 agent workflow。

### 路由决策四问

用户要完成什么任务？交给哪个能力模块？当前信息够不够？有没有风险？

- 意图从**产品能力**出发定义（先看产品能做什么、各模块输入输出与适用边界），不是只从 query 归纳标签——query 只提供表达方式。
- 边界划分标准：路由错了之后**后续执行逻辑是否明显不同**——走同一 workflow、输出形态差不多就不拆；流程/输入/风险/输出明显不同就必须拆。
- 意图分层："**两级 + 槽位**"——一级意图（任务大类：问答/检索/文件分析/工具执行/无法处理）、二级意图（具体能力模块）、槽位（执行参数）。

### Fallback / 降级触发

- 置信度不足 → 追问或 fallback 兜底；信息不足/高风险 → 追问、降级、拒绝、转人工。
- 评论区实践经验（@KakaluoteW45042）：router 是搭 agent 时最容易被低估的环节；单独训练分类器做路由一直不太稳，反而把能力描述塞给主模型让它自己决策效果更好；**真正难的不是第一跳分对，是中途发现走错了还能回退和自救**。

### 评估五指标

路由准确率、任务成功率、Fallback 率、用户重试率/追问率、人工改派率。目标不是最强模型，而是 token/延时/准确率三者平衡；router prompt 要短（只放意图定义+边界+输出 schema）、输出结构化、安全前置、常见 query 缓存结果。

### 跟你项目的咬合

- opencode-fuse 三档模型自动选档 = "由便宜到贵"的级联；"说不行自动升档" = 低置信度上浮；D13 的 fallback 率/升级率/任务成功率正好是这里的评估指标。
- D14 三个"事中请示"触发点 = 追问/转人工的触发条件，口径一致。
- thinktank Phase 3 的"Router 视角"（judge 低置信追问/降级）直接对应这篇的降级触发——"路由错了，大模型救不回来"有了理论背书。

---

## 补：FDE-Gym / AI 交付最后一公里（2026-10-17 补）

> 原文：https://arxiv.org/abs/2610.22350（2026-10-15，DeepLethe + 清华/上交等）
> 解读帖：https://x.com/Xudong07452910/status/2111306709318951189
> 详解：~/workspace/your_files/fde-gym-paper-summary.md
> 一句话：会写代码 ≠ 会交付——在 Terminal-Bench 拿 88% 的模型，真实客户交付只能拿 0.56 分；FDE 的核心（挖隐性约束、把事实变成贴合组织的系统）正是 AI 最弱、人类最强的部分。

### 测什么

- 95 个端到端交付任务，20 个客户场景、18 个行业，由行业专家从真实交付项目改造
- Agent 起手只有 sponsor 的一句话需求（可能指向错误问题），得自己读文档、查系统、找 stakeholder 确认
- 评分 = 客户业务指标改善（0=没动，1=专家参考方案）− stakeholder 接触成本（问问题/试运行/等待都收费）
- 四个指令级别 L0→L3：规则全给 → 规则自己挖 → 需求含糊 → sponsor 原始需求（可能跑偏）

### 五个发现

1. 最好模型（Claude Opus 5.5）平均 0.56，95 个任务只解决 14 个
2. **挖隐性约束是最大断崖**：L0→L1 掉 0.28，L1→L3 只再掉 0.04——瓶颈不是"需求跑偏"，是"约束没写出来"
3. 拿到 72–85% 关键事实 ≠ 交出系统：只有参考方案 60–70% 的业务提升；contact cost 再扣 0.14–0.22
4. 弱模型不如不做：Haiku 4.5 在 79/95 个任务上不如 do-nothing（期望贡献为负）
5. 没有全能选手；花钱多 ≠ 分高；"知道何时算做完"本身就是能力

### 跟你的咬合

- **职业**：0.56 vs 1.0 的差距 = "有经验的工程师" vs "AI" 的价值差，可量化进 AI Solutions Architect 的面试框架（需求澄清/约束发现/系统交付/业务指标导向/stakeholder 管理）
- **thinktank**：judge 评交付类任务时，业务指标改善 + 接触成本是现成的评分维度
- **open-memex**：企业版 pitch 话术——"90 分的模型真实交付 56 分，弱的还不如不做，所以需要人把最后一公里走完"
- fde-gym.com 在线平台：人类可同场练习，等人类基线出来值得做几个任务

---

## 补：阿里云 AI Agent Handbook（2026-10-17 补）

> 原文：https://github.com/aliyun/ai-agent-handbook（Apache-2.0，~1.6k star，2026-10-16 仍在更新）
> 一句话：企业级 AI Agent 全生命周期实战指南——30 章 + 2026 Agent 开发者调研；从"怎么搭"转向工程化/规模化/组织化三大挑战。

### 结构（8 大部分）

- **架构**（1–2）：AI 原生应用新阶段、Agentic 应用参考架构
- **构建**（3–6）：Harness 构建模式、任务编排与长程协作、Context/状态/可复用资产、受控执行与验证（Function Calling、MCP、A2A、HITL）
- **运行时**（7–12）：Agent Runtime 与沙箱、状态存储、AI 网关与统一流量治理、异步任务、多智能体协同、分布式通信
- **治理**（13–16）：可观测性、安全（prompt 注入、逐动作校验、数据外泄控制）、AI 资产发现与管理、行为生成与质量验证
- **优化**（17–24）：模型调优、Trajectory 数据、Golden 数据集、坏 case 改进、受控自进化、边缘运行时
- **实战**（25–29）：20 个企业案例——内核补丁测试（ABACI/PatchPilot）、PolarDB-X 告警自愈、吉利/塔斯汀智能运维、B 站内容洞察、MiniMax 长程记忆
- **Jev 专题**：结构化决策（含 HiRoute 智能模型路由）
- **结论**（30）：从 Agentic 应用到 Agentic OS

### 正好补上清单里点的缺口

10-16 小沐评价里点的 5 个缺口，这本直接补上 3 个半：
- **安全**（13–16 章·治理）：prompt 注入、逐动作校验、数据外泄控制
- **可观测性**（13 章）：tracing/日志、行为质量验证
- **Human-in-the-loop**（6 章·构建）：受控执行与验证（Function Calling、MCP、A2A、HITL）
- **Router/调度**（Jev 专题）：HiRoute 智能模型路由——kafkaup 那篇的理论版
- 仍缺：**Prompt Engineering** 仍无专门章节

### 建议阅读顺序

实战案例（25–29，有体感）→ 构建（3–6，动手用得上）→ 治理（13–16，企业版必备）→ 优化（17–24，进阶）

### 跟你的咬合

- **职业**：README 明确目标读者含"架构师和平台工程师"（架构/运行时/治理）、"技术管理者"（架构/治理/实战）——就是 AI Solutions Architect 的知识地图
- **thinktank**：Harness 构建模式、Trajectory→Golden 数据集飞轮可直接借鉴（judge 评测、eval harness）
- **open-memex**：AI 网关、agent 可观测性、安全治理是企业版必备件
- 20 个企业案例是面试弹药；PolarDB-X 告警自愈等"最后一公里"案例与 FDE-Gym 结论互相印证

---

## 补：龙井《2小时从零看懂AI》（2026-10-17 补）

> 原文：https://x.com/long_jingai/status/2111356255889723723（X Article，约2.5万字）
> 详解：~/workspace/your_files/longjing-ai-primer-summary.md
> 一句话：8000元/小时企业内训同款公开版——大模型通识→提示词方法→Agent入门→Agent实操，四段式AI认知体系。

### 四部分要点

1. **大模型通识**："超级图书管理员"原理解释LLM（预测下一个token、不懂装懂）；AI软件=大模型（心）+产品界面（皮）；三种优化方式（提示词/微调/RAG）；选模型框架+自建测试用例
2. **提示词工程**（⭐最有价值）：公式=清晰指令+必要上下文；"提示词工程已死"是伪命题（被普及+形态进化）；六技巧 Task/Context/Examples/Persona/Format/Tone；**核心方法论"升维提问，逐级降维"**；"先出60分再迭代"
3. **Agent入门**：定义=自主规划+调工具+执行；三维度评估（厂商/产品形态/任务类型）；"工具决定能做什么，大脑决定做得多好"；学习路径：说清需求→GUI agent实战→按需深入
4. **Agent实操**：WorkBuddy上手（工作区/完全访问权限/选模型）+ 宠物猫烘焙粮市场调研完整案例

### 关键意义

- **prompt工程缺口清零**：10-16点的5个缺口全部补完（安全/可观测性/HITL/router/prompt工程）
- 方法论互文："60分先出再迭代"=surgical-edits+breakpoint-feedback；"升维提问"=think-before-code实操版；"真实任务实测"=run-dont-read
- 企业内训框架可直接借鉴（以后给团队/客户讲AI用）

---

## 补：Karpathy "AI 理解漏斗"（2026-10-18 补）

> 原文：https://x.com/karpathy/status/2109361（2026-10-11 19:12 UTC 发布，4 月旧帖翻新，77 万浏览）
> 解读参考：https://cellcog.ai/blog/karpathy-llm-understanding-funnel/
> 一句话：你眼里的 AI 和别人眼里的不是同一个东西——差距不再是"两拨人各说各话"，而是一个四层漏斗，而且在变陡。

### 四层（都是他自称的 napkin math，无出处）

1. **约 60 亿人（75%）**：几乎没接触过 LLM
2. **10–20 亿（约 20%）**：免费层 casual 用户——把 AI 当"更好用的搜索/写作助手"用，很多高管也在这一层
3. **约 2000 万（0.2%）**：数学/代码领域的专业用户——亲眼看到 agent 一句话完成过去几周/几个月的工作（Karpathy 把自己放这一层：不到一年前他还在手写代码）
4. **约 5000 人（0.00006%）**：实验室内部——看到的是"成群的 agent 为大项目连续工作几周"

### 漏斗为什么存在：三个原因

1. **Ambition（问题水位）**："You need a reservoir of big, difficult problems that you really care about." 一段话能答完的问题，测不出系统的上限
2. **Jaggedness（能力锯齿）**：能力在"数字化、可验证、有经济价值"的领域最先爆发——这就是为什么数学和代码先行（RL on verifiable rewards）
3. **Access（访问层级）**：免费层 / 付费层 / 内部

### 跟你的咬合

- **你的位置**：第三层，而且是第三层里动手造 harness 的那一小撮（thinktank 陪审团、opencode-fuse 三档路由 = 在造"让 agent 干几周活"的工具链）
- **第四层是路线图方向**：实验室内部看到的是"agent 群连续工作几周"——thinktank Phase 3 的"judge 低置信追问/降级"、opencode-fuse 的"常驻"形态，都是往这个方向摸
- **Jaggedness 解释了你的选型**：为什么你的 agent 工具先从代码/评审切入——可验证的领域 RL 效果最好，judge 才有判据
- 他 4 月说"两拨人各说各话"，10 月改口"漏斗在变陡"：顺带解释了为什么你跟 iPipeline 同事聊 AI 时总觉得鸡同鸭讲——你们字面不在同一层
- 警句："Meanwhile, human review and comprehension are starting to fall behind."（指 OpenAI/HF 密钥事件 + 数学手稿撤稿）——这正是你 incident-to-eval / mistake-class 机制要挡的东西

## 补：码良《Agent 高频面试题单》（2026-10-19 补）

来源：https://x.com/cxjwin/status/2111644503341953409（X Article，18 分钟）

**是什么**：从牛客网 343 篇 Agent 岗面经（180 作者、~80 家公司，8/18–10/18）统计出的 29 道高频题，每道带作者数、场次数、公司/轮次分布、原帖例问和牛客链接。另有算法岗、低频题、面试结构、月度趋势、方法论/局限性章节。

**考得最多的**：
1. **RAG pipeline** 和 **"你怎么用 AI Coding 工具"**——各超 1/3 作者被问
2. **Skill / MCP / Function Calling 边界**、**Agent 评测**——9–10 月热度陡升
3. **Harness**——1/4 作者被问，已成常规题
4. 手撕代码基本还是 LeetCode，极少数现场手写 Agent Loop；30% 有项目深挖

**方法论**（作者自述局限）：1818 候选 → 1138 全文精读，排除水军号和合集帖；关键词归类可能有误、发帖日期≠面试日期、纯图片帖和小红书未纳入。

### 跟你的咬合

- 这份题单≈你最近三个月在造的东西的目录：RAG（open-memex 检索）/ Skill+MCP（opencode-fuse D18）/ Agent 评测（thinktank Phase 3）/ Harness（Harness² 学习资料）
- 市场在考的正好是你手里有的——这份题单可以当"能力对标清单"用：每道题问自己"能不能讲清楚"，讲不清的就是学习缺口
- Harness 从"新概念"变成"1/4 面试官会问的常规题"只用了两个月——佐证了《谈 AI 工程化》里"概念一波波"的判断
