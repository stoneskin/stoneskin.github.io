# UMich EECS 498 AASE 导读：把「指挥 Agent 写代码」当工程学科教

[← 返回目录](index.md)

> 仓库：https://github.com/eecs498-aase/materials （lectures/ 每讲 slides.md + pdf + pptx、labs/、demos/ 可运行代码、egm/ 五个可安装 skill）
> 课程站：https://eecs498-aase.github.io （EECS 498-016，Fall 2026 进行中，8/31 开课；无考试，全项目制；已放出 L01–L11、L13–L15，后半程排到 L28 陆续更新）
> 读法：分讲分级——标「对照正文」的讲读 slides.md，其余看下面逐讲摘要

---

## 一句话

把"指挥 agent 写代码"当工程学科教的大学课程——先学开（Aider），再拆真 harness（Claude Code / Codex / Aider 的 loop、skills、guardrails、subagents、compaction），最后在现成 harness 上做东西。与 MIT 6.S950 互补：MIT 偏原理，这门偏工程实践与拆解。

## 对照正文读（6 讲）

- **L03 The Big Three: Context, Model, Prompt**——全课的诊断框架：任何一次 agent 失败，先归因到三个杠杆之一。Context 讲"外科手术式上下文"（窗口里每样东西都要有理由）和 token 去向；Model 讲选型——"start on the model that fails"（先用会失败的便宜模型摸清任务难度，再升档）；Prompt 讲规格深度（说太细变手把手、太粗变抽奖）。这是给多模型评审与 harness 调试用的归因法
- **L04 Spec-Driven Development**——spec 的本质是"收窄采样分布"：写 spec 不是写文档，是把模型的输出空间压到你要的那一小块。含 spec anatomy、Prompt Levels、Architect Mode（先架构后实现）。这是 Spec-Driven 方法论的工程落地版
- **L09 Stop Conditions and the Approval Layer**——loop 安全的硬清单：六个停止条件（step 上限、token 预算、wall clock、重复相同调用、连续工具错误、done test 六行判据）各自坐在 loop 的什么位置检查；外加 approval 层与 /undo 能回滚到哪一步。拿这张清单对任何 agent loop：哪几个条件还没显式设？
- **L10 Skills and the Elephant-Goldfish Model**——skill 解剖：frontmatter 与正文的分工、三级加载（元数据常驻、正文按需、资源再按需）、"指令的四个家"、skill 与 tool 的区别、"知道一切的代价"。EGM 部分见下
- **L11 Guardrails: Errors, Retries and Approval Gates**——失败分三类（瞬时 / 永久 / 语义），重试与超时（"a timeout is not a no"：超时不等于对方拒绝）；审批门三型、auto-review 看什么、"what you approved without reading"；"thresholds are code"（阈值要写成代码不是感觉）
- **L15 Compaction and Prompt Caching**——窗口满了的四种处理法、compaction 实际怎么跑、摘要留什么丢什么、"compaction 即交接"；缓存按前缀匹配、加在末尾不破缓存、什么操作会 reset 缓存、compaction 与缓存如何相互作用

## 摘要即可（8 讲 + labs）

- **L01 课程导论 + AI 编程版图**：课程形态与工具版图速览，知道即可
- **L02 LLM 怎么写代码**：tokenization 的实际代价、大上下文的三种成本（钱、注意力稀释、二次方 attention）、context drift、"上下文沉默时统计先验获胜"（幻觉的机制解释）、能力 vs 知识之分、按任务配模型
- **L05 现代 agentic CLI**：自主性五级阶梯（级数越高、问得越少、花得越多）；agentic 工具的四原语；"repair 是插入不是阶段"
- **L06 从结对编程到 agent 编排**：可迁移的两点——"judgment at the right distance"（判断力要站在正确的距离上）和用命名 / 决策码压缩与模型的沟通
- **L07 调用内部：messages、streams、tool calls**：一次 API 调用的请求对象全字段、三种 finish reason、流式事件六型、失败流规则、"没人报告的截断"、你看不见的 reasoning token。手写 harness 时才需要正文
- **L13 浏览器扩展与可发消息的助手**：一个扩展、多个 harness 驱动；"channel 是一个会开启回合的 MCP server"；常开机器、heartbeat、triggers（让助手先开口）
- **L14 Subagents**：长会话的代价、subagent 启动时带什么（干净上下文 + 一份 brief）、报告如何返回、fresh vs forked 的取舍、harness 列明的生成成本
- **Labs**：Lab00 环境、Lab01 Aider 怎么工作、Lab03 回到 Aider、Lab04 触达计算机（Shell、MCP、浏览器）。动手材料，用时再翻。demos/ 三个代码库带 ./reset，可直接跑

## EGM 五个 skill（egm/ 目录，可安装）

方法源头：Dave Rensin（Google）2026-04《Elephants, Goldfish and the New Golden Age of Software Engineering》——"设计是新代码"：Elephant（长会话共写设计文档）产出文档，Goldfish（全新会话，只凭文档）来评审与实现，文档过不了金鱼关就是不合格。

五件套：peanuts（大库逐层 README 树）→ elephant（无代码设计对话，四节文档）→ goldfish（三个 fresh reviewer 并行，循环到只剩 nits）→ egm-implement（只建文档列的文件，漂移即停、先修文档）→ mean-review（狠审 diff，脚本强制四道扫描）。这是"换一批 fresh 眼睛评审"想法的流程化版本。

## 三个关键问题

1. 用 Big Three 给一次真实翻车归因，哪个杠杆修起来最便宜？
2. L09 六个停止条件里，你的 loop 还缺哪几个，缺的那个靠什么兜住？
3. EGM 的 goldfish（只凭文档的新会话）与多模型评审（换模型但带任务书）哪个更严、差在哪？

## 后半程

L16 起的 memory、知识库、"多模型挂一个 harness"三题与本课最相关，出讲后补记。
