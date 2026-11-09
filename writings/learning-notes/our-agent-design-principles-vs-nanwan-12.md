# 我们的设计思想总结

[← 返回目录](index.md)

> 对照基准：南晚 2026-11-08 推文《构建自己的 Agent 至少需要完成这些》（12 条清单）。本稿只总结我们已有设计文档里的思想，每条注出处；未在文档中明确的写明，不硬凑。
> 本篇是我们做 WorkBuddy、harness-landing 与某生产 Agent 项目时沉淀的 13 条设计原则，逐条对照南晚的 12 条；公司项目相关出处已泛化，原则与结论不变。

## A. 我们的设计思想总结

1. **确定性规则先行，模型只处理模糊** — 能用代码、正则、状态机、硬规则解决的逻辑，先写死，跑在模型前面，且模型覆盖不了。某生产 Agent 项目的规则引擎先跑，规则结果而非 LLM 决定下一步；WorkBuddy 的信任分层是架构约束大于自动验证大于文字规则大于人工评审；model-fuse 的 D15 信任金字塔同款：自有系统按 1→2→3 顺序投入，prompt 只写最少够用。出处：某生产 Agent 项目设计文档；WorkBuddy §5.3；model-fuse D15。
2. **人只做纠偏与拍板，不做每圈执行者** — 人是 loop 里必要的一环，而不是瓶颈。Stage 0 定位句的后半句就是这句话；WorkBuddy 的 loop 是计划→执行→验证→纠偏，人只占纠偏位与拍板位；某生产 Agent 项目的生产变更永远要人；修正案 #4 定：用户批准是框架里的硬批准，不是建议。出处：Stage 0 成果 §定位；WorkBuddy §2 G3、§5.3；某生产 Agent 项目设计文档；修正案 #4。
3. **最小权限按工具集分，不按 prompt 分** — 权限是工具集的硬边界，不是 prompt 里的叮嘱。某生产 Agent 项目把一个 agent 拆成只读的分析器与只写、只执行已验证计划的执行器，两者无直接通道，工单状态机是编排契约；WorkBuddy 的权限按 L0–L3 分级、deny 优先，L3 外发永不自动。出处：某生产 Agent 项目设计文档；WorkBuddy §5.6。
4. **状态机是编排，状态文件是事实来源** — 不靠 agent 之间聊天传进度。某生产 Agent 项目的工单状态机是编排契约，API 按状态触发 agent；WorkBuddy 的 loop 是状态机，任务状态文件 task.md 加 state.json 记录圈数与摘要链，中断后 wb resume 从状态文件重建；open-memex 的 Markdown 是正本，索引可重建。出处：某生产 Agent 项目设计文档；WorkBuddy §5.2、§5.3；open-memex decisions.md D1。
5. **上下文打包、分层、带来源信任等级** — 上下文不是一股脑拼进 prompt。WorkBuddy 的 Context Pack 分常驻、项目、任务、召回四层，按预算裁剪，每层带来源与信任等级，低信任片段只能当数据进包、带来源标签；model-fuse 的 panel 成员各用独立 session，fan-out 前先压缩。出处：WorkBuddy §5.2；model-fuse §7.2、§7.3。
6. **验证不信口头汇报，只认独立执行结果** — agent 说做完了不算，验收命令跑过了才算。WorkBuddy 的验证圈跑测试、lint、构建，结果是结构化 pass/fail；某生产 Agent 项目先跑只读试点、对着真实工单测准确率，达标才给写权限；thinktank 的 golden cases 离线回归，指标退化非零退出。出处：WorkBuddy §5.3、§10 场景 1；某生产 Agent 项目设计文档；thinktank 设计文档 §14 Phase 2。
7. **预算六项硬上限，拿不到数字就标未计量** — 圈数、墙钟、工具调用、输出字节、美元、连续失败，六项都是 WorkBuddy 可自计数的硬上限，永远生效；model-fuse 在 Router 阶段静态预估、运行时动态熔断；thinktank 启动前算最坏路径封顶价，超线拒绝启动。底座不回报可信用量时，成本状态写未计量，绝不写 0 美元。出处：WorkBuddy §5.3；model-fuse §7.9；thinktank 设计文档 §11、§9 D12。
8. **便宜先行，失败升档，但绝不静默回退到付费** — 免费/便宜档先跑，不满意再升档，升档要人确认或按规则触发；池子空了就报空池，绝不悄悄走到付费版。model-fuse 的 D9 是这条的硬规则，panel 模式免费池不足时自动升 standard 并写审计日志，单模型显式 cheap 仍报空池；thinktank 的免费转付费永远先确认、附预估与余额。出处：model-fuse D9、§7.7；thinktank 设计文档 §3.1；WorkBuddy §5.5。
9. **多模型陪审：并行作答、裁判打分、人终审** — 重要判断不只问一个模型。thinktank 的 panel→judge→synth，judge 有拒绝权、噪音按严重性分级、人终审，judge 输出是结构化契约、代码层强校验；model-fuse 的 judge 输出结构化 JSON，可验证性优先，遇到矛盾先停、不许在存疑前提上堆结论；WorkBuddy 把陪审内嵌为 workflow。出处：thinktank 设计文档 §2、§11；model-fuse §7.5、§7.6；WorkBuddy §5.5。
10. **记忆保鲜：只记有价值的，按复用度量，入库要人确认** — 记忆的价值按复用算，不按存了多少算。open-memex 的 D77 用 retrieved/useful 计数算复用率，僵尸记忆进衰减候选；D78 整理默认自动、人管例外，可逆代替预批；WorkBuddy 的 loop 收尾只产记忆候选，人确认才入库，旧结论被推翻时走更新加冲突标注、不静默覆盖。出处：open-memex decisions.md D77、D78；WorkBuddy §5.4。
11. **知识要编译，不要每问重算** — 记忆是知识的入口，不是最终形态。open-memex 的图加编译 wiki 是派生层：边带 EXTRACTED/INFERRED 来源加置信度，推断边永远标注；lint 只报告、不自动解；确定性抽取不用 LLM；图丢了可从原始记忆重建，原始记忆不可变。出处：open-memex knowledge-graph.md §20、decisions.md D88/D91。
12. **中心不变、手可换；核宿主无关** — 助理内核与治理层是本体，后端只是手。WorkBuddy 的双手切换契约钉死统一输入输出、能力矩阵、两层指令投递、权限翻译不等价时降级为 worktree 沙箱；model-fuse 的核是宿主无关的路由核，版本相关代码收敛到 Adapter 接口之后，四方消费者共用路由与档位映射；harness-landing 选底座按 loop、工具调用、skill 机制、扩展性、可替换性五项打分。出处：WorkBuddy §4、§5.1；model-fuse §4、§14；harness-landing Roadmap Phase 0。
13. **先验证需求与测量，再动手；失败变考题** — 新项目先回答谁用、解决什么现有方案解决不了的问题，答不上来不动手；检索改动先落 fixture 加基线数，改动前后对照才算数；同一错误出现两次即记为一类，按架构大于类型大于 lint/CI 大于文档的顺序修；评测先怀疑外壳再下模型结论。出处：AGENTS.md demand-before-code、first-principles；open-memex AGENTS.md 测量先于机制；thinktank AGENTS.md 评测方法；model-fuse D15。

