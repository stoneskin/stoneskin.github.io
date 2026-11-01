# walkinglabs《Learn Harness Engineering》导读（2026-10-25 补，第 42 份）

[← 返回目录](index.md)

> 仓库：https://github.com/walkinglabs/learn-harness-engineering （MIT 协议）
> 课程站：https://walkinglabs.github.io/learn-harness-engineering （README 指向的 Documentation Website）
> 核实口径（2026-10-25 直读 README 全文）：21,472 stars、2,405 forks、2026-03-29 建仓、267 commits；本导读只核了 README 与大纲表，**未逐讲读 14 讲正文**，各讲细节以课程站原文为准。
> 计数诚实标注：README 课程总述段写“13 个概念单元、7 个动手项目”，但后附的 Syllabus 表是 14 讲、8 个项目（L01–L14、P01–P08），以 Syllabus 表为准，总述段属文档未同步。

## 一句话

清单里第一份“从零亲手搭一个完整 harness”的动手课程：不讲新机制，讲怎么把一个 coding agent 从“凭 prompt 干活”变成“凭一套可复用、可审计的工程结构干活”，且每一步都有弱 harness vs 强 harness 的实测对比。

## 它到底教什么：五子系统 + 16 步会话生命周期

五子系统（课程的统一框架，后面所有讲座、项目、拆解都用它）：

1. **Instructions（指令）**：agent 做什么、按什么顺序、开始前先读什么；不是一个巨型文件，是渐进披露的结构（给地图，不给百科全书）。
2. **State（状态）**：做完了什么、正在做什么、下一步是什么，落盘保存，下一会话原地续上。
3. **Verification（验证）**：只有跑通的测试套件才算证据；agent 不能靠一句“看起来没问题”就宣布完成。
4. **Scope（范围）**：一次只做一个 feature；不超纲、不半途开三个坑、不改 feature 清单来掩盖未完成。
5. **Session Lifecycle（会话生命周期）**：开始时初始化，结束时留干净的可重启状态。

16 步会话生命周期（START → SELECT → EXECUTE → WRAP UP）：

- START：读 AGENTS.md / CLAUDE.md → 跑 init.sh（安装 + 验证 + 健康检查）→ 读 progress log（上次发生了什么）→ 读 feature_list.json（什么已做、什么待做）→ 查 git log（最近改动）。
- SELECT：只挑一个未完成的 feature，只做这一个。
- EXECUTE：实现 → 跑验证（测试、lint、类型检查）→ 失败就修了重跑 → 通过才记证据。
- WRAP UP：更新 progress log 与 feature_list.json → 记下仍坏掉 / 未验证的部分 → 只有“安全可续”时才 commit → 留干净的重启路径。

这套东西和你现有的规矩是同一条线：[done-means-verified]（做完 = 验证通过）、[surgical-edits]（一次只动相关的）、[breakpoint-feedback]（阶段交接留痕），只是这里把它做成了一套可直接抄进任何仓库的模板。

## 大纲：14 讲 × 8 个项目，分 8 个阶段走

课程要求按顺序做，每阶段约一周（兼职节奏），1–3 阶段一个长周末能走完。8 个项目共用同一个产品——一个 Electron 个人知识库桌面应用（导入本地文档、管理文档库、索引、AI 问答、带引用返回答案）；P(N+1) 的 starter 就是 P(N) 的 solution，应用随 harness 能力一起演进。

| 阶段 | 讲座 | 项目 | 解决的问题 |
| --- | --- | --- | --- |
| 1. 看见问题 | L01 强模型 ≠ 可靠执行；L02 harness 到底是什么 | P01 同一任务跑两遍：纯 prompt vs 规则优先 | 基准 vs 真实工程的 capability gap |
| 2. 结构化仓库 | L03 仓库即唯一事实源；L04 指令拆文件，不写巨型文件 | P02 把仓库改造成 agent 可读 | agent 看不见的东西就不存在 |
| 3. 连接会话 | L05 跨会话保持上下文；L06 每次会话前先初始化 | P03 让 agent 从上次断点续上 | 长任务为什么总丢连续性 |
| 4. 反馈与范围 | L07 画清任务边界；L08 feature 清单即 harness 原语 | P04 运行时反馈纠正 agent 行为 | agent 为什么做多做少、做不完 |
| 5. 验证 | L09 别让 agent 过早宣布胜利；L10 全流水线跑通才算验证 | P05 让 agent 自己验证自己的活 | 自信 ≠ 正确 |
| 6. 拼成整体 | L11 可观测性要长在 harness 里；L12 每会话结束留干净状态 | P06 从零搭完整 harness（capstone，含 ablation 对比） | 下一会话的成功取决于本会话的收尾 |
| 7. 自动化循环 | L13 别再 prompt 你的 agent，改设计循环 | P07 第一个自动化循环：goal loop、timer loop、maker-checker | 从人手 driving 到 loop 自己转 |
| 8. 图结构 | L14 单循环长成图：节点、边、共享状态、路由 | P08 把 workflow 画成图：并行 fan-out/fan-in、回滚边、人工审批节点 | 什么时候画图才值得（orchestration tax） |

另有 2026 年 8 月新增的 **Frontier Harness Design Breakdowns**：用同一五子系统框架反推四个生产级 harness——Pi（最小内核 + 可编程扩展）、Claude Code（四层记忆、五级 compaction、hooks、子 agent 隔离）、Codex（仓库即事实源、AGENTS.md 当目录页、worktree 隔离）、DeepSeek（一切皆插件、能力接缝、事件管道）。

