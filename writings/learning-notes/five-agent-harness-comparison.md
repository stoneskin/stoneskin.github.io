# 五个 Agent Harness 的对照：Opencode、Strands、Codex、Claude Code、Pi

[← 返回目录](index.md)

> 两把尺子：一是 namiai《从零手写 Agent》的 11 个零件（循环、工具、权限、上下文、Skills、聊天接入、定时/心跳、MCP、子 Agent、计划、记忆）；二是南晚的生产 Agent 12 条（确定性边界、轻量级路由、上下文隔离、主动获取上下文、工具接口设计、结构化报错回传、显式状态管理、并发与过期状态拦截、循环上限与预算控制、人类审批节点、断点续跑与持久化、沙箱环境隔离）。重合的维度合并成一行。namiai 自己的手写 agent 不在比较对象里，只借他的尺子。
>
> 五家都是读源码或官方文档拆出来的，不是按宣传页抄的：Opencode、Strands、Codex、Pi 读了源码；Claude Code 闭源，结论来自官方文档与社区分析，推断处会标明。基线与核查日期见文末。

## 一张表：五个工具，十九行

| 维度 | Opencode | Strands Harness | Codex | Claude Code | Pi |
|---|---|---|---|---|---|
| 循环 | 有，while 循环 + per-agent steps 上限 | 有，单 cycle + 递归 + 外层 resume 循环 | 有，单 Receiver 串行 + 34 个 Op | 有，模型+工具循环，Stop hook 可续 | 有，双层循环 + steering 中断 |
| 工具系统 | 有，扁平小工具，Schema.Struct 强类型 | 有，@tool 装饰器 + 注册表，自带 shell/读写/改文件等 | 有，115 行 facade + 22 mod，ToolDefinition 30 行 | 有，约 50 个内置，名字精确贯穿三处配置 | 有，4 个核心工具 + 只读集，JSON Schema 校验 |
| 权限与确定性边界 | 部分，allow/ask/deny + last-match-wins + hook；无独立规则引擎 | 有，Intervention 五拦截点 + Cedar 策略；但 Harness 默认 interventions 全关 | 有，三层：Starlark execpolicy + 内核沙箱 + 网络策略 | 部分，deny/ask/allow + 33 钩子 + 沙箱拼出边界；无独立规则引擎 | 部分，prompt + 工具表，无代码硬规则；默认不审批 |
| 人类审批节点 | 有，ask 弹确认、hook 可改判、server API 远程回复、无人值守 ask→deny；无批量审批 | 有，机制最全：event.interrupt + HumanInTheLoop 白名单/LLM 分类 fail-closed/信任记忆 + Cedar；但 Harness 默认全关，须显式开 | 有，ExecApproval/PatchApproval 真同步阻塞 + 双向审批请求 | 有，权限弹窗、plan 批准、PreToolUse、auto 模式分类器 | 无，核心默认不审批，扩展给 permission-gate |
| 上下文管理 | 有，AGENTS.md 自动加载 + 自动压缩默认开（keep 15k）；无分层打包 | 有，两代并存互斥：SlidingWindow 40 条 / Summarizing / 新 ContextManager；Harness 默认 context-manager auto + caching auto | 有，compact + 双轨持久化；compact 失败是短板 | 有，压缩是唯一回收机制，自动 + 手动 + /rewind；1M 上下文变体 | 有，结构化 prompt + 压缩（reserve 16k / keep 20k）；无主动拉取 |
| Skills | 有，skill 工具按 id 显式加载，agentskills.io SKILL.md | 有，SKILL.md + 渐进披露，按名激活；Harness 默认 skills 开 | 有，一等公民，catalog/provider/快照 | 有，Agent Skills 标准，四种触发 | 有，Agent Skills 规范，渐进披露 |
| 聊天接入 | 无，只有 serve HTTP API + SDK | 无，只有 interrupt/handoff 原语 + A2A server | 无，CLI/TUI/IDE/Cloud/SDK，无聊天软件 | 无原生，终端/桌面/IDE/网页/手机；Slack 靠 MCP 连接器 | 无，TUI/Print/RPC/SDK；OpenClaw 是集成例 |
| 定时 / 心跳 | 有，schedule 工具 cron + every，SQLite + leader 选举；需 server 进程活着 | 无，background_tasks 只是后台执行，无定时触发 | 无，用户级定时/心跳空白；cloud-tasks 是人发起云上跑 | 部分，三套互不相通：云端定时任务、桌面定时、会话内 CronCreate//loop | 无，核心无心跳/定时；扩展 session_start 后自起 |
| MCP | 有，完整客户端，`<server>_<tool>` 命名 | 有，完整客户端 stdio/SSE/streamable-http；无内置 server 暴露 | 有，双向 + 两级审批；审批叠加优先级未文档化 | 有，HTTP/SSE/stdio/WebSocket + resources/prompts/elicitation；本地 MCP 在沙箱外 | 有，客户端 stdio + streamable HTTP；扩展可注册 server |
| 子 Agent / 多 Agent | 有，subagent 工具独立 child session，可并行；无调度器 | 有，最完整：Graph 有向图 + Swarm + subagent 工具 + A2A；深度上限 2 | 有，父子拓扑，InterAgentCommunication + agent-graph-store；单实例不并行 turn | 有，子 agent 独立窗口 + Agent Teams（实验性）+ Agent View；五种并行形态互不正交 | 无，核心无；示例扩展多进程跑独立 pi 进程 |
| 计划 | 无独立规划器，Plan agent + todo 工具；edit 全 deny | 无，Graph 须手写节点边；无自主规划器 | 部分，plan_mode bool 开关，不是独立规划器 | 有，Plan mode 只读规划 + 批准三选一；无分级规划/版本管理 | 无，核心无；示例 plan-mode 扩展只读 |
| 记忆 | 无长期记忆，AGENTS.md + SQLite 会话 + 压缩摘要 | 部分，MemoryManager opt-in；FileMemoryStore 关键词检索；Harness 默认 memory 开，落 ./.agent/memory | 有，三层持久化 + SetThreadMemoryMode；谁写记忆未深核 | 有，CLAUDE.md 人写 + MEMORY.md 模型写；无复用度量/入库审批/知识编译 | 无长期记忆，会话树 + 压缩；扩展做 RAG |
| 轻量级路由 | 无，单会话单模型，无自动升档 | 有，ModelRouter + Fallback/Classifier 策略；无成本/延迟策略；默认模型 Bedrock Opus 5 | 部分，provider 可换，无轻重分流 | 无，人手选模型；auto 分类器是审查器不是路由器 | 部分，15+ provider 会话中手动换模型；无自动路由 |
| 结构化报错回传 | 部分，ToolFailure 结构化回传；无统一错误 schema/重试设计 | 有，工具级 success/error + 循环级 13 值 stop_reason + 结构化异常 | 部分，FunctionCallError 二分：回传模型 vs 致命；无细化协议 | 部分，PostToolUseFailure hook + 错误回填；无统一工具层 schema | 有，isError + details + structuredContent；无错误码枚举 |
| 显式状态管理 | 有，SQLite 会话 + run-coordinator 同 key 串行 | 有，state 三层 + 版本化同步；SessionManager hook 驱动 | 有，Op 枚举即状态机 + Session + 三轨落盘 | 部分，任务列表 + transcript；无单一状态机文件 | 有，JSONL 会话树 + entry 事件 + 用量统计 |
| 并发与过期拦截 | 无，全缺；doom_loop 只有配置无实现 | 部分，同一实例禁并发 + 幂等 token + interrupt 版本计数；无通用过期拦截 | 无，单 Receiver 串行消灭并发；无版本校验/过期拦截 | 无，文件锁防同改；无版本校验/过期拦截 | 部分，并行 + 同文件串行 + steering 中断；无过期拦截 |
| 循环上限与预算控制 | 部分，per-agent steps 上限；成本只统计不封顶 | 部分，limits turns/token 须每次调用传，默认不限；无美元预算；Harness 亦无默认上限 | 部分，token 预算 max_goal_token_budget 有；循环次数上限无 | 部分，交互会话无硬上限；print 模式的 --max-turns/--max-budget-usd 据社区转述，未逐字核对 | 无，两者皆无；用量只统计 |
| 断点续跑与持久化 | 部分，SQLite + 恢复 + fork + 压缩摘要；长会话恢复有已知问题 | 有，SnapshotSessionManager 时间旅行快照 + File/S3 session；Checkpoint 只是暂停点标记，实验性 | 有，三轨 rollout/state/thread-store；compact 失败是短板 | 有，JSONL transcript + --continue/--resume/--fork + /rewind | 有，会话树 + /tree 续跑；另有实验性 durable 包先提交再展示 |
| 沙箱隔离 | 无，SECURITY.md 明说不沙箱；须套容器/VM | 部分，SDK 默认零隔离；Docker/SSH 换后端；Box 是独立 Rust 项目 Dogwood permit/forbid，预览版，macOS Apple Silicon + Linux ARM64，无 Windows | 有，全场最强：5 值 SandboxType，三 OS 内核后端 | 部分，Bash 沙箱真实存在但默认关、只管 shell；文件工具/MCP/hook 在外 | 无，核心无沙箱；部署时自己套容器/VM；Gondolin 扩展 micro-VM |

