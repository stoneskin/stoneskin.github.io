# ai-memory 总结（akitaonrails/ai-memory）

[← 返回目录](index.md)

- 仓库：https://github.com/akitaonrails/ai-memory（MIT，10k star，Rust 单二进制）
- 定位：给 AI coding agent 的长期记忆，核心卖点是**跨 agent handoff**——Claude Code 写到一半，换 Codex 在同一目录继续，不用重新解释架构和失败尝试

## 和 open-memex 像的地方

- Markdown 文件是 source of truth，数据库是可重建的派生索引——架构信条一致
- Zero-LLM 默认路径：capture、search、handoff 都不用 API key
- 对自己诚实：实测数字（write ceiling ~700/s）、audit log、purge 命令说清楚"删除"到底是什么意思

## 它走得更远的地方

1. **跨 agent handoff（杀手功能）**：typed protocol + claim-once，20+ harness 集成（Claude Code、Codex、Cursor、Gemini CLI、OpenCode…）
2. **自动捕获**：lifecycle hooks 静默记录 prompt/tool 调用/session 边界，不用你说"记住"；在 typed privacy boundary 先脱敏再存
3. **无 LLM 的记忆老化**（最值得看）：
   - per-tier 衰减曲线（可按 tier 调）
   - **access-weighted retention：用得越多衰减越慢**（打开/搜索/链接都算 use）
   - 冷的 episodic 笔记压缩成 durable facts（文件路径、错误码、决策）而不是丢掉
   - 近似去重合并、矛盾标记——全部零 LLM、可逆（git 兜底，restore-page 恢复）
   - 重写/删除类操作（compaction、dedup）默认关闭，手动开
4. **Dream 模式**（opt-in）：LLM 后台把冷笔记集群重写成连贯页面，空闲时跑、你一回来就取消；必须先过 recall eval 才可能变默认
5. **跨项目 profile**：你的工作习惯（包管理器、测试布局）跟着你到每个新 repo
6. **Server 架构**：记忆住在你自己跑的 server 上（本机/homelab），跨机器、团队共享内置（multi-user auth、per-person attribution、audit log，不是付费 tier）

## 对 open-memex 的借鉴点

- **access-weighted retention 正是三区架构"换入换出策略"的具体实现**：我们今天刚写进 V2-DESIGN §18 backlog 的难点（"有用 ≠ 最近用过"），他们用"访问加权衰减"给了一个零 LLM 的工程答案。建议看 `docs/ARCHITECTURE.md` 的 decay 一节
- "Coming from another tool?" 迁移对照表——诚实的竞品定位写法，值得学
- 零 LLM 老化机制比"定期人工复审"更工程化，可作为 Warm 区（堆肥区）自动化的参考实现

## 不借鉴的

- Server 架构：open-memex 是 local-first，方向不同
- Rust 重写：没必要，借鉴机制不借鉴实现

*整理：2026-10-18 · Stone 推荐*
