# MIT 6.S950《Agency with AI》课程全景（学习清单第 28 份 · 原文 + 导读成对收录）

[← 返回目录](index.md)

收录日期：2026-10-22。收录方式：原文与导读成对——原文定锚，导读给地图；两者定性分开标注，不混引。

## 原文侧：课程官网

- 来源：MIT EECS 公开课 6.S950 官网 https://agencyai.mit.edu/ （2026-10-22 小沐直读核对）
- 课程全名：6.S950 Agency with AI: Effective AI Use in Applied Machine-Learning Projects（Fall 2026，12 学分，Course 6 选修）
- 讲师：Shen Shen（MIT 资深教学讲师，主讲 6.390 机器学习导论）
- 先修（严格执行）：6.390 机器学习、6.101 编程基础、6.121 算法导论——默认学生已有扎实的 ML 与 CS 基础，不教基础，只教在真实 ML 工程中正确地使用 AI
- 官网课程描述要点（原文口径）：
  - 核心概念 Agency 的定义：the judgment about what to delegate, what to verify, and what to keep for oneself to do（判断什么该委托、什么该验证、什么该留给自己做）
  - 明列要教的 agentic-AI 实践：spec-driven development（规格驱动开发）、context management（上下文管理）、harness engineering（外围工程）
  - 讲 LLMs 为何"天生会失败"（fail by construction），并教如何设计评测去测这些失败
  - 学期项目包含：AI 辅助阅读并与源头核对、汇成领域地图；从零与 Agent 协作搭一个小 ML 组件；外包数据集要 vet；产出物与其评判者（artifacts and their judges）都要审计
  - 每个概念都锚定一个已有的 EECS 原理，同时讲清真正新在哪里

## 导读侧：@shao__meng 全景长文

- 来源：X 长文《MIT 公开课 6.S950 Agency with AI：Spec 先于 Prompt，验证先于信任——AI 时代工程判断力课程全景解读》（2026-09-25）https://x.com/shao__meng/status/2103461095566676365
- 标题口号的定性（2026-10-22 核对后定）：
  - "Spec 先于 Prompt"：有课程依据——Lec 4 讲题就叫 "Specs before prompts"，且官网描述明列 spec-driven development 为课程实践
  - "验证先于信任"：作者对 Agency 定义的提炼，非课程原话；根子在定义里的 "what to verify"
- 导读给出的课程地图：
  - 学习目标递进链：会用工具 → 知道它为何有效 → 知道它为何天生会失败 → 能对每项工作做出委托 / 验证 / 重定向 / 保留的决策并说明理由
  - 四问读法（delta thinking，增量思维）：它解决了什么问题？方案是什么？哪些更老的 ideas 能解释它？它真正新在哪里？
  - 讲题举例（名字即方法论）：specs before prompts（先规格后提示词）；evals as experimental design（把评测当实验设计）；auditing the artifact and the judge（审计产出物，也审计评判者，包括 LLM-as-judge 和你自己）
  - 两个 Lab：Close Enough（kNN 分类器）；Connect Four（论文研读）
  - 评分：Lab checkoff 30% / 学期项目 40% / portfolio 30%；关键政策：AI 使用默认允许、不按数量评分，但任何无法说明理由的工作，无论多精美，都不得分

## 标注与保留

- 作者自标：文中 Lec 3–12 的展开解读为基于课程框架的推断，非课程原文复述
- 导读作者转述精度有前科（Lec 5 介绍推文曾有两处实错，小沐已抓正）；本篇定位为导读 / 地图，事实以官网与各讲讲义为准
- 与第 27 份的关系：第 27 份是 Lec 5《The Harness》单讲精读（扒讲义原文）；本份是整门课全景，配套使用

## 跟你的咬合

- Agency 的定义就是判断力本身：委托 / 验证 / 保留——你今早刚立的 action-self-check（行动先自检、理由先行、不和谐先商议）正是这套判断的个人版
- Lec 4 与已收的 Spec-Driven 论文、given-when-then 规矩接成一条线：spec 先行在你的体系里从"论文观点"升级为"名校课程的正式讲题"
- "auditing the artifact and the judge" 直连 thinktank：judge 层本身要被审计，与你给智囊团定的 judge 纪律（选人分数链、judge 模型稳定性记录）是同一个问题
- 课程政策"无法说明理由的工作不得分"与你的 teach-to-learn 验收标准同构：能讲清原理 / 实现 / trade-off 才算学会
