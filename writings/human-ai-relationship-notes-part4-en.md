# Part Four: Outside Input — Cases and Readings

*Cases and articles I've read, distilled, with source links.*

*[中文版](./human-ai-relationship-notes-part4.md)*

[← Back to index](./human-ai-relationship-notes-en.md)

---

## 17. The neo-feudal layering of the AI era (one person's take: pretty framework, dubious predictions) (2026-10-15)

From rick awsb's long post. He argues AI society will be neither Hayekian utopia nor digital Leviathan, but an inverted pyramid of "neo-feudal layering": compute and energy monopolized by "digital lords" at the top, middle-class knowledge intermediaries collapsing into AI-leveraged micro-teams in the middle, and the bottom degrading into tribal society on zero-cost AI content.
Source: https://x.com/rickawsb/status/2110464793467584996

Three things genuinely worth keeping:

- **"Prosperity without pricing power"**: AI-amplified individuals and micro-teams see efficiency explode, but the surplus flows back to the top as API fees and cloud rent — the amplifier itself charges "digital rent."
- **The middle-collapse list** (legal compliance, junior finance analysis, routine software outsourcing, middle management): the macro version of point 14's "grunt work gets skipped" — what's being skipped isn't just a learning process, it's an entire employment class.
- **Cognitive environment decay at the bottom**: zero-cost hyper-realistic content dissolves the shared factual base — the societal-scale version of point 16's "AI lies."

Two doubts:

