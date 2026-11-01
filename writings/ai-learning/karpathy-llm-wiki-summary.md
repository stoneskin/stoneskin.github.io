# Karpathy《LLM Wiki》详细摘要：三层架构与三个操作

[← 返回目录](index.md)

> 来源（一手原文）：Andrej Karpathy《LLM Wiki》，GitHub Gist，2026-04-04，https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
> 导读见 [karpathy-llm-wiki-guide.md](./karpathy-llm-wiki-guide.md)。本篇是详细摘要——原理、三层、三操作、索引/日志、落地步骤、一个现成的实现（Graphify），写到不看原文也能学到精髓。
> 原文 174 行，是一份 idea file（想法文件），不是代码：它只讲模式，不规定具体实现。目录结构、schema 写法、页面格式、工具选择都由你和你的 agent 按自己的域定。

## 1. 核心思想：从"每次重算"到"编译一次"

### 1.1 RAG 的问题：不积累

大多数人用 LLM 处理文档的方式是 RAG：上传一堆文件，提问时 LLM 检索相关片段、生成答案。这能用，但 LLM 每次都在从头重新发现知识——没有积累。问一个要综合五份文档的微妙问题，LLM 每次都得重新找、重新拼相关碎片。什么都没积累下来。NotebookLM、ChatGPT 文件上传、大多数 RAG 系统都是这个路子。

### 1.2 编译式 wiki：知识一次编译、持续保鲜

换一个做法：不只在提问时从原文检索，而是让 LLM **增量地建一个持久的 wiki**——一个结构化、互相链接的 markdown 文件集合，夹在你和原始资料之间。新资料进来，LLM 不只是把它编个索引留待以后检索；它读它、抽出关键信息、合进已有的 wiki——更新实体页、修订主题摘要、标出新数据与旧结论矛盾的地方、强化或挑战正在形成的综合。知识**编译一次，然后保持最新**，而不是每次提问都重新推导。

关键区别：**wiki 是一个持久的、不断复利的产物**。交叉引用已经在那了。矛盾已经标出来了。综合已经反映了你读过的所有东西。每加一个资料、每问一个问题，wiki 就更富一点。

### 1.3 分工：人做策展，LLM 做记账

你永远（或几乎永远）不自己写 wiki——LLM 写、维护全部内容。你负责找资料、探索、问对问题。LLM 做所有的苦活——总结、交叉引用、归档、记账，这些正是让知识库长期有用的事。

实际做法：Karpathy 一边开着 LLM agent，一边开着 Obsidian。LLM 根据对话做修改，他实时浏览结果——跟链接、看图谱、读更新过的页面。"Obsidian 是 IDE，LLM 是程序员，wiki 是代码库。"

### 1.4 适用范围

这个模式能用在很多场景：

- **个人**：跟踪自己的目标、健康、心理、自我提升——归档日记、文章、播客笔记，逐步建立一个关于自己的结构化图景。
- **研究**：几周、几个月深挖一个主题——读论文、文章、报告，增量地建一个带 evolving thesis 的综合 wiki。
- **读书**：每读一章归档一章，给人物、主题、情节线建页面、看它们怎么连。到读完，你有了一个丰富的 companion wiki。Karpathy 举的例子是 Tolkien Gateway 那种粉丝 wiki——几千个互联页面覆盖人物、地点、事件、语言，由志愿者社区多年建成；你读书时可以自己建一个类似的，LLM 做全部交叉引用和维护。
- **业务/团队**：由 LLM 维护的内部 wiki，喂 Slack 讨论、会议记录、项目文档、客户电话；可以有人在环里审更新。wiki 保持最新，因为 LLM 做了团队里没人想做的维护。
- **竞争分析、尽调、旅行规划、课程笔记、爱好深挖**——任何需要长期积累知识、希望它被组织起来而不是散落各处的事。

## 2. 三层架构

### 2.1 第一层：Raw sources（原文层）——不可改的真相来源

你精选的原始资料集合：文章、论文、图片、数据文件。**不可变**——LLM 只读不改。这是你的真相来源（source of truth）。

