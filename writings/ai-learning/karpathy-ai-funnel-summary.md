# Karpathy "AI 理解漏斗"

[← 返回目录](index.md)

分级：【摘要即可】——四层漏斗与三个成因条内齐全。

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
