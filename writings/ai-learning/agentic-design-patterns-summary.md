# Antonio Gulli《Agentic Design Patterns》导读（全书 21 章）

[← 返回目录](index.md)

> Antonio Gulli 著，https://github.com/evoiz/Agentic-Design-Patterns（21 章 + 7 个附录，每章配可运行的 Jupyter Notebook；版税全部捐给 Save the Children）
> 结构：全书 21 章，每章一个模式，按由浅入深排列；示例多用 LangChain / LangGraph 与 Google ADK。
> 覆盖范围：第 1–17 章已读，逐章要点；第 18–21 章未读，只有一句话简介。
> 我的学习笔记（第三部分讲回）见 [agentic-design-patterns-notes.md](../learning-notes/agentic-design-patterns-notes.md)。
> 阅读建议：先读第三部分（生产模式，与 AI 平台工作最直接相关），再补第一部分打底，第四部分按需读。

## 一句话

前两部分讲 agent 怎么搭（核心模式与进阶模式），第三部分讲 agent 怎么在生产里活下来（出错恢复、让人接手、答案来源），第四部分讲企业级规模化（通信、资源、推理、安全护栏、评估、优先级、探索）。

## 第一部分：核心模式（第 1–7 章）

### 第 1 章：Prompt Chaining（提示链）

复杂任务拆成一串小步骤，前一步的输出作后一步的输入（也叫 Pipeline 模式）。

- 分而治之：每步只聚焦一个操作，可靠性与可调试性都提高；单提示做多面任务容易丢指令、跑偏、错误放大。
- 每步可接外部知识与工具，不只靠模型内部知识。
- LangChain / LangGraph、Google ADK 有现成支持。

### 第 2 章：Routing（路由）

按条件动态选下一步，不再走固定线性流程。

- 核心是“判断 + 分流”：先分类（意图、状态、前一步结果），再把流程交给专门的子 agent、工具或升级通道。
- 三种实现：LLM 分类、embedding 相似度、规则（if-else）。
- 客服问答分流是典型例子；LangGraph 与 ADK 有结构化支持。

### 第 3 章：Parallelization（并行化）

独立任务并发执行，降延迟、提响应速度。

- 等外部资源（API 调用）时最划算。
- 代价是设计、调试、日志的复杂度与成本都上升。
- LCEL 的 RunnableParallel、ADK 的 LLM-Driven Delegation（协调 agent 的 LLM 识别独立子任务，并发交给专门 sub-agent）。

### 第 4 章：Reflection（反思）

执行→评价→修正的反馈环，自我纠错，提质量与准确度。

- 最有力的实现是 Producer-Critic：生产者与评审者分离，评审更客观、反馈更结构化。
- 代价是延迟、算力、上下文窗口压力（还可能撞 API 限流）。
- 单步反思可用 LCEL 实现；完整迭代需有状态工作流（如 LangGraph）。

### 第 5 章：Tool Use / Function Calling（工具调用）

让 agent 调外部系统、拿动态信息、做真实动作。

- 工具要有清晰的描述与参数，LLM 决定何时调用并生成结构化调用；框架执行调用并把结果返回。
- LangChain 用 @tool 定义工具，create_tool_calling_agent 与 AgentExecutor 搭工具 agent；ADK 有预置工具（Google Search、Code Execution、Vertex AI Search）。

### 第 6 章：Planning（规划）

复杂目标拆成可执行的顺序步骤，从反应式执行者升级为目标导向的执行者。

- LLM 按任务描述生成分步方案；显式要求规划步骤能激发这种行为。
- 从简单顺序执行（如 CrewAI 按写作计划执行）到动态系统（如 Google DeepResearch 的迭代式研究计划，随新信息调整）。

### 第 7 章：Multi-Agent Collaboration（多 agent 协作）

多个专长 agent 协作完成共同目标。

- 形式有顺序交接、并行处理、辩论、分层结构。
- 适合需要多领域专长或多个不同阶段的复杂问题。
- 关键在角色分工、任务分配与 agent 间通信。

## 第二部分：进阶模式（第 8–11 章）

### 第 8 章：Memory Management（记忆管理）

短期记忆（单次会话内上下文，受上下文窗口限制）+ 长期记忆（跨会话持久化，存外部存储、用检索取回）。

- 记忆让 agent 跟踪状态、学习、个性化交互。
- ADK 的三件套：Session（会话线程）、State（临时数据）、MemoryService（可检索的长期知识）；SessionService 管会话全生命周期（含历史事件与临时状态）。

### 第 9 章：Learning and Adaptation（学习与适应）

agent 用经验越做越好、适应新情况；“适应”是学习带来的行为或知识上的可见变化。

- SICA（自我改进编码 agent）：自己改代码提性能，产出 Smart Editor、AST Symbol Locator 等工具。
- 专长 sub-agent + overseer（监督者）管大任务、保方向。
- 上下文窗口的组织（system / core / assistant 消息）决定效率；适合一直在变、不确定或需个性化的环境。

### 第 10 章：Model Context Protocol（MCP）

开放标准，LLM 与外部应用、数据源、工具之间标准化通信。

