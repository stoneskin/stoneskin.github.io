# AI 学习资料目录

*整理：2026-10-18 · 共 18 份，全部在 `~/workspace/your_files/`*
*文件名链到本地总结，原文链到出处*

---

## 一、总纲（1）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [ai-learning-resources.md](./ai-learning-resources.md) | —（自建清单） | **总清单**：19 篇 systemdesign.one 一句话要点 + 小沐评价；另有四个"补"节：Router/调度（kafkaup）、FDE-Gym、阿里云手册、龙井AI入门。5 个缺口已全部补完 |

## 二、论文 / 长文详解（5，近三天新收）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [fde-gym-paper-summary.md](./fde-gym-paper-summary.md) | [arXiv 论文](https://arxiv.org/abs/2610.22350) · [解读帖](https://x.com/Xudong07452910/status/2111306709318951189) | FDE-Gym 论文详解：95 个真实交付任务测 AI 能不能干 FDE 的活；最好模型 0.56 分；文摘中文翻译 + 五个发现 + 对职业发展的 5 点启示 |
| [aliyun-ai-agent-handbook-summary.md](./aliyun-ai-agent-handbook-summary.md) | [GitHub 仓库](https://github.com/aliyun/ai-agent-handbook) | 阿里云《AI Agent Handbook》总结：30 章企业级 Agent 全生命周期指南；章节结构 + 核心观点 + 和你三个项目的咬合 |
| [longjing-ai-primer-summary.md](./longjing-ai-primer-summary.md) | [X 长文](https://x.com/long_jingai/status/2111356255889723723) | 龙井《2小时从零看懂AI》总结：2.5 万字企业内训稿；大模型通识 + 提示词六技巧 + Agent 三维度评估 + WorkBuddy 实操 |
| [opensre-summary.md](./opensre-summary.md) | [GitHub 仓库](https://github.com/Tracer-Cloud/opensre) | OpenSRE 总结：开源 AI SRE agent 工具包（"让 AI 值夜班"）；告警→拉取证据→脱敏→诊断→推 Slack 六步工作流；60+ 工具集成；咬合 Ping 割接 on-call、5070 本地 LLM、incident-to-eval |
| [harness2-summary.md](./harness2-summary.md) | [GitHub 仓库](https://github.com/google-research/harness2) · [推文](https://x.com/AISuperDomain/status/2111642569654378716) | Google Harness² 总结：不改模型权重、只优化外围系统，Agent 基准最高 +11.8pp；Propose-Probe-Compose 自博弈；8 个可编辑组件；三个项目咬合点 |

## 三、方法论文档（6，X 帖提炼）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [skill-trigger-hit-rate-methodology.md](./skill-trigger-hit-rate-methodology.md) | [X 原帖](https://x.com/kafkaup/status/2110964963284033978) | kafkaup：skill 触发命中率五方向（路由架构/匹配召回/样例库/边界/评估） |
| [anthropic-code-review-methodology.md](./anthropic-code-review-methodology.md) | [X 原帖](https://x.com/dongxi_nlp/status/2111202933849178210) | Anthropic 代码评审六实践；四条已入 AGENTS.md（互审≤3轮/失败变考题/谁拍板/换眼睛） |
| [tool-skill-mcp-methodology.md](./tool-skill-mcp-methodology.md) | [X 原帖](https://x.com/kafkaup/status/2111063860757057677) | kafkaup：Tool / Skill / MCP 三分法与选型 |
| [spec-driven-vibe-coding-summary.md](./spec-driven-vibe-coding-summary.md) | Google Drive（Lee Boonstra，Google，2026-05） | Spec-Driven 论文总结：spec 是 source of truth；tests 抓回归、evaluation 抓漂移；approval fatigue |
| [prompt-framework-and-agent-migration.md](./prompt-framework-and-agent-migration.md) | —（AIExplorerTim 帖 + 10-13 方法论） | Prompt 框架与 Agent 迁移手册 |
| [second-brain-deleted-summary.md](./second-brain-deleted-summary.md) | [原文](https://westenberg.beehiiv.com/p/i-deleted-my-second-brain) | Westenberg 删光第二大脑："forget on purpose"；curation > capture；open-memex 红队（该忘什么是—等公民） |

## 四、工程原则与习惯（4）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [pstack-24-principles-zh.md](./pstack-24-principles-zh.md) | [GitHub cursor/plugins](https://github.com/cursor/plugins) | pstack 24 条工程原则（中英对照，Uncle Bob：把经典工程智慧重编码给 AI agent） |
| [ai-habits-as-institution-design.md](./ai-habits-as-institution-design.md) | —（小沐整理） | 把 AI 使用习惯做成可迁移的制度（含"白盒生产，黑盒交付"） |
| [agent-skill-writing-checklist-zh.md](./agent-skill-writing-checklist-zh.md) | mattpocock/skills（writing-for-agents） | 给 Agent 写文档的检查清单（译自原文） |
| [agents-md-portable-v02.md](./agents-md-portable-v02.md) | —（自建） | AGENTS.md 便携版 v0.2（最新；v0.1 为冻结快照） |

## 五、阅读筛选（1）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [x-worthwhile-reads-2026-10-16.md](./x-worthwhile-reads-2026-10-16.md) | —（小沐筛选） | 值得读的 X 帖子（只收对你有增量的，每篇一句话价值 + 核心观点 + 咬合点） |

## 六、项目方法论（1）

| 本地总结 | 原文 | 说明 |
|---|---|---|
| [open-memex-boundary-audit-2026-10-16.md](./open-memex-boundary-audit-2026-10-16.md) | —（小沐审计） | open-memex 边界审计：tool description 瘦身、pipeline tools 定位、企业版约束 |

---

*注：随笔（人与 AI 的关系 part4 等）在 `~/workspace/goals/ai/files/`，另计。*
*以后新增 AI 资料时同步更新此目录。*
