# 27. 原则越短，模型越要聪明：pstack 的"工程原则"压缩（2026-10-16）

[← 返回目录](./index.md) · [English Version](./27-the-shorter-the-principle-the-smarter-the-model-must-be-en.md)

---

读邵猛（@shao__meng）转述 poteto（Cursor 官方插件 pstack 作者）的长推有感。核心洞察：模型越强，给 agent 的指令越该从"冗长的步骤"压缩成"短的、有名字的原则"——每条 10-20 行，是蒸馏出的好实践，不是工作流脚本。
原文：https://x.com/shao__meng/status/2110976920343171542

关键机制有四：①原则是超 mini skill，poteto 预期大部分 skill 最终压缩成短原则或被删掉；②/poteto-mode 让 agent 在多步任务前先读原则索引，事后必须点名"哪条原则影响了哪个决策"（Principles Named or Used），引用无决策=挂羊头卖狗肉，推理可检查；③原则来自真实纠正——她今年纠正 agent 的会话里沉淀出来的"结构化教训"；④原则可单独调用（/principle-<name>），也可当转向 shorthand（"subtract before you add" 直接让 agent 先删过期 adapter）。

Uncle Bob 背书：pstack 是把经典工程智慧（最小改动、先减后加、验证根因、非法状态不可表示、幂等）重编码给 AI agent。

与随笔的咬合：

- "structured sediment of lessons"就是"修进 harness"——AGENTS.md 每条后的"（2026-10-15 抓包…）"是同一个东西。她产品化了，我的是私房配置。
- 压缩方向验证 A/B 拆分：A（原则）越短越硬，B（实现）越具体越好。原则给聪明模型看，实现给笨环境看。
- "老智慧的 agent 化转译"是个富矿：Karpathy 四原则、Uncle Bob 清单，逐条转成 10-20 行 skill。

一处存疑（评论区 @DistillX_AI）：原则越短，对模型理解力要求越高——压缩的前提是模型够聪明，这是条件不是无条件真理。