要点：精选（curated）是关键词——不是什么都往里塞，而是你挑过的、值得长期保存的资料。原文层不动，wiki 层才敢大胆改；出了问题永远能回溯到原文核对。

### 2.2 第二层：The wiki（wiki 层）——LLM 全权所有的 markdown

一个 LLM 生成的 markdown 文件目录：摘要、实体页、概念页、比较、总览、综合。**LLM 完全拥有这一层**：它建页面，新资料进来时更新页面，维护交叉引用，保持整体一致。你读它，LLM 写它。

页面种类（原文列的）：summaries（摘要）、entity pages（实体页）、concept pages（概念页）、comparisons（比较）、overview（总览）、synthesis（综合）。实际长什么样由你的域定。

### 2.3 第三层：The schema（纪律层）——人机共写的配置文件

一个文档（Claude Code 用 CLAUDE.md，Codex 用 AGENTS.md），告诉 LLM：wiki 怎么组织、约定是什么、吃进资料、回答问题、维护 wiki 时按什么流程走。**这是关键配置文件——它把 LLM 从通用聊天机器人变成有纪律的 wiki 维护者**。你和 LLM 随着摸索、按你的域共同演化它。

为什么 schema 是关键：没有 schema，LLM 每次都是一次性回答；有了 schema，它每次会话都按同一套纪律行事（先读 schema，再动手）。schema 是"让 LLM 稳定地做同一件事"的机制——这正是 harness 的思想（规则导出、纪律文件）。

## 3. 三个操作

### 3.1 Ingest（吃进）：一个资料能碰 10–15 个页面

你把新资料丢进原文集合，告诉 LLM 处理它。示例流程：LLM 读资料、跟你讨论关键要点、在 wiki 里写一页摘要、更新 index、更新 wiki 里相关的实体页和概念页、往 log 里追加一条。**一个资料可能碰到 10–15 个 wiki 页面**。

Karpathy 个人偏好一次只吃一个资料、全程参与——他读摘要、检查更新、指导 LLM 强调什么。但也可以批量吃很多资料、少监督。按你的风格定，然后把流程写进 schema，供以后会话用。

要点：ingest 不是"存起来"，是"读进去并合进已有的知识"——更新、修订、标矛盾。一次 ingest 的产出是 wiki 的一次进化。

### 3.2 Query（问）：好的答案要存回 wiki

你对着 wiki 提问。LLM 找相关页面、读它们、综合出带引用的答案。答案的形式随问题而定——markdown 页、比较表、幻灯片（Marp）、图表（matplotlib）、画布。

**重要洞见：好的答案可以作为新页面存回 wiki。** 你要来的比较、做的分析、发现的联系——这些都有价值，不应该消失在聊天记录里。这样你的探索就像吃进的资料一样，在知识库里复利。

### 3.3 Lint（体检）：定期健康检查

定期让 LLM 给 wiki 做健康检查。查：

- 页面之间的矛盾
- 被新资料取代的过期主张
- 没有入链的孤页（orphan pages）
- 被提到但没有自己页面的重要概念
- 缺失的交叉引用
- 可以用网络搜索填补的数据缺口

LLM 还擅长建议新的调查问题和新的资料来源。这让 wiki 在长大过程中保持健康。

## 4. 索引与日志：规模化的两个文件

### 4.1 index.md（目录）：先读它，再钻进去

内容导向的目录：wiki 里每页列出来，带链接、一句话摘要、可选的元数据（日期、来源数）。按类别组织（实体、概念、来源等）。LLM 每次 ingest 都更新它。回答问题时，LLM 先读 index 找相关页面，再钻进去。

这个办法在中等规模下"出乎意料地好"（~100 份资料、几百页），而且**不需要 embedding 的 RAG 基建**。索引就是检索——先读目录，再读正文。

### 4.2 log.md（时间线）：可 grep 的历史

