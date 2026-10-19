# Stone 谈人机交互（2026-10-19）

> 起因：读 InfoQ《Anthropic Lead: HTML Increasingly Better Than Markdown at Keeping Humans Engaged in Agentic Loops》有感。https://www.infoq.com/news/2026/06/anthropic-html-markdown-agent/

Anthropic 的 Thariq Shihipar 说 HTML 比 Markdown 更能让人保持在智能体循环里，Simon Willison 附和，反对者说这是倒退。两边都有道理，但我觉得**这个问题本身被问小了**。

AI 与人的交互是个长期不断发展的大课题，不是 HTML 或 Markdown 这么简单的二选一。它是自从有电脑以来人机交互的延续——命令行到图形界面到触屏到语音，每一次都是"人怎么和机器说话"这个老问题的新版本。AI 只是最新的一章。

当前 MD 和 HTML 都能用，解法不是二选一，而是**加一个转换器**：机器用 token 效率最高的数据层，人用信息密度最高的数据层，中间做转换。就像编译器——没人争论该用汇编还是高级语言写业务代码，因为编译器解决了分层问题。

输入端也一样：现在人可以用语音、手势输入，将来也许是脑机接口。输出端今天争 HTML/Markdown，明天可能争别的。**没有什么一成不变的标准答案**，标准答案只存在于"当前的人机界面是什么"这个上下文里。

所以 Shihipar 和反对者其实不矛盾：他解决的是"今天，人在手机/浏览器前怎么看住 agent"；反对者担心的是"token 税、安全、git"。都是对的，只是站在不同的层。分层 + 转换器，两边都要。

—— Stone，2026-10-19
