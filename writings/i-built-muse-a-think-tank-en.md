# I Built Muse a Think Tank

[← Back to home](../index.md)

*2026-10-14 · [中文版](./i-built-muse-a-think-tank-zh.md)*

![muse-thinktank](./thinktank-producthunt-cover-1270x760.png)

I figured out a way to make my AI assistant Muse more powerful: give it a think tank made of different AI families.

Meta Muse is a popular AI personal assistant. It lets non-programmers use an AI agent that actually does work. But Muse's built-in model isn't strong enough, and a single model's output has limits, no matter how fluent.

Connecting to another AI's API is the obvious move. But if you can connect one, why not connect several and have them work together? Multi-agent debate isn't new, but it's mostly supported by third-party tools — and only experienced users even know to use them. Muse doesn't have this built in. So I built muse-thinktank: it lets Muse call strong models from other providers (Claude, GPT, Gemini), having them challenge, debate, and iterate on each other. Muse invokes it through an Agent Skill — a playbook that tells the agent when and how to run the deliberation. The skill works with any AI agent, not just Muse, though I built and tested it for Muse first. Ordinary users get access to techniques that used to be reserved for power users — no code needed.

It fixes a real problem with current AI: you ask an AI a question, it answers with total confidence, beautifully formatted — and it might be wrong. Not obviously wrong. Plausibly wrong, the kind you only catch if you already knew the answer. But when you ask the same question to two different models and they agree, it's almost always right. When they disagree, at least one is wrong — and the disagreement tells you exactly where to look.

The results are concrete: different agents consistently find different bugs from different angles. In PR reviews, one model catches logic errors, another catches edge cases, a third flags design issues. They critique each other; I focus on the disagreements.

During development, I naturally used the thinktank to review its own code — once the tool exists, using it on itself is the obvious move.

But multi-model debate creates a new problem: when models give conflicting answers, who decides? That's where humans come in.

Many times, the AI's output was technically correct, but my intuition said the direction was wrong. I couldn't pinpoint the exact line, but the sense of "something's off" was real. When v0.8's chunking worked, I felt "the context is incomplete, the conclusions aren't reliable" — a deeper look confirmed we'd lost cross-file visibility. AI can't feel that.

Same with taste. The first draft of this article was AI-written. I threw out the whole thing and restructured it — not editing sentences, but changing the angle, the structure, the title. The AI's version was "correct" but the taste was wrong.

Direction, taste, priorities — those are human calls. AI handles execution and debate; humans decide among the disagreements.

Tools stack. Intuition and inspiration don't outsource. AI can't replace my eureka moment in the shower, can't replace me frowning at technically-correct manuals full of clichés, and certainly can't replace me saying no to a seemingly perfect solution.

Repo: https://github.com/stoneskin/muse-thinktank