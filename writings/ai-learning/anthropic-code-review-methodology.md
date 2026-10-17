# Anthropic 的 Code Review 方法论提炼

*来源：https://x.com/dongxi_nlp/status/2111202933849178210（2026-10-17，转述 Anthropic 博客）*
*背景：Claude 已写 Claude Code 约 90% 代码；2026 年 6–9 月合并 PR 翻倍，revert 反而降 40%+*
*提炼：2026-10-17，小沐*

## 六条

### 1. 机器做大部分，人只看高风险
- 人只负责高风险判断，配快速回滚兜底

### 2. PR 前：自测 + fresh eyes
- Claude 自己跑测试和构建
- 再起一个**全新 agent** 审 diff（避免自己审自己）

### 3. 每个 PR：多 agent 找 bug + 投票过滤
- 多个 AI agent 并行找 bug，**投票过滤误报**
- 加安全审查 + CI 全过
- 所有 finding 必须处理完才能合

### 4. 人工审批按风险分级
- 低风险 0 人 / 中风险 1 人 / 高风险 2 人，**分类器定级**
- bot 的 approve 不能代替人
- **谁 drive 的 agent，谁对 change 负责**（责任不转移）

### 5. 发布：灰度 + 一键回滚
- merge queue + feature flag
- 先内部狗粮，再逐步放量
- 出问题一键回滚

### 6. 持续改进：incident → eval
- 历史 incident 编成 **daily eval**，持续考 reviewer
- **限制 review 轮数**，防止 agent 互相审到天荒地老（死循环烧钱）

## 与项目的咬合

| 观点 | 咬合点 |
|---|---|
| 谁 drive 谁负责 | approve-fatigue-guard 的另一面：省审批轮次可以，责任不能省 |
| 投票过滤误报 | 智囊团陪审团机制在 code review 上的同构 |
| incident 编成 daily eval | PR #23 Evaluation harness 要干的事，Anthropic 已在生产跑 |
| 限制 review 轮数 | 写进 harness：agent 互审必须有终止条件 |
| fresh agent 审 diff | thinktank 评审团"换一批人看"的同理：自己审自己有盲区 |
