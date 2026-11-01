# 22. AI native 不是用 AI，而是默认 AI 在场（2026-10-16）

[← 返回目录](./index.md) · [English Version](./22-ai-native-isn-t-using-ai-it-s-assuming-ai-is-in-the-room-en.md)

---

读卡夫卡（@kafkaup）长推有感。他认为 "AI native" 正在变成营销词——就像 cloud native 不是"把软件搬上云"，真正的 AI native 是从一开始就围绕 AI 重新设计产品、流程和解题方式。
原文：https://x.com/kafkaup/status/2110860521008206107

他给的试金石：遇到问题时第一反应从"我怎么做"变成"这件事里 AI 能接哪段"。以及 AI first（先问 AI 工具合不合适）vs AI native（流程默认 AI 参与）的区分。

与随笔的咬合：

- 这个区分照到我自己：我说"去"，剩下的 estimate、执行、验证、收尾全在小沐那，我只做判断和拍板——这已经不是"用 AI 工具"，是把 AI 当默认执行层。AI native 不是态度，是工作流的形状。
- "AI-friendly 的信息格式"那段（自然语言表意图、Markdown 共读、JSON/Schema 传结构、MCP 给 AI 执行）几乎就是 open-memex 的设计文档：想让 AI 可靠干活，先把信息摆成它好消化的形状。
- "context engineering 的本质是让 AI 住进你的环境，而不是你把上下文搬进聊天框"——open-memex 干的正是这个，只不过他从 workflow 角度谈，我从 infrastructure 角度做。

一处纠正（Stone 2026-10-16 亲口）：上面"只在分歧处介入"写得不对。准确的说法是——AI 互相审完之后，最后的结果还是我来拍板。AI 评审是提高输入质量的手段，拍板权始终在人手里，不是"分歧才介入"，是"审完我定"。这比"人当质检员"高一层：质检员是被动把关，拍板是主动担责。
