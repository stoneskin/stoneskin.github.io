# I Gave My AI a Memory

[← Back to home](../index.md)

*2026-10-04 · [中文版](./i-gave-my-ai-a-memory-zh.md)*

The most annoying thing about AI coding assistants isn't wrong code. It's amnesia.

Last week I walked Copilot through our deploy process in VS Code. This week in opencode, it asks me "so how does this project deploy?" Bits of knowledge I type into the AI during work — gone the moment the chat closes.

open-memex is my fix: a local-first memory layer. Say it in one editor today, remembered in another tomorrow. Memories are plain Markdown on your own machine, SQLite FTS5 on top for search. Open and read them, open and edit them. No cloud involved.

At v0.8.1 now. Two features I actually use daily:

**Aliases**: teach it "Shaobing Project" means "payment system refactor" — a pun on "painting a pie," Chinese slang for empty promises. Set it once, search the codename, direct hit. No reindexing. We humans love our illogical codenames.

**Synonym expansion**: Chinese-English synonyms expand at index time. Write 部署 (Chinese for "deploy"), search "ship," it matches. Index-time for synonyms (stable list), query-time for aliases (always changing) — two mechanisms, on purpose.

Retrieval: recall@5 97.7% on our own small benchmark (54 memories / 44 queries). Fully local, zero external API calls.

Built mostly pairing with Muse. MiniMax (free beta) helped with code review and bug fixes.

Apache-2.0, `npm install -g open-memex`, listed in the official MCP Registry.

https://github.com/stoneskin/open-memex