# AI Skills

[← 返回首页](../../index.md)

*2026-11-04 · [English Version](./skills-en.md)*

Agent Skills 是给 AI 用的能力包：一段提示词 + 脚本 + 参考文档，agent 按需加载，不用时不占上下文。只收我自用、认真评估过、或热门到值得知道的。**使用强度与评价分开算**：使用强度是我的实际用量，评价是推荐度——没用过的按口碑与公开资料给分，不是实测。★★★★★ 强烈推荐，★★★★☆ 值得用/试，★★★☆☆ 可以看看，★★☆☆☆ 评估过、没采用。每类最多 5 个完整条目，多出的放“其他”一行，只列名字。工具在另一页：[AI 工具箱](./index.md)。

## 一、自用 Skills

| Skill | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [diagram-design](https://github.com/cathrynlavery/diagram-design) | 常用 | ★★★★★ | 画图 skill：45 种图型，自包含 HTML + 内联 SVG，零外部依赖；Pi 架构图（静态 + 动态 loop 版）就是它画的；删繁是最高质量的动作，每个节点都要配得上位置。 |
| [thinktank writing](https://github.com/stoneskin/muse-thinktank) | 常用 | ★★★★☆ | thinktank 种子 skill：搭双语写作上下文（LinkedIn 文章、文档），触发词写作/write/文章；随笔与技术文章的写作上下文从这里来。 |
| [thinktank stock-analysis](https://github.com/stoneskin/muse-thinktank) | 常用 | ★★★★☆ | thinktank 种子 skill：跑 tt/stock_context.py 拉技术面，输出进共享 context 再喂给评审团；投资分析先拉数据再动笔的执行层。 |
| [thinktank code-review](https://github.com/stoneskin/muse-thinktank) | 常用 | ★★★★☆ | thinktank 种子 skill：评审的固定前置动作，输出进共享 context 再喂给评审团。 |
| local-questioning | 常用 | ★★★★☆ | 本地自研追问方法（grill-me 的本地版）：学习验收与需求澄清两处自动激发——学习时问到原理/实现/trade-off 三层讲清为止，动手前先把需求问清、免得 review 才发现做错；不用 "grill" 这个词。 |

## 二、热门 Skills：发现、追问与协作

*出自 Ethan 恩宇 2026-10-21 X 帖《全球最热门的 10 个 AI Skills》（[原文](https://x.com/UPing123zzz/status/2112843303330738503)），安装量为帖子口径；10 个里 7 个出自 mattpocock/skills。*

| Skill | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [find-skills](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md) | 未用 · 已有等价物 | ★★★★☆ | 约 380 万安装，榜首：让 AI 自动发现可安装的现成 Skill；我已有 local-skill-discovery-first 做同样的事，排行榜优先那套就是从它学的。 |
| [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) | 未用 · 理念已落地 | ★★★☆☆ | 约 130 万安装：AI 持续追问，把模糊需求问清楚；理念已进我的参谋模式与 local-questioning，但他原版的 "grill" 一词我不用。 |
| [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) | 未用 · 想吸收 | ★★★★☆ | 约 110 万安装：结合项目文档深度追问，统一术语、当场记录决策；最想吸收的一个，与 doc-impact-checklist、future-goes-to-doc 天然合流。 |
| [handoff](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md) | 未用 · 想吸收 | ★★★★☆ | 约 95.4 万安装：把当前进度与上下文整理成 Markdown 交接文档；长会话/跨设备接续都用得上，交接里点名下一个会话该用的 skill 是它的好设计。 |
| [agent-browser](https://github.com/vercel-labs/agent-browser) | 未用 · 已有等价物 | ★★★☆☆ | 约 110 万安装：AI 操作浏览器（开网页、点击、填表、读页面）；我的浏览器委派能力是托管版等价物，带登录态。 |

## 三、热门 Skills：工程实践

| Skill | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) | 未用 · 半吸收 | ★★★☆☆ | 约 110 万安装：测试驱动，先写失败测试再实现；全套未必合身，只想吸收"新功能先写验收脚本再实现"与 seams 确认、反同义反复自查。 |
| [improve-codebase-architecture](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md) | 未用 · 想吸收 | ★★★★☆ | 约 110 万安装：检查代码库架构，找出可优化的模块；两个 repo 都到了需要定期架构体检的体量，Deletion test（删掉它，复杂度是被浓缩还是搬家）是好问题。 |
| [setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md) | 未用 · 不采用 | ★★☆☆☆ | 约 97.4 万安装：初始化整套 Matt Pocock 工程工作流；我已有自己的 AGENTS 体系，不被接管，略过。 |
| [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | 未用 · 暂无落点 | ★★★☆☆ | 约 96.9 万安装：Anthropic 官方前端设计 skill，减少模板化 UI；质量不差，但站点是 Markdown 静态站、图有 diagram-design，暂无落点，备查。 |
| [triage](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md) | 未用 · 等量上来 | ★★★☆☆ | 约 91.7 万安装：GitHub Issues 自动分类；邮件分诊已在用，issue 分诊等 open-memex issue 量上来再说。 |

---

*补充规则：进表与出表都由我定；参考不直装，吸收重写自维护（2026-10-14 原则）；只写用后感或试后感，不转述官网文案。榜单安装量为 Ethan 帖子口径（2026-10-21），不是实时数。*
