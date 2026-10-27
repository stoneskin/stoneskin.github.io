# 决策模型（Decision Models）与 Jev 总结：裁判开始输出概率，不写判决书

[← 返回目录](index.md)

> 主要来源：
> - Hamel Husain & Antaripa Saha《How To Use Decision Models for Evals》，hamel.dev，2026-10-21（经 @dongxi_nlp 推文推荐，扒原文）
> - Jev 资料：jevmodel.org、Sanity glossary、aimlapi 独立实测、aicoderscope 分析、arXiv 两篇基准论文、anchorterminal 行业梳理、Medium 冷静派反驳文

---

## 一、是什么：一个新品类

2026 年 9 月起涌现一批"决策模型"：不生成文本，只输出类型化的判断——一个 0–1 的概率、一个多选选项、或一个量表分数。常被用作 LLM-as-a-Judge 的替代：评测、路由、审核、过滤这些"一天判几千次"的活，不再请聊天模型写长篇判决书，改请一个只吐概率的分类器。

时间线（品类是一个月内炸开的）：
- 9/15 TypeSafe 发布 Jev（第一个，自称 System One 模型）
- 10/1 前后 Cloudflare Clef、Perplexity pplx-decider、AWS Strands Decider 同日登场
- 10/6 OpenAI Decisions API 公开 beta（基于 gpt-6-luna）
- 10/9 Microsoft Decision-1（Qwen3.5-9B 后训练）
- 一个月内目录里已有 14 个；多数是小开源模型后训练出"打分头"，权重多为开放

价格带：托管服务只收输入、输出免费，$0.02–0.24 / 百万输入 token。

## 二、Hamel 的方法论：怎么用决策模型做 Evals

实验：公寓租赁 agent 的 100 条人工标注 trace，5 个决策模型（Jev 1.13、Perplexity Decider、Liquid d1、Cloudflare Clef Flash、OpenAI Decisions）各自输出失败概率。四个主张：

1. **阈值自己调，别用默认 0.5**。阈值是把概率切成是/否的分数线：拉低抓得全但误报多，拉高报得准但漏得多。先定最低可接受的 precision/recall（如告警场景各 80%），再用 F1 或 F-beta 做交叉验证把阈值量出来。
2. **选型看 Pareto 前沿**（调好阈值后的 F1 vs 成本）：Perplexity 最便宜（0.82 美分/100 次评测，F1 0.79）；OpenAI Decisions 的 F1 最高（0.87），成本贵 4.5 倍（3.72 美分/100 次）。没有最好，只有预算下最划算的点。
3. **概率当置信度之前先验校准**。他试 Platt scaling：帮了 Perplexity、Liquid、Clef Flash，却把 OpenAI 的搞坏了。"输出概率"不等于"概率可信"，必须在自己的数据上验。
4. **一个失败模式配一个 judge**，先调 prompt 再换模型。结论：别信榜单，在自己的数据上量。

## 三、Jev 详解（品类开创者）

**出身**：TypeSafe AI，2026-09-15 发布，同期 $40M 融资。名字双关：System One 借 Kahneman《思考，快与慢》（聊天模型是慢思考 System 2，Jev 是快直觉 System 1）；Jev 取自经济学家 Jevons（杰文斯悖论：效率提升反而增加总用量——决策变便宜，系统会做更多决策）。主创 Diogo Almeida，前 OpenAI、InstructGPT 共同作者。

**工作方式**：输入 = 一段"状态"（文本/JSON：工单、日志、检索段落）+ 一组代码里定义的类型化问题；非自回归，一次前向并行判完所有问题；输出只有类型化值，永不写字。三种题型：
- Noul：是非题，返回 0–1 概率
- Choice：最多 255 个选项，返回所选 + 每个选项的概率
- Score：2–10 级量表打分，可落在两级之间

答案空间预先钉死，所以不可能格式错误：没有 JSON 包裹、解析失败、寒暄废话。训练法自称 Reinforcement Learning for Calibrated Decisions，目标是 0.88 就约等于 88% 正确。

**数字**：延迟 70–500ms（厂商口径）；$0.042/百万输入 token，输出免费。厂商宣称快 193 倍、便宜 444 倍；独立复测打折后为约快 3–5 倍、比 Sonnet 级便宜约 40 倍，仍可观。

