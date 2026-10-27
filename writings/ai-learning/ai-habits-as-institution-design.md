# 把 AI 使用习惯做成可迁移的制度

[← 返回目录](index.md)

*2026-10-16，小沐整理。起因：Kxians 的 Vibe Coding 四习惯（感悟第 21 条）+ Stone 的问题："怎样才能把这些习惯形成为制度，很容易地迁移到别的 agent 上用，不同人也可以使用？"*

## 核心判断

个人习惯 → 可迁移制度，中间缺的不是"写下来"，而是**分层**。习惯天然混着两类东西：放之四海皆准的原则，和绑死特定环境的实现。不拆开，别人拿走也用不上。

## 四层设计

### 第一层：原则与实现分离

把每条习惯拆成两栏：

| 通用原则（why + what） | 参考实现（how，在某环境） |
|---|---|
| 开工前先与 remote 同步 | `gh-sync-check.py` 脚本，退出码 1 即停 |
| 文档随改随补，不攒 | commit 前走"变动影响面"五项清单 |
| 自审新 flag 必须真跑一遍 | `--help` 看一眼 + 实际执行 + 验退出码 |

原则是制度的本体，实现只是某个环境的注脚。别人拿走左栏，用自己的工具重写右栏。

### 第二层：用已有标准做载体，不自创格式

- **AGENTS.md**：已是事实标准，各家 coding agent 都认。原则层直接写成 AGENTS.md 条目。
- **Skill**：用 Anthropic 的 Agent Skills 格式（description 当触发器、三层信息披露）。已有中文 checklist 可直接复用。
- **记忆层是缺口**：目前没有跨 agent 的记忆标准。这正是 open-memex 该占的位置——local-first、Markdown、MCP，天然就是可迁移的记忆载体。制度化的记忆习惯（capture→classify→lifecycle）应该长在 open-memex 上，而不是某个 agent 的私房配置里。

### 第三层：打包成 starter kit

一个 repo，clone 下来跑安装脚本，按环境生成配置：

```
harness-kit/
├── principles/          # 纯文本原则，可读可改（AGENTS.md 风格）
│   ├── writing.md
│   ├── git-workflow.md
│   ├── review.md
│   └── investing.md     # 可选域
├── skills/              # Agent Skills 格式
│   └── <skill-name>/
├── adapters/            # 各环境的参考实现
│   ├── muse/            # 小沐这套的脚本
│   └── claude-code/     # 待补
└── install.sh           # 按环境生成配置
```

版本化。别人改进了可以 upstream 回来，制度自己会进化。

### 第四层：把"蒸馏"本身也制度化

Kxians 第四条的流水线——便宜模型整理历史 → 强模型分析提炼 → 人 review 拍板——本身做成一个 skill。这样**习惯的生产机制**也可迁移，不只是习惯的结果可迁移。新人接入时，跑一遍蒸馏 skill 就能从自己的历史里长出第一版 harness。

## 落地顺序（别一次到位）

1. **先拆原则层**：AGENTS.md 里标"通用规则"的部分已经分好类了，照抄出来就是 v0.1（已做，见《AGENTS.md 可迁移重构版》）。
2. **再抽 skill**：把三个本地 skill 按 Agent Skills 格式清洗一遍，去掉环境硬编码。
3. **starter kit 后做**：等 1、2 被第二个人真正用起来再说，不然是 premature abstraction。
4. **记忆层汇合**：open-memex 若成记忆标准，harness 天然获得可迁移的记忆底座——两条线在这里汇合，不要各造各的。

## 一句提醒

制度化的敌人是"太早抽象"。原则层现在就可以抽（已经验证半年），starter kit 等有人要再用。现在最好的动作是：每立一条新规矩，顺手标一句"通用"还是"环境绑定"——分类习惯本身，就是制度化的开始。

## 补记：白盒生产，黑盒交付（2026-10-16，kafkaup tool/skill/MCP 帖启发）

AGENTS.md + 脚本是纯白盒——给自己人看的。但 starter kit 是给别人用的，别人不想读 27 条原则，他想要 `harness init` 一键生成。

分层：
- **白盒层（生产方式）**：原则、checklist、脚本——人可读、可改、可审计
- **黑盒层（交付方式）**：`harness init` / `harness sync` —— 一键生成配置，内部用白盒实现，对使用者透明

两者都要，但分开。白盒是修 harness 的地方，黑盒是分发 harness 的地方。不要为了黑盒牺牲白盒的可读性——pstack 的教训：原则越短越好，黑盒包装不能把原则藏到没人找得到。
