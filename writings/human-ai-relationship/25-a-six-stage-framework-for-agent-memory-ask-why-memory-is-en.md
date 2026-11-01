# 25. A six-stage framework for agent memory: ask why memory is needed first (2026-10-16)

[← Back to index](./index-en.md) · [中文版](./25-a-six-stage-framework-for-agent-memory-ask-why-memory-is.md)

---

Reflections on a long post by Kafka (@kafkaup). He argues that before choosing tech (vector DB, graph DB, stuffing chat history), one should ask why the agent needs memory at all: experience continuity, efficiency, personalization, long-term task tracking, business moat. Memory's core value is continuity across long-term interaction, not remembering everything.
Source: https://x.com/kafkaup/status/2110812455488151766

His six stages: (1) decide what to remember (long-term value, structurability, personalization impact); (2) extract and classify (entity/relation/time/source/confidence; user preferences, business facts, process conclusions, task state, procedural memory); (3) staging, dedup, merge (avoid dirty data); (4) layered storage (session state for short-term, long-term store for preferences, vector DB for semantic search, graph DB for relationship-heavy business); (5) retrieval (when/what/how much to query; compress rather than stuff; weigh relevance, recency, source reliability, usage frequency, business importance); (6) dynamic maintenance (add, search, update, delete, reflection — otherwise memory becomes noise).

How it connects to these notes:

- open-memex covers nearly this entire framework — capture, aliases, lifecycle state machine, retrieval ablation — each stage has a corresponding implementation. Not chasing the hotspot; the homework was done months early.
- "Match complexity to business need" is the most valuable line: it's the theoretical backing for the "no embeddings by default" bet — lexical + synonyms suffice for most cases, embeddings only as opt-in for clear gaps like cross-lingual.
- Zipeng Wu's sharp question in the replies (how to rank when usage frequency conflicts with business importance? A deadline mentioned once shouldn't be crowded out by daily preferences) — that's exactly what D77 feedback-weighted ranking addresses. The question arrived before the implementation, but the answer is already on the way.
- Of his four criteria for good memory (accurate, correct retrieval, useful, deletable), "deletable" is the most overlooked. open-memex's forget/supersede chain and the hard rule that retracted memories can't silently return to active (D64) make deletability a hard constraint — something most memory projects don't do, and a differentiator worth naming.