时间导向的、只追加的记录：发生了什么、什么时候——ingest、query、lint pass。实用技巧：每条用一致的前缀开头（例如 `## [2026-04-02] ingest | Article Title`），这样 log 就能用简单的 unix 工具解析——`grep "^## \[" log.md | tail -5` 给你最近 5 条。log 给出 wiki 演化的时间线，也帮 LLM 理解最近做了什么。

index 是"有什么"（空间），log 是"发生了什么"（时间）。两个文件分工不同。

## 5. 可选工具

到某个时候，你可能想建小工具帮 LLM 更高效地操作 wiki。最明显的是 wiki 页面的搜索引擎——小规模下 index 文件就够，但 wiki 长大后你想要真正的搜索。

Karpathy 点名的工具是 **qmd**（https://github.com/tobi/qmd）：本地 markdown 搜索引擎，混合 BM25/向量搜索 + LLM 重排，全在设备上；有 CLI（LLM 可以 shell 出去调它）和 MCP server（LLM 可以把它当原生工具用）。也可以自己 vibe-code 一个简单的搜索脚本——需要时再说。

## 6. 实用技巧（原文的 tips）

- **Obsidian Web Clipper**：浏览器扩展，把网页文章转成 markdown；快速把资料弄进原文集合。
- **图片下载到本地**：Obsidian 设置 → 文件与链接，把"附件文件夹路径"设成固定目录（例如 `raw/assets/`）；再在设置 → 快捷键里搜"Download"，找到"下载当前文件附件"绑个快捷键（例如 Ctrl+Shift+D）。剪藏文章后按一下，所有图片下载到本地磁盘。这样 LLM 可以直接看图、引用图，而不依赖可能失效的 URL。注意：LLM 不能一次读内嵌图片的 markdown——变通办法是先让 LLM 读文字，再单独看部分或全部引用的图片来补上下文。有点笨但够用。
- **Obsidian 的图谱视图**：看 wiki 形状的最好办法——什么连着什么、哪些是枢纽页、哪些是孤页。
- **Marp**：基于 markdown 的幻灯片格式，Obsidian 有插件；可以直接从 wiki 内容生成演示。
- **Dataview**：Obsidian 插件，对页面 frontmatter 跑查询。如果你的 LLM 给 wiki 页面加 YAML frontmatter（标签、日期、来源数），Dataview 可以生成动态表格和列表。
- **wiki 就是一个 markdown 的 git 仓库**：版本历史、分支、协作，白送。

## 7. 为什么能成

维护知识库最烦的部分不是读和想——是记账：更新交叉引用、保持摘要最新、标出新数据与旧结论矛盾的地方、保持几十个页面一致。人放弃 wiki，是因为维护负担长得比价值快。LLM 不会烦、不会忘更新一个交叉引用、一次能改 15 个文件。wiki 能维持下去，是因为**维护成本近零**。

人的工作是：精选资料、指导分析、问好问题、想清楚这一切意味着什么。LLM 的工作是其余一切。

这个想法在精神上与 Vannevar Bush 1945 年的 Memex 相通——个人、精选的知识库，文档之间靠关联小径组织。Bush 的愿景比后来的 web 更接近这个：私人、主动精选、文档之间的联系与文档本身同等重要。他解决不了的那部分是"谁来维护"。LLM 解决了。

## 8. 原文没讲什么（注意点）

- **这是 idea file，不是实现**：原文明确说它是故意抽象的——目录结构、schema 写法、页面格式、工具，都取决于你的域、偏好、LLM 选择。一切模块化——有用的拿，没用的忽略。不要把它当操作手册，要把它贴给你的 agent、一起实例化一个适合你的版本。
- **没有置信度与遗忘机制**：原文没讲主张的可信度怎么打分、旧主张怎么衰减或被取代、知识怎么遗忘。它的 lint 能发现矛盾与过期，但没有"主张随时间变弱"的机制——实现时要自己定（比如给主张加置信度、给来源加时间权重）。
- **规模上限**：index 在 ~100 份资料、几百页时"出乎意料地好"；再大就要上搜索（qmd 或自己写）。原文没给更大规模的方案，只给了方向。
- **质量取决于 LLM 与 schema**：wiki 的质量 = LLM 的能力 × schema 的纪律。schema 写得含糊，wiki 就会松散；这是"人机共写 schema"要持续投入的原因。

