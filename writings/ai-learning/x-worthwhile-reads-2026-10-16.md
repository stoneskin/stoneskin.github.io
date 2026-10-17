# 值得读的 X 帖子（2026-10-16）

*小沐筛选：只收对 Stone 有增量的，nini 美股六法那篇已过滤（新手常识，无增量）。每篇：一句话价值 + 核心观点 + 咬合点。详细感悟见随笔 part4。*

---

## 1. AI native 不是用 AI，而是默认 AI 在场

- 作者：卡夫卡 @kafkaup｜https://x.com/kafkaup/status/2110860521008206107
- 一句话：AI first vs AI native 的区分，照出你自己的工作流已经是 AI native。
- 核心：
  - 试金石：第一反应从"我怎么做"变成"AI 能接哪段"
  - AI-friendly 信息格式：自然语言表意图 / Markdown 共读 / JSON 传结构 / MCP 给执行
  - Context engineering = 让 AI 住进环境，不是把上下文搬进聊天框
- 咬合：open-memex 的设计文档几乎就是这篇的工程版；纠正后记——AI 审完还是你拍板（感悟 #19）

## 2. Agent memory 六阶段框架：先问为什么需要记忆

- 作者：卡夫卡 @kafkaup｜https://x.com/kafkaup/status/2110812455488151766
- 一句话："按业务需要匹配复杂度"是你"默认不用 embedding"赌注的理论背书。
- 核心：
  - 六阶段：记什么 → 抽取分类 → 去重合并 → 分层存储 → 检索 → 动态维护
  - 好记忆四标准：准确、检索对、有用、**可删除**（最易被忽视）
  - 评论区 Zipeng Wu 好问题：频率 vs 重要性冲突时怎么排？= 你的 D77
- 咬合：open-memex 六阶段全覆盖；D64（retracted 不可悄悄回 active）是差异化（感悟 #20）

## 3. Vibe Coding 四习惯：模型是公共品，harness 是护城河

- 作者：Kxians @xulijian1994｜https://x.com/xulijian1994/status/2110615259979649507
- 一句话：第四条"定期蒸馏历史"就是你的"修进 harness"，他写成建议，你做成纪律。
- 核心：
  - 别造轮子（先搜 GitHub）/ 定期换对话窗口 / 别让 AI 无脑读整文件 / 定期蒸馏历史→Skill+AGENTS.md
  - "模型大家都能用，但每个人积累的工作流差距会越来越大"
  - 评论区 chaim chen：交接文档只留四项——目标/已确认结论/未解决报错/下步验证法
- 咬合：compaction 摘要学"四项交接"；Karpathy 第二条"简单优先"与第一条同构（感悟 #21）

## 4. pstack 24 条工程原则：指令从步骤压缩成原则

- 作者：邵猛 @shao__meng 转述 poteto（Cursor 官方插件作者）｜https://x.com/shao__meng/status/2110976920343171542
- 一句话：模型越强，指令越该从"冗长步骤"压缩成"短的、有名字的原则"——你 AGENTS.md 起名运动的理论源头。
- 核心：
  - 每条 10-20 行，是蒸馏的好实践不是工作流脚本
  - /poteto-mode：事后必须点名"哪条原则影响了哪个决策"，推理可审计
  - 原则来自真实纠正 = "structured sediment of lessons" = 修进 harness
  - Uncle Bob：把经典工程智慧重编码给 AI agent
  - 存疑：原则越短对模型要求越高，压缩是有条件的
- 咬合：已收编 4 条进 AGENTS.md（attack-the-premise / explain-the-number / build-the-lever / fix-root-causes）；24 条全表中英对照见 lib（感悟 #22）
- 全表：`pstack-24-principles-zh.md`

---

*过滤记录：nini_incrypto_ 美股六法（2026-10-16）——新手常识清单，六条无一超出 Stone 现有系统，唯一亮点是评论区"难的是人性"一句，已有三方针覆盖，不收录。*
