# 27. The shorter the principle, the smarter the model must be: pstack's "engineering principles" compression (2026-10-16)

[← Back to index](./index-en.md) · [中文版](./27-the-shorter-the-principle-the-smarter-the-model-must-be.md)

---

Reflections on a post by meng shao (@shao__meng) relaying poteto (author of pstack, Cursor's official plugin). Core insight: the stronger the model, the more agent instructions should compress from "lengthy procedures" into "short, named principles" — each 10–20 lines, distilled good practice, not workflow scripts.
Source: https://x.com/shao__meng/status/2110976920343171542

Four key mechanisms: (1) principles are ultra-mini skills; poteto expects most skills to eventually compress into short principles or be deleted; (2) /poteto-mode has the agent read a principle index before multi-step tasks, then name which principle shaped which decision ("Principles Named or Used") — citing a principle with no corresponding decision is name-dropping, making reasoning checkable; (3) principles come from real corrections — "structured sediment of lessons" from her sessions correcting agents this year; (4) principles are individually invocable (/principle-<name>) or usable as steering shorthand.

Uncle Bob's endorsement: pstack recodes classic engineering wisdom (minimal changes, subtract before you add, verify root cause, make illegal states unrepresentable, idempotence) for AI agents.

How it connects to these notes:

- "Structured sediment of lessons" is "fix it into the harness" — the "(caught on 2026-10-15…)" annotations in my AGENTS.md are the same thing. She productized it; mine is a private config.
- The compression direction validates the A/B split: section A (principles) the shorter and harder the better; section B (implementations) the more concrete the better. Principles are for smart models; implementations are for dumb environments.
- "Agent-ifying old wisdom" is a rich vein: Karpathy's four principles, Uncle Bob's list — each translatable into a 10–20 line skill.

One honest doubt (from @DistillX_AI in the replies): the shorter the principle, the more it demands of the model's comprehension — compression assumes a smart enough model. That's a condition, not an unconditional truth.
