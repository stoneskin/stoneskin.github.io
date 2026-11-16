# OpenAI《Harness engineering》导读：纪律不在代码里，在脚手架里

[← 返回目录](index.html)

> 来源（一手原文）：OpenAI，Ryan Lopopolo《Harness engineering: leveraging Codex in an agent-first world》，2026-02-11。原文：https://openai.com/index/harness-engineering/
> 本篇是导读（为什么值得看、主线、怎么读）；详细摘要学习时补。
> 术语史提醒：这篇不是“harness engineering”最早的文章——这个词是 Dex Horthy 2025-11-04 先造的，Anthropic 的 Justin Young 2025-11-26 先出了成体系讲 harness 做法的文章；OpenAI 这篇是第一次把这个词当标题、把它推成主流的那篇。

## 一句话结论

一支 3 到 7 人的小队，用 Codex 在 5 个月里从零交付了一个内部产品，约 100 万行代码、约 1,500 个合入的 PR，0 行手写代码——文章讲的不是模型多强，而是人不再写代码之后，工程的活变成了什么：设计环境、写清意图、搭反馈回路，让 agent 能可靠干活。人的稀缺资源只剩时间和注意力。

## 为什么值得看

- **最详实的 agent-first 实战记录**：不是方法论宣言，是一支真团队 5 个月的账本——数字、踩的坑、改的流程全有出处；作者自己也打了折扣（单团队、内部产品，不一定能直接搬走）。
- **“harness engineering”这个词的定稿处**：词不是他造的，但这篇之后它成了行话；读这篇等于读这个词的定义现场。
- **跟你的三个项目同一条线**：PingPilot 的确定性规则、WorkBuddy 的长期存活、harness-landing 的底座选型，这篇的每条经验都能直接对照——AGENTS.md 当目录、invariant 机械执行、golden principles 当垃圾回收。
- **一句话就值回票价**：“building software still demands discipline, but the discipline shows up more in the scaffolding rather than the code.”（纪律不在代码里，在脚手架里。）

## 叙事主线

1. 实验设定：2025 年 8 月末空仓库起步，Codex CLI + GPT-5 搭脚手架，连 AGENTS.md 都是 Codex 写的；立约 0 行手写代码；5 个月后约 100 万行、约 1,500 个 PR，3 人到 7 人，人均每天 3.5 个 PR，吞吐量还随人数上升；产品有内部日常用户和外部 alpha 测试者。
2. 工程师的活变了：环境没给够时 agent 寸步难行；人的活变成 depth-first 拆小积木（设计、代码、评审、测试），再用积木去解更大的题；失败时不喊“再试一次”，而是问“缺什么能力，怎么让它对 agent 又清晰又可强制执行”；Codex 自审 + agent 评审 + 回应反馈循环到满意（Ralph Wiggum loop），人可以审 PR 但不是必须，评审基本 agent 对 agent。
3. 让应用对 agent 可读：瓶颈变成人的 QA 容量；每个 worktree 起一个可跑的实例、接 Chrome DevTools Protocol（DOM 快照、截图、导航）、日志指标 traces 走本地临时可观测栈（LogQL/PromQL），单次运行经常干 6 小时以上（人睡觉时也在干）。
4. 仓库知识当 system of record：一个 1,000 页的 AGENTS.md 试过，死法可预期——上下文被挤占、处处重点等于没重点、立刻腐烂、没法机械校验；改成约 100 行的 AGENTS.md 只当目录，知识住在结构化的 docs/ 里（设计文档编目 + 验证状态 + 核心信念、架构地图、质量分级、计划当一等工件带进度与决策日志），progressive disclosure + linter/CI 机械校验 + doc-gardening agent 扫过期文档提修复 PR。
5. Agent legibility 是目标：仓库首先为 Codex 的可读性优化——上下文里看不到的东西等于不存在；Slack 里的架构共识不进仓库就等于新同事三个月后不知道；“无聊”的技术对 agent 更友好（可组合、API 稳定、训练数据里有）；宁可让 agent 重写一小部分功能，也别绕不透明的上游行为（p-limit 的例子：自写 map-with-concurrency，100% 测试覆盖、接 OpenTelemetry）。
6. 用 invariant 管架构、用 taste 管细节：只定不变量、不 micromanage 实现（边界处 parse 数据形状，Zod 只是模型顺手选的，没强制）；每个业务域固定分层 Types → Config → Repo → Service → Runtime → UI，依赖方向只许向前，横切关注点只走 Providers 一个接口；全部由自定义 linter + 结构测试机械执行，lint 报错信息里直接写修复指引，喂回 agent 上下文。
7. 吞吐量改写合并哲学：阻塞门禁最少、PR 短命、flake 用后续跑解决不无限堵；agent 吞吐远超人的注意力时，修正便宜、等待昂贵——低吞吐环境下这叫不负责任，这里是对的 trade-off。
8. 熵与垃圾回收：Codex 会复制仓库里已有的模式，包括次优的，漂移不可避免；团队以前每周五花 20% 的时间清“AI slop”，扩不下去；改成 golden principles 编进仓库 + 定期后台 Codex 任务扫偏差、更新质量分级、开重构 PR（多数 1 分钟内可审、可自动合）；技术债是高利贷，小步持续还比攒着疼。
9. 还在学什么：多年尺度上 agent 生成系统的架构一致性怎么演化还不知道；人的判断力在哪层杠杆最大、怎么编码才能复利，也还不知道；最难的挑战已经变成设计环境、反馈回路与控制系统。

