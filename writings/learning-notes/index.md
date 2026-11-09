# 学习笔记 / Learning Notes

[← 返回首页](../../index.md)

Stone 的每日学习笔记：导读 + 三层验收（原理 / 实现 / trade-off）。每篇记录一个知识点的完整学习过程。

Daily learning notes: guided reading plus the three-layer test (principle / implementation / trade-offs). Each note captures one concept's full learning arc.

| 笔记 Note | 说明 Description |
|---|---|
| [AI 安全：提示词注入与防御](./ai-security-prompt-injection-learning-note-2026-10-20.md) | 第一课：直接 vs 间接注入、四类防御、最小权限为何是根本解；附 open-memex 三道防线案例（2026-10-20）/ Lesson 1: direct vs indirect injection, four defenses, why least privilege is fundamental; with the open-memex case study |
| [Gulli《Agentic Design Patterns》第三部分：异常恢复 / Human-in-the-Loop / RAG](./agentic-design-patterns-notes.md) | 第三部分讲回：出错了怎么恢复、什么时候必须让人接手、答案从哪来才靠得住（2026-10-30）/ Part 3 teach-back: how agents recover from errors, when humans must step in, and where answers come from |
| [namiai《从零手写 Agent》：最小循环、权限与心跳](./namiai-agent-notes.md) | EP01–07 讲回：double loop、quote-ai 最小上下文、权限渐进放宽与硬审批、聊天接入分层、定时任务 = 心跳（2026-11-06）/ EP01–07 teach-back: double loop, quote-ai minimal context, progressive permissions with hard approval, chat-layer sessions, heartbeat as scheduler |
| [我们的设计思想总结：13 条原则对照南晚 12 条](./our-agent-design-principles-vs-nanwan-12.md) | WorkBuddy、harness-landing 与某生产 Agent 项目沉淀的 13 条设计原则，逐条对照南晚生产 Agent 12 条；唯一全缺的是第 8 条并发与过期拦截（2026-11-08）/ 13 design principles from our agent projects, checked against Nanwan's 12 production-agent points; the one gap is #8 concurrency and stale-state interception |
| [五个 Agent Harness 的对照：Opencode、Strands、Codex、Claude Code、Pi](./five-agent-harness-comparison.md) | 一张表、十九行：namiai 11 零件 + 南晚 12 条两把尺子量五家；Strands 列按 Harness 生产默认写；收尾是第一性原理读法——分歧背后是哪条约束（2026-11-08）/ Five harnesses, one table, 19 rows: namiai's 11 parts + Nanwan's 12 points; Strands column is the Harness defaults; closes with a first-principles reading of what drives each difference |
