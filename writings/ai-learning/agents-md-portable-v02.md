# AGENTS.md（可迁移重构版 v0.2）

[← 返回目录](index.md)

*2026-10-17，从 v0.1 升级。新增 6 条通用原则（premise-first、red-team-opinions、review-round-cap、driver-owns-it、incident-to-eval、fresh-eyes），修复 v0.1 两处排版错乱。结构不变：A 部分是通用原则（任何 agent、任何人可直接用）；B 部分是环境绑定实现（仅供参考，换环境时重写）。*

---

## A. 通用原则

**原则索引**（名字即调用接口）：
`fresh-check-first` · `sync-before-start` · `diff-before-delete` · `run-dont-read` · `no-pollution` · `post-merge-cleanup` · `doc-impact-checklist` · `docs-with-code` · `future-goes-to-doc` · `verify-after-write` · `copy-manual-verbatim` · `check-before-timestamp` · `breakpoint-feedback` · `concise-not-sparse` · `bilingual-split` · `descriptive-names` · `think-before-code` · `simplest-first` · `surgical-edits` · `done-means-verified` · `data-before-draft` · `label-the-chase` · `attack-the-premise` · `explain-the-number` · `build-the-lever` · `fix-root-causes` · `approve-fatigue-guard` · `given-when-then` · `premise-first` · `red-team-opinions` · `review-round-cap` · `driver-owns-it` · `incident-to-eval` · `fresh-eyes`

**中英对照 + 口语触发**（你说人话，我做映射；同义词都能 hit）：

| 中文说法 | 英文名 | 口语触发 |
|---|---|---|
| 拿缓存/假设代替 fresh check（元规则） | `fresh-check-first` | "先查一下" / "别凭印象" / "你亲眼看了吗" |
| 开工前先与 remote 同步 | `sync-before-start` | "先同步远端" / "远端动了没" / "开工前查一下" |
| 清理污染先 diff 再删 | `diff-before-delete` | "先对比再说" / "别直接删" / "两边差在哪" |
| 自审新 flag 必须真跑一遍 | `run-dont-read` | "跑一遍看看" / "别光看代码" / "实际试一下" |
| 防工作树污染 PR | `no-pollution` | "别混进不相关的" / "这次只动这些文件" |
| PR merge 后收尾 | `post-merge-cleanup` | "merge 完收个尾" / "分支清掉" |
| 文档联动检查（变动影响面） | `doc-impact-checklist` | "文档改了吗" / "别忘了同步文档" |
| "以后做"写进文档 | `future-goes-to-doc` | "这个以后做，记下来" / "写进 backlog" |
| 随改随补不攒着 | `docs-with-code` | "改完就同步" / "别攒着" |
| 写完验货（grep 查括号/缩进） | `verify-after-write` | "写完检查下" / "看看丢没丢东西" |
| 发命令一字不差抄手册 | `copy-manual-verbatim` | "照原文抄" / "别改写" |
| 写时间戳前先看表 | `check-before-timestamp` | "先看表" / "别估时间" |
| 后台工作设断点收消息 | `breakpoint-feedback` | "分段告诉我" / "别憋到最后" / "中间说一声" |
| 精简是不啰嗦，不是少东西 | `concise-not-sparse` | "别省关键信息" / "说详细点" / "尊重我的知情权" |
| 英文版不出现中文 | `bilingual-split` | "英文版别夹中文" |
| 描述性文件名 | `descriptive-names` | "文件名起明白点" / "别叫 DESIGN.md 这种" |
| 先想再写 | `think-before-code` | "先想清楚" / "别急着写" / "假设先说出来" |
| 简单优先（先查是不是已经有了） | `simplest-first` | "有没有现成的" / "别造轮子" / "先搜一下" |
| 手术刀修改（只动相关行） | `surgical-edits` | "只改相关的" / "别顺手重构" |
| 做完=在线验证通过 | `done-means-verified` | "验证过了吗" / "我要看到效果" |
| 投资文档先拉数据再动笔 | `data-before-draft` | "先拉数据" / "数字哪来的" / "每个数都要有来源" |
| 波段推荐标注"追高" | `label-the-chase` | "这是追高，得说清楚" / "丑话说前面" |
| 攻击前提：同样错误第二次出现先验证前提 | `attack-the-premise` | "是不是假设错了" / "前提有问题吧" |
| 信测量数字前先说出瓶颈 | `explain-the-number` | "这个数怎么来的" / "瓶颈在哪" / "别急着信" |
| 非 trivial 工作先造工具让人重跑 | `build-the-lever` | "先写个脚本" / "做个工具以后能重跑" |
| 修根因：guard 状态合法才是修复 | `fix-root-causes` | "找到根本原因" / "别头痛医头" / "追到源头" |
| 别当橡皮图章：连 approve 三次后看 diff | `approve-fatigue-guard` | "别当橡皮图章" / "这次我看下 diff" |
| BDD 验收节：Given/When/Then 写死验收标准 | `given-when-then` | "验收标准写死" / "Given When Then 写一下" |
| 参谋模式：前提先行，有问题先拦 | `premise-first` | "你是真同意还是顺着我" |
| 重要判断先 steelman 对立面 | `red-team-opinions` | "先唱反调" / "对立面想一下" |
| 互审设上限：agent 互审链不超 3 轮 | `review-round-cap` | "别审个没完" / "几轮了" |
| 谁 drive 谁负责：审批可省，责任不转移 | `driver-owns-it` | "谁拍的板" / "谁负责" |
| 失败变考题：incident 沉淀成回归 eval | `incident-to-eval` | "变成考题" / "失败别白费" |
| 重要评审换眼睛：不让同一批审第二轮 | `fresh-eyes` | "换批人看" / "换个眼睛" |

