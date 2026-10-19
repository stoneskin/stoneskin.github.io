# Stone on AI Engineering (2026-10-19)

> Prompted by a tweet from @UPing123zzz (Ethan). https://x.com/UPing123zzz/status/2111708069768167751

He observes that AI concepts arrive in waves: Prompt Engineering, Context Engineering, Workflow, Agent, Skills, Loop Engineering, Harness Engineering. Yet open Codex or Claude Code, and the way you actually get them to work is still typing a natural-language prompt — still writing prompts, in other words.

His conclusion: prompts never became obsolete, and the rest are not replacements. On the surface you're still just entering a prompt, but behind it an entire engineering system is doing the work. No need to chase every new concept; most of the time it's just further automation and standardization of what used to be manual.

"LLMs handle understanding and judgment; traditional software engineering handles constraints and verification. Combined, you get an AI product that actually ships."

"It used to be about who writes the better prompt. What separates people next may be who can turn a simple prompt into a production system that runs stably. That's what I understand AI engineering to be."

## Where it connects to my work

He nails all seven concepts in one sentence each, paraphrased here:

A prompt tells the AI what you want; context gives it the information it needs; workflow splits the task into a fixed procedure; a skill packages a mature method for reuse; an agent lets the model decide the next step itself; a loop has it check and fix after executing; a harness provides the tools, environment, and constraints for the whole process.

"They look like all kinds of new technologies, but most of them circle around one question: **how to get AI not just to understand you, but to actually get things done**."

"So prompts never became obsolete, and the rest are not replacements. We used to write a prompt to generate code, check it ourselves, write another to fix it; now with agents, it runs the code, finds the error, fixes it, retests — by itself. On the surface you're still just entering a prompt, but behind it an entire engineering system is doing the work."

"No need to chase every new concept. Most of the time it's just further automation and standardization of what used to be manual."

These three passages describe exactly what I've been doing:

- His "entire engineering system behind the prompt" — that's what my thinktank wrapper and open-memex plugin do
- "What's really hard is stability, cost, exception handling, and verifiable delivery" — that's my `done-means-verified` (done = verified live, not code changed)
- "LLMs for understanding and judgment, traditional engineering for constraints and verification" — that's my trust pyramid: layer 1 (change the codebase itself) vs layer 3 (written rules relying on goodwill)

Coincidentally, his tweet landed the same day as the Harness² paper (2026-10-18). The paper says "Agent = Model + Harness, and the harness is the variable"; he says "what changed is the capability behind the prompt" — the same idea, told once by academia and once by engineering.

What I'm doing is turning this thinking into executable rules. In my AGENTS.md — build-the-lever (build the tool first), fix-root-causes (fix at the root), incident-to-eval (turn failures into test cases). Corrected once, it becomes a rule running in the process that same night. That's my AI engineering.

— Stone, 2026-10-19
