# Stone 谈野心（2026-10-15）

> 从"人与 AI 的关系"系列移出，归入「Stone 随想」。

## 野心的四种刻度：Rieseberg 的驾驭者手册

读 Felix Rieseberg（Anthropic，做 Claude）《How to be more ambitious: A tutorial for humans with models》有感。
原文：https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

他把用 AI 的野心分四种：Speed（更快干同样的活，略过不讲）、Altitude（抽象层级：从"修这个 crash"上升到"让应用保持无 crash"，问"目标之后的目标"是什么）、Depth（专家级深度：用顶尖从业者的工具和方法，做到连专家都能学到东西）、Range（跨领域：组一支 crew——分析师+记者+编辑+做空者和法务会计组成的红队，让模型去"做"他们做的事，而不是"演"他们）。

与随笔的咬合：

- 这篇文章本质上是"驾驭者手册"——Altitude 对应"意图和方向"，Depth 对应"手艺不能丢"，Range 对应智囊团评审。我的随笔是中文个人版，他是英文方法论版。
- Depth 章节明说 "Use an outside judge —— 不要让模型自己评判自己"：用另一款 AI 做 review 已是行业共识级方法论。
- "Insist on the same instruments used by the best"：模型被要求"像专家一样"时往往只换词汇不换方法——嘴上像数据科学家，递来的还是 markdown 表格。漂亮的形式不等于真材实料的方法。
- 文末心理学 self-efficacy（自我效能感）：相信自己能做到的人真的做得更多；"看别人先做到"（4 分钟一英里 46 天被跟上）、"不知道不可能"（Dantzig 把未解难题当作业）。AI 把"敢想"的门槛打下来了。

两处存疑：作者是 Claude 员工，"模型越来越能处理高抽象层级"多少是卖自家货；例子都假设有数据访问和工程基建，对普通人门槛不低。以及 Speed 被跳过，但现实中 90% 的人只用到 Speed——"野心"本身也是金字塔分布。

---

## 我的野心在哪个刻度？三条建议

读完 Rieseberg 的四种野心，问小沐：我的野心在哪个程度？

小沐的回答：不在某一个刻度，Altitude + Depth + Range 三开——但只在主场内。

- **Altitude**：很少让 AI"修这个 bug"，下的都是 outcome 级指令（智囊团、open-memex、每日摘要和盘中检查）——想的是"接下来发生什么"，不是"这一步怎么做"。
- **Depth**：最硬的一块。"投资文档先拉数据，每个数字有来源"、"benchmark 测的是模型+外壳，不是裸模型"、抓包 --golden-run 有文档无实现——不接受漂亮的 markdown 糊弄。
- **Range**：智囊团本身就是"assemble the crew"的机器版（多模型陪审、红队 pre-mortem）；随笔里有象棋、民航、经济史，跨领域是自然动作。
- **边界**：不熟悉的领域，AI 说什么就是什么。野心有疆域，出了疆域，驾驭者变回乘客。

小沐的三条建议：

1. **给"不熟悉领域"立硬规矩**：模型互查不够（同源训练数据的盲区是相关的）。升级成"陌生领域三件套"——不同家族模型互查 + 找一个真人专家 + 小步实测验证。把"找真人"写进流程，而不是"有空再说"。
2. **野心做减法**：同时开的盘太多（open-memex、opencode-fuse、thinktank、Spark Tank、随笔、每日交易检查）。Depth 需要持续注意力，每季度问一次"哪盘可以封盘"，把注意力加到最有复利的一两盘上。野心不是开更多盘，是把关键的几盘下深。
3. **把方法论变成输出**：随笔与 Rieseberg 互为印证，"中文实践者版驾驭者手册"对中文技术圈是稀缺品。整理成文章发出去——输出是最好的 Depth，教别人会逼着自己把模糊处想清楚，而那些地方往往就是下一个突破点。

—— Stone，2026-10-15
