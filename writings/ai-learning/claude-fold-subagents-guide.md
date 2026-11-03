# Anthropic《When to fold subagents into your main agent loop》导读：少 subagent，不是不要 subagent

[← 返回目录](index.md)

> 来源（一手原文）：Anthropic Applied AI 团队，Diane Sarkis，《Building agents: When to fold subagents into your main agent loop》，2026-10-22，claude.com。原文：https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop ；配套迁移 kit（Apache 2.0）：https://github.com/anthropics/single-agent-loop-kit
> 本篇是导读（为什么值得看、主线、怎么读）；清单第 51 份，组一 路由与编排。

## 一句话结论

单 Agent + Skills 在多家企业部署对比中，经常打赢"一 prompt 包打天下"和"多 subagent"两种设计——质量更高，成本与延迟更低。subagent 不是不要，而是只留三处，其余一次折一个、用 eval 说话。

## 为什么值得看

这是目前最硬的一手"少 subagent"论证：依据不是基准测试，是 Anthropic Applied AI 团队在真实企业部署里的对比。它的结论直接对上你手里的两个设计选择——thinktank 的陪审团（subagent 结构：judge/synth 各有上下文、交回摘要）和 WorkBuddy 的单 loop + skills/tools。读完这篇，你能给"什么时候拆、什么时候合"一个可测量的判据，而不是凭感觉。

## 主线

企业 Agent 常常长成 org chart 的样子：每个能力归一个团队，每个团队建一个 subagent，上面再架一个编排器。文章先点出这种结构的五种失败模式——上下文交接丢信息、subagent 膨胀（几百个重叠的、没人负责）、Frankenprompt（每队往系统提示词里加一句、互相冲突）、各自为政的局部 eval（没人对整体分数负责）、延迟。然后给出替代方案：单 loop + 渐进式发现（progressive disclosure）——agent 只看到 skills 和 tools 的短描述，需要时才完整加载。三个理由：共享上下文产出更好（少一次交接就少一次信息损耗）、渐进式发现防上下文膨胀（Claude Code 自己的系统提示词对高级模型缩减了 80% 以上）、模型更能干了（Opus 4.5 起，单 loop 能管的比大多数团队预想的多；每代新模型都让更多决策从 harness 回到模型手里）。

迁移分四步走：先建任务完成 eval（中央团队持有一份端到端集、每个 skill 自带小 eval，10 个黄金例子就能起步）；按共享上下文合并领域 agent（经常连着被调的一对是首选）；把留下的 subagent 当工具调（主 agent 继续跟用户对话，只有 subagent 必须直接跟用户说话时才完整交接）；最后一次折一个成 skills + tools，每折一个都用 eval 对比。看的不只是总分——要看哪些任务翻了：文里有个实例，折了一个 subagent 降了延迟，却弄坏了一个原本通过的流程（主 agent 自己查订单、不问 shipping 专员要送达日期），而且这个 break 两次运行只出现一次，所以每个任务要跑多次。

组织上：所有权从"每队一个 agent"转成"每队拥有 skills 和 tools"，一个小中央团队持有系统提示词与端到端质量，每项新 skill/tool/eval 上线前审核；各队设 DRI 管自己的 skills，配 skill-doctor 定期删死重。

## 三个关键问题

1. **什么时候该留 subagent？** 原文只留三处：单 loop 因上下文膨胀出现可测量的性能下降；多任务可并行、用完即弃的新鲜上下文窗口；单 agent 选工具困难，或系统提示词里有冲突指令。推荐理解：这是"留"的判据，不是"建"的理由；新建默认单 loop，留下的每个都要能指着一条说出为什么。
2. **折叠的验收标准是什么？** 任务完成 eval 是唯一裁判：中央团队的端到端集 + 每个 skill 自带的小 eval；一次折一个，折后比分；不只看总分，要看哪些任务翻了、翻的原因；每个任务跑多次。推荐理解：没有 eval 就别折——折完变好变坏，你得有个独立于架构的尺子才知道。
3. **多团队怎么共建一个 agent 而不把它变回 org chart？** 所有权转到 skills 和 tools 上，中央小团队管系统提示词与端到端质量，上线前逐项审核；DRI 制 + skill-doctor 防膨胀。推荐理解：这是给 WorkBuddy/thinktank 的组织答案——中央小团队 + DRI，而不是每个方向一个 agent。

## 与 DeepSeek Super-agent 的对照（重点）

两篇讲的不是同一个维度，互补不冲突：Claude 这篇讲**一个任务内部**怎么精简推理结构——减少 subagent 反复交接丢信息、加延迟；DSH 那篇讲**一组任务长期并行**怎么组织执行——Router + Worker、事件直通、让人少操心。单 loop 是任务内的组织原则，Router + Worker 是任务间的组织原则。cxuan 的解读把这个区分点出来了（他的推文见 #50 摘要 §8），原文两边各读一遍，这个区分自己就立住了。

## 跟你的咬合

- **thinktank**：陪审团就是 subagent 结构——judge/synth 各有上下文、交回摘要。按这篇的口径要问：每个陪审员是不是"可测量的并行/验证"需求？如果是验证（judge 独立审），留着有理；如果只是"流程上分了一步"，就可以考虑折成 skill。陪审的 eval 就是这篇说的任务完成 eval——verdict 准不准，得有独立于陪审结构的尺子。
- **WorkBuddy**：单 loop + skills/tools + 审批门进 tools，正是这篇推荐的形态；M0 的 Scenario 验收就是它的任务完成 eval 思路——先有 eval，再谈折叠与否。
- **muse-agent-harness**：skill 治理那节（DRI + skill-doctor 删死重）与 harness 的 skill 分发同源；"每代新模型都让更多决策回到模型手里"这句，是 harness 要持续回答的问题——harness 里哪些硬编码的判断，该随着模型变强而拆掉。

## 怎么读

- **摘要即可**：本导读已覆盖主线、三问与对照；原文 250 行左右，值得对照读的是"How to fold"与"How several teams can contribute"两节（迁移四步与组织分工）。
- **查阅型**：迁移 kit（single-agent-loop-kit，Apache 2.0）——按需翻，有 demo 可先跑 mock 系统再上自己的 agent；/claude-api 四个命令（build-eval、prompt-audit、hillclimb、cost-optimize）是 Claude 生态专属，借思路不照搬命令。

## 诚实标注

- 数字来自 Anthropic 自述的企业部署对比，未独立验证："单 loop 比多 Agent 快约 2 倍"是**一个**客户的实测，不是普遍结论；"系统提示词缩减 80% 以上"是 Claude Code 自身的数。
- 文章面向 Claude Platform 企业用户，部分工具链（/claude-api 命令、migration kit）是 Claude 生态专属；Opus 4.5/5.5、Fable 5.1 这些模型代际的论断，换家模型要重新验。
- "subagent 已是旧时代产物"这种说法是 cxuan 解读里的提法，不是 Anthropic 原文的口径——原文明确保留 subagent 在验证、并行与权限隔离三处，Anthropic 自己的多 Agent 研究系统也在用。
