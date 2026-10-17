# 给 Agent 写文档的检查清单

译自 mattpocock/skills 的 `writing-for-agents`（SKILL.md + SKILL-MECHANICS.md），按原文结构整理，
措辞尽量贴原文。原文是英文，这里翻成中文检查项，写 skill / AGENTS.md / CLAUDE.md 时逐条过。

> 来源：https://github.com/mattpocock/skills

## 一、Context Pointer（上下文指针）

指针 = 常驻在 agent 上下文里、指向上下文之外的材料的一句话（skill 的 description 就是一个指针；
AGENTS.md 里点名某个文档的那一行也是）。**是指针的措辞、而不是目标内容，决定 agent
什么时候去取那份材料**——好材料配弱措辞 = variance bug，先修措辞，修不好才考虑 inline。

- [ ] 指针只干两件事：说清材料是什么 + 列出触发分支（branch：文档覆盖的不同情形，
      不同 run 会走不同路径）
- [ ] 触发词前置（front-load the leading word）：指针触发靠的是开头几个词
- [ ] 一个分支只写一个触发词：同义词改写同一分支 = 写了两遍，合并，只留真正不同的分支
- [ ] 删掉正文已有的身份信息：指针里别重复自我介绍

## 二、两种 Load（负载预算）

你加的每一份文档、每一个指针，都在花两种预算中的一种：

- [ ] **Context load**：常驻材料的成本——AGENTS.md 的一行、skill 的 description，
      每一轮都在烧 token 和注意力，不管触不触发。常驻的东西，精简要下狠手。
- [ ] **Cognitive load**：人的成本——人要记住"有这份文档、什么时候用它"。
      这不是要消灭的成本，是人的主权价格：该人判断的地方就让人记，不该让人记的才拿掉。
- [ ] 只有经指针才触达的材料：context load 为零，只付指针那一行的钱。

## 三、信息分层（Information Hierarchy）

文档由两种内容构成：**steps**（agent 按顺序做的事）+ **reference**（按需查的定义/规则/事实）。
核心决策是每块材料放在分层的哪一 rung：

1. **In-file step**：主体层，agent 按顺序做的事
2. **In-file reference**：同文件内按需查阅（平铺的规则集是合法形态，不是坏味道）
3. **Disclosed reference**：拆到独立文件，经 context pointer 触发才加载

- [ ] **Progressive disclosure**：只把所有分支都需要的东西 inline，部分分支才需要的推到指针后面。
      最干净的判据是分支：inline 每个分支都要的，disclose 只有部分分支走的。
- [ ] **Co-location**：一个概念的定义、规则、caveat 放在同一标题下，别打散。
      检验：一处读完，邻居自然带到。注意这不是 duplication（重复是同一意思写两遍；
      打散是一个意思碎成多片）。
- [ ] 防 **Sprawl**：文档太长本身就是病——每行都活着也照样稀释注意力。
      治法就是分层：reference 往指针后藏，按分支/序列拆。

## 四、Step 的完成标准（Completion Criteria）

每个 step 结尾都要有一个"做完的条件"。两个属性决定它是不是杠杆：

- [ ] **Clarity**：agent 能分清做完 vs 没做完吗？模糊的标准（如"理解到位"）会诱发
      **premature completion**（提前收工——注意力滑向"做完了"而不是"做对了"）。
      防守顺序：先 **sharpen the bound**（把标准写死，本地最便宜）；只有标准本质上
      fuzzy、**且**你观察到抢跑，才考虑把后面的 step 藏起来（拆分）。注意：藏只在真实
      context 边界后有效（subagent 派发 / handoff）；inline 调用藏不住，后面的 step
      还在上下文里，等于没藏。
- [ ] **Demand**：要求够狠吗？"每个改过的模型都交代了"逼 agent 挖地三尺，
      "列个改动清单"不逼。Demand 不只绑 step：纯 reference 文档里"每条规则都执行了"
      同样是穷尽性要求。
- [ ] 最强的标准：**可检查 + 穷尽**，两者兼备。

## 五、什么时候拆分

拆分要花掉一种 load（见第二条），所以切口必须赚回来：

- [ ] **按 sequence 拆**：后面的 step 会诱惑 agent 在当前 step 抢跑时，把后面藏起来。
      反过来警惕：合并序列会让每步都看到后面的 step，同样诱发抢跑。
- [ ] **按 invocation 拆**（skill 专用）：见第六条。

## 六、Skill 专属机制（SKILL-MECHANICS）

- [ ] **Model-invoked**（默认）：写 description，agent 可自主触发、别的 skill 可调用。
      代价是 description 常驻上下文（permanent context load）换可发现性。
      description 里按指针规则写触发分支。纯 reference 内容也可以做成 model-invoked skill，
      当几个 skill 共享引用的唯一住处。
- [ ] **User-invoked**：设 `disable-model-invocation: true`，只有人手输名字能触发，
      别的 skill 也调不到。零 context load，代价是 cognitive load——人得记得它存在。
      **只会被人手触发的 skill，一律用这个，别付常驻的钱。**
- [ ] 共享引用的死角：两个 user-invoked skill 都需要的公共材料，放哪个 skill 里都不对
      （都没 description，互相够不着）→ 抽成 skill 系统之外的普通文件，各 skill 用指针引用。
- [ ] **Router skill**：user-invoked skill 多到记不住时，加一个 router skill 列出它们和各自的
      使用时机，人只要记住这一个。它只能 hint，不能替人触发。
- [ ] 拆出新 skill 的时机：有独立触发词（你会在 prompt 里实际用的词），或别的 skill 需要调用它。
      独立触达必须值回一份常驻 description 的价。

## 七、给你的 skill 写作规范的适配建议（我加的，非原文）

- [ ] description 评审三问：触发分支穷举了吗？触发词前置了吗？有没有同义重复？
- [ ] 新 skill 默认 user-invoked，除非 agent 必须自主触发或被别的 skill 调用——先省 context load
- [ ] 引用/改编别人的 skill，把 credit 写进 frontmatter `metadata`（学 pr skill 的 `credits` 字段：
      skill 名、作者、机构、原文 URL），署名纪律做进格式里