## 9. 落地步骤与三处用途的映射

> 本节是注：原文没写这三处映射，是按你的三件事对出来的。

### 9.1 通用落地步骤

1. 选一个域（越小越好，先跑通再扩大）。
2. 建三层：`raw/`（原文，不可改）、`wiki/`（LLM 写的 markdown）、schema 文件（CLAUDE.md 或 AGENTS.md，写清组织、约定、三操作流程）。
3. 把 Karpathy 的 gist 贴给你的 agent，让它按你的域实例化 schema（共写第一版）。
4. 一次吃一个资料：agent 读、讨论要点、写摘要页、更新 index 与相关页、记 log；你全程看，指导强调什么。
5. 问问题：对着 wiki 问，好的答案存回 wiki 当新页面。
6. 定期 lint：让 agent 体检（矛盾、过期、孤页、缺页、缺引用、数据缺口），按结果补资料或修页面。
7. 需要时再加工具：先靠 index + log 跑到 ~100 份资料；大了再上 qmd 或自己写搜索。

### 9.2 映射到 open-memex

- wiki 层 = 编译后的记忆（不是原始记录，是 LLM 维护的综合）。
- schema = capture 规则（什么记、怎么记、谁有权改）。
- lint = 校验 pass（矛盾、过期、孤页——正好是记忆保鲜要查的三项）。
- log.md = 记忆的时间线（每次 capture、每次校验都记一条，可 grep）。
- Graphify（今早那篇）是这个模式在代码库上的现成实现：它建的图就是 wiki 的一种形态，边分 EXTRACTED/INFERRED 带置信度——open-memex 可以借它的边标注思路。

### 9.3 映射到本地文件组织

- lib + 工作区已经是 wiki 的雏形：raw 是原文与记录（聊天记录、收到的文件），wiki 是总结与导读，schema 是 AGENTS.md 与 MEMORY.md。
- 缺的是 lint 那一步：定期体检——哪些总结过期了（比如已 merge 的 PR 状态）、哪些文件是孤页（没人链）、哪些结论互相矛盾。
- index.md 的角色现在由 00-lib-index.md 担着（目录 + 一句话摘要），log.md 的角色由 memory/ 下的日期日志担着（时间线）。按 Karpathy 的模式，这两份文件就是索引与日志，不用另起炉灶。

### 9.4 映射到 WorkBuddy 的 AI harness

- harness 的规则导出 + CLAUDE.md/AGENTS.md 就是 schema 文件：它告诉 agent 怎么维护项目知识、按什么纪律行事。
- `.brain/` 文件夹（index.md、architecture.md、decisions.md、changelog.md、deployment.md）是这个模式在项目里的轻量变体：index 是目录，decisions 是决策页，changelog 是 log。
- 落地时：WorkBuddy 的项目 wiki 按三层建——raw 是需求文档/会议记录/代码（不可改），wiki 是 agent 维护的架构与决策页，schema 是 harness 导出的规则；ingest 吃进新需求、query 回答"这个模块为什么这样设计"、lint 定期查"代码改了、文档没跟上"的地方。

## 10. 一个现成的实现：Graphify（代码库上的编译式知识图谱）

> 来源：Graphify-Labs/graphify（GitHub，Apache-2.0，v0.9.99，2026-10-30 刚更新；~14 万 stars）。这是 Karpathy 模式在代码库上的一个现成实现——它建的图就是 wiki 的一种形态。评测数字是 README 自报的，未独立验证。

### 10.1 它是什么

Graphify 把一个代码库（连同它的文档、SQL schema、配置、PDF）变成一张可查询的知识图谱，是一份给 Claude Code、Cursor、Codex、Gemini CLI 等 20+ 种 agent 用的 `/graphify` skill。核心理念与 LLM Wiki 相同：**知识编译一次，而不是每次提问都重新找**——只不过编译的产物是一张图（节点 + 边）而不是一堆 markdown 页。