- "Digital lords" may overstate how inevitable concentration is — open source, distillation, and local small models keep tearing down the wall (open-memex's local-first is exactly that direction). The mainframe era also predicted centralized computing; then came the PC revolution.
- Straight-line extrapolations like "high walls in 1–3 years, hard landing in 3–7" have a reliably terrible track record.

---

## 18. Ambition in four measures: Rieseberg's driver's manual (2026-10-15)


From Felix Rieseberg (Anthropic, works on Claude), "How to be more ambitious: A tutorial for humans with models."
Source: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

He sorts ambition with AI into four measures: Speed (doing the same work faster — skipped), Altitude (abstraction level: from "fix this crash" up to "keep the app crash-free" — ask "what's the goal beyond the goal"), Depth (field-expert depth: use the tools and methods of the top practitioners, until even the experts learn something), Range (cross-field: assemble a crew — analyst + journalist + editor + a red team of short sellers and forensic accountants — and have the model *do* what they do, not *play* them).

How it connects to these notes:

- The piece is essentially a "driver's manual" — Altitude maps to point 3's "intent and direction," Depth to "keep your craft sharp," Range to think tank review. My notes are the Chinese practitioner's edition; his is the English methodology edition.
- The Depth chapter says it outright: "Use an outside judge — don't let the model judge itself." Points 4 and 5's "use another AI to review" is industry-consensus methodology by now.
- "Insist on the same instruments used by the best": asked to "act like an expert," models often change vocabulary without changing methods — talks like a data scientist, hands you a markdown table. Echoes point 5: pretty form isn't real method. The person reading the board (point 15) has to check what pieces are being played with.
- The closing psychology bit, self-efficacy: people who believe they can do it really do more; "watching someone do it first" (the four-minute mile was matched 46 days later), "not knowing it's impossible" (Dantzig turned unsolved problems into homework). The counterpoint to point 14: the learning process really does get skipped — but AI also smashed the threshold for "daring to think big."

Two doubts: the author works on Claude, so "models keep reaching higher abstraction levels" is partly selling his own product; the examples all assume data access and engineering infrastructure, a high bar for ordinary people. And Speed gets skipped — yet in reality 90% of people only ever use Speed. Ambition itself is pyramid-distributed.

---

---

## 22. AI native isn't using AI — it's assuming AI is in the room (2026-10-16)


Reflections on a long post by Kafka (@kafkaup). He argues "AI native" is becoming marketing fluff — just as cloud native isn't "moving software to the cloud," true AI native means redesigning products, workflows, and problem-solving around AI from the start.
Source: https://x.com/kafkaup/status/2110860521008206107

His litmus test: your first reaction to a problem shifts from "how do I do this?" to "which part of this can AI take?" Plus the distinction between AI first (ask whether an AI tool fits) and AI native (the workflow assumes AI participation by default).

How it connects to these notes:

- That distinction reflects back on me: I say "go," and everything else — cost estimate, execution, verification, wrap-up — lives with 小沐; I only judge and decide. That's no longer "using an AI tool" — it's treating AI as the default execution layer. AI native isn't an attitude; it's the shape of the workflow.
- His section on "AI-friendly information formats" (natural language for intent, Markdown for shared reading, JSON/Schema for structure transfer, MCP for AI execution) reads like open-memex's design doc: to make AI work reliably, first arrange information into shapes it digests well.
- "The essence of context engineering is letting AI live inside your environment, not carrying context into the chat box yourself" — that's exactly what open-memex does, except he approaches it from workflow and I from infrastructure.

One correction (Stone's own words, 2026-10-16): the "only step in on disagreement" framing above isn't right. The accurate version: after the AIs have reviewed each other, I still make the final call. AI review is a means to improve input quality; decision authority stays with the human — not "intervene on disagreement" but "reviewed, then I decide." That's a level above "human as QA": QA is passive gatekeeping; making the call is active ownership.

---

## 25. A six-stage framework for agent memory: ask why memory is needed first (2026-10-16)


Reflections on a long post by Kafka (@kafkaup). He argues that before choosing tech (vector DB, graph DB, stuffing chat history), one should ask why the agent needs memory at all: experience continuity, efficiency, personalization, long-term task tracking, business moat. Memory's core value is continuity across long-term interaction, not remembering everything.
Source: https://x.com/kafkaup/status/2110812455488151766

His six stages: (1) decide what to remember (long-term value, structurability, personalization impact); (2) extract and classify (entity/relation/time/source/confidence; user preferences, business facts, process conclusions, task state, procedural memory); (3) staging, dedup, merge (avoid dirty data); (4) layered storage (session state for short-term, long-term store for preferences, vector DB for semantic search, graph DB for relationship-heavy business); (5) retrieval (when/what/how much to query; compress rather than stuff; weigh relevance, recency, source reliability, usage frequency, business importance); (6) dynamic maintenance (add, search, update, delete, reflection — otherwise memory becomes noise).

How it connects to these notes:

- open-memex covers nearly this entire framework — capture, aliases, lifecycle state machine, retrieval ablation — each stage has a corresponding implementation. Not chasing the hotspot; the homework was done months early.
- "Match complexity to business need" is the most valuable line: it's the theoretical backing for the "no embeddings by default" bet — lexical + synonyms suffice for most cases, embeddings only as opt-in for clear gaps like cross-lingual.
- Zipeng Wu's sharp question in the replies (how to rank when usage frequency conflicts with business importance? A deadline mentioned once shouldn't be crowded out by daily preferences) — that's exactly what D77 feedback-weighted ranking addresses. The question arrived before the implementation, but the answer is already on the way.
- Of his four criteria for good memory (accurate, correct retrieval, useful, deletable), "deletable" is the most overlooked. open-memex's forget/supersede chain and the hard rule that retracted memories can't silently return to active (D64) make deletability a hard constraint — something most memory projects don't do, and a differentiator worth naming.

---

## 26. Four habits of Vibe Coding: models are commodities, harness is the moat (2026-10-16)


Reflections on a long post by Kxians (@xulijian1994). His thesis: after long use of Vibe Coding, what most affects efficiency isn't how strong the model is, but one's own habits. Four of them: (1) don't reinvent the wheel — have AI search GitHub for mature solutions first; (2) rotate conversation windows — one endless chat leads to compression amnesia and goal drift; switch after 2–3 independent features, prerequisite being docs + persistent memory; (3) don't let AI blindly read whole files — search keywords/directories first, read only what's relevant; (4) periodically "distill" history (he calls this the most valuable) — have AI analyze conversation history, turn frequent tasks into Skills, write recurring mistakes into AGENTS.md, crystallize experience into conventions.
Source: https://x.com/xulijian1994/status/2110615259979649507

How it connects to these notes:

- Habit 4 is the Chinese version of "fix it into the harness" — except others treat it as advice, while I land it the same night I'm corrected. AGENTS.md, scripts, skills: that's the moat being dug.
- A reply worth noting (chaim chen, on habit 2): handoff docs shouldn't become walls of summary — keep four items: current goal, confirmed conclusions, unresolved errors, how to verify next steps. Compaction summaries should learn this: not the fuller the better, but the more "pick-up-able" the better.
- Habit 1 maps to Karpathy's second principle, "simple first, check if it already exists" — wild experience and Karpathy's principles growing into each other.
- His sharpest closing line: "Everyone can use the models, but the workflows each person accumulates will diverge more and more."

---

## 27. The shorter the principle, the smarter the model must be: pstack's "engineering principles" compression (2026-10-16)


Reflections on a post by meng shao (@shao__meng) relaying poteto (author of pstack, Cursor's official plugin). Core insight: the stronger the model, the more agent instructions should compress from "lengthy procedures" into "short, named principles" — each 10–20 lines, distilled good practice, not workflow scripts.
Source: https://x.com/shao__meng/status/2110976920343171542

Four key mechanisms: (1) principles are ultra-mini skills; poteto expects most skills to eventually compress into short principles or be deleted; (2) /poteto-mode has the agent read a principle index before multi-step tasks, then name which principle shaped which decision ("Principles Named or Used") — citing a principle with no corresponding decision is name-dropping, making reasoning checkable; (3) principles come from real corrections — "structured sediment of lessons" from her sessions correcting agents this year; (4) principles are individually invocable (/principle-<name>) or usable as steering shorthand.

Uncle Bob's endorsement: pstack recodes classic engineering wisdom (minimal changes, subtract before you add, verify root cause, make illegal states unrepresentable, idempotence) for AI agents.

How it connects to these notes:

- "Structured sediment of lessons" is "fix it into the harness" — the "(caught on 2026-10-15…)" annotations in my AGENTS.md are the same thing. She productized it; mine is a private config.
- The compression direction validates the A/B split: section A (principles) the shorter and harder the better; section B (implementations) the more concrete the better. Principles are for smart models; implementations are for dumb environments.
- "Agent-ifying old wisdom" is a rich vein: Karpathy's four principles, Uncle Bob's list — each translatable into a 10–20 line skill.

One honest doubt (from @DistillX_AI in the replies): the shorter the principle, the more it demands of the model's comprehension — compression assumes a smart enough model. That's a condition, not an unconditional truth.
