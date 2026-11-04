# AI Toolbox

[← Home](../../index.md)

*2026-11-04 · [中文版](./index.md)*

Only tools and skills I have actually used or seriously evaluated. Ratings reflect how much I use them, not an objective ranking: ★★★★★ daily use, ★★★★☆ regular use, ★★★☆☆ in progress or worth trying, ★★☆☆☆ evaluated, not adopted. Continuously updated; v1 has 16 entries.

## 1. Code Understanding & Graphs

| Tool | Rating | One-line verdict |
|---|---|---|
| [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | ★★★☆☆ | Code knowledge-graph plugin: Tree-sitter + LLM multi-agent pipeline builds the graph; interactive dashboard, guided tours, semantic search, diff impact analysis; 90k stars; evaluated, not yet tried — best for getting oriented in a large unfamiliar codebase before reading code. |
| [Graphify (inside thinktank)](https://github.com/stoneskin/muse-thinktank) | ★★★★☆ | Curated code graph built into thinktank: 1,029 nodes / 1,701 edges / 61 communities; read the graph before a review to see what a change touches. |

## 2. Multi-Model Orchestration & Review

| Tool | Rating | One-line verdict |
|---|---|---|
| [muse-thinktank](https://github.com/stoneskin/muse-thinktank) | ★★★★★ | My multi-model jury: one question to N models in parallel, dual judges cross-validate, synth merges a verdict; used in weekly reviews — disagreement is signal. |
| model-fuse | ★★★☆☆ | My opencode plugin: one question to many models, merge the best; three auto tiers; in private development; D10/D11 direction settled (not replacing with Copilot Fusion). |
| GitHub Copilot Fusion | ★★☆☆☆ | Evaluated, not adopted: D10 adversarial review is roughly Critique, D11 verdict differs from Cascade quality gates — not equivalent. |

## 3. Memory & Knowledge

| Tool | Rating | One-line verdict |
|---|---|---|
| [open-memex](https://github.com/stoneskin/open-memex) | ★★★★★ | My local-first memory layer: Markdown as source of truth, SQLite FTS5 search, MCP + CLI; npm 0.8.2; long-term memory for AI coding assistants. |

## 4. AI Coding Assistants

| Tool | Rating | One-line verdict |
|---|---|---|
| [Claude Code](https://claude.com/product/claude-code) | ★★★★★ | My primary coding agent; native host for plugins like Understand-Anything. |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot) | ★★★★☆ | Company-approved AI tool; WorkBuddy's main execution backend, called through AgentAdapter. |
| [OpenCode](https://github.com/opencode-ai/opencode) | ★★★★☆ | Open-source AI coding CLI; WorkBuddy's personal hand, interchangeable with Copilot CLI. |

## 5. Agent Frameworks & Runtimes

| Tool | Rating | One-line verdict |
|---|---|---|
| [DeepSeek Harness (dsh)](https://github.com/deepseek-ai/deepseek-harness) | ★★★☆☆ | v0.2.2-alpha.2, plugin-based micro-kernel agent runtime; high borrowing value (skill catalog lazy loading, flow skills, "model-visible <=> logged"), not adopted directly. |

## 6. Investing

| Tool | Rating | One-line verdict |
|---|---|---|
| [Ainvest Amie](https://www.ainvest.com) | ★★★★☆ | Daily three questions as an outside reference: take the framework, never the numbers; holdings are never disclosed; answers must be re-checked against our own closing prices. |
| [moomoo OpenD](https://www.moomoo.com) | ★★★★☆ | The only real API for quotes + paper trading; 1024-bit RSA encrypted handshake, laptop listening on 0.0.0.0 over Tailscale; live-trading unlock expires ~Dec 1. |
| Sector Navigator | ★★★☆☆ | In-app AI sector navigator in moomoo: sector rotation analysis only, no trade recommendations, no orders; once picked it can't be changed. |
| tt/stock_context.py | ★★★★☆ | Homegrown: pull technicals before writing any investment analysis; every number needs a source; a draft with framework but no data is half-baked. |

## 7. Homegrown Workflow Tools

| Tool | Rating | One-line verdict |
|---|---|---|
| gh-sync-check.py / gh-api-push.py / gh-post-merge.py | ★★★★☆ | The publishing chain: sync with remote before starting, push branches via API, clean up after merge; used daily. |
| backup-sync.py | ★★★★☆ | Nightly 22:00 backup of the muse-agent-harness private repo straight to main; the only exception to the branch + PR rule. |

---

*Admission rule: a tool enters this list only after I've used it or seriously evaluated it; entries are hands-on notes, not vendor copy. Send me a link if you want me to try something.*
