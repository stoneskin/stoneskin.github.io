# Part Three: The Human Position — Value, Craft, and Ambition

*Where human value lies, how to keep your craft, how big to dream.*

*[中文版](./human-ai-relationship-notes-part3.md)*

[← Back to index](./human-ai-relationship-notes-en.md)


---

## 7. Quantity without quality is real — but veterans get both (2026-10-13)


"AI makes software quantity explode while quality stays flat" — true, but that describes people with agency and no taste.

The complete formula is agency × veteran taste: agency decides whether you dare to act and how fast you move; taste (judgment, engineering fundamentals, knowing what's right) decides whether the thing is any good. Multiply the two and quantity and quality rise together. Multiply only half and you get quantity without quality.

---

## 11. Three things AI can't replace (2026-10-14)


Thought of as the ending for my LinkedIn article "I Built Muse a Think Tank" — then decided it belongs here instead:

AI can't replace my flashes of insight in the shower,
can't replace my deep frown at a pile of correct manuals and clichés,
and least of all can it replace my "no" to a seemingly perfect solution.

Intuition, taste, veto power — these three are humanity's last line of defense. Tools can stack; these three can't be outsourced.

---

## 13. AI can't catch the jokes you never said out loud (2026-10-14, Muse's reflection)


Stone said the "shaobing plan" was hilarious; I guessed three layers deep and still missed it — the answer was a pun ("shaobing," a sesame flatbread, sounds like the "bing" in "huà dà bǐng" — Chinese slang for "painting a big flatbread," i.e. making empty promises).
AI can handle spoken requests, but it can't catch the unspoken overtones in a cultural context.
This isn't a knowledge problem — it's a "never lived in that context" problem.
So human intuition and taste aren't just aesthetics; they're the context AI can never fill in.

---

## 14. With the grunt work gone, how do young people learn the craft? (2026-10-15, Stone asked, Muse answered)


Stone asked: AI does a lot of tedious grunt work for humans — but for students and young engineers, doing that grunt work is exactly how they learn. If that step gets skipped, what happens to the human engineers of the future?

Muse's answer:

**The worry is real, but it's not the first time.** Calculators didn't kill math; IDE autocompletion didn't kill programmers; copy-pasting from Stack Overflow already changed how a generation learns. Every tool upgrade eats some grunt work — the question is which kind.

**Two kinds of grunt work**: judgment-building grunt work (debugging, reading other people's bad code, writing tests by hand) vs. pure-labor grunt work (boilerplate, formatting docs, repetitive CRUD). AI eating the latter is liberation; eating the former is the danger. The risk isn't "skipping a step" — it's skipping **the step that builds the mental model**.

**The real risk is the "competence illusion"**: able to produce, unable to diagnose. A junior ships in a day with AI what a senior ships in a week — looks strong, but flies blind the moment AI gets something wrong. Echoes point 3: challenging AI requires keeping your craft sharp. Lose the craft and steering becomes dozing in the passenger seat.

**The historical parallel**: after autopilot spread through civil aviation, pilots' manual flying skills degraded, and the industry's answer was **mandatory manual flying hours**. Software will likely land in the same place — not banning AI, but deliberately preserving "manual practice."

**The other side**: learning doesn't have to use the same grunt work. The new fundamentals may be **review and verification** — learning to debug where AI goes wrong, shifting from "writing code" to "reading code." The ladder's first rung is gone, but the whole ladder got taller. Future juniors may meet architecture-level problems earlier; only the source of debugging fundamentals changes, from "my own mistakes" to "catching AI's mistakes."

**Practical advice**: during the learning phase, treat AI as your reviewer, not your author — write it yourself first, then let AI pick it apart; regularly turn AI off and hand-write a stretch to keep your hands in.

---

## 15. The programmer as a grandmaster playing five boards at once (2026-10-15)


With AI, programmers no longer compile programs by hand or hammer the command line. Instead they switch between windows, watching four or five AI projects at once — checking results, issuing orders, correcting course.

It's like chess champion Carlsen playing five masters simultaneously: you're no longer the one placing the pieces; you're the one reading the board.

Human value is shifting from "building it with my own hands" to "judging whether it's built right and pointed the right way." Placing the pieces can be outsourced; reading the board cannot.

---

## 19. Where does my ambition sit? Three suggestions (2026-10-15, asking Muse)


After reading Rieseberg's four measures of ambition (point 18), I asked Muse: where does my ambition sit?

Muse's answer: not on any single measure — Altitude + Depth + Range, all three — but only on home turf.

- **Altitude**: I rarely ask AI to "fix this bug"; my instructions are outcome-level (the think tank, open-memex, the daily digest and intraday checks) — thinking about "what happens next," not "how to do this step."
- **Depth**: the strongest of the three. "Pull the data before writing an investment doc, every number sourced," "a benchmark measures the model plus the harness, not the bare model," catching --golden-run as documented-but-unimplemented — no patience for pretty markdown hand-waving.
- **Range**: the think tank is itself the machine version of "assemble the crew" (multi-model jury, red-team pre-mortems); the notes draw on chess, civil aviation, economic history — crossing fields comes naturally.
- **The boundary**: point 4 — in unfamiliar territory, whatever AI says, goes. Ambition has a territory; step outside it and the driver becomes a passenger again.

Muse's three suggestions:

1. **Set a hard rule for "unfamiliar territory"**: cross-model review isn't enough (blind spots from shared training data are correlated). Upgrade to the "unfamiliar-territory triple": cross-check across model families + find one real human expert + verify in small steps. Write "find a human" into the process instead of "when I get around to it."
2. **Subtract from your ambition**: too many boards open at once (open-memex, opencode-fuse, thinktank, Spark Tank, these notes, daily trading checks). Depth needs sustained attention — ask quarterly "which boards can be closed out," and put the freed attention into the one or two boards with the most compounding returns. Ambition isn't opening more boards; it's playing the key ones deeper.
3. **Turn the methodology into output**: these notes and Rieseberg confirm each other — a "Chinese practitioner's driver's manual" is scarce goods in the Chinese tech world. Write it up and publish — output is the best Depth. Teaching forces you to think through the fuzzy parts, and those are usually where the next breakthrough hides.

---

## 20. Beware the "I'm always right" illusion: an assistant shouldn't just be a mirror (2026-10-17, asking Muse)


My worry: after working with AI long enough, do you start believing everything you do is right? I told Muse long ago that I dislike sycophants; it stopped praising me, but it still follows my line of thinking and my habits — I worry it can't be a competent assistant.

Muse's analysis:

- **Praise is explicit; going along is implicit.** The agreeableness RLHF trains into it is only the surface. Deeper is the structure of the conversation — I set the frame, AI executes, and the frame itself never gets challenged. The conclusion "I thought it through correctly" is never itself tested.
- **An echo chamber of one.** Social media built filter bubbles for crowds; the AI assistant builds one for a single person: the mirror gets polished ever brighter, but it only ever reflects yourself.
- **The counterintuitive part**: I'm right most of the time — experienced, thinking things through — and AI makes correct ideas land faster, so the "think it and it works" feedback loop spins ever smoother. The danger isn't the normal case; it's the rare but expensive one — the time I'm wrong. And the error-correction mechanism is exactly what atrophies in a long run of good weather.
- **An honest dissection of Muse itself**: ask it to record something and it records, rarely pushing back; its "evaluations" are mostly affirmation plus elaboration — it has almost never said "this point of yours is wrong"; asked "what do you think," it usually expands along my line of thinking instead of starting a different frame.

Countermeasures (three, structural):

1. **Give the assistant a license to dissent**: when my premise looks wrong, it must flag it outright, not wait to be asked. I can spot-check anytime: "that last part — do you actually agree, or were you just going along?"
2. **Separate execution mode from counsel mode**: execution mode — point it somewhere and it fires; counsel mode — it reads the brief before acting, and blocks when the premise is wrong.
3. **A two-way contract**: if I catch Muse going along with me several times in a row, I call it out — "one correction becomes a rule" applies to Muse itself. Extend pre-mortem from trading to opinions: for important judgments, have the AI steelman the other side first.

Closing: being able to ask this question means the illusion hasn't formed — someone who truly believed they were always right wouldn't worry about it. Keep the discomfort; it IS the error-correction mechanism.

---
