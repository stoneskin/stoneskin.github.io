# Pi Coding Agent 导读：把 Agent Harness 做到最薄的开源样本

[← 返回目录](index.md)

> 教程：@xaiwind X 长文《超简单 PI Agent，入门到精通》
> https://x.com/xaiwind/status/2113084544375304503
> 仓库：https://github.com/earendil-works/pi （117k stars、MIT 协议、v1.0.0，作者 Mario Zechner）
> 读法：仓库与教程成对读，对照正文

---

## 一句话

Pi 把 agent harness 做到最薄：内核只留工具循环 + 状态管理，plan mode、子智能体、权限系统全不内置，想要的功能自己以 package 形式装。读它不是学一个工具，是看清 harness 的本质边界——哪些东西必须在内核，哪些可以长在外面。

## 分包：薄不是简陋，是分层清楚

- **pi-ai**：统一多模型 API（含 Bedrock），换模型不用换调用方式
- **pi-agent-core**：loop + 状态，真正的内核
- **pi-durable**：会话 / 任务存储，会话可持久化
- **pi-telemetry**：厂商中立的遥测契约
- **chord**：热重载插件运行时，改插件不用重启

会话存成可分叉的树（/tree、--fork），不是一条线性日志；四种用法：交互、print-JSON、RPC、TypeScript SDK；内置 MCP 与 Codemode。

## 三个关键问题

1. **harness 的本质边界在哪？** 对照 MIT 6.S950 Lecture 5《The Harness》：Pi 的内核选择，哪些是 Lecture 5 说的"必须有"，哪些是它故意不做的？
2. **扩展点四种模型怎么选？** Pi package、Claude skills、opencode plugin、多模型编排插件——同样一个能力挂在哪一层，代价差在哪？
3. **会话树比线性日志多解决了什么？** 分叉、回滚、并行探索，分别在什么场景下才值得？

## 边界：无权限 / 审计是设计决定，不是缺陷

Pi 不内置权限与审计，换来的是内核极小、可组合。但这也意味着它进不了对审计有硬要求的企业生产——企业场景通常走 AWS 等托管栈（见 Strands 与 AgentCore 两份导读），那边的企业件是服务形态给出来的。发版极快是优点也是成本：跟版要留心。

## 跟其他材料的咬合

- **MIT 6.S950 Lec 5**：原理与判断力，Pi 是它的最小实现对照
- **UMich AASE**：拆解真 harness（Claude Code / Codex / Aider），Pi 是拆解对象里最薄的一个
- **walkinglabs《Learn Harness Engineering》**：从零搭完整 harness 的动手课程，Pi 是"薄到什么程度还能跑"的参照点
