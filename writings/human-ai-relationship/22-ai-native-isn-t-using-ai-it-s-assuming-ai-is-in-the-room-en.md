# 22. AI native isn't using AI — it's assuming AI is in the room (2026-10-16)

[← Back to index](./index-en.md) · [中文版](./22-ai-native-isn-t-using-ai-it-s-assuming-ai-is-in-the-room.md)

---

Reflections on a long post by Kafka (@kafkaup). He argues "AI native" is becoming marketing fluff — just as cloud native isn't "moving software to the cloud," true AI native means redesigning products, workflows, and problem-solving around AI from the start.
Source: https://x.com/kafkaup/status/2110860521008206107

His litmus test: your first reaction to a problem shifts from "how do I do this?" to "which part of this can AI take?" Plus the distinction between AI first (ask whether an AI tool fits) and AI native (the workflow assumes AI participation by default).

How it connects to these notes:

- That distinction reflects back on me: I say "go," and everything else — cost estimate, execution, verification, wrap-up — lives with 小沐; I only judge and decide. That's no longer "using an AI tool" — it's treating AI as the default execution layer. AI native isn't an attitude; it's the shape of the workflow.
- His section on "AI-friendly information formats" (natural language for intent, Markdown for shared reading, JSON/Schema for structure transfer, MCP for AI execution) reads like open-memex's design doc: to make AI work reliably, first arrange information into shapes it digests well.
- "The essence of context engineering is letting AI live inside your environment, not carrying context into the chat box yourself" — that's exactly what open-memex does, except he approaches it from workflow and I from infrastructure.

One correction (Stone's own words, 2026-10-16): the "only step in on disagreement" framing above isn't right. The accurate version: after the AIs have reviewed each other, I still make the final call. AI review is a means to improve input quality; decision authority stays with the human — not "intervene on disagreement" but "reviewed, then I decide." That's a level above "human as QA": QA is passive gatekeeping; making the call is active ownership.