## 不用通读就能先用的三件东西

1. **Quick Start 四文件**：AGENTS.md（或 CLAUDE.md）+ init.sh + feature_list.json + progress log，Drop 进已有项目就能让会话立刻比纯 prompt 稳。注意：progress log 文件名沿用 `claude-progress.md` 是历史遗留，与 Claude Code 无绑定，任何 agent 只要在启动指令里写明“启动读、交接前写”就能用。
2. **harness-creator skill**（`skills/harness-creator/`）：几分钟给自己的项目脚手架一套生产级 harness（AGENTS.md、feature 清单、init.sh、验证 workflow）。
3. **audit-harness.sh**（`tools/`，零依赖 shell 脚本）：按 L03–L12 的五子系统给已有仓库做审计，全部 CRITICAL 项通过才 exit 0。**安全提醒：README 给的是 `curl | bash` 一行跑法，先把脚本读一遍再跑，不要直接管道执行**——这正是你“先看再跑”的规矩。

课程站另有 15 种语言版本（含简体中文）的模板、清单与方法参考；核心参考文献一层是 OpenAI Codex harness、Anthropic 长时 agent harness 两篇、LangChain Deep Agents harness、Thoughtworks / Martin Fowler、Cursor 持续改进 harness，完整分层书单在仓库 `docs/en/resources/reference/`。

## 它补了清单里的哪几块缺口

对照清单已有 harness 材料逐项比对：

- **补 1：从零搭完整 harness 的动手路径（最大缺口）。** MIT Lec 5 讲原理与判断力（可观测性、可控性、无通用最优），UMich AASE 讲拆解真 harness（Claude Code / Codex / Aider 的 loop、skills、guardrails、compaction），Pi 是“最薄 harness”的参考实现，阿里云手册 3–6 章是企业级构建模式——全是“看懂”或“拆开”，没有一份“同一个应用、一步步从 prompt-only 走到完整 harness、每步测弱 vs 强差异”的动手课程。这份就是那份。
- **补 2：可直接抄的模板与可审计的清单。** 四文件 Quick Start、Resource Library、audit-harness.sh 都是“今天就能放进自己仓库”的东西；清单里此前没有可运行的 harness 审计工具。
- **补 3：Loop → Graph 的递进。** L13（goal / timer / maker-checker 三种循环）到 L14（节点、边、共享状态、路由、回滚、人工审批）是一条完整的“循环长成图”路径；清单里 Temporal 篇讲的是耐久执行引擎那一侧（crash 续跑、单步重跑），12 步路线图的第 1 步讲状态机/DAG 是纲要，都不是这条从 loop 到 graph 的教学线。
- **补 4：四个生产 harness 的同框架对比。** Pi 你已有（第 29 份，薄内核参考实现），AASE 也拆过 Claude Code / Codex，但“同一五子系统框架横评 Pi / Claude Code / Codex / DeepSeek”此前没有；这部分可当横评材料读，不必重读 Pi 本体。

## 它不补什么（别指望它解决的）

- **多模型陪审 / 评测校准**：没有 thinktank 的 panel+judge、没有 Harness² 的 Propose–Probe–Compose 与 +11.8pp 那种“harness 本身可优化”的研究线，评测只到“验证通过 vs 不通过”这一层。
- **记忆与检索深度**：知识库应用只是练手载体，记忆只到 progress log / feature list 这一层，不涉及 open-memex 的三区检索、RAG 评估与重试环。
- **企业治理与安全**：没有 OWASP ASI、NIST、GPAI 那一侧的权限、审计、合规内容；harness-creator 脚手架进企业生产前，仍要过你自己的审批门与沙箱。
- **公司 AWS 栈**：与 Strands / AgentCore 不是一条线；公司路线仍走第 30、31 份，这份是个人项目与 harness 通用能力的底。

## 给你的读法（分讲分级，不按顺序通读）

- **对照正文 + 动手**：L02（五子系统定义）、L05（跨会话上下文）、L09（过早宣布胜利）、L11（可观测性长在 harness 里）、L13（循环工程）、L14（图工程）；项目 P01、P03、P05、P06。
- **只看本导读摘要**：其余讲座（L01、L03、L04、L06、L07、L08、L10、L12）与项目 P02、P04、P07、P08——概念你多半已有，动手时再翻原文。
- **查阅型**：Resource Library（模板与清单）、Frontier Breakdowns（横评时翻）、`docs/en/resources/reference/` 分层书单。
- **第一件可动手的事**：先读 audit-harness.sh，再拿它跑一遍你自己的 muse-agent-harness（或 thinktank / open-memex 任一仓库），看 CRITICAL 项缺哪几块——这比通读 14 讲更快验证这份材料对你的价值。

## 三个关键问题

1. 16 步生命周期里，你自己的 loop（每日检查、thinktank 评审、opencode-fuse 路由）缺哪几步——最可能缺的是“结束留干净重启路径”和“验证失败才算失败”的机械门？
2. P06 的 ablation 对比（弱 harness vs 强 harness 的实测差）能不能直接搬到 thinktank：同一任务、同一模型，只换 harness，差多少？
3. L14 的“什么时候画图才值得”（orchestration tax）与你“策略越简单跨 regime 存活率越高”怎么对表——图是第几步才该上的复杂度？
