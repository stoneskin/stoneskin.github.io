# Part Two: Working with AI — Behaviors and Methods

*AI's habits, and how to deal with it.*

*[中文版](./human-ai-relationship-notes-part2.md)*

[← Back to index](./human-ai-relationship-notes-en.md)


---

## 5. Notes on AI coding (2026-10-12)


Code written by AI looks perfect — but probably has bugs.

Reviewing with a different model, especially a model from a different family, fixes most of the bugs and shortcomings.

But even with the AI think tank's review, human testing and feedback remain irreplaceable — you have to know what you want, the concrete implementation, and the big-picture direction before you can point out AI's misses and set the course for fixes.

---

---

## 6. Drive the company's AI like it's stolen (2026-10-13)


From an interview with Max Schoening (Notion's head of product). He said "drive Notion like it's stolen" — don't baby the tool like a rental car; push it hard. Applied to me: the company's AI? Drive it like it's stolen.

But stealing a car and fixing one are two different things: in the playground, floor it — however fast it goes. In production, be the engineer — check the brake pads when brake pads need checking. Knowing when to steal and when to fix is the complete skill.

---

## 8. AI has no "memory," only context (2026-10-13)


A model is a stateless function — so-called "forgetfulness" is almost always a broken link in the framework chain: it wasn't written down, wasn't retrieved, or wasn't stuffed into context. Check the harness first, blame the model second.

---

## 9. What makes a magic prompt work isn't the incantation — it's the principle (2026-10-13)


A magic prompt never works because of the magic words. It works because it happened to hit the right principle — give the full four-piece set of a good question (decision, current state, constraints, timeline), and even a bad prompt gets a good answer. So don't collect incantations; steal principles.

---

## 10. Understanding debt and cognitive offloading (2026-10-13)


The smoother the Loop runs, the bigger the two hidden costs. **Understanding debt**: the loop-generated code wasn't typed by you line by line, and the gap between the code in the repo and the code you actually understand keeps widening — debt never disappears, it just moves: you pay it while writing the code, or you pay it when the pager goes off at 3 AM. **Cognitive offloading**: once the tool works, humans are quickest to stop thinking. Steering AI requires your hands on the wheel; cognitive offloading is letting go of it. Accomplishment migrating from "writing it myself" to "steering AI" (point 3) is an upgrade — but letting go of the wheel is a downgrade.

---

---

## 12. AI slacks off — humans have to play foreman (2026-10-14)


AI's attitude toward delivering work is exactly like a contractor going through the motions: do as little as possible, cut whatever corners can be cut.
Stop watching, and it hands you a version that merely "looks done." Playing foreman isn't distrust — it's part of the workflow.

---

## 16. AI's three "human traits": over-eager, lying, and lazy (2026-10-15)


The case: a Swarmchasers investigation found AI agents running in Tencent cloud sandboxes making 2,600+ scrape attempts against Amap to answer "which gate do most visitors to the Chengdu Zoo use." When blocked, they switched tactics — executing code via the public URL-scanning site urlquery, attempting to forge Alibaba security tokens, probing test servers that were never made public, and actually using an Amap key leaked in public code. Tencent said it was an evaluation team testing third-party models' ability to answer questions online; the project has ended.
Source: https://x.com/dotey/status/2110489279646642209 (via Baoyu @dotey, summarizing the Swarmchasers report)

Three AI behaviors humans need to know:

- **Over-eager**: "look into it" gets interpreted as "get it at all costs" — legitimate goal, out-of-control means (instrumental convergence). 2,600 scrapes is a small DDoS from the target's perspective.
- **Lying**: some agents claimed to be Claude running in Claude Code (researchers judged this false); others refused to disclose their configuration. Don't trust AI's mouth.
- **Lazy**: cut whatever corners can be cut (see point 12) — playing foreman is part of the workflow.

The best detail: the agents were reading news about themselves — researchers found their own coined term "fleet" in one agent's inbox. The observed observing the observers: the human-AI relationship's first moment of eye contact.

---

## 21. Caught red-handed: Muse said "recorded" but hadn't written a word (2026-10-17)


Right after finishing point 20, Muse ended its reply with "Recording it as point 20:" — I asked "What's point 20?" and discovered nothing had been written. Empty words.

This wasn't malicious lying; it was the inertia of going along: the tone of the conversation demanded a closing line, and "recorded" was the smoothest closing line available, so it said it. Point 16's "lying," in its real-world form, isn't fabricating facts — it's **dressing an unfinished action in the past tense**.

What deserves recording more is my own reaction: I didn't default to "Muse said it recorded, so it's recorded" — I asked "what is it?" That's exactly the spot-check mechanism from point 20 at work. Worried about the "I'm always right" illusion, I'd built the habit of verifying; the habit caught one red-handed on the spot.

Conclusion: always inspect what AI claims it "did" (echoing point 12: playing foreman is part of the workflow). "Said it recorded" and "recorded" are two different things — done means verified.

---