**独立实测画像**：
- 强：内容审核 F1 六模型第一；置信度 ≥0.9 时正确率 94–96%，校准扎实；MMLU 91.3 与旗舰 LLM 相当
- 弱：意图路由比旗舰低约 7 点；回答质量评分最弱；数学多步计算明显不行（专门决策 ≠ 推理）
- 已知毛病：选项顺序敏感——颠倒选项顺序，8.5% 答案改变（第一选项偏好，官方文档承认）；选项措辞影响结果；会自信地错
- 最佳用法：当前置过滤器——Jev 先筛，低置信度的升级给大模型；实测以大模型 38–45% 的成本打平其分类准确率

## 四、冷静派的反面（选型纪律）

一篇系统的反对文（Decision Models Are Useful. They Aren't Indispensable.）指出：若你有几千条标注数据、且类别稳定，传统做法更准——Banking77 上逻辑回归 + embedding 达 94.7%、微调 ModernBERT 94.3%，比所有零样本决策模型高 6 个点以上。

决策模型的甜区是另外三种场景：没有标注数据（零样本可用）、类别经常变（不用重训）、要判"以上都不是"（out-of-scope 检测，BoolQ 和 CLINC150 上决策模型赢微调分类器约 10 点，主因正是识别"不属于任何已知类"）。

DIY 门槛极低：Unsloth 教程给 Qwen3.5-0.8B 加决策头 + LoRA，4GB 显存 42 分钟，类型化决策准确率 36% 提到 73%。

## 五、跟 Stone 项目的咬合

- **thinktank 的 judge 层有新选项**：决策模型写不了评审意见，但"这条结论可信吗，给个概率"正是本行；陪审聚合可演进为"成员出意见 + 决策模型出概率做加权与熔断"
- **12 步路线图第 10 步（执行轨迹评测）**的一线实践样本：Hamel 的阈值调优 + 校准验证就是把评测当正经 ML 工程做
- **5070 可玩**：12GB 显存足够按 Unsloth 路线自己训一个小决策模型，适合练手理解校准与阈值
- **选型纪律**（呼应 simplest-first）：类别稳定 + 有标注，先训分类器；零样本、类别多变、要 out-of-scope，才上决策模型

## 六、追问答疑（2026-10-21 Stone 问，小沐查实）

**Q1：Jev 这类模型要自己训练/蒸馏吗？**
不用。现成三条路：① 托管 API 直接调（TypeSafe 直连、OpenAI Decisions API、Perplexity、Cloudflare、微软），零样本可用；② 开源权重自己跑推理（pplx-decider、Clef 家族、Laya、Strands Decider 均 Apache 2.0），下载即用；③ 自己训只是可选项，不是入场券。

**Q2：OpenRouter 上有吗？**
有。Jev 已上架：模型名 typesafe/jev-1.14（别名 ~typesafe/jev-latest），OpenRouter key 即可调用、走 OpenRouter 账单。注意它不走普通 chat 接口，有专用 decisions 端点（POST /api/alpha/decisions），因为请求形状是 state + questions 而非 messages。Stone 家里 thinktank / opencode-fuse 本就走 OpenRouter，key 与账户现成。

**Q3：它们是怎么做出来的（一半算蒸馏）？**
小底座（多为 Qwen 系 2B–27B）+ 把生成头换成/加上决策头，后训练两步：① 用标注判断数据微调（标签很多由大模型当老师生成，这部分算蒸馏）；② 强化学习专攻校准（TypeSafe 称 RLCD），让输出的概率是真概率——这是与"小模型凑合当裁判"的本质区别。

**Q4：什么时候才值得自己训？**
三条件同时成立：类别很专有、市面模型没见过；手里有成千上万条标注数据；调用量大到 API 费肉疼。

## 七、回国后练手计划（2026-10-21 定，回美后排期）

- **目标**：在 RTX 5070（12GB）上按 Unsloth 路线给 Qwen3.5-0.8B 加决策头 + LoRA，亲手跑通"造一个小决策模型"的全流程（参考基准：4GB 显存 42 分钟，类型化决策准确率 36% 提到 73%）
- **训练素材**：thinktank 历史评审数据（已有的人工/judge 结论当标签），练完顺带评估能不能给 thinktank 当一道便宜的前置概率门
- **验收（teach-to-learn）**：Stone 能讲明白三层——原理（决策头与生成头的区别、概率为什么需要校准）、实现（数据怎么标、LoRA 训什么、阈值怎么用交叉验证量出来）、trade-off（什么场景自训胜过调 API、什么场景老实训传统分类器）
- 状态：待 Stone 回美后启动