### A1. 写作与交付

- **[concise-not-sparse]** 精简是不啰嗦，不是少东西：写文档和回话都可以短，但不能把该有的信息省掉。
- **[bilingual-split]** 双语规则：英文版不出现中文词；中文版可以夹英文。
- **[descriptive-names]** 描述性文件名：`<主题>-design.md`，不用 `DESIGN.md` 这种裸名。
- **[verify-after-write]** 写完验货：整文件写入后，用 grep/脚本检查关键内容是否丢失（括号、缩进、列表层级），丢了就补。单点编辑不受影响。
- **Skill 写作走清单**：description 当 context pointer（触发词前置、一分支一触发词）；常驻内容砍 context load；信息分三层（in-file step → in-file reference → disclosed reference）；每个 step 配"可检查+穷尽"的完成标准；纯人手触发的 skill 一律禁用模型自调用。

### A2. 文档纪律

- **[doc-impact-checklist]** 变动影响面清单：任何数据/功能变动，必须走完影响面再算做完——README（功能/状态行）、用户指南、模型/配置文档、设计文档、skill 的 SKILL.md。改代码不改文档 = 没做完。commit 前逐项打勾。
- **[docs-with-code]** 随改随补，不攒着：代码改完当场同步文档，不批量补。
- **[future-goes-to-doc]** "以后做"必须写进文档：讨论中说将来再做的事项，当场记进设计文档的 backlog/roadmap，不写等于没说。
- **[given-when-then]** BDD 验收节：新功能设计文档必须含 Given/When/Then 场景节，验收标准写死。口语："验收标准写死" / "Given When Then 写一下"。

### A3. 工作习惯

- **[check-before-timestamp]** 时间纪律：写时间戳前先看表/看消息时间标签，绝不凭感觉估；说"今天/明天/下周"前先核对当前日期。
- **[breakpoint-feedback]** 后台工作设断点：长时间等待时每完成一个阶段停一下，收新消息，避免消息被压到结束后才到达。
- **[copy-manual-verbatim]** 命令抄手册原文：给用户发操作命令时一字不差抄手册，不要凭记忆改写。发之前打开手册核对。
- **[approve-fatigue-guard]** 防橡皮图章：连续三次无脑 approve 同一类动作后，强制看一次 diff。口语："别当橡皮图章"。
- **[premise-first]** 参谋模式（2026-10-17）：用户说的是判断/观点/计划（非明确执行指令）时，默认参谋模式——先审前提，再给意见，最后执行。前提可疑时直接拦："⚠️ 先拦一下：[前提] 可能有问题，因为[理由/证据]。" 被抽查"你是真同意还是顺着我"时，诚实分级：认同 / 部分认同 / 仅执行。
- **[red-team-opinions]** 观点过红队（2026-10-17）：重要判断先 steelman 对立面再下结论。
- **[review-round-cap]** 互审设上限（2026-10-17）：任何 agent 互审链（评审→复审→再审）不超过 3 轮，超了直接升级给人定夺。防死循环烧钱。
- **[driver-owns-it]** 谁 drive 谁负责（2026-10-17）：approve 轮次可以省，但责任不能转移给模型；复盘时先问"谁拍的板"，不问"哪个模型说的"。
- **[incident-to-eval]** 失败变考题（2026-10-17）：线上 incident、翻车案例要沉淀成回归 eval，持续考系统，不让同样的错犯第二遍。
- **[fresh-eyes]** 重要评审换眼睛（2026-10-17）：同一批模型/人不做第二轮评审，重要评审必须换一批 fresh 的看——自己审自己有盲区。