## 每家一句话

- **Opencode**：权限是全部治理，沙箱是零；定时任务是五家里少有的内置项；无路由、无预算；子 agent 与 Plan 都是"agent 配置 + 权限"拼出来的。
- **Strands Harness**：给得最多的一家，也是默认最"空"的一家——Harness 默认开了 session/skills/memory，但 interventions 全关、无 loop 上限、无美元预算；人工批准机制五家最全（interrupt + HITL + Cedar），但默认不开；多 Agent 五家最完整（Graph/Swarm/subagent/A2A）；沙箱一分为二（SDK 内很薄 + 独立的 Box 预览版）。
- **Codex**：产品化 harness + 协议中枢 + 内核沙箱；治理三层最硬；Hook 只有 AfterAgent 是最大债；入口对象已变（Session + app-server），原章"入口 5 字段"的方法论已失效；compact 是短板。
- **Claude Code**：治理最重、锁定最硬。33 个钩子（不是旧数的 26 个）+ 三层权限 + 分类器自动审批 + 沙箱（默认关），是五家人类审批与确定性拦截做得最细的一个；代价是只跑 Claude 模型、没有路由与成本升档；记忆与定时各有两三套互不相通的机制，不是统一设计。
- **Pi**：五家里唯一把"少做"当卖点的——"Primitives, not features"。核心只有 5/11 个零件（循环、工具、上下文、Skills、MCP），缺的不是没做，是设计上推给扩展；循环是核心最完整的一块，也是唯一没有上限的一块；治理五家最弱（默认不审批、无沙箱）；持久化是最强的两项之一（会话树 + 实验性 durable 包）。

