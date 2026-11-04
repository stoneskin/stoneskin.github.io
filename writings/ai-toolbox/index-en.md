# AI Toolbox

[← Home](../../index.md)

*2026-11-04 · [中文版](./index.md)*

Only AI tools I have used, seriously evaluated, or that are popular enough to be worth knowing. **Usage and rating are scored separately**: usage is how much I actually use a tool; rating is my recommendation — for tools I haven't used, the rating is based on reputation and public material, not hands-on testing. ★★★★★ highly recommended, ★★★★☆ worth using/trying, ★★★☆☆ worth a look, ★★☆☆☆ evaluated, not adopted. At most 5 full entries per category; overflow goes in an "Others" line with names only. Continuously updated; v4 has 21 entries, plus 6 more listed under "Others". Skills live on their own page: [AI Skills](./skills-en.md).

## 1. Code Understanding & Graphs

| Tool | Usage | Rating | Comment |
|---|---|---|---|
| [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Not used yet — popular, want to try | ★★★☆☆ | 90k-star code knowledge-graph plugin, Tree-sitter + LLM graph building; best for getting oriented in a large unfamiliar codebase before reading code. |
| [Graphify (inside thinktank)](https://github.com/stoneskin/muse-thinktank) | Regular use | ★★★★☆ | Curated code graph built into thinktank: 1,029 nodes / 1,701 edges / 61 communities; shows what a change touches at a glance. |

## 2. Multi-Model & Multi-Agent Orchestration

| Tool | Usage | Rating | Comment |
|---|---|---|---|
| [muse-thinktank](https://github.com/stoneskin/muse-thinktank) | Daily use | ★★★★★ | One question to N models in parallel, dual judges cross-validate, synth merges a verdict; disagreement between models is itself signal. |
| [model-fuse](https://github.com/stoneskin/model-fuse-private) | In development | ★★★☆☆ | Homegrown opencode plugin (private repo): one question to many models, merge the best; direction for D10/D11 settled, a different mechanism from Copilot Fusion. |
| GitHub Copilot Fusion | Evaluated, not adopted | ★★☆☆☆ | D10 adversarial review is roughly Critique, D11 verdict differs from Cascade quality gates — not equivalent. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Not used yet — popular, want to try | ★★★★☆ | Graph orchestration framework; state-machine agent flows are a production-grade pattern; Meta's Thin Orchestrator paper describes the same idea — a useful side-by-side read. |
| [AutoGen](https://github.com/microsoft/autogen) | Not used yet — popular, want to try | ★★★☆☆ | Microsoft's multi-agent framework, the classic conversational agent orchestration; conceptually comparable to thinktank's jury review, but a different job. |

## 3. Memory & Knowledge

| Tool | Usage | Rating | Comment |
|---|---|---|---|
| [open-memex](https://github.com/stoneskin/open-memex) | Daily use | ★★★★★ | Local-first memory layer: Markdown as source of truth, SQLite FTS5 search, MCP + CLI; npm 0.8.2. |
| [Mem0](https://github.com/mem0ai/mem0) | Not used yet — popular, want to try | ★★★☆☆ | Memory layer for agents, marketed as pluggable long-term memory; same space as open-memex, useful as a design reference. |

## 4. AI Coding Assistants

| Tool | Usage | Rating | Comment |
|---|---|---|---|
| [Claude Code](https://claude.com/product/claude-code) | Not used | ★★★★★ | Native host for plugins like Understand-Anything; one of the best-regarded coding agents. |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot) | Regular use | ★★★★☆ | Company-approved AI coding CLI; usable as an agent execution backend, called through AgentAdapter. |
| [OpenCode](https://github.com/opencode-ai/opencode) | Daily use | ★★★★☆ | Open-source AI coding CLI; close in role to GitHub Copilot CLI, interchangeable with it. |
| [Cursor](https://www.cursor.com) | Used | ★★★★☆ | The most popular AI editor, completion + agent mode in one. |
| [Codex](https://github.com/openai/codex) | Not used yet — popular, want to try | ★★★★☆ | OpenAI's coding agent, CLI + cloud in parallel; same space as Claude Code. |

Others: Gemini CLI, Cline, RooCode, VSCode, Antigravity, Aider (Gemini CLI, Cline, RooCode, VSCode and Antigravity used; names only, no rating).

## 5. Agent Frameworks & Runtimes

| Tool | Usage | Rating | Comment |
|---|---|---|---|
| [DeepSeek Harness (dsh)](https://github.com/deepseek-ai/deepseek-harness) | Evaluated (borrowed ideas) | ★★★☆☆ | v0.2.2-alpha.2, plugin-based micro-kernel agent runtime; notable for skill catalog lazy loading, flow skills, "model-visible <=> logged". |
| [LangChain](https://github.com/langchain-ai/langchain) | Not used yet — popular, want to try | ★★★★☆ | The oldest agent framework, the biggest ecosystem; new projects rarely start from it. |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Not used yet — popular, want to try | ★★★☆☆ | Role-based multi-agent orchestration (Role + Task + Crew), easier to start than AutoGen; a reference for small-team multi-agent prototypes. |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Not used yet — popular, want to try | ★★★☆☆ | OpenAI's official lightweight agent SDK. |
| [Pi](https://github.com/badlogic/pi) | Not used yet — personal project | ★★★★☆ | 117k-star thinnest agent harness: the kernel only connects model/tools/persistence, deliberately without permissions, Plan mode, or sub-agents; many FDEs use it directly as their harness. |

## 6. Investing

| Tool | Usage | Rating | Comment |
|---|---|---|---|
| [moomoo OpenD](https://www.moomoo.com) | Regular use | ★★★★☆ | The only real API for quotes + paper trading; 1024-bit RSA encrypted handshake, laptop listening on 0.0.0.0 over Tailscale. |
| [tt/stock_context.py](https://github.com/stoneskin/muse-thinktank) | Regular use | ★★★★☆ | Homegrown (inside thinktank): pull technicals before writing any investment analysis; every number needs a source. |

---

*Admission rule: I decide what enters and leaves this list; a tool gets in after I've used it, seriously evaluated it, or because it's popular enough to be worth knowing; comments evaluate each tool on its own merits, not vendor copy; homegrown tools need a repo link to enter, third-party AIs don't enter. Send me a link if you want me to try something.*
