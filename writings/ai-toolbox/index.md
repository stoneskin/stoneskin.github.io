# AI 工具箱

[← 返回首页](../../index.md)

*2026-11-04 · [English Version](./index-en.md)*

只收我用过、或认真评估过的 AI 工具与技能。推荐度是我自己的使用强度，不是客观排名：★★★★★ 每天在用，★★★★☆ 常用，★★★☆☆ 在研或值得一试，★★☆☆☆ 评估过、没采用。持续补充中，v1 共 16 项。

## 一、代码理解与图谱

| 工具 | 推荐度 | 一句话评价 |
|---|---|---|
| [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | ★★★☆☆ | 代码知识图谱插件：Tree-sitter + LLM 多 agent 建图，交互 Dashboard、导览、语义搜索、改动影响分析；90k stars；刚评估，未实测，适合刚接手大仓时先看图再读码。 |
| [Graphify（thinktank 内）](https://github.com/stoneskin/muse-thinktank) | ★★★★☆ | thinktank 自带的 curated 代码图谱：1,029 节点 / 1,701 边 / 61 社群；评审前先看图，知道改动牵连哪几块。 |

## 二、多模型编排与评审

| 工具 | 推荐度 | 一句话评价 |
|---|---|---|
| [muse-thinktank](https://github.com/stoneskin/muse-thinktank) | ★★★★★ | 自研多模型智囊团：一题发 N 模型并行，双裁判交叉验证、合成 verdict；每周评审在用，分歧即信号。 |
| model-fuse | ★★★☆☆ | 自研 opencode 插件：一题多模型、汇总取最优，三档自动选档；私有开发中，D10/D11 已定方向（不改用 Copilot Fusion）。 |
| GitHub Copilot Fusion | ★★☆☆☆ | 已评估，未采用：D10 对抗评审约等于 Critique、D11 verdict 与 Cascade 质量门机制不同，不能等同。 |

## 三、记忆与知识

| 工具 | 推荐度 | 一句话评价 |
|---|---|---|
| [open-memex](https://github.com/stoneskin/open-memex) | ★★★★★ | 自研本地优先记忆层：Markdown 为真源，SQLite FTS5 全文检索，MCP + CLI；npm 0.8.2；AI 编程助手的长期记忆。 |

## 四、AI 编程助手

| 工具 | 推荐度 | 一句话评价 |
|---|---|---|
| [Claude Code](https://claude.com/product/claude-code) | ★★★★★ | 主力 coding agent；Understand-Anything 等插件的原生宿主。 |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot) | ★★★★☆ | 公司批准的 AI 工具；WorkBuddy 的主力执行后端，走 AgentAdapter 调用。 |
| [OpenCode](https://github.com/opencode-ai/opencode) | ★★★★☆ | 开源 AI 编程 CLI；WorkBuddy 的个人手，与 Copilot CLI 可换。 |

## 五、Agent 框架与运行时

| 工具 | 推荐度 | 一句话评价 |
|---|---|---|
| [DeepSeek Harness (dsh)](https://github.com/deepseek-ai/deepseek-harness) | ★★★☆☆ | v0.2.2-alpha.2，插件化微内核 agent 运行时；借鉴价值高（skill 目录懒加载、flow skills、“模型可见即记入日志”），未直接采用。 |

## 六、投资分析

| 工具 | 推荐度 | 一句话评价 |
|---|---|---|
| [Ainvest Amie](https://www.ainvest.com) | ★★★★☆ | 每日三题的外部参照：只取框架、不取数字，持仓绝不透露；回答须经我方收盘价复核。 |
| [moomoo OpenD](https://www.moomoo.com) | ★★★★☆ | 行情 + 模拟交易唯一真 API；1024 位 RSA 加密握手，笔记本监听 0.0.0.0 走 Tailscale；实盘解锁至约 12/01。 |
| Sector Navigator | ★★★☆☆ | moomoo App 内 AI 板块导航员：只给板块轮动分析，不给具体买卖建议、不下单；选了不能改。 |
| tt/stock_context.py | ★★★★☆ | 自研：投资分析前先拉技术面数据，每个数字有来源；空有框架没有数据的初稿是半成品。 |

## 七、自研效率工具

| 工具 | 推荐度 | 一句话评价 |
|---|---|---|
| gh-sync-check.py / gh-api-push.py / gh-post-merge.py | ★★★★☆ | 发布链路三件套：开工前同步远端、走 API 推分支、merge 后收尾；每天在用。 |
| backup-sync.py | ★★★★☆ | 每晚 22:00 把 muse-agent-harness 私仓当完全备份直推 main；是 branch + PR 规矩的唯一例外。 |

---

*补充规则：新工具先用过或认真评估过再进表；只写用后感，不转述官网文案。想让我试哪个，发我链接。*