## 本质：分歧背后是哪条约束

这张表最值得看的不是"谁有谁没有"，而是每一行分歧背后都有一条约束在推。抄功能清单没用，要抄的是"约束→选择"的映射：

- **Codex 把沙箱做到 OS 内核层**，因为它要跑在云端多租户环境，不可信代码必须由内核拦；**Claude Code 只有应用层钩子加默认关闭的沙箱**，因为它是跑在用户机器上的单厂商产品，要的是细粒度控制而不是规则引擎。
- **Pi 故意少做**，因为它卖的是"可读可改"——harness 薄到能读完、能改掉，功能由用户自己长出来，代价是组装成本归用户；**Strands 默认全是 opt-in**，因为它的本质是做 Agent 的工具箱：库里多半都有，默认不开，按需打开、自己设计——挺好的框架，设计是你自己的事。
- **Claude Code 没有路由**，不是忘了做——它只跑自家模型，产品形态决定了不需要 cheap→expensive 的升档；**Opencode 没有预算熔断**，是因为它首先是服务端产品形态（serve + TUI + 插件生态），成本控制不在它的责任边界里。

还有一条要先说清楚：这张表用同一把尺子量五家，但五家的目标工作不一样。Opencode、Codex、Claude Code 首先是写代码的编码助手（人在终端前互动）；Strands 是做 Agent 的工具箱；Pi 是极小 harness。Opencode 尤其如此：它的定位是 AI 写代码的编辑器，不是自动化工作的 Agent——用生产 Agent 的 12 条量它，量的是边缘能力，表里的"无"要结合各家主场读。

我们的约束跟他们都不一样，所以答案也不一样。我们的 13 条设计原则（见《我们的设计思想总结》）就是按自己的约束推导的答案：确定性规则先行、人只做纠偏与拍板、预算六项硬上限、记忆保鲜与知识编译、多模型陪审——没有一条是从这五家里抄的。harness-landing Phase 0 选底座的五项标准（loop、工具调用、skill 机制、扩展性、可替换性），就是这套第一性原理落到选型上的样子。

表里最值得标出来的一行是**并发与过期拦截**：五家没有一家真正有它。Codex 用串行消灭并发，Claude Code 用文件锁防同改，Strands 只有 interrupt 一处的版本计数，Pi 和 Opencode 干脆全缺——全行业都没做。我们自己也没做出来，先不把话说在前面，只标这是可以做的一个方向：以后做三个项目时可以往这个方向看。

## 基线与诚实标注

- **Opencode**：anomalyco/opencode（原 sst，已改名），HEAD f29228b，v2.2.5，2026-11-09 读源码。官方权限文档页本次抓取失败，默认值说法只转述二手资料，写表以源码为准。
- **Strands**：strands-agents/sdk-python HEAD 3d32c22（含 harness-py）+ strands-agents/box HEAD 4268891，2026-11-08。Strands 列按 **Harness**（`create_harness()` 的生产默认）写，裸 `Agent()` 的行为只当底层机制提。
- **Codex**：openai/codex HEAD 8703d32，2026-11-09。底本 xiaonancs 第 24 章是 2026-05 快照，Codex 侧 14 项承重事实已逐项抽查：架构判断全成立，行号与数量多已漂移（`Codex` 结构体已不存在、Op 25→34 个、crate 120→168 个），表里数字以本次抽查为准，不照抄原章。
- **Claude Code**：闭源，无源码可读。结论来自官方文档（code.claude.com，v2.1.x，2026-11-09）与社区分析；"26 个钩子"是旧数，现为 33 个。报告里每条结论标了［官方文档］/［社区分析］/［推断］，本文只取了已核实的部分。
- **Pi**：github.com/earendil-works/pi，commit 7d07332，coding-agent 1.5.0，2026-11-08。

2026-11-08；尺子来源：namiai《从零手写 Agent》EP01–18（11 零件）与南晚 2026-11-08 推文《构建自己的 Agent 至少需要完成这些》（12 条，南晚此文已入学习清单第 55 份）。