- 客户端–服务器架构，定义资源、提示词、工具的暴露与消费方式。
- ADK 既能用现成 MCP 服务器，也能把 ADK 工具暴露为 MCP 服务器；FastMCP 简化 Python 的 MCP 服务器开发。
- 让 LLM 与真实系统交互、拿动态信息、做真实动作。

### 第 11 章：Goal Setting and Monitoring（目标设定与监控）

给 agent 明确目标 + 持续跟踪进度，把反应式系统变成主动的目标导向系统。

- 目标要 SMART（具体、可衡量、可达成、相关、有时限）；监控看 agent 动作、环境状态、工具输出。
- 监控的反馈环让 agent 调整计划或升级问题。
- ADK 里目标常放在 agent 指令中，监控靠状态管理与工具交互。

## 第三部分：生产模式（第 12–14 章）

### 第 12 章：Exception Handling and Recovery（异常处理与恢复）

检测错误、优雅处理、恢复到稳定状态，是 agent 在不可预测的真实环境里仍能有效运行的前提。

- 检测：校验工具输出、查 API 错误码、设超时。
- 处理策略：记 log、重试、回退、优雅降级、通知。
- 恢复：诊断、自我纠正或升级。

### 第 13 章：Human-in-the-Loop（人机回路）

把人的判断接进 AI 工作流，用于安全、伦理、高风险场景。

- 关键在人工监督、干预、反馈学习、决策增强；升级策略决定何时交给人。
- 代价是不好 scaling（准确率与规模的权衡），且依赖领域专家；实施难点包括培训操作员与匿名化敏感信息。

### 第 14 章：Knowledge Retrieval / RAG（知识检索）

检索（从知识库找相关片段）+ 增强（把片段放进提示词）。

- 克服训练数据过时、减少幻觉、支持领域知识、答案可归因到来源。
- GraphRAG 用知识图谱回答需多源合成的复杂问题；Agentic RAG 用 agent 主动推理、验证、精炼外部知识。
- 应用：企业搜索、客服、法律研究、个性化推荐。

## 第四部分：企业模式（第 15–21 章）

第 15–17 章已读（逐章要点）；第 18–21 章未读，只有一句话简介，读完再补。

### 第 15 章：Inter-Agent Communication / A2A（agent 间通信）

不同框架的 agent 也能协作——Google 的 A2A 协议是跨 agent 通信的开放标准，管任务委派、协调与信息交换。

- Agent Card：放在固定地址的 JSON 描述，写明 agent 的能力与调用方式，client agent 靠它发现 remote Agent。
- 任务有状态：`tasks/send`（同步）、`tasks/sendSubscribe`（流式订阅，长任务回进度）、`tasks/get` / `tasks/cancel`，还有 `input-required`（做到一半缺信息可停下反问）。
- 与 MCP 的分工：MCP 管 LLM 接上下文与工具（无状态、同步请求响应、输入输出定死）；A2A 管 agent 之间的任务协调（有状态、可同步/异步/并行、agent 自主决定处理方式）。

### 第 16 章：Resource-Aware Optimization（资源感知优化）

动态监控与管理计算、时间、金钱资源，在预算内达成目标；在更准但更贵的模型与更快但较弱的模型之间做取舍。

- 按任务难度动态选模型：难任务用强模型，简单任务用便宜模型，省成本、反应快。
- Router 先判断任务难度/复杂度，再分流到合适档位的模型。
- 质量把关：便宜模型先答，校验器判质量，不过关就升级到更高档模型重做（cascade 级联 + verifier 校验）；既不为省钱牺牲质量，也不一味用最贵模型浪费。
- 优雅降级：资源紧张时主动降档保可用。

### 第 17 章：Reasoning Techniques（推理技术）

多步逻辑推理，让 agent 的内部推理显性化；核心是推理时多分配算力（更多时间 / 步骤）。

- CoT：大问题拆小问题，一步步答。
- ToT：在 CoT 基础上允许分叉，探索多条路径、树状结构，可回溯。
- ReAct：推理与行动交错循环，做一步、看反馈、调计划、再做下一步，可自我纠错。
- CoD：多模型辩论、共同求解（与并行独立作答 + 裁判的陪审团模式不同）。
- 推理时算力（test-time compute）：多个小模型多次推理，也能达到大参数模型相似的高质量；质量不一定靠更大模型，也能靠推理时多花算力换来。

### 第 18 章：Guardrails / Safety Patterns（护栏与安全模式）

保护层，确保 agent 安全、合乎伦理、按预期运行；可在输入校验、输出过滤等多个阶段实施，防有害、有偏、无关的输出。

### 第 19 章：Evaluation and Monitoring（评估与监控）

持续、常在外部地衡量 agent 的效果、效率与合规性；定指标、建反馈环、做报告，确保性能与要求对齐。

### 第 20 章：Prioritization（优先级）

在多个可能动作、冲突目标、有限资源面前，按重要性、紧急性、依赖关系给任务排优先级，把精力集中在最关键的事上。

### 第 21 章：Exploration and Discovery（探索与发现）

让 agent 主动探索未知、发现新可能性、找出 unknown unknowns；适合开放式、复杂、快速变化的领域。