## B. 异同对照

### B1. 逐条对照南晚 12 条

1. 确定性边界——［已有］某生产 Agent 项目规则引擎先跑且不可覆盖；WorkBuddy 信任分层；model-fuse D15。出处同 A1。
2. 轻量级路由——［已有］model-fuse Router 只定档位与模式，M1 规则版；WorkBuddy 路由层先选后端类再选档；某生产 Agent 项目 API 按工单状态触发 agent，不另设编排 agent。出处：model-fuse §7.7；WorkBuddy §5.5；某生产 Agent 项目设计文档。
3. 上下文隔离——［已有］model-fuse panel 成员独立 session；WorkBuddy 记忆 namespace 目录/索引/权限三件套隔离；某生产 Agent 项目分析器/执行器工具集隔离。出处：model-fuse §7.2；WorkBuddy §5.4；某生产 Agent 项目设计文档。
4. 主动获取上下文——［部分有］WorkBuddy Context Pack 在运行前自动组装项目规则、相关记忆与文件清单；某生产 Agent 项目分析器先读工单、系统状态与规则集再给结论，信息缺了就问、不硬答。未在文档中明确：信息不全时不许模型直接生成答案，这条没有写成显式规则。出处：WorkBuddy §5.2；某生产 Agent 项目设计文档。
5. 工具接口设计——［部分有］某生产 Agent 项目所有写操作只走项目 API，执行器只执行已验证计划；WorkBuddy adapter 统一输入输出、能力矩阵；model-fuse deliberate 模式只让 synth 拿真实工具 schema。未在文档中明确：给模型封装扁平、参数少、语义明确的工具这一条本身。出处：某生产 Agent 项目设计文档；WorkBuddy §5.1；model-fuse §7.4。
6. 结构化报错回传——［部分有］thinktank v0.16 结构化角色契约失败给一次修复重试、把失败原因喂回去；WorkBuddy 验证失败把失败摘要回灌为下一圈纠偏输入。未在文档中明确：工具层捕获异常、超时、参数错误并把具体原因返给模型自修重试，这条没有写成工具层设计。出处：thinktank 设计文档 §14 Phase 3；WorkBuddy §5.3。
7. 显式状态管理——［已有］某生产 Agent 项目工单状态机是编排契约；WorkBuddy loop 状态机加任务状态文件；model-fuse LastRun。出处同 A4。
8. 并发与过期状态拦截——［没有］未在文档中明确。最接近的是 WorkBuddy 并行上限 2–3 个子任务且必须 worktree 隔离（防互相干扰，不防过期结果覆盖），以及某生产 Agent 项目的工单状态机（状态流转是协调，但无版本号校验与取消旧任务的设计）。出处：WorkBuddy §2 非目标；某生产 Agent 项目设计文档。
9. 循环上限与预算控制——［已有］WorkBuddy Budget 六项硬上限；model-fuse 静态预估加动态熔断、连续 3 次 /better 未解决则停；thinktank 最坏路径封顶价加单模型熔断。出处同 A7。
10. 人类审批节点——［已有］某生产 Agent 项目的生产变更永远要人、按环境分级、生产动作还要带外确认；WorkBuddy L3 外发永不自动；model-fuse 与 thinktank 的人终审。出处同 A2。
11. 断点续跑与持久化——［已有］WorkBuddy wb resume 从状态文件与摘要链重建、不依赖 CLI 私有会话格式；某生产 Agent 项目的工单与注册表是事实来源，状态即恢复点。出处：WorkBuddy §5.2、§10 场景 4；某生产 Agent 项目设计文档。
12. 沙箱环境隔离——［部分有］WorkBuddy 权限翻译不等价时降级为 worktree 沙箱加事后 diff 审查，Copilot CLI 限定可访问目录与域名；某生产 Agent 项目用限流、配额、分阶段上线控爆炸半径。未在文档中明确：在受限容器或虚拟环境里跑模型生成的代码与命令这一条。出处：WorkBuddy §5.1、§5.6；某生产 Agent 项目设计文档。

