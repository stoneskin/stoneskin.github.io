# pstack 24 条工程原则（中英对照）

*来源：https://github.com/cursor/plugins `pstack/skills/principle-*/SKILL.md`，2026-10-16 抓取。每条约 10-20 行，此处为名称 + 一句话中文释义。Uncle Bob 评价其为"把经典工程智慧重编码给 AI agent"。*

| # | 英文名 | 中文释义 |
|---|---|---|
| 1 | Attack the Premise | 攻击前提：多个修复共享同一前提且都失败时，先把前提写下来直接验证，别再写基于它的修复 |
| 2 | Boundary Discipline | 边界纪律：验证/类型收窄/错误处理集中在系统边界，内部信任类型，业务逻辑用纯函数 |
| 3 | Build the Lever | 造杠杆：非 trivial 的工作先造工具（codemod/脚本/生成器），让 reviewer 能重跑而不是信手改 |
| 4 | Encode Lessons in Structure | 教训进结构：同一指示写第二遍时，把它编码成 lint/元数据/运行时检查，而不是更多文字 |
| 5 | Exhaust the Design Space | 穷尽设计空间：无先例的新交互/架构决策，先做 2-3 个竞争原型并排比较再定 |
| 6 | Experience First | 体验优先：实现便利与用户愉悦冲突时选后者；少而精胜过多而糙 |
| 7 | Explain the Number | 解释数字：信一个测量数字前，先说出瓶颈是什么，排除它测的不是你以为的东西 |
| 8 | Fix Root Causes | 修根因：每个症状追到系统最先出错的地方修；guard 只有处理的状态合法时才是修复 |
| 9 | Foundational Thinking | 地基思维：先把核心数据结构和顺序搞对（数据形状、脚手架、共享状态），下游代码自然水落石出 |
| 10 | Guard the Context Window | 守住上下文窗口：上下文满时把大块工作路由给子 agent，主线程只留摘要不留原始 payload |
| 11 | Laziness Protocol | 懒人协议：偏向删除和最小改动；每个决策收敛到单一事实源 |
| 12 | Make Operations Idempotent | 幂等操作：操作设计成跑多少次、从哪里崩了重跑，都收敛到同一终态 |
| 13 | Migrate Callers Then Delete Legacy APIs | 先迁调用方再删老 API：引入新内部 API 时同波次迁完调用方并删老 API，不留兼容层 |
| 14 | Minimize Reader Load | 减轻读者负担：可维护性=读者的工作量；数要追踪的层数和记住的状态，合并单调用方 wrapper，缩小可变作用域 |
| 15 | Model the Domain | 领域建模：把真实领域编码成数据结构（状态机/类型模型/注册表/联合类型），别散落在条件分支里 |
| 16 | Never Block on the Human | 不等人：可逆工作不问直接干，让人来事后纠偏；只有不可逆动作才要确认 |
| 17 | Outcome-Oriented Execution | 结果导向执行：为可验证的终态优化；计划内重写/迁移中，有范围、可逆的中间 breakage 可接受 |
| 18 | Prove It Works | 证明它 work：每个输出对照真实产物验证（不是代理指标/自述/"能编译"），检查能脚本化就脚本化 |
| 19 | Redesign from First Principles | 第一性重设计：接新需求时，当它是最初的基本假设来重设计，别打补丁 |
| 20 | Separate Before Serializing Shared State | 先分离再串行化：并发 actor 可能共享可变状态时先消除共享；只有一个共享写者是真不变量时才结构串行化 |
| 21 | Sequence Verifiable Units | 可验证单元排序：多步工作拆成小单元，每单元结束于可检查状态；commit/PR 按能向 reviewer 证明的顺序堆叠 |
| 22 | Subtract Before You Add | 先减后加：先删死代码、冗余校验、stub 引用，再在更简的基础上建 |
| 23 | Test Behavior, Not Implementation | 测行为不测实现：断言用户通过接口能观察到的；行为坏了测试才挂，内部重构测试不挂 |
| 24 | Type System Discipline | 类型系统纪律：让非法状态不可表示；语义原语打 brand，边界处解析外部数据，穷尽变体，类型从权威 schema 派生 |

## 与 Stone 现有原则的对照（小沐注）

已覆盖（名字不同，意思到了）：
- `Prove It Works` ≈ `run-dont-read` + `done-means-verified`
- `Never Block on the Human` ≈ "去/go/👌 就是放行"
- `Encode Lessons in Structure` ≈ "修进 harness"本身
- `Guard the Context Window` ≈ `breakpoint-feedback` + 定期换窗口
- `Subtract Before You Add` ≈ `surgical-edits` 的一半（删的部分）

缺口（值得收编的）：
- `Attack the Premise`：同样错误第二次出现时，先验证前提——opencode-fuse D14 的 advisor 触发点之一，正好咬合
- `Explain the Number`：信测量数字前先说出瓶颈——智囊团 judge 机制可用
- `Build the Lever`：非 trivial 工作先造工具让 reviewer 重跑——"修进 harness"的上游
- `Fix Root Causes`：guard 只有状态合法时才是修复——比"修根因"口号更锋利的版本
