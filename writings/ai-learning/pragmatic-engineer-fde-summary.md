# Pragmatic Engineer《What are Forward Deployed Engineers, and why are they so in demand?》

[← 返回目录](index.md)

分级：【对照正文】——目前关于 FDE 最扎实的一手深挖，定义、日常、方法、案例、反哺五件套齐全。

> 原文：https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers（Gergely Orosz，2025-08-12）
> 一句话：采访了 OpenAI 的 FDE 负责人、Ramp 的 FDE 负责人和一位 7 年 Palantir FDE，把起源、日常、三段工作法和两个真实案例都讲透了。

- 起源与定义：角色由 Palantir 在 2010 年代初创立，内部叫 Delta。到约 2016 年之前，Palantir 的 FDE 人数多于普通软件工程师；2016 年 Foundry 发布后，更多 FDE 回流核心产品，把一线经验带回平台。Palantir 对 Delta 的定义是"一客户、多能力"，对应普通开发的"一能力、多客户"；FDE 的工作被概括为"像一家 AI 创业公司的 CTO"——小团队、高风险、端到端负责。
- FDE 与 SA 的分界（OpenAI 口径）：OpenAI 仍保留 Solutions Architect 角色，但两者不同：SA 偏顾问，很少在客户基础设施上写代码，通常用匿名化或离线数据做 MVP / PoC；FDE 直接在客户基础设施上、用客户的工具写代码，面对的模糊性更大，且工作要对齐 OpenAI 的研究目标。OpenAI 的 FDE 团队 2025 年初由 2 人起步，写稿时已超过 10 人，分布在 8 个城市、3 大洲。
- OpenAI FDE 的三段工作法：① 早期 scoping：在客户现场待几天，坐到用户身边梳理流程、找出最大价值点、用合成数据做原型、白板讨论并排优先级。② 验证：先回答"我们 scoping 出来的东西，是不是对客户最有价值的事"，再定验证标准——与用户一起建 evals 并做标注、扩大标注规模、在 evals 上爬坡优化、最后出报告对照目标呈现 eval 成绩。先验证再交付是反常的，但有原因：客户描述与现场数据/系统现实经常对不上，要先快速证伪撞墙点再调整范围。③ 交付：每周几天在客户现场，抠问题细节、拿客户数据、在 OpenAI 办公室建方案再向客户演示，追求"能构成端到端解法的最小单元"。
- 两个真实案例：① 语音客服：OpenAI FDE 为呼叫中心自动化客户建语音模型 evals，初期模型成绩不够客户签约部署；FDE 把数据带回研究部门改进语音能力，客户成为第一个生产部署方，改进成果进入 Realtime API，客户与厂商双赢。② John Deere（爱荷华）：把原来人工给农民打电话做个性化指导，改成规模化个性化干预，帮农民更好地用新型除草技术、减少农药喷洒；FDE 和负责人亲自下农场与农民一起工作，且必须赶在下一个种植季前交付，时限极紧，最终按时成功。
- FDE 对产品的反哺机制：FDE 团队定期与研究团队知识共享（约双周）、与产品负责人及 PM 双周汇报、有全员可见的"FDE Field notes"Slack 频道、每季度全员集训；FDE 团队也是 OpenAI Agents SDK 的重要贡献者（前身是 SA 团队为降低 agent SDK 学习曲线而建的 Swarm 框架）。
- 备注：Ramp 四条运营原则与薪酬细则：原文抓取在 Ramp 节开头处截断，未核到，本条不写。

### 跟你的咬合

- 三段工作法里的"先验证再交付"和 evals 爬坡，与 thinktank 的评测思路直接同构。
- SA 与 FDE 的分界帮你定位自己：企业内 SA 转 AI SA 时，FDE 模式可以内化为"企业内部的 FDE 小队"，而不必照搬驻场形式。
