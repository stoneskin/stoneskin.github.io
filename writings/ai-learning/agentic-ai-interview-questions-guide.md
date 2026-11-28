# Atul Kumar《250 道 Agentic AI 面试题》导读

[← 返回学习清单目录](./index.md)

> **原文**：Atul Kumar，LinkedIn 帖子，2026-11-27，[lnkd.in/p/e79iseqW](https://lnkd.in/p/e79iseqW)
> **分级**：［摘要即可］——250 道题全文收在本页，题库本身就是内容，只看本页、跳过原文
> **编号**：第 72 份（组三 Harness 与课程）

## 导读层

### 一句话结论

250 道题，18 组，从 Agent 基础到编码与电脑操作——一份 agentic AI 面试的题库总汇。不是教程，是自测清单。

### 为什么值得看

题的质量高，问的都是"怎么做决定"而不是"背定义"：compounding-error 的数学、model vs harness 哪个更重要、工具调用幻觉怎么防、评测为什么要在 RL 之前。覆盖面全，18 组对应 agent 工程的完整拼图。

对 Stone 来说，两用：AI SA 面试准备的自测卷，平时设计评审的提问清单——很多题直接对应 PingPilot/WorkBuddy 的设计决策（终止条件、HITL、评测先于 RL、成本与可观测性）。答不上来的题，就是该去翻的学习资料：#70 架构、#71 评测工具、#74 治理词表都是这份题库的参考答案来源。

### 叙事主线

按 agent 从"单个循环"到"生产系统"的顺序排：先懂 loop 与规划，再懂工具与 MCP，再懂记忆与 RAG，再懂多 agent 与框架，最后是评测、安全、生产、成本、系统设计。

### 怎么读

不用从头读到尾——按你想练的那组挑题，先口头答一遍，答不上的再去翻对应的学习资料。

## 精读层

250 道题全文如下，按原文 18 组排。题库出处是 K21Academy 的培训材料（LinkedIn 文档，15 页），题目按 Q001–Q250 编号。

### AGENT FUNDAMENTALS

- **001.** How is an agent different from a chain and a workflow?
- **002.** When should you NOT build an agent?
- **003.** Walk me through the core agent loop. What are its stop conditions?
- **004.** Explain the autonomy spectrum. Where should your agent sit?
- **005.** Explain ReAct in depth. What are its failure modes?
- **006.** How does an agent decide to call a tool vs answer from knowledge?
- **007.** What is the difference between reactive and proactive agents?
- **008.** Explain stateless vs stateful agents.
- **009.** What is agent state, and how is it different from memory?
- **010.** How do you design termination conditions for an agent?
- **011.** Walk me through the compounding-error math for agents.
- **012.** How do you design the system prompt for an agent?
- **013.** How does an agent's tool call differ from a workflow's function call?
- **014.** Name three anti-patterns in agent design.

### HARNESS & PATTERNS

- **015.** What belongs to the model vs the harness in an agent?
- **016.** For a coding agent like Claude Code: model or harness, which matters more?
- **017.** Explain the 6 canonical single-agent architectures.
- **018.** What is the Router pattern? LLM vs rule-based routing?
- **019.** What are subagents, and when should you spawn one?
- **020.** What is harness engineering vs prompt and context engineering?
- **021.** What are Agent Skills? When do they beat a tool or MCP server?
- **022.** A new model ships. Which parts of your harness do you revisit?
- **023.** What is the Critic (verification) pattern for agents?
- **024.** What is the Map-Reduce pattern for agents?
- **025.** Explain the Hierarchical Agent pattern.
- **026.** How would you decompose a travel-planning task across sub-agents?
- **027.** How does an agent prioritize competing goals or tasks?
- **028.** Compare ReAct, Plan-and-Execute, ToT, Reflexion and LLM Compiler.

### PLANNING & REASONING

- **029.** Plan-then-execute vs ReAct: which wins when?
- **030.** Compare agent planning strategies: CoT, ToT, GoT.
- **031.** Why does Chain-of-Thought matter in agentic applications?
- **032.** What are the trade-offs of CoT inside an agent loop?
- **033.** How does self-consistency prompting improve reasoning?
- **034.** When is tree-of-thought's extra cost justified?
- **035.** When do reflection loops actually help, and what do they cost?
- **036.** A sub-agent is wrong and reflection can't fix it. What now?
- **037.** Reasoning model vs fast model inside an agent loop: when each?
- **038.** How should an agent allocate reasoning effort across steps?
- **039.** What do you do with the model's reasoning between tool calls?
- **040.** How does inference-time compute scaling change agent design?
- **041.** Your long-running agent drifts onto the wrong task. Fix it.
- **042.** Your agent loops or gives up too early. Diagnose both.

### TOOL CALLING

- **043.** How does tool calling work mechanically, end to end?
- **044.** "The model executes the tool." What's wrong with that?
- **045.** Parallel tool calls vs tool-choice forcing: when each?
- **046.** What makes a good tool definition? Give concrete rules.
- **047.** What does strict mode on a tool schema guarantee, and not?
- **048.** How should tool errors be surfaced back to the model?
- **049.** Consolidated vs granular tools: how do you decide?
- **050.** How do you make tool outputs token-efficient?
- **051.** Structured output vs function calling: what's the difference?
- **052.** What is tool-call hallucination, and how do you defend?
- **053.** Right tool, wrong parameters. How do you fix it?
- **054.** Many tools, and the agent picks the wrong one. How do you fix it?
- **055.** The tool succeeds but returns garbage. How do you handle it?
- **056.** How do you avoid malformed arguments? Constrained decoding?

### MCP & A2A

- **057.** What is MCP, and what problem does it solve?
- **058.** Explain MCP's Host / Client / Server architecture and primitives.
- **059.** Why use MCP instead of an OpenAPI spec?
- **060.** Building an MCP server: tool, resource, or prompt?
- **061.** MCP stdio vs HTTP transport: when do you choose each?
- **062.** How does MCP differ from function calling?
- **063.** 6 MCP servers, 130 tools, 45k tokens of schema. What do you do?
- **064.** Expose tools as a code API the agent scripts against: trade-offs?
- **065.** How does auth for a remote MCP server work? What goes wrong?
- **066.** Your agent calls 40 tools. What do you cut first?
- **067.** What does A2A solve that MCP does not?
- **068.** How does an A2A client discover an agent's capabilities?
- **069.** What does "opaque agent" mean in A2A, and why does it matter?
- **070.** Exposing your agent to another company's agent: what crosses?

### CONTEXT ENGINEERING

- **071.** What is context engineering vs prompt engineering?
- **072.** Why can't a bigger context window replace context engineering?
- **073.** Your context fills up mid-task. What are your options?
- **074.** What is context rot, and which compaction strategies work?
- **075.** How does compaction differ from structured note-taking?
- **076.** Why does compaction conflict with prompt caching?
- **077.** What is context pollution, and how do you deal with it?
- **078.** How do you budget tokens across memory types?
- **079.** Design a token budget for a 200k context. How do you enforce it?
- **080.** Message 30: 40K tokens, $0.40 per reply. How do you compress?
- **081.** Prompt cache hit rate is 20%, not 90%. How do you debug it?
- **082.** How do sub-agents help manage context?
- **083.** How do you manage context handed between agents?
- **084.** How does a coding agent avoid stuffing the whole repo in context?
- **085.** What belongs in an AGENTS.md or CLAUDE.md file?

### AGENT MEMORY

- **086.** LLMs are stateless. How does agent memory actually work?
- **087.** Short-term, long-term, episodic, semantic memory: explain each.
- **088.** Working memory vs persistent memory in agent design.
- **089.** Cross-session memory: vector store or rolling summary?
- **090.** What is the write-back loop in memory-augmented generation?
- **091.** Why is forgetting a feature? Which strategies work?
- **092.** How do you prevent memory leaks between users?
- **093.** How do you handle memory conflicts when facts change?
- **094.** How do you share memory across agents?
- **095.** How do you evaluate a memory system?
- **096.** What should never be written into long-term memory?
- **097.** Design memory and personalisation for millions of users.
- **098.** RAG hits and memory preferences conflict. Who wins?
- **099.** Design a conversational system with memory across sessions.
- **100.** Agent does a task 500 times a week, never improves. Make it learn.

### AGENTIC RAG

- **101.** What is agentic RAG vs single-shot RAG?
- **102.** When does retrieval-as-a-tool beat retrieve-then-generate?
- **103.** Retrieval as an MCP tool vs a retrieval API?
- **104.** Replace the vector index with grep and file reads? Discuss.
- **105.** Chunked RAG vs a browsable knowledge tree: when each?
- **106.** How do you handle multi-hop questions in agentic RAG?
- **107.** When is GraphRAG worth the complexity?
- **108.** Why add a reranker after vector search?
- **109.** What is Contextual Retrieval, and how does it help?
- **110.** How does retrieval over code differ from retrieval over prose?
- **111.** "Long context made RAG obsolete." Argue both sides.
- **112.** When should the agent abstain and say "I don't know"?
- **113.** Relevant docs come back, but answers are still poor. Why?
- **114.** The answer is in chunk #12 but top-k=5. How do you get it?

### MULTI-AGENT SYSTEMS

- **115.** When does multi-agent beat single-agent, and when is it worse?
- **116.** Explain orchestrator-worker. What's the real benefit?
- **117.** What are handoffs, and how do they differ from orchestration?
- **118.** Describe the Supervisor multi-agent pattern.
- **119.** Coordinator, peer-to-peer, consensus: compare the patterns.
- **120.** Orchestrator + subagents: what crosses the boundary?
- **121.** A router sends a compound-intent request to one agent. Now what?
- **122.** The router misroutes to the wrong specialist. What happens?
- **123.** How do you resolve conflicts when agents disagree?
- **124.** Your agent gets conflicting answers from tools. Reconcile them.
- **125.** How do you keep async multi-agent tasks consistent?
- **126.** Two agents deadlock. How do you detect and break it?
- **127.** Can multiple agents collaborate to improve accuracy?
- **128.** Give 5 ways to cut costs in a multi-agent system.
- **129.** Which metrics do you track for multi-agent in production?
- **130.** Multi-agent scores improved. Was it really the pattern?

### AGENT FRAMEWORKS

- **131.** Compare LangGraph, CrewAI, AutoGen, LlamaIndex, SmolAgents.
- **132.** Why does LangGraph exist when LangChain already has agents?
- **133.** LangGraph: explain nodes, edges, state and reducers.
- **134.** How do you manage state in complex agent workflows?
- **135.** What is the State Machine pattern for agents?
- **136.** How does CrewAI's multi-agent approach differ?
- **137.** Explain AutoGen (AG2) and its conversational pattern.
- **138.** OpenAI Agents SDK vs third-party frameworks?
- **139.** How do frameworks differ in error recovery?
- **140.** Compare observability and debugging across frameworks.
- **141.** When is LangChain overkill? Give your decision framework.
- **142.** Framework or your own agent loop? Defend it.
- **143.** Result changed: framework, model, or harness? How do you tell?
- **144.** You're locked into a vendor framework. What now?
- **145.** How do you migrate frameworks in production without downtime?
- **146.** New agentic project today: what's your tech stack?

### AGENT EVALS

- **147.** How do you evaluate an agent? Trajectory vs outcome evals.
- **148.** pass@k vs pass^k: why does it matter in production?
- **149.** How is agent eval different from LLM eval?
- **150.** What's the difference between capability and regression evals?
- **151.** How do you test an agent in CI in under five minutes?
- **152.** How do you build a deterministic replay harness for evals?
- **153.** Flaky, nondeterministic evals: how do you get real numbers?
- **154.** Users change their minds mid-conversation. Build that eval.
- **155.** How do you evaluate hundred-step, hours-long tasks?
- **156.** How do you prove your agent actually got better?
- **157.** How do you stop agents learning "looks right" shortcuts?
- **158.** Why must you read transcripts, not just scores?

### JUDGES & BENCHMARKS

- **159.** What is LLM-as-judge, and what are its known biases?
- **160.** Pointwise vs pairwise judging: which is more reliable?
- **161.** How do you calibrate your LLM judge?
- **162.** What are code-based graders good at, and where do they fail?
- **163.** Why not pick models by MMLU, HumanEval or SWE-bench?
- **164.** How can SWE-bench pass rates mislead?
- **165.** Passes hidden tests, but maintainers would reject the PR. Why?
- **166.** What is benchmark contamination? How do you detect it?
- **167.** What do you make of agent benchmarks being reward-hacked?
- **168.** 99.9% on its own harness, 62.7% on standard. Trust which?
- **169.** Same model, two clusters differ by 6 points. Infra noise?
- **170.** Design an agentic verifier that runs checks. Calibrate it.

### AGENT SECURITY

- **171.** Prompt injection vs jailbreak: what's the difference?
- **172.** How does injection via tool results work? Mitigations?
- **173.** What is the lethal trifecta? How do you design around it?
- **174.** Agent reads untrusted email and web and calls tools. Defend it.
- **175.** Explain the confused deputy problem for LLM agents.
- **176.** Excessive agency (OWASP): name its three sub-types.
- **177.** What does the OWASP Agentic Top 10 add to the LLM Top 10?
- **178.** What is memory poisoning, and why is it worse than injection?
- **179.** How can a compaction summary become an injection channel?
- **180.** Explain markdown-image exfiltration and how you'd defend.
- **181.** What is slopsquatting? Stop agents installing fake packages.
- **182.** What are the risks of third-party MCP servers?
- **183.** Can prompt injection spread agent-to-agent like a worm?

### GUARDRAILS & HITL

- **184.** How do you sandbox a code-executing agent?
- **185.** How do you implement least privilege for agents?
- **186.** Design approval gates that don't become rubber-stamping.
- **187.** Users approve 93% of prompts. Design a classifier auto mode.
- **188.** Kill switch vs circuit breaker: why do you need both?
- **189.** Shared service account or on-behalf-of the user?
- **190.** Walk me through threat-modeling an agent before it ships.
- **191.** What security problems are unique to multi-agent systems?
- **192.** What guardrails does a production agent loop need?
- **193.** When should an agent pause for human input?
- **194.** Agent deleted a production database. Prevent irreversible actions.
- **195.** How do agents handle rollback and compensating actions?

### PRODUCTION RELIABILITY

- **196.** Agent stuck in an infinite loop. How do you detect and break it?
- **197.** Explain agent circuit breakers. Why do they matter?
- **198.** How do you implement error recovery for agents?
- **199.** Card charged twice, but the trace shows one call. What happened?
- **200.** How does checkpointing enable pause and resume?
- **201.** How do you build agents that survive days-long tasks?
- **202.** A tool call takes 20 minutes or needs user input. Model it.
- **203.** User hits Stop mid tool call. Design streaming and cancellation.
- **204.** Works in the demo, fails in production. Your approach?
- **205.** Ship a system-prompt change without breaking customers?
- **206.** Design an always-on agent that wakes on schedules and events.
- **207.** Define SLOs when every span returns 200. What do you alert on?

### COST & OBSERVABILITY

- **208.** How do you cut cost and latency without wrecking quality?
- **209.** Your agent burns too many tokens per task. Reduce it.
- **210.** Your agent keeps exceeding its budget. Enforce limits.
- **211.** Agent bill jumped $8k to $40k in a month. Find out why.
- **212.** Your agent takes too long to finish. Speed it up.
- **213.** Beyond RPM limits, what should an agent cost firewall cap?
- **214.** What does good observability look like for agents?
- **215.** What are traces and spans in an agentic system?
- **216.** What should trajectory logging capture?
- **217.** What's the minimum trace to replay a wrong ticket purchase?
- **218.** The agent erred three days ago. Reproduce it from the trace.

### SYSTEM DESIGN

- **219.** Design a customer support multi-agent system with escalation.
- **220.** Design a Deep Research Agent.
- **221.** Design an AI Coding Agent.
- **222.** Design a real-time voice AI agent.
- **223.** Design a browser agent system with enterprise security.
- **224.** Design an agent platform for 100+ internal teams.
- **225.** Design an agent safety and kill-switch system.
- **226.** Design an agent cost attribution system.
- **227.** Design an agent evaluation infrastructure.
- **228.** Design a human-agent handoff system.
- **229.** Design an agent for a regulated industry (healthcare/finance).
- **230.** Design a Text-to-SQL agent over thousands of tables.
- **231.** Design an AI email assistant agent.
- **232.** Design the approval flow for an expense-report agent.
- **233.** Design a platform where tenants bring their own MCP servers.
- **234.** Design an AI gateway routing GPT, Claude, Gemini with fallback.

### CODING & COMPUTER USE

- **235.** How do computer-use agents work?
- **236.** How do browser agents work, and what are their unique risks?
- **237.** Why are computer-use agents harder to make reliable?
- **238.** Coding agents vs research agents: how do they differ?
- **239.** Code-generating vs tool-calling agents: what's the difference?
- **240.** How do you build a code execution agent safely in a sandbox?
- **241.** Threat-model a coding agent that runs generated code.
- **242.** Implement a minimal agent loop with tool dispatch and a step cap.
- **243.** Implement an MCP server with a tool, a resource and a prompt.
- **244.** How would you scale an MCP server to 10,000 requests/sec?
- **245.** Fine-tuned a model for agent abilities? How did you get data?
- **246.** The agent calls tools wrong: fix it with SFT or RL?
- **247.** How does human feedback get absorbed by an agent?
- **248.** Why should evals come before RL for agents?
- **249.** How do you handle multimodal inputs and outputs in agents?
- **250.** Real or simulated environment vs tool agent: what differs?


### 小沐的分析与判断

- 这份题库的价值在"问法"——它问的不是概念，是 trade-off 和 failure mode；建议当面试前的自测卷用，也当设计评审的提问清单用（比如 Q010 终止条件、Q184–Q195 Guardrails 与 HITL，直接能拿去审 PingPilot 的 L 级别设计）。
- 18 组的顺序本身就是学习路径：单 agent 循环 → 工具与协议 → 记忆与检索 → 多 agent → 评测与安全 → 生产与成本 → 系统设计。
- 最值得练的三组：评测（Q147–Q170，含 Judge 与基准）、安全与护栏（Q171–Q195）、生产可靠性与成本（Q196–Q218）——面试最爱问、生产最容易翻车的地方。

### 证据不支持什么

- 只有题目，没有答案——题库没给标准答案，答案得自己写；本页不补答案，补了就是小沐的答案不是题库的。
- 题目来自 K21Academy 的培训材料（LinkedIn 文档），不是某家公司的真实面试题；"250 道来自 GitHub 真实面试准备仓库"是帖子正文的说法，题库本身没逐题标注出处。
- 帖子附的两个免费资源（Agentic AI Interview Guide、Agentic AI Masterclass）链接目的地未验证。
