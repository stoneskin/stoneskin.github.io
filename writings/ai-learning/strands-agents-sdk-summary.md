# Strands Agents SDK 导读：AWS 的开源 Agent 框架，「是库不是平台」

[← 返回目录](index.md)

> 官方文档：https://strandsagents.com/
> 仓库：https://github.com/strands-agents/harness-sdk
> 读法：对照官方文档；与 Bedrock AgentCore 配套读

---

## 一句话

AWS 的开源 agent 框架，定位是「是库不是平台」：Agent 对象 + @tool 装饰器，模型默认 Bedrock、一行可换。现分两层：harness（create_harness 一行整装）与 SDK（自己拼 loop）。企业 agent 路线走 AWS 栈时，这份与 AgentCore 是最先要学的两份。

## 关键机制

- **hooks 可拦截 loop 每一步**：日志、校验、改道都能挂在 loop 上——这是企业审计与审批门的天然挂点，不用在业务代码里到处埋点
- **guardrails、steering、context 管理内置**：不像最薄 harness 那样全靠外挂
- **MCP、流式、多 agent 模式内置**：工具接入与多 agent 不用自己再搭一层
- **部署靶子就是 AgentCore Runtime**：Nx plugin 可生成 CDK / Terraform 脚手架，与 AgentCore 是一套的上下层

## 三个关键问题

1. **harness 的预置默认到底是什么？** 官方说的 benchmarked defaults 具体是哪些，每一项能逐项覆盖到什么程度？
2. **hooks 的拦截粒度够不够做「写操作要审批」？** 审批门挂在哪个 hook 点，误放与误拦的边界在哪？
3. **与 Pi 对照：同是薄 loop，取舍差在哪？** Pi 故意不做的企业件（observability、context 管理），Strands 以 AWS 默认带上了——多出来的默认，什么时候是助力、什么时候是包袱？

## 练手

官方 quickstart 号称 20 分钟跑通（Bedrock 版）；再换本地 Ollama 跑一遍，验证 provider 抽象是不是真的一行切换。跑通之后再回头读 hooks 那一节，才知道拦截点该挂在哪。

## 跟其他材料的咬合

- **Bedrock AgentCore**：Strands 是框架层，AgentCore 是托管基础设施层，两份合起来才是 AWS 路线的全貌
- **Pi**：同是薄 loop，Pi 是最小内核参照，Strands 是"薄 + 企业默认"的参照
- **UMich AASE L09/L11**：停止条件与审批门那两讲，是给 Strands 的 hooks 与 guardrails 做验收清单用的
