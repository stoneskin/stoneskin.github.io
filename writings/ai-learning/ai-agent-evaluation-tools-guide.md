# Maryam Miradi《AI Agent 评测工具全景》导读

[← 返回学习清单目录](./index.md)

> **原文**：Maryam Miradi，PhD，LinkedIn 帖子，2026-11-23，[lnkd.in/p/eqXkHByS](https://lnkd.in/p/eqXkHByS)
> **分级**：［摘要即可］——本页已把 20 个工具按 5 组写到能独立成立，只看本页、跳过原文
> **编号**：第 71 份（组三 Harness 与课程）

## 导读层

### 一句话结论

生产级 agent 不能只看最终答案对不对——工具调用、检索质量、推理路径、失败步骤、延迟、成本、安全、回归，这些都得测。这篇是一张 20 个评测工具的地图，按 5 组排好，拿来当选型起点。

### 为什么值得看

评测工具这两年冒出一大堆，名字都像、定位都含糊。这篇的价值是分类：Eval 框架、RAG 与回答评测、追踪与可观测性、测试与红队、Agent 基准，5 组 20 个工具，一行一个定位。不是教你怎么用，是让你在要搭评测时知道有哪些选择、每类该找谁。

对 Stone 来说，价值在对照不在学习：PingPilot 的 eval 方法论（golden set + Verifier 一致率 + L3 毕业）刚合进 main，这篇的 5 组正好是那套方法论的工具箱对照——追踪层（Langfuse、Phoenix）对上 Verifier 的证据链，红队层（Promptfoo、garak、PyRIT）对上 L2 的对抗验证，基准层（AgentBench、τ-bench、SWE-bench）对上回归测试。作者下一步想做的横向对比（DeepEval vs Ragas vs Langfuse vs Phoenix vs Opik vs Promptfoo）还没发，出来了值得再收一次。

### 叙事主线

先立前提——最终答案正确不等于 agent 可靠；再按 5 组摊开 20 个工具；最后落到一句话：表现最好的 agent 不一定是最可靠的，目标是走出一条可靠、高效、安全的路径。

### 怎么读

只看下面的 5 组表就够了。需要搭评测时，按你要测的那一层去找对应组的工具；不需要现在选型，知道有这 5 组就够了。

## 精读层

### 1. Eval 框架（Eval Frameworks）

- **DeepEval**：LLM 应用评测框架，带指标与测试集。
- **Inspect AI**：Anthropic 出的评测框架，偏结构化评估。
- **AutoEvals**：轻量评测库，快速搭指标。
- **Evidently**：偏 ML 评估与监控，也覆盖 LLM。

### 2. RAG 与回答评测（RAG + Response Evals）

- **Ragas**：RAG 专用的评测指标（检索质量 + 回答忠实度）。
- **TruLens**：RAG 与 LLM 应用的反馈式评测。
- **LlamaIndex Evals**：LlamaIndex 生态内的评测模块。
- **LangChain Evals**：LangChain 生态内的评测模块。

### 3. 追踪与可观测性（Tracing + Observability）

- **Langfuse**：LLM 应用的追踪、评测与监控，开源。
- **Arize Phoenix**：追踪与可观测性，偏实验分析。
- **Opik**：Comet 旗下，追踪 + 评测 + 提示词管理。
- **Helicone**：LLM 可观测性与成本监控，偏生产监控。

### 4. 测试与红队（Testing + Red Teaming）

- **Promptfoo**：提示词与 LLM 输出的测试框架，红队常用。
- **Giskard**：ML 与 LLM 的测试框架，偏合规与偏见检测。
- **garak**：LLM 弱点探测器，专做越狱与安全探针。
- **PyRIT**：微软的红队自动化工具箱。

### 5. Agent 基准（Agent Benchmarks）

- **AgentBench**：多环境 agent 能力基准。
- **τ-bench**：工具调用型 agent 基准，偏真实任务。
- **BrowserGym**：浏览器操作 agent 基准。
- **SWE-bench**：软件工程任务基准，编码 agent 的标准尺子。

### 小沐的分析与判断

- 与 #70 的信任层互补：#70 的信任层提了 Ragas、Langfuse、NeMo Guardrails，这篇把同类工具按 5 组展开，两份一起读才是完整的评测工具箱。
- 与 #69 的 Eval Flywheel skill 对上：那个 skill 讲评测飞轮的方法论，这篇给工具清单。
- 选型建议：别按名气选，按你要测的那一层选——先定测什么（回答质量 / 工具调用 / 轨迹 / 安全），再从对应组里挑 1–2 个试。
- 注意：工具名录是 2026-11-23 的快照，新工具出现快，选型前再核一次各工具的最新状态。

### 证据不支持什么

- 这篇只给地图，不给比较：20 个工具都没有实测、没有分数，不能直接当选型依据。
- 作者承诺的横向对比（DeepEval vs Ragas vs Langfuse vs Phoenix vs Opik vs Promptfoo）还没发表，引用时别写成已发表。
- 各工具的一行定位来自原文的分组本身，不是小沐实测；具体能力以各工具官网为准。
