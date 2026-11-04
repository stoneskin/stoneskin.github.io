# AI 工具箱

[← 返回首页](../../index.md)

*2026-11-04 · [English Version](./index-en.md)*

只收我用过、认真评估过、或热门到值得知道的 AI 工具。**使用强度与评价分开算**：使用强度是我的实际用量，评价是推荐度——没用过的按口碑与公开资料给分，不是实测。★★★★★ 强烈推荐，★★★★☆ 值得用/试，★★★☆☆ 可以看看，★★☆☆☆ 评估过、没采用。每类最多 5 个完整条目，多出的放“其他”一行，只列名字。持续补充中，v4 共 21 项，另有 6 项列在“其他”。Skills 单独一页：[AI Skills](./skills.md)。

## 一、代码理解与图谱

| 工具 | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 未用 · 热门想试 | ★★★☆☆ | 90k stars 的代码知识图谱插件，Tree-sitter + LLM 建图；适合刚接手大仓先看图再读码。 |
| [Graphify（thinktank 内）](https://github.com/stoneskin/muse-thinktank) | 常用 | ★★★★☆ | thinktank 自带 curated 图谱，1,029 节点 / 1,701 边 / 61 社群；改动牵连一目了然。 |

## 二、多模型与多 Agent 编排

| 工具 | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [muse-thinktank](https://github.com/stoneskin/muse-thinktank) | 每天在用 | ★★★★★ | 一题发 N 模型，双裁判交叉验证合成 verdict；模型间分歧本身就是信号。 |
| [model-fuse](https://github.com/stoneskin/model-fuse-private) | 在研 | ★★★☆☆ | 自研 opencode 插件（私有仓），一题多模型、汇总取最优；D10/D11 已定方向，与 Copilot Fusion 机制不同。 |
| GitHub Copilot Fusion | 评估过未采用 | ★★☆☆☆ | D10 对抗评审约等于 Critique、D11 verdict 与 Cascade 质量门机制不同，不能等同。 |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 未用 · 热门想试 | ★★★★☆ | 图编排框架，状态机式 agent 流程是生产级样本；与 Meta Thin Orchestrator 同类思路，可对照读。 |
| [AutoGen](https://github.com/microsoft/autogen) | 未用 · 热门想试 | ★★★☆☆ | 微软多 agent 框架，对话式 agent 编排的代表；概念上可与 thinktank 的陪审团评审对照，但定位不同。 |

## 三、记忆与知识

| 工具 | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [open-memex](https://github.com/stoneskin/open-memex) | 每天在用 | ★★★★★ | 本地优先记忆层，Markdown 为真源，SQLite FTS5，MCP + CLI；npm 0.8.2。 |
| [Mem0](https://github.com/mem0ai/mem0) | 未用 · 热门想试 | ★★★☆☆ | 给 agent 用的记忆层，号称可插拔的长期记忆；与 open-memex 同赛道，设计上可以对照借鉴。 |

## 四、AI 编程助手

| 工具 | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [Claude Code](https://claude.com/product/claude-code) | 未用过 | ★★★★★ | Understand-Anything 等插件的原生宿主；业界口碑最好的 coding agent 之一。 |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot) | 常用 | ★★★★☆ | 公司批准的 AI 编程 CLI；可作 agent 执行后端，走 AgentAdapter 调用。 |
| [OpenCode](https://github.com/opencode-ai/opencode) | 每天在用 | ★★★★☆ | 开源 AI 编程 CLI；与 GitHub Copilot CLI 定位相近，可互换。 |
| [Cursor](https://www.cursor.com) | 用过 | ★★★★☆ | 最火的 AI 编辑器，补全 + agent 模式一体。 |
| [Codex](https://github.com/openai/codex) | 未用 · 热门想试 | ★★★★☆ | OpenAI 的 coding agent，CLI + 云端并行；与 Claude Code 同赛道。 |

其他：Gemini CLI、Cline、RooCode、VSCode、Antigravity、Aider（Gemini CLI、Cline、RooCode、VSCode、Antigravity 用过；只列名字，无评价）

## 五、Agent 框架与运行时

| 工具 | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [DeepSeek Harness (dsh)](https://github.com/deepseek-ai/deepseek-harness) | 评估过（借鉴） | ★★★☆☆ | v0.2.2-alpha.2，插件化微内核 agent 运行时；亮点在 skill 懒加载、flow skills、“模型可见即记入日志”。 |
| [LangChain](https://github.com/langchain-ai/langchain) | 未用 · 热门想试 | ★★★★☆ | 最老牌的 agent 开发框架，生态最全；新项目一般不从它起手。 |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 未用 · 热门想试 | ★★★☆☆ | 角色化多 agent 编排（Role + Task + Crew），上手比 AutoGen 直观；小团队做多 agent 原型可参考。 |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 未用 · 热门想试 | ★★★☆☆ | OpenAI 官方轻量 agent SDK。 |
| [Pi](https://github.com/badlogic/pi) | 未用 · 个人项目 | ★★★★☆ | 117k stars 的最薄 agent harness：内核只连模型/工具/持久化，刻意不做权限/Plan mode/Sub-agents；不少 FDE 直接拿它当 harness 用。 |

## 六、投资分析

| 工具 | 使用强度 | 评价 | 点评 |
|---|---|---|---|
| [moomoo OpenD](https://www.moomoo.com) | 常用 | ★★★★☆ | 行情 + 模拟交易唯一真 API；1024 位 RSA 加密握手，笔记本监听 0.0.0.0 走 Tailscale。 |
| [tt/stock_context.py](https://github.com/stoneskin/muse-thinktank) | 常用 | ★★★★☆ | 自研（thinktank 内）：投资分析前先拉技术面数据，每个数字有来源。 |

---

*补充规则：进表与出表都由我定；新工具先用过、认真评估过、或是热门到值得知道再进表；点评从中立角度评价工具本身，不转述官网文案；自研工具须有 repo 链接才进表，第三方 AI 不进表。想让我试哪个，发我链接。*
