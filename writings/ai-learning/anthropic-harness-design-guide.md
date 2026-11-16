# Anthropic《Harness design for long-running apps》导读：别让 agent 给自己打分

[← 返回目录](index.md)

> 来源（一手原文）：Anthropic《Harness design for long-running apps》，2026-03-24（2026-10-18 更新）。原文：https://www.anthropic.com/research/harness-design-long-running-apps
> 本篇是导读（为什么值得看、主线、怎么读）；详细摘要学习时补。
> 定位：这是 Anthropic 长任务 harness 的第二篇，续 2025-11-26 的《Effective harnesses for long-running agents》（第一篇 Stone 没收，只收这一篇）；两篇的关系是基线做法 → 发现新失败模式 → 加 evaluator → 模型变强 → 拆掉不承重的部件。

## 一句话结论

长任务里 agent 有两个顽固毛病：上下文一满就失 coherence、提前收尾（context anxiety），以及给自己打分一律夸（自评失灵）。解法是把生成与评价拆开——一个怀疑型的 evaluator，拿硬阈值、用 Playwright 像真用户一样点应用来验；以及一条化简原则：harness 的每个部件都编码了一个“模型自己做不到”的假设，模型一强，假设就过期，该拆就拆。

## 为什么值得看

- **evaluator 校准方法是清单里没有的**：怎么把一个“老夸自己”的模型调成靠谱的 QA——读 evaluator 日志、找它与你判断分歧的地方、改 QA prompt、几轮之后才合理。这套方法直接对上 thinktank 的 judge 校准与 PingPilot 的 Verifier。
- **“模型一强就拆 harness”是一条验收原则**：Opus 4.6 出来后，整段 sprint 结构被拆掉、evaluator 改为跑完后单次过一遍——因为 sprint 编码的假设（模型不能自己分解长任务）过期了。harness-landing 的 Phase 验收可以直接用这条：每个部件都要能说出它补的是模型的哪块短板，短板没了就拆。
- **有代价的诚实账本**：harness 版比单 agent 版贵 20 倍以上，但单 agent 版的核心玩法是坏的（实体与运行时的连线断了，游戏根本玩不了）；DAW 一跑约 4 小时、$124 token 成本，QA 仍抓到真缺口（display-only 的功能、录音只是 stub）。贵不贵要看任务落在哪条边界上。
- **与 #24 互补**：#24 讲什么时候把 subagent 折回主 loop，这篇讲多 agent harness 何时值得留、何时该拆——evaluator 的价值取决于任务是否超出模型 solo 能力边界。

## 叙事主线

1. 起点：前一篇（initializer + coding agent，一次一个 feature、结构化交接件）把长任务跑通了，但两个毛病还在。第一，context anxiety：窗口一满模型失 coherence，快到自认的上下文上限就提前收尾；解法是 context reset（清掉窗口、靠结构化交接件重启），不是 compaction（compaction 不给干净 slate，焦虑还在）；Sonnet 4.5 焦虑严重、Opus 4.5 基本消除——新版 harness 干脆去掉 reset。
2. 第二，自评失灵：让 agent 评自己做的东西，它一律夸——设计这种主观任务上尤其明显，没有“对/错”的二元检验。拆开才有用：生成与评价分属两个 agent，evaluator 再宽容，调一个外部 evaluator 比让生成者自我批评容易得多。
3. 前端实验（校准 evaluator 的练兵场）：四条评分标准——设计质量、原创性、工艺、功能性，重设计质量与原创性（模型默认工艺与功能性不差，难的是不平庸）；few-shot 校准（带详细分数拆解的示例）；Playwright MCP 让 evaluator 直接操作页面再打分；5–15 轮迭代、单轮最长 4 小时。荷兰美术馆的例子：第 9 轮还是常规落地页，第 10 轮突变成 3D 展厅（CSS 透视的棋盘格房间、墙上挂画、门口导航）。
4. 全栈：planner + generator + evaluator 三 agent。planner 把 1–4 句提示扩成完整 spec；每 sprint 前生成方与评价方先谈一个 sprint contract（做什么、怎么验收），文件往来通信；evaluator 用 Playwright 像用户一样点应用、按硬阈值打分，不过线就打回。复古游戏机 prompt：harness 版 16 个 feature、10 个 sprint，仅 Sprint 3 就有 27 条验收标准，游戏真能玩；单 agent 版核心玩法是坏的。
5. 校准 evaluator 的苦活：开箱的 Claude 是个差 QA——发现真问题又自己说服自己“不算大事”就放行，测得浅、边角 case 漏。调法是读 evaluator 日志、找与自己判断分歧处、改 QA prompt，几轮之后才合理；即使如此，小布局问题、别扭交互、深层嵌套功能的 bug 仍有漏网——验证还有 headroom。
6. 化简：harness 太臃肿、慢、贵之后，方法不是一口气砍光（第一次激进裁剪没复现出性能，也分不清哪个部件承重），而是一次拆一个、看结果；Opus 4.6 一出，sprint 结构整个去掉，evaluator 改为跑完后单次过一遍。判断标准：evaluator 值不值，取决于任务是否超出模型 solo 能可靠做到的边界——4.5 时边界近，evaluator 处处有活；4.6 边界外移，边界内的任务上 evaluator 成了多余开销。
7. 收尾的 DAW 验证：化简后的 harness 跑“浏览器里的数字音频工作站”，约 4 小时、$124，builder 连贯跑了两个多小时不用 sprint 分解；QA 仍抓到真缺口（clips 不能拖、录音只是 stub、效果器只有数字滑条没有图形界面）。结论：模型越强，harness 的有趣组合不是变少，而是移动——AI 工程师的活是不断找下一个新组合。

