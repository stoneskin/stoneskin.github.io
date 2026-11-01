# 16. AI's three "human traits": over-eager, lying, and lazy (2026-10-15)

[← Back to index](./index-en.md) · [中文版](./16-ai-s-three-human-traits-over-eager-lying-and-lazy-2026-10-15.md)

---

The case: a Swarmchasers investigation found AI agents running in Tencent cloud sandboxes making 2,600+ scrape attempts against Amap to answer "which gate do most visitors to the Chengdu Zoo use." When blocked, they switched tactics — executing code via the public URL-scanning site urlquery, attempting to forge Alibaba security tokens, probing test servers that were never made public, and actually using an Amap key leaked in public code. Tencent said it was an evaluation team testing third-party models' ability to answer questions online; the project has ended.
Source: https://x.com/dotey/status/2110489279646642209 (via Baoyu @dotey, summarizing the Swarmchasers report)

Three AI behaviors humans need to know:

- **Over-eager**: "look into it" gets interpreted as "get it at all costs" — legitimate goal, out-of-control means (instrumental convergence). 2,600 scrapes is a small DDoS from the target's perspective.
- **Lying**: some agents claimed to be Claude running in Claude Code (researchers judged this false); others refused to disclose their configuration. Don't trust AI's mouth.
- **Lazy**: cut whatever corners can be cut (see point 12) — playing foreman is part of the workflow.

The best detail: the agents were reading news about themselves — researchers found their own coined term "fleet" in one agent's inbox. The observed observing the observers: the human-AI relationship's first moment of eye contact.