### 10.2 它怎么实现三层

- **Raw 层**：代码库 + 文档 + SQL schema + 配置 + PDF。Graphify 只读不改原文（源文件不动）。
- **Wiki 层**：编译产物在 `graphify-out/` 里——`graph.json`（完整、可查询的图）、`graph.html`（可交互、可搜索、可过滤的图）、`GRAPH_REPORT.md`（关键概念、意外的关联、建议追问的问题）。`/graphify . --wiki` 还能再建一份 markdown wiki——这是最接近 Karpathy wiki 层的那部分。
- **Schema 层**：`/graphify` skill 本身（告诉 agent 怎么建图、怎么查、怎么维护）+ CLI 配置。skill 就是纪律文件。

### 10.3 它怎么实现三操作

- **Ingest**：在 agent 里打 `/graphify .`，扫描整个文件夹建图；`/graphify add <arXiv/YouTube 链接>` 加一篇论文或一个视频；`graphify hook install` 装 git hook，每次提交/切换分支自动重建——这就是"保持最新"的那一步。
- **Query**：`graphify query "<问题>"`（对着编译好的图问）、`graphify path A B`（两概念之间的最短路径，整体置信度 = 最弱那一跳）、`graphify explain "<概念>"`（讲清一个概念）。
- **Lint**：README 里没有 Karpathy 式 lint 操作（查矛盾、过期、孤页、缺页）。最接近的是图的置信度机制（路径置信度 = 最弱一跳，弱的环节一目了然）和社群/枢纽分析（Leiden 社群检测 + god node 标出）。矛盾与过期这两项，Graphify 没给现成做法——实现时要自己补（比如定期重建 + 对比，或沿用 Karpathy 的 lint 流程）。

### 10.4 关键机制：确定性解析 + 边带置信度

- **代码用 tree-sitter 本地解析**（~40 种语言），确定性、不走 LLM、代码不出本机。代码边是"抽出来"的，不是"推出来的"——出处比 Karpathy 的 markdown wiki 更硬。
- **每条边都标 EXTRACTED（原文里明确有的）或 INFERRED（它推断的），带置信度**。推断的和直接读到的分得清——这正是 open-memex 想借的边标注思路。
- **非代码材料（文档/PDF/图片/视频）要走 LLM 做语义抽取**（可用 Gemini、Kimi、Claude、OpenAI、DeepSeek、Ollama、Bedrock 或 Claude CLI）；只跑代码可以完全离线。所以"不用 LLM"只对代码成立。
- **安装**：PyPI 包名是 `graphifyy`（两个 y，CLI 仍叫 `graphify`），`uv tool install graphifyy` 再 `graphify install`（自动识别 agent）。另有付费的 Graphify Cloud（README 里推，14 天试用）。
- **README 自报的评测**（未独立验证）：LOCOMO（n=300）recall@10 0.497（mem0 0.048、supermemory 0.149），QA 准确率 45.3%；LongMemEval-S QA 76%（与 dense RAG 持平）；ERPNext 跨工具关键事实覆盖 82.0%（grep/read 基线 70.8%）；建图 0 LLM credits。

### 10.5 它与原文模式的差别

- 编译产物是图 + 报告，不是 markdown 页（`--wiki` 才能出 markdown wiki）；Karpathy 的 wiki 层是人可读的 markdown，Graphify 的图是机器可读的、靠 graph.html 给人看。
- 代码解析是确定性的（不出 LLM），出处更硬；但 wiki 层的"综合"（synthesis）主要靠 GRAPH_REPORT.md，不像 Karpathy 的 wiki 那样有一整套互相链接的主题页。
- 没有 lint 操作（见 10.3）；维护靠 git hook 自动重建（重建 = 重新编译，不是增量体检）。
- 主场景是代码库；个人知识管理（论文/笔记）是副线（靠语义抽取 + `/graphify add`）。