## 怎么读（分级）

- 【对照正文】——“仓库知识当 system of record”与“enforce invariants”两节：这是全文的骨架，直接对着你的 PingPilot 设计文档读——他们的 docs/ 编目 + 验证状态就是你的 DESIGN.md/REPORT 纪律，他们的 invariant 机械执行就是你的 Tier 1 确定性检查。
- 【对照正文】——“熵与垃圾回收”一节：golden principles + 定期清理的机制可以直接抄进 harness-landing 与 WorkBuddy 的运维设计；“每周五 20% 时间清 slop”这个数字是判断要不要自动化的标尺。
- 【摘要即可】——实验经过与数字（100 万行、1,500 PR、3.5 PR/人/天、6 小时单跑）：本导读已全数转述，结论与保留条件都在，不用回去抠原文。
- 【摘要即可】——应用可读性的工具细节（CDP、LogQL/PromQL、per-worktree 实例）：知道“给 agent 配可观测栈”这个方向就够了，具体工具等你搭 WorkBuddy 可观测性时再翻。
- 【摘要即可】——“单 prompt 端到端做功能”那张清单（验状态、复现 bug、录失败视频、修、验证、录修复视频、开 PR、回反馈、修构建失败、只在要判断时找人、合入）：作者自己说了，高度依赖这个仓库的结构与工具，不假设能直接搬走。

## 跟你的咬合

- **PingPilot**：最直接。①确定性规则先行 = 他们的 invariant 机械执行（Tier 1 检查、linter、结构测试同一路数）；④状态机是编排 = 他们的计划当一等工件（case 状态机 + 决策日志）；docs/ 当 system of record = 你的 DESIGN.md + REPORT + 决策日志；doc-gardening agent = 你的 P3 Monitor agent 的雏形（只读、抽查、提修复）。
- **harness-landing（底座 Pi）**：“约束是速度不腐烂的前提”——Pi 的薄是有意的薄，这篇给 Phase 1–4 一个验收问题：每一层加的东西，是让 agent 更容易推理，还是更难？“无聊技术优先”也是选底座时的标尺。
- **WorkBuddy**：长期存活的助手最缺的就是这篇讲的两样——legibility（WhatsApp/邮件/日历消息进来，agent 能不能直接看到上下文）与反馈回路（跑偏了谁发现、谁纠正；Watchdog/Monitor 就是答案）。
- **open-memex**：这篇的“仓库即记忆”与你的编译式记忆是同一路数——wiki 层是编译后的记忆，doc-gardening 是记忆保鲜；差别是他们把记忆放在仓库里，你把它做成独立服务。
- **thinktank**：agent 对 agent 的评审就是陪审团的影子；差别是你的陪审团终审在人，他们推到 agent 对 agent——这正是你要守住的那条线：人只做纠偏，不做瓶颈，但终审权不交出去。
- **要警惕的两处，不要照搬**：①“0 行手写代码”是他们有意的实验约束，不是你的目标——你的项目是 brownfield + 公司合规，人工写代码仍是把关手段；②“最少阻塞门禁、PR 短命”的合并哲学不适用于你——你的 branch + draft PR、手机 review 是刻意保留的人工关口，吞吐量不是你的瓶颈，正确性才是。
