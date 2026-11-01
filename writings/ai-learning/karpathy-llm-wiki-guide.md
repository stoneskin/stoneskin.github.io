# Karpathy《LLM Wiki》导读：把知识一次编译进 wiki，而不是每次重算

[← 返回目录](index.md)

> 来源（一手原文）：Andrej Karpathy《LLM Wiki》，GitHub Gist，2026-04-04，https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
> 详细摘要见 [karpathy-llm-wiki-summary.md](./karpathy-llm-wiki-summary.md)；本篇是导读（为什么值得看、主线、怎么读）。
> 背景：Karpathy 2026-04-03 先发推"LLM Knowledge Bases"，次日贴出这份 gist。他称之为 idea file——不是代码，是拿去贴给自己的 agent 的想法文件；48 小时内 5,000+ stars。

## 一句话结论

RAG 每次都从头找答案、不积累；LLM Wiki 让 LLM 把知识一次编译进一个持久的、互相链接的 markdown wiki，越用越富，而不是每次重算。

## 为什么值得看

- **换了一个问题**：大家都在优化"怎么找得更准"（更好的检索、更好的 embedding），Karpathy 换成了"怎么让知识积累下来"。检索是索引，wiki 是蒸馏——这是整篇文章的区分点，也是它值得看的原因。
- **短，而且能直接用**：全文 174 行，没有代码，只有一个想法 + 三层 + 三个操作。它是 idea file——你把它贴给自己的 agent，agent 帮你实例化一个适合你的版本。
- **跟你的三件事都对得上**：open-memex（编译式记忆、边带出处）、本地文件组织（lib 与工作区本身就是一套 wiki）、WorkBuddy 的 AI harness（schema 文件就是 harness 的纪律）。这篇是三件事共用的地基。
- **有来头**：Karpathy 自己点名这是 Vannevar Bush 1945 年 Memex 的精神后继——私人、精选、靠关联组织知识；Bush 解决不了"谁来维护"，LLM 解决了。

## 叙事主线

1. RAG 的毛病：每次提问都从头拼碎片，不积累；问一个要综合五份文档的问题，LLM 每次都得重新找、重新拼。
2. 换成编译：LLM 增量地建一个持久 wiki，夹在你和原始资料之间；新资料进来，它读、抽、合进已有页面、标出与旧结论的矛盾，综合随之进化。
3. 三层 + 三操作：raw（不可改的原文）/ wiki（LLM 写的 markdown）/ schema（告诉 LLM 怎么维护的纪律文件）；ingest（吃进新资料）、query（对着 wiki 问，好的答案也存回 wiki）、lint（定期体检：矛盾、过期、孤页、缺页）。
4. 规模化：index.md（目录，先读它再钻进去）+ log.md（时间线，可 grep）；~100 份资料、几百页的规模下，index 就够用，不用 embedding；再大就上本地搜索（qmd）。
5. 为什么能成：维护知识库最烦的不是读和想，是记账（更新交叉引用、保持摘要最新、标矛盾、保一致）。人会因为维护成本超过价值而放弃；LLM 不会烦，一次能改 15 个文件，维护成本近零。

> 摘要第 10 节：一个现成的实现 Graphify——这个模式在代码库上的落地（确定性解析、边带置信度、git hook 自动重建）。

## 怎么读（分级）

- 【摘要即可】——详细摘要已写到能独立成立（原理、三层、三操作、索引/日志、落地步骤都齐了），只看摘要就能学到精髓、跳过原文。
- 原文本身只有 174 行，写得干净；想看 Karpathy 原话（尤其是"Obsidian 是 IDE，LLM 是程序员，wiki 是代码库"那句）再对照原文。
- 读完摘要后值得动手的一步：挑一个最小的域（比如 open-memex 的一个子集，或 WorkBuddy 的一个模块），按摘要末尾的落地步骤搭一个三层 wiki 跑一周，看维护成本是不是真的近零。

## 跟你的咬合

- **open-memex**：wiki 层就是编译后的记忆；schema 就是 capture 规则；lint 就是校验 pass。Graphify（今早那篇）是这个模式在代码库上的一个现成实现——它建的图就是 wiki 的一种形态，边分 EXTRACTED/INFERRED 带置信度。
- **本地文件组织**：lib + 工作区已经是 wiki 的雏形（raw 是原文与记录，wiki 是总结与导读，schema 是 AGENTS.md 与 MEMORY.md）；缺的是 lint 那一步（定期体检：过期、孤页、矛盾）。
- **WorkBuddy harness**：harness 的规则导出 + CLAUDE.md/AGENTS.md 就是 schema 文件；.brain 文件夹（index/architecture/decisions/changelog/deployment）是这个模式在项目里的轻量变体。
