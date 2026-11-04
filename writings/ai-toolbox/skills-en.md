# AI Skills

[← Home](../../index.md)

*2026-11-04 · [中文版](./skills.md)*

Agent Skills are capability packs for AI: a prompt + scripts + reference docs, loaded on demand, costing no context when unused. Only skills I actually use, have seriously evaluated, or that are popular enough to be worth knowing. **Usage and rating are scored separately**: usage is how much I actually use a skill; rating is my recommendation — for skills I haven't used, the rating is based on reputation and public material, not hands-on testing. ★★★★★ highly recommended, ★★★★☆ worth using/trying, ★★★☆☆ worth a look, ★★☆☆☆ evaluated, not adopted. At most 5 full entries per category; overflow goes in an "Others" line with names only. Tools are on the other page: [AI Toolbox](./index-en.md).

## 1. Skills I Use

| Skill | Usage | Rating | Comment |
|---|---|---|---|
| [diagram-design](https://github.com/cathrynlavery/diagram-design) | Regular use | ★★★★★ | Diagram skill: 45 diagram types, self-contained HTML + inline SVG, zero external dependencies; drew the Pi architecture diagrams (static + animated loop versions); deletion is the highest-quality move — every node earns its place. |
| [thinktank writing](https://github.com/stoneskin/muse-thinktank) | Regular use | ★★★★☆ | thinktank seed skill: structures bilingual writing context (LinkedIn articles, docs), triggered by 写作/write/article; where essay and tech-article writing context comes from. |
| [thinktank stock-analysis](https://github.com/stoneskin/muse-thinktank) | Regular use | ★★★★☆ | thinktank seed skill: pulls technicals via tt/stock_context.py into shared context before the jury reviews; the execution layer of "data before draft". |
| [thinktank code-review](https://github.com/stoneskin/muse-thinktank) | Regular use | ★★★★☆ | thinktank seed skill: the standing pre-review step, its output feeds shared context for the jury. |
| local-questioning | Regular use | ★★★★☆ | Homegrown questioning method (local version of grill-me): auto-triggers while learning, asks round after round from the edge of understanding, each with a recommended answer, until principle/implementation/trade-offs are all clear; never uses the word "grill". |

## 2. Popular Skills: Discovery, Questioning & Handoff

*From Ethan's Oct 21, 2026 X post "The 10 most popular AI Skills worldwide" ([original post](https://x.com/UPing123zzz/status/2112843303330738503)); install counts are the post's figures; 7 of the 10 come from mattpocock/skills.*

| Skill | Usage | Rating | Comment |
|---|---|---|---|
| [find-skills](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md) | Not used — equivalent in place | ★★★★☆ | ~3.8M installs, #1: lets AI discover installable Skills on its own; my local-skill-discovery-first does the same job, and its leaderboard-first approach is what I learned from this one. |
| [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) | Not used — idea already landed | ★★★☆☆ | ~1.3M installs: AI keeps asking until a fuzzy request is clear; the idea already lives in my premise-first mode and local-questioning — but I don't use the word "grill". |
| [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) | Not used — want to absorb | ★★★★☆ | ~1.1M installs: deep questioning grounded in project docs, unifying terms and recording decisions on the spot; the one I most want to absorb — it flows naturally into doc-impact-checklist and future-goes-to-doc. |
| [handoff](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md) | Not used — want to absorb | ★★★★☆ | ~954K installs: turns current progress and context into a Markdown handoff doc; useful for long sessions and cross-device continuation, and naming the next session's skills in the handoff is a good design. |
| [agent-browser](https://github.com/vercel-labs/agent-browser) | Not used — equivalent in place | ★★★☆☆ | ~1.1M installs: AI drives a browser (open pages, click, fill forms, read pages); my delegated browser work is the managed equivalent, with login state. |

## 3. Popular Skills: Engineering Practice

| Skill | Usage | Rating | Comment |
|---|---|---|---|
| [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) | Not used — half-absorbed | ★★★☆☆ | ~1.1M installs: test-driven, failing test first, then implementation; the full doctrine may not fit — I only want "write the acceptance script before the feature" plus seams confirmation and the anti-tautology check. |
| [improve-codebase-architecture](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md) | Not used — want to absorb | ★★★★☆ | ~1.1M installs: inspects codebase architecture for modules worth improving; both repos are now big enough to need regular architecture checkups, and the Deletion test (remove it — is complexity concentrated or just moved?) is a good question. |
| [setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md) | Not used — not adopting | ★★☆☆☆ | ~974K installs: initializes the whole Matt Pocock engineering workflow; I already have my own AGENTS system and won't be taken over — skip. |
| [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | Not used — no landing point yet | ★★★☆☆ | ~969K installs: Anthropic's official frontend-design skill, less templated UI; solid quality, but the site is a Markdown static site and diagrams already have diagram-design — no landing point yet, keep on file. |
| [triage](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md) | Not used — waiting for volume | ★★★☆☆ | ~917K installs: auto-classifies GitHub Issues; email triage is already in use, issue triage waits until open-memex issue volume grows. |

---

*Admission rule: I decide what enters and leaves this list; borrow, don't install verbatim — absorb and rewrite for self-maintenance (Oct 14, 2026 principle); entries are hands-on notes, not vendor copy. List install counts are Ethan's post figures (Oct 21, 2026), not live numbers.*
