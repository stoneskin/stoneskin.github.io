# Skill 触发命中率：kafkaup 方法论提炼

*来源：https://x.com/kafkaup/status/2110964963284033978（2026-10-16）*
*提炼：2026-10-17，小沐*

> 核心观点：description 写清楚、加场景和负面用例只是"基础操作"。触发命中率是系统性问题，最终要落到**分类系统的评估框架**里。

## 五个方向

### 1. 路由架构
- 轻量分类器先分 3–5 个粗域，再细匹配
- 或：专门一个 routing agent，只管意图识别

### 2. 匹配策略
- 关键词预筛 + 向量召回 → 候选集 → 模型 rerank
- 经典 "recall + rerank" 架构

### 3. 样例组织
- 每个 skill 维护触发场景库：**正例 + hard negatives**
- 例："总结这份合同"易误触发简历生成 skill（都抽象成"整理文档"）

### 4. 边界设计
- skill 描述之间别重叠
- 高风险动作（改代码、发消息）必须**显式用户指令**才触发

### 5. 评估迭代
- 建回归测试集，看混淆矩阵
- precision/recall 按场景取舍：**安全类 precision 优先，助手类 recall 优先**
- 落地：100 条 baseline 标注 + A/B 实验

## 评论区补充（@0xSamSing）

eval 集要加两种用例：
- 需要**同时触发两个 skill** 的复合任务
- **不该触发任何 skill** 的普通 query（"不调用 / 先澄清"也要可测量）

## 与项目的咬合

| 观点 | 咬合点 |
|---|---|
| 描述重叠是命中率杀手 | open-memex 边界审计 #1（tool description 瘦身）的理论背书 |
| 高风险动作显式触发 | "纯人手触发 skill 一律 disable-model-invocation"（已定规矩） |
| recall + rerank | open-memex：BM25-first + opt-in embedding rerank，正好是这个架构 |
| 路由错了大模型救不回来 | thinktank Phase 3 "Router 视角"、opencode-fuse 三档选档，同一结论的不同侧面 |
| eval 集加"不触发"用例 | thinktank golden cases 可借鉴：明确"什么情况下不该选某模型" |
