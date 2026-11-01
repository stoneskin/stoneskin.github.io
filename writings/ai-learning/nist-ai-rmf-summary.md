# NIST《AI Risk Management Framework 1.0》+ Playbook + 生成式 AI Profile

[← 返回目录](index.md)

分级：【摘要即可】（框架概念、四职能、七特征、GenAI Profile 的 12 类风险）；Playbook 本身按查阅型工具书用——按项目查子类别的建议动作，不通读。

> 原文：https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf（NIST AI 100-1，2023 年 1 月，DOI: 10.6028/NIST.AI.100-1）；Playbook：https://airc.nist.gov/airmf-resources/playbook/
> 一句话：美国官方的 AI 风险管理框架：自愿性、跨行业，用 Govern / Map / Measure / Manage 四个职能 + Playbook 建议动作，把"可信 AI"变成可执行的管理循环。

- 定性：这是自愿框架，不是法律；不绑定特定行业和技术，任何规模的组织都能套用；定位是"活文档"，NIST 原文写明不晚于 2028 年做正式复审。Playbook 官方页也已声明"Playbook 将在 AI RMF 修订后更新"——所以引用时以 1.0 现行版为准，同时知道它正在修订中，不要把它当 frozen 标准背。
- 第一部分讲"可信 AI"的七个特征，其中 Valid and Reliable（有效可靠）是必要条件、是底座，Accountable and Transparent（负责与透明）是纵贯全部特征的一条线；其余五个是 Safe（安全）、Secure and Resilient（安全与韧性）、Explainable and Interpretable（可解释）、Privacy-Enhanced（隐私增强）、Fair with harmful bias managed（公平、管住有害偏见）。
- 第二部分是核心：四个职能，Govern 是横贯全程的职能，Map / Measure / Manage 按具体系统和生命周期阶段应用：
  - Govern（治理）：建文化、政策、角色、问责与流程，让 AI 风险管理成为组织能持续的纪律。落地到人就是三句话：谁是负责人、谁有叫停权、证据放哪里。还包括影响评估政策与流程，并定期验证评估真的在做。
  - Map（映射）：给单个系统建共识：用途、利益相关方、数据流、预期收益、潜在危害，覆盖全生命周期。重点是"预期用途"和"误用场景"要写下来——不是写给审计看，是让后面 Measure 知道测什么。
  - Measure（度量）：用量化与定性方法分析、基准测试、监控风险，包括性能、偏见、鲁棒性、安全。关键取舍：度量降低不确定性，不消除不确定性；阈值要预先定好，触发人工复核。
  - Manage（管理）：对已映射、已度量的风险排优先级、做处置——缓解、转移、接受、回避——并验证处置是否有效。处置决策按可能性 × 严重性 × 组织风险容忍度排，不按"哪个最好修"排；管理在上线后继续：模型、数据、用户行为、外部条件一变，就要重新 Map / Measure / Manage；模型一更新，旧测试报告只是历史证据，不自动等于新版合格。
- Playbook 的定位要特别注意：官方原话是它"既不是清单，也不是要从头跟到尾的步骤"；建议动作是自愿的，组织按行业、用例、兴趣借多借少都行。照单全抄而不连到真实决策，只会造出 paperwork 而不产生更安全的结果。这句话对 Stone 这种讨厌认证式学习的人很关键：Playbook 是按子类别查动作的工具书，不是考试大纲。
- 两个配套要知道：第一，Profile（画像）：现状画像 vs 目标画像，两者之间的差距就是具体的改进 backlog——这是把框架变成工作计划的机制，不是写文档。第二，生成式 AI Profile（NIST AI 600-1，2024 年 7 月）：把四职能套到生成式 AI，识别出 12 类生成式 AI 独有或被放大的风险并配建议动作；对 Stone 来说，读这份 Profile 比重读 1.0 全文划算（600-1 原文本次未抽查，12 类这个数字以原文为准）。
- 还有一处和他现有工作同构：框架要求"建模型的人"和"验证模型的人"分离是最佳实践——这正是 thinktank 里 judge 与 panel 分离的组织版。
- 备注：Playbook 的 Govern 子类别页动态渲染、具体建议动作条目未逐条核对，子类别细节以官网为准；框架的跨标准 crosswalk（映射到 ISO/IEC 42001）本次未核 crosswalk 文档，引用前复核。
