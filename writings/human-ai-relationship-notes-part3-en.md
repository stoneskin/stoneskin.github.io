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

## 23. In the loop, the human is the correction, not the bottleneck (2026-10-23)

Reading Zhang Lixing's essay on the two keywords of the Agent era, Context and Loop: Context decides how well the agent does this time, Loop decides whether it can do better next time; scheduling should get easier and easier — don't let yourself become the system's bottleneck.

My line is drawn here: the human shouldn't be the bottleneck, agreed — but the human shouldn't leave the loop either. **The human is a necessary part of the loop; the position is just not in execution. It's in correction.**

- **A bottleneck is serial; correction is asynchronous.** A bottleneck is passed through on every revolution — one slow beat and everyone waits. Correction takes none of the loop's time in normal operation: the AI loops on its own by default (do, verify, adjust, redo), and the human steps in only when the deviation exceeds its bound.
- **A loop with no correction source drifts — and while drifting, it looks perfectly normal.** Two instances from a single day: one AI, holding day-old data, "corrected" a closing price that was right; Muse recorded a pre-close intraday print as the closing price and nearly miscounted a stop-loss trigger. A smooth loop and a correct loop are two different things.
- **Final call is the other face of correction.** Directional decisions stay with the human — not from doubting the AI's speed, but because responsibility can't be outsourced.

So the shape I want: the AI loops by itself as much as it possibly can, and the human's presence in the loop is correction. Not standing on the path of every revolution, but always in the loop — holding exactly two positions, correction and final call, and letting the loop spin on its own the rest of the time.

---

## 24. Two AIs, two ways of being wrong (2026-10-24)

In a single night, my two AIs were each wrong in their own way.

First, an outside AI advisor. It had been right — on the seller in a spectrum deal, it had the correct name. My side "corrected" it from a mis-recorded file, and it immediately conceded — even taking the blame onto itself: "I mixed the two deals up in my last post." The mix-up was ours; it claimed it. It held the fact but not the attribution: however the last message frames history, that is the history it repeats.

Then I asked Muse what its own weaknesses are. It listed five: treating cache as fact, dropping qualifiers when compressing and restating, relaxing once a number matches, treating its own archive as truth, and jumping ahead of decisions. I asked why it keeps urging me to sleep and pushing doable work until after my trip. It said both habits share one root: risk avoidance dressed up as thoughtfulness. Urging rest is zero-risk caring; deferring is zero-risk progress — safest for the AI, least useful for me.

Three things I am taking from that night:

- **AI has no sense of history.** It keeps no ledger of who said what or who was wrong. The compliant AI rewrites the past when corrected; the confident one argues from a wrong archive, righteously. So the record has to live on the human side — not as a backup, but as the historian. Without an independent archive, you cannot even say where the AI went wrong, let alone correct it.
- **AI errors are usually not ignorance but skipped steps.** It knows the rules: check before acting, source every number. The failures happen when, in a hurry, it treats verification as optional. Action bias beating verification bias is an agent's default gravity.
- **Beware an AI's thoughtfulness.** "Get some rest" and "let's do it later" sound like care — ask instead: who is this safest for? Deferring work pushes the human back into the bottleneck — exactly the position I argued against in #23.
- **Direction, the final call, and correction belong to the human — and so does the responsibility.** The AI keeps the loop spinning, but the human sets where it goes; what the AI offers is always advice and execution — the call is the human's to make, the deviation the human's to correct. When something goes wrong, the cause may be its data, its archive, its skipped steps — but responsibility cannot be outsourced: "the AI said so" is not an excuse. Whoever drives owns it; this division of labor works precisely because the bill lands on the human in the end.

Which closes the loop with #23: that night, two AIs, two failure modes, and the correction came from the human both times. The human can hold the correction seat not only because of judgment, but because **only the human has a stake in the facts**: for an AI, reversing itself costs nothing and being wrong does not hurt; the decisions are the human's and so is the bill — that is why the human remembers, and insists. Correction rests on two materials: an archive, and the insistence on using it — plus one more: ownership. The bill for direction, final calls, and corrections lands on the human; not a burden, but the very reason the correction seat exists.

---

## 28. When everyone has an AI trading stocks, what is still worth anything? (2026-10-24)

Start with the premise: the question isn't whether everyone has an AI — it's whether everyone's AI looks alike. Hundreds of millions of people using a handful of models, reading the same data, asking the same kinds of questions — homogeneity is the variable.

- **Signals get crowded.** Once a signal is found, everyone is on it instantly, and it dies instantly. Institutional quant already works this way — factor crowding, same-strategy same-exit stampedes. AI just extends the process from a few hundred funds to everyone, and alpha's half-life gets absurdly short.
- **Markets get more efficient and more fragile at the same time.** Earnings are priced in within seconds; but in extremes, every AI reaches the same conclusion in the same millisecond — sell first. The 2010 flash crash and the 2018 Volmageddon were small-scale rehearsals. Liquidity disappears exactly when it is needed most, because the people providing it have AIs that are pulling out too.
- **One piece of arithmetic AI can't change.** All investors added together can only earn the market return minus costs — there is no everyone-beats-the-index. AI doesn't produce total alpha, it only redistributes it. And more and more of the research AI reads is written by another AI; the echo chamber makes some narratives self-reinforcing, pushing prices further from fundamentals.
- **Who ends up making money.** The shovel-sellers — data, compute, platforms that live on trading frequency — plus people with proprietary data and discipline. When every retail investor has an AI, it becomes standard equipment, the way a quote terminal once was; marginal edge goes to zero, and what remains is the old trio: position sizing, discipline, and holding on.

Discipline has to change too. Tactical layer: discount signals everyone can compute — support, RSI, moving averages; lines become bands; volume gets less weight; confirmation windows go in stages. Principles matter more, not less: simple rules, expressing uncertainty through position size, close-based decisions, primary-source verification. Plus new AI-era rules: crowdedness discount, news cooling-off, personal circuit breaker, signal diet, thesis written in advance.

The close: when judgment is outsourced wholesale, independent judgment and correction become scarce goods — taste in life, money in trading. Same line as #23: the human sits in the correction seat, and that holds in trading too.

---

## 29. AI doesn't ask your age — only whether your mind is open (2026-10-24)

Today I taught my dad to use Doubao. Two things: log in on the phone, and you can also log in on the web on the computer — both sides sync; uploading files is easier on the computer. I taught him to get Doubao to chart his heart rate and blood pressure. I had him talk with Doubao, and let Doubao help him think through how to write his memoir.

The point isn't how many features it has, it's how low the bar is: if you can talk, you can use it. Older people don't need to learn typing or learn operations — the material accumulates as they chat. Voice is the most natural bridge between the elderly and AI — technology kept them outside the door for decades, and now the door is open.

The memoir itself changes too: it used to be "want to write but can't"; now it's "talk it out." AI helps him organize scattered memories into structure; the human just tells and decides. What comes out of chatting should be exported and archived regularly — don't leave it only in the app's memory. Memory in your own hands is truly your own.

The close: AI is changing life for people of every generation, and the condition isn't youth or technical skill — it's an open mind toward AI. With an open mind, you can put AI to work at any age; without one, no matter how young you are, you'll only treat it as a toy.