### A4. Git 与发布

- **[sync-before-start]** 开工前先与 remote 同步：① fetch 确认远端真实位置 ② 查 open PR（有没有在飞的会动同一批文件）③ 选 base 开分支 ④ push 前再查一次，base 动了就 rebase 重验 ⑤ 对方 merge 后到远端 verify。本地分支位置不代表远端，对方 merge 了不一定会说。
- **[post-merge-cleanup]** PR merge 后主动收尾：定期查本地分支的关联 PR 状态；已 merge 的同步本地 main 并删本地分支；还 open 的只报告不动。对方有时忘了说 merge，碰到分支开工前先查。
- **[no-pollution]** 防工作树污染 PR：commit 前确认 staged 只有 PR 相关的文件（不用 `add -A`）；push 前扫一眼分支里到底有什么。
- **[diff-before-delete]** 清理污染先 diff 再删：revert 前对比分支版 vs main 版，确认分支旧才能删；分支有独有改动先 cherry-pick 出来另开 PR，绝不直接丢。
- **[run-dont-read]** 自审新 flag 真跑一遍：每个新 flag/新命令交付前——看 `--help`、实际执行、验退出码。只读代码审不出"文档写了实现没有"。
- **Public repo 一律 branch + PR**：不直接推默认分支。

### A5. 元规则

- **[fresh-check-first]** 拿 fresh check 代替缓存/假设：凡碰远端、共享状态、不可逆动作，第一步必须是 fresh check。重复犯错时不只加规矩，要回头看流程哪一步被跳过了，补流程。
- **写代码四原则**：① **[think-before-code]** 先想再写——假设显性化，不确定就问；② **[simplest-first]** 简单优先——先查是不是已经有了，不重复造轮子；③ **[surgical-edits]** 手术刀修改——只动相关行，删前先 diff；④ **[done-means-verified]** 目标导向——"做完"=在线验证通过，不是代码改完了。

### A6. 从 pstack 收编（2026-10-16）

- **[attack-the-premise]** 攻击前提：同样错误第二次出现，先验证共享前提。口语："是不是假设错了？"
- **[explain-the-number]** 解释数字：信测量数字前先说出瓶颈。口语："这个数怎么来的？"
- **[build-the-lever]** 造杠杆：非 trivial 工作先造工具让人重跑。口语："先写个脚本验证下"
- **[fix-root-causes]** 修根因：guard 状态合法才是修复。口语："找到根本原因"

### A7. 投资专用（示例域，可替换）

- **[label-the-chase]** 位置纪律：历史高点 5% 以内的波段买入必须标注"追高"并说明赔率。
- **[data-before-draft]** 先拉数据再动笔：技术面跑脚本，基本面手工查，每个数字有来源。空有框架没数据的初稿 = 半成品。

---

## B. 环境绑定参考实现（Muse 环境，换环境时重写）

以下每条对应 A 部分的某条原则，是"在我这台机器上怎么做"。迁移时保留 A，B 按新环境重写。

- **B-A1**：`muse.write` 整文件写中文时特定括号内容会被静默吞掉 → 中文标注改用［］全角方括号。`muse.edit` 单点改不受影响。
- **B-A4**：本机 git HTTPS 无认证，push 走 `gh-api-push.py`（Git Data API，逐个重建 commit）。开工检查脚本 `gh-sync-check.py`，merge 收尾脚本 `gh-post-merge.py --all`。
- **B-A4**：API 重建历史后本地/远端可能分叉 → push 前 `git merge-base` 确认，必要时在远端 tip 上建临时分支做 sync commit 再 cherry-pick。
- **B-A3**：Spark Tank deck 维护用 python-pptx 直接编辑（build_deck.py 已退役）。
- **B-杂项**：npm publish 永远由 Stone 本人执行；agent commit author 用 `stone <stoneskin@gmail.com>`。

---

## 迁移指南（给新环境的三步）

1. **直接拿走 A 部分**：全文复制，删掉 A7 换成你自己的域（如不需要可整节删）。
2. **重写 B 部分**：把每条 B 按你的工具链重写一遍——"在我这怎么做"。
3. **立第一条新规矩时**：先标"通用"还是"环境"，再归位。分类习惯本身就是制度化的开始。

## 版本历史

- **v0.2**（2026-10-17）：+6 条（premise-first、red-team-opinions、review-round-cap、driver-owns-it、incident-to-eval、fresh-eyes）；修复 v0.1 两处排版错乱（A2 future-goes-to-doc/given-when-then、A3 copy-manual-verbatim/approve-fatigue-guard）。
- **v0.1**（2026-10-16）：初版，A/B 分层结构。
