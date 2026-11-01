# Generative Agents / Smallville 论文

[← 返回目录](index.md)

分级：【摘要即可】——三件套参数与实验数字条内齐全，原文备查。

来源：https://arxiv.org/abs/2304.03442（Park et al.，Stanford/Google，UIST '23）

**是什么**：Agent 记忆系统的开山之作。25 个 agent 在 Smallville 小镇里生活两天， emergent 出传派对邀请、约会、协调到场等社会行为。

**三件套架构**：
1. **Memory Stream**：每条记忆 = 自然语言 + 创建时间戳 + 最后访问时间戳；检索 = recency（0.995 指数衰减）+ importance（写入时 LLM 打 1–10 分）+ relevance（embedding 余弦），等权重
2. **Reflection**：最近事件 importance 总分 >150 触发（一天 2–3 次）；生成问题 → 检索 → 提炼 5 条带引用的高层洞察；可递归成树
3. **Planning**：一天 5–8 大块 → 每小时 → 每 5–15 分钟递归分解；感知新事件时重排计划

**实验**：派对消息 1→13 人（52%），5/12 到场；消融 TrueSkill 29.89 vs 21.21，Cohen's d = 8.16；代价：两天烧几千美元 token。

### 跟你的咬合

- Hot/Warm/Cold 三区 ≈ 他们的 recency/importance/relevance 三维打分的显式分区版
- 他们没解决你解决的：importance 每条调一次 LLM 太贵；你的 top 8+5 是更省的工程实现
- 可借鉴：reflection 触发机制（攒够 importance 分量再批量反思）→ auto-capture 的"攒够分量"触发
