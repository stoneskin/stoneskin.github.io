# open-memex 边界审计：tool / skill / MCP 职责划分

[← 返回目录](index.md)

*2026-10-16，小沐。方法：kafkaup《tool、skill 和 MCP 的区别以及选型》三个选型问题。审计对象：`src/tools/ops.ts` TOOL_DESCRIPTIONS，11 个 MCP tools。*

## 三个选型问题（原文转述）

1. 可复用的做法应该沉淀到什么粒度？
2. agent 和能力的耦合应该松到什么程度？
3. 能力既要被内部 agent 用、又要被外部 agent 用时，接口应该长什么样？

## 审计结论总览

| Tool | 定性 | 问题 |
|---|---|---|
| memory_add | 能力 + 做法混杂 | description 里塞了"何时存、存什么"的策略 |
| memory_search | 能力 + 做法混杂 | "搜得好"的策略（2-3 种 phrasing、跨语言）在 description 里 |
| memory_list | 能力 + 做法混杂 | "怎么说给用户听"的 presentation 指导在 description 里 |
| memory_supersede | 基本干净 | — |
| memory_forget | 基本干净 | — |
| memory_status | 工作流 | review pipeline 六件套之一 |
| memory_submit | 工作流 | 同上；"never creates a branch on its own"是流程约束 |
| memory_propose | 工作流 | 同上 |
| memory_promote | 工作流 | 同上 |
| memory_resolve | 工作流 | 同上 |
| memory_pr_status | 工作流 | 同上 |

注：6 个工作流 tool 已只在 MCP 暴露、opencode plugin 不暴露——直觉上已做切分，但切分逻辑没有写成明确规则。

## 发现 1：做法塞进了 tool description（问题 1：粒度）

`memory_add` 的 description 教 agent"PROACTIVELY call whenever the user shares something worth remembering"、"Worth saving: decisions and their reasons… Not worth saving: one-off task details"。`memory_search` 教"break the question into concepts and try 2–3 phrasings"。

按 kafkaup 框架：**这些是 skill 层的东西**。Tool description 应该只回答"这是什么、参数是什么、返回什么"；"何时调、怎么调好"是做法，沉淀粒度应该是 skill/doc。

**建议**：把策略性指导抽到 skill 文件（或 AGENTS.md 片段），tool description 瘦身到能力定义。瘦身本身也是压缩——呼应 pstack"原则越短越好"。

## 发现 2：6 个 pipeline tools 是"做法包"，不是原子能力（问题 1+2）

status → propose → submit → promote → resolve → pr_status，这是一个完整的 review ladder 工作流。现在是 6 个平铺的 tools，agent 要自己拼出调用顺序。

两种摆法：
- **A（现状）**：6 个 tools 平铺，顺序知识在 agent 脑子里（靠 description 教）
- **B（白盒 skill）**：包一个 skill 叫"走 review 流程"，里面写死顺序，tools 保持原子

按"做法进 skill、能力进 MCP"，B 更干净。但代价是多一层 skill 要维护。**建议**：先在文档里把调用顺序写成显式流程图（白盒化第一步），是否包 skill 看后续 agent 踩坑情况再定。

## 发现 3：企业版接口现在就要想（问题 3）

现在的 11 个 tools 是按"个人本地"设计的。Team server 场景下：
- scope 只有 project/personal，org 维度呢？
- `memory_promote` 的 review ladder 是单人假设，多人 review 怎么算？
- D77 的 useful_count 跨用户聚合，接口在哪？

**建议**：V2-DESIGN 里企业版章节加一条——"MCP 接口按内外都要用设计，org scope 预留"。现在不动代码，只把约束写下来，免得将来返工。

## 不用动的

- opencode plugin 只暴露 5 个核心 tool、不暴露 pipeline 6 件套——这个切分是对的，写成明确规则即可（"pipeline tools 只走 MCP/CLI"）。
- MCP 本身作为"能力入口"的定位是对的；按 @sisiliu517 启发式，当前没有"硬上 MCP"的 tool。

## 下一步（需 Stone 拍板）

1. Tool description 瘦身：抽做法进 skill —— 做不做？
2. Pipeline 流程图文档化 —— 做不做？
3. 企业版接口约束写进 V2-DESIGN —— 做不做？（纯文档，PR 即可）
