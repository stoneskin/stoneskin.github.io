# 25. Agent memory 的六阶段框架：先问为什么需要记忆（2026-10-16）

[← 返回目录](./index.md) · [English Version](./25-a-six-stage-framework-for-agent-memory-ask-why-memory-is-en.md)

---

读卡夫卡（@kafkaup）长推有感。他主张选技术（向量库、图库、塞聊天记录）之前，先问 agent 为什么需要记忆：经验连续、效率、个性化、长期任务跟踪、业务护城河。记忆的核心价值是长期交互的连续性，不是记住一切。
原文：https://x.com/kafkaup/status/2110812455488151766

他给的六阶段：①决定记什么（长期价值、可结构化、个性化影响）②抽取分类（实体/关系/时间/来源/置信度；用户偏好、业务事实、过程结论、任务状态、程序性记忆）③暂存去重合并（防脏数据）④分层存储（短期任务状态放 session，长期偏好放存储，语义检索走向量，关系密集走图）⑤检索（何时查、查什么、查多少；压缩而非硬塞； relevance/recency/来源可靠度/使用频率/业务重要性加权）⑥动态维护（增删改查 + 反思，不然记忆变噪音）。

与随笔的咬合：

- 这套框架 open-memex 基本全覆盖——capture、alias、lifecycle 状态机、retrieval-ablation，每一步都有对应实现。不是追热点，是提前把作业写完了。
- "按业务需要匹配复杂度"是全文最值钱的一句：正是"默认不用 embedding"赌注的理论背书——大部分场景词法+同义词就够，embedding 只在跨语言这种明确缺口上 opt-in。
- 评论区 Zipeng Wu 的好问题（使用频率 vs 业务重要性冲突时怎么排？只提过一次的 deadline 不能被天天聊的偏好挤掉）——正是 D77 feedback-weighted ranking 要解决的。问题比实现先到，但答案已在路上。
- 他列的"好记忆四标准"（准确、检索对、有用、可删除）里，"可删除"最容易被忽视。open-memex 的 forget/supersede 链和"retracted 不可悄悄回 active"（D64）把可删除做成了硬约束——很多 memory 项目没做到，可当差异化讲。