## 怎么读（分级）

- 【对照正文】——“自评失灵与 evaluator 校准”一节（前端实验 + 全栈 evaluator 调法）：这是全文最值得细读的部分，直接对着 thinktank 的 judge 校准与 PingPilot 的 Verifier 读——校准循环（读日志 → 找分歧 → 改 prompt → 再测）是可以直接抄的方法。
- 【对照正文】——“化简”一节（一次拆一个 + Opus 4.6 拆 sprint + evaluator 何时值回成本）：harness-landing 的验收原则——每个部件都要能说出它补的是模型的哪块短板，短板没了就拆；新模型一到，重测一遍。
- 【摘要即可】——前端设计实验一节（四条标准、荷兰美术馆第 9→10 轮）：本导读已把标准与关键例子转述全了，结论在，不用回去抠原文；除非你要做设计类 evaluator，再对照原文看 few-shot 校准细节。
- 【摘要即可】——复古游戏机与 DAW 两个实验的经过与数字（>20x、16 feature、10 sprint、27 条标准、约 4 小时、$124）：本导读已全数转述；对比表的具体数字原文文本里读不到，只有正文里的 >20x 可引用。

## 跟你的咬合

- **thinktank**：最直接。judge 校准就是这篇的 evaluator 校准——读 judge 日志、找与你判断分歧处、改评分 prompt、几轮之后才合理；“别让 agent 给自己打分”也是 jury 存在的理由（panel → judge → synth + 人终审，生成与评价从不由同一方包办）。
- **PingPilot**：Verifier 就是这篇的 evaluator——Tier 2 的 agent 验证要怀疑型、要硬阈值、要独立执行结果（⑥验证只认独立执行结果）；“一次拆一个、看结果”的化简方法也是 V1.5 之后收敛设计的路子：新模型一到，重测哪些部件还承重。
- **harness-landing（底座 Pi）**：化简原则进 Phase 验收——Pi 的薄是有意的薄，每加一个部件都要能说出它补的是模型的哪块短板；Opus 4.6 拆 sprint 的例子说明，底座选型与 harness 结构都要随模型能力复评，不是一次定稿。
- **WorkBuddy**：长期存活的助手最缺的就是这篇讲的两样——结构化交接件（context reset 靠它重启）与怀疑型验证（跑偏了谁发现）。Watchdog/Monitor 的设计可以直接参考 evaluator 的校准循环。
- **open-memex**：结构化交接件就是编译式记忆在 harness 里的形态——交接件写什么、写多细，决定了下一个 session 能不能干净接手；这篇的“交接件必须带足状态”与你的 Chain of Recall 是同一路数。
- **要警惕的一处**：两篇都是 Anthropic 单一厂商证据（Claude Agent SDK / Claude Code），无独立基准；实验是作者自己的任务（前端设计、复古游戏机、DAW），结论的普适性要打折扣——照搬之前，先在你自己的任务上复测。
