# Suraj Sharma《AI Agent 工程师 12 步学习路线图》

[← 返回目录](index.md)

分级：【摘要即可】——12 步与缺口盘点条内齐全。

来源：[英文原帖](https://x.com/suraj_sharma14/status/2111789399176335412)（@suraj_sharma14，10/18，14 万浏览）· [中文解读](https://x.com/UPing123zzz/status/2112157681729564861)（Ethan 恩宇 @UPing123zzz，10/19）· 图：`~/workspace/your_files/agent-roadmap/roadmap-12steps.jpg`

**是什么**：12 步学习路线，每步三列（学什么 / 练手项目 / 为什么）。核心观点：Demo 和生产系统的分水岭是稳定运行、安全执行、故障恢复、交付客户。

**12 步**：
01 架构和状态机（DAG/LangGraph/Temporal）→ 02 工具调用和 MCP → 03 操作电脑界面（Playwright）→ 04 记忆和上下文 → 05 多 Agent 协作（A2A）→ 06 沙箱执行（E2B/gVisor）→ 07 Agent 安全防护 → 08 人工审批 → 09 自我纠错 → 10 执行轨迹评测（作者注：最常被跳过）→ 11 降级兜底 → 12 公开复盘

### 跟你的咬合（2026-10-20 盘点）

12 步中已亲手做过 8 步：04（open-memex 三区记忆）、05（thinktank 陪审团）、10（thinktank PR #23 评测）、08（estimate go/no-go）、11（opencode-fuse fail-closed）、02（open-memex MCP）、12（site 双语写作）、09（升档重跑）。

**两个缺口**：03 操作电脑界面（Playwright/DOM/Set-of-Mark）、06 沙箱执行（E2B/gVisor/Docker-in-Docker）——都是"让 Agent 真正动手"的执行层。
