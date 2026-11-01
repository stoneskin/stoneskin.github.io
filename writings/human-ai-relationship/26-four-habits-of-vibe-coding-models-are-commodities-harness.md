# 26. Vibe Coding 的四个习惯：模型是公共品，harness 是护城河（2026-10-16）

[← 返回目录](./index.md) · [English Version](./26-four-habits-of-vibe-coding-models-are-commodities-harness-en.md)

---

读 Kxians（@xulijian1994）长推有感。他的论点：Vibe Coding 玩久了，真正影响效率的不是模型多强，而是自己的使用习惯。四条：①别重复造轮子——先让 AI 搜 GitHub 成熟方案；②定期换对话窗口——一个 chat 用到底会压缩失忆、偏离目标，2-3 个独立功能或几次压缩后就换，前提是文档+持久记忆；③别让 AI 无脑读整文件——先搜关键词/目录/索引，只读相关的，省 token 少污染；④定期"蒸馏"历史（他说最有价值）——让 AI 分析对话史，高频任务做成 Skill，常犯错误写进 AGENTS.md，经验结晶成项目约定。
原文：https://x.com/xulijian1994/status/2110615259979649507

与随笔的咬合：

- 第四条就是"修进 harness"的中文版——只不过别人是建议，我是被纠正一次当晚落地。AGENTS.md、脚本、skill，就是在挖这条河。
- 第二条的评论区补充（chaim chen）：交接文档别写成总结墙，只留四项——当前目标、已确认结论、未解决的报错、下一步怎么验证。compaction 摘要该学这个：摘要不是越全越好，是"接得上"才好。
- 第一条对应 Karpathy 第二条"简单优先，先查是不是已经有了"——野生的经验和 Karpathy 的原则长到一起去了。
- 他结尾最狠："模型大家都能用，但每个人积累出来的工作流，差距可能会越来越大。"