### B2. 我们有、南晚没有的 distinctive 思想

1. **记忆保鲜与知识编译** — 南晚 12 条里没有记忆这一项。我们把记忆当一层：只记有价值的（捕获先问记不记）、按复用度量有用性、知识编译成图加 wiki（派生层、可重建、推断永远标注）。出处：open-memex decisions.md D77、D78、D88/D91；Stage 0 成果定位句。
2. **多模型陪审团评审** — 南晚只谈单个 Agent 跑稳。我们的重要判断走 panel→judge→synth：并行作答、裁判结构化打分、红队对抗挑刺、人终审；judge 有拒绝权，噪音按严重性过滤。出处：thinktank 设计文档 §2、§11；model-fuse §7.5、§7.6。
3. **成本与路由的二维定价** — 南晚的预算只有上限。我们还管路由经济学：定档按 input 加 output 二维混合成本划线，router 按能力分选最便宜的达标模型（便宜又强靠机制保证，不是碰运气），并明说价格不等于能力。出处：model-fuse §7.11、§7.12、§7.9。
4. **人是纠偏不是瓶颈** — 南晚的审批节点是事前关卡。我们的定位是 loop 里的分工：人只占纠偏位与拍板位，不做每圈的执行者；重要判断先审前提、可唱反调、可调陪审；这是 Stage 0 定位句的后半句，也是 WorkBuddy 的 G3/G9。出处：Stage 0 成果定位句；WorkBuddy §2 G3/G9、§5.3。
5. **测量与证据纪律** — 南晚没有评估这一项。我们要求改动先落 fixture 加基线数、golden tasks 离线回归、失败两次就停、同一错误出现两次记为一类并按层修、评测先怀疑外壳。出处：open-memex AGENTS.md；thinktank AGENTS.md；model-fuse D13、D16。

## C. 一句话结论

最大的共同点是底层判断一致：demo 能跑不等于生产能跑，可靠性来自确定性规则在前、人在关键点上、预算有硬上限；最大的不同点是我们的设计多了一整层南晚没谈的东西——记忆与知识的积累（保鲜、编译、复用度量）以及多模型陪审（panel→judge→synth、人终审），即我们不只关心单个 Agent 跑稳，还关心知识怎么越用越多、判断怎么越审越准。

## D. 适用范围（Stone 2026-11-08 定）

- 南晚 12 条 + 我们 13 条是 WorkBuddy、harness-landing 与某生产 Agent 项目三个项目的共同设计基线：做这三个的时候，这些设计思想都要包括进去。
- 不同 agent 任务不同，可以取舍：不是 12 条全套进每个项目，按任务选。
- 唯一全缺的第 8 条（并发与过期拦截）是三个项目都要补的设计缺口，建 POC/框架时优先补。
- 落地：WorkBuddy 走设计修正案（fork 攒批、一次 PR 到上游）；生产 Agent 项目进其设计文档（POC 设计细化时）；harness-landing 进 Phase 0 底座评价标准。

---
2026-11-08；来源：某生产 Agent 项目设计文档、WorkBuddy 设计文档 v0.3 与修正案 #4、model-fuse 设计文档 DRAFT 0.3、open-memex decisions.md 与 knowledge-graph.md、muse-thinktank 设计文档与 AGENTS.md、Stage 0 成果、harness-landing Roadmap、AGENTS.md 通用规则。南晚推文已于同日入学习清单第 55 份（组七 Agent Ops，只加清单一行，不写导读；私仓 PR #18 已合并）。
