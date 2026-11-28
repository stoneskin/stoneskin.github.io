# Google 官方 Agent Skills 库导读：200 多个第一方 skill，一份写法参照

[返回 AI 学习资料总目录](./index.md)

**来源：** Google《Agent Skills》，GitHub 仓库 [google/skills](https://github.com/google/skills)，2026-03-31 建库，Cloud Next 2026 发布，Apache 2.0。［原文仓库](https://github.com/google/skills)

**快照：** 本导读按 2026-11-28 的 README 写：主清单 219 项，star 24,851，fork 2,073，670 个 commit。库长得很快（发布时 13 个，8 个月到 200+），数字以仓库为准。

**分级：** ［摘要即可］——价值判断、重点 skill 与分类清单已写到能独立成立；想装 skill 直接按 README 的命令，不用读完全文。

## 一句话结论

Google 把"agent 该怎么用 Google 产品"写成 200 多个按需加载的 SKILL.md：不是一篇讲 skill 的文章，是第一方 skill 写法的大样本，也是一份查阅型工具书——用 GCP 时按需翻，不用全读。

## 为什么值得看

第一，**第一方 skill 写法的大样本**。Stone 写 skill 有自己的方法论（mattpocock 的 writing-for-agents 清单），这是 Google 怎么写 SKILL.md 的参照：每个 skill 都是一个文件夹，description 当触发器、正文给步骤与检查标准、信息分层，想看"大厂怎么写 skill"直接读原文，不用猜。

第二，**Agent Platform 那组跟他的项目直接相关**。Eval Flywheel（评测飞轮）、Prompt Management、RAG Engine、Model Garden、Skill Registry、Agent Registry——PingPilot 的 eval 方法论、智囊团的评审思路，都能拿这组对照。Agent Gateway 多智能体安全、Google Skill Finder 也是同一路的。

第三，**格式本身正在成标准**。Agent Skills（agentskills.io）那套 SKILL.md 格式，Google、Anthropic 都在往这靠；装法也统一了：`npx skills add google/skills` 挑着装，`npx skills update` 更新，Claude Code / Codex / Antigravity 还能整包当 plugin 装。

第四，**清单本身就是价值**。200 多个 skill 按 11 个大类排好（见下文精读层），Stone 之前问"不收 skills 工具 list 吗"——收的就是这份清单：以后用 GCP 某个产品，先来这里查有没有官方 skill，不用自己从零写。

## 局限与注意

- **大头是 GCP 运维**。GKE 一个大类就占 54 个（创建、排障、扩缩容、TPU），再加 BigQuery、Cloud SQL、Spanner、Firebase。Stone 日常是 AWS + iPipeline，整库装没意义，挑几个读就行。
- **数字长得快**。13 个起步，8 个月到 219 个；本导读的清单是 2026-11-28 的快照，新增的 skill 以仓库 README 与 `index.json` 为准。
- **姊妹库不在这个仓库里**。Gemini API 开发技能在 google-gemini/gemini-skills，前端/demo 技能在 google-gemini/demolab，README 的"Additional Google skills"另列了 ADK、Android、Dart、Firestore、Flutter、Maps 等外链库。

## 怎么用

- 只想看写法：读两三个 skill 的 SKILL.md 原文（建议从 Eval Flywheel 或 BigQuery Basics 入手），对照自己的 skill 写作清单。
- 要用 GCP：`npx skills add google/skills`，按提示挑 skill、挑 agent、挑安装范围（项目级或全局）。
- 要跟进：`npx skills update` 更新已装的 skill，顺带清掉过时的。

## 精读层：分类技能清单（2026-11-28 快照）

★ = 与 Stone 的项目（PingPilot / 智囊团 / open-memex / WorkBuddy）直接相关，优先看。其余只留名，按需翻。原文链接见仓库 README。

### 入门（3）

- Authenticating and Authorizing to Google Cloud (IAM)
- Google Cloud Recipe: Foundation Builder
- Onboarding to Google Cloud

### 多产品方案（12）

- Google Cloud solution-architecture workflow
- ★ Agent Gateway multi-agent security——多智能体安全网关，与 PingPilot 的权限边界、WorkBuddy 的 brain/hand 划分对照
- Agentic analytics across cloud providers and data types
- Borderless open data lakehouse agentic AI system
- ★ Build and deploy AI agents on Google Cloud——官方的 agent 落地流程
- Dynamic Hybrid Search using AlloyDB
- Event-driven decoupling with Pub/Sub
- ★ Google Skill Finder——帮 agent 找到该用哪个 skill，skill 注册与发现的官方做法
- Live bidirectional multimodal streaming agentic AI solution
- Migrate AI Workloads to GKE Inference
- RAG for enterprise search using GKE and AlloyDB
- Secure n-tier serverless web application with strict private application tiers

### AI/ML（32）

- Agent Access Audit
- Agent Platform Alert Configuration
- Agent Platform Autorater Customization
- Agent Platform Endpoint Management
- ★ Agent Platform Eval Flywheel Skill——评测飞轮，PingPilot eval 方法论的对照组
- Agent Platform GenAI Inference Skill
- Agent Platform Model Garden Deploy Skill
- Agent Platform Model Registry Management
- Agent Platform Model Tuning
- ★ Agent Platform Prompt Management——官方的提示词管理做法
- ★ Agent Platform RAG Engine Management——官方 RAG 引擎管理
- Agent Platform Troubleshooting
- Agent Platform Tuning Management
- API Gateway Remote MCP Server (Public Preview)
- Apigee as an Agent Gateway Service Extension
- BigQuery AI & ML
- Gemini API in Gemini platform
- Gemini Enterprise Agent Platform - Managed Agents API Skill
- ★ Gemini Interactions API Skill——Gemini 新一代 Interactions API
- Gemini platform Architecture and Engineering Guide
- Genkit Dart
- Genkit Go
- Genkit JS
- Genkit Python
- ★ Google Cloud Agent Registry——agent 注册表
- LiteRT on Google Tensor: compile, benchmark, package for apps
- LiveAPI Service Skill
- Migrating from Gemini API in AI Studio to Agent Platform
- Pathways on Cloud Workload Debugging Skill
- ★ Skill Registry——skill 注册表，skill 发现与治理的官方做法
- Troubleshoot GKE TPU multi-slice hangs with the MXLA Hang Analyzer
- Troubleshoot GKE TPU performance degradation with ML Diagnostics Workload Monitoring

### 基础设施（54）

- Cloud Network Insights
- Cloud Storage Basics
- Cloud Storage Bucket Architect
- Cloud Storage Diagnostic
- Cloud Storage FUSE
- Compute Engine Future Reservations & Calendar-Mode Feasibility
- Compute Engine Managed Instance Group (MIG) Autoscaling Troubleshooting
- Compute Engine On-Demand Reservations
- Compute Engine Resource Availability and Stockout Troubleshooting
- Compute Engine Spot Capacity Advice
- Compute Engine VM Creation
- Compute Engine VM Host Events & Infrastructure Crash Troubleshooting
- Designing and Deploying GCP Infrastructure with Application Design Center
- Filestore Auditing Skill
- Filestore Autoscale
- Filestore Log-Based Troubleshooting
- Filestore NFS File Browser
- GKE AI/ML Inference
- GKE Alert Configuration
- GKE App Onboarding
- GKE Backup & Disaster Recovery
- GKE Basics & Critical Gotchas
- GKE Batch & HPC Workloads
- GKE Cluster Autoscaler
- GKE Cluster Creation
- GKE ComputeClasses
- GKE Golden Base Image Discovery Expert
- GKE Golden Path Configuration
- GKE JobSet Interruption Troubleshooting
- GKE Kueue troubleshooting
- GKE Manifest Generation Skill
- GKE Multi-Tenancy
- GKE Networking
- GKE Node NotReady Troubleshooting Skill
- GKE Productionize Skill
- GKE Reliability
- GKE Service Networking Skill
- GKE StatefulSet without readiness probes
- GKE Storage
- GKE Storage Troubleshooting Skill
- GKE TPU Dynamic Slices Monitoring & Management
- GKE unprotected StatefulSet skill
- GKE Upgrades & Maintenance
- GKE Workload Scaling
- GKE Workload Scaling Troubleshooting Skill
- GKE Workload Troubleshooting Skill
- Google Cloud global external Application Load Balancer Configuration Skill
- Google Cloud Networking Observability Expert
- Triage GKE capacity constraints for a Pending workload
- Troubleshoot GKE TPU reservation stockouts caused by leaked node pool capacity
- Troubleshoot GKE TPU slice creation blocked by an unstable MIG
- Troubleshoot GKE TPU VMs stuck in Compute Engine repair (`REPAIRING`)
- Troubleshoot TPU slice creation failures caused by partition overlap
- Troubleshoot unresponsive GKE TPU and GPU nodes (`NodeStatusUnknown`)

### 数据库与分析（26）

- AlloyDB Basics
- BigFrames (BigQuery DataFrame) basics
- BigQuery Asset Impact Analysis
- BigQuery Basics
- BigQuery Migration Data Exporter
- BigQuery Migration Data Loader
- BigQuery Migration Metadata Extraction
- BigQuery Migration Service (BQMS) SQL Translator
- BigQuery Migration Validator
- BigQuery Observability
- BigQuery Optimization Workflow
- BigQuery Troubleshooting
- BigQuery User-Defined Functions (UDFs)
- Bigtable Basics
- Cloud SQL Basics
- Data Lineage Summary
- dbt Snowflake to BigQuery Translator
- GCP Managed Airflow DAG Authoring Guide
- Google Cloud Database Onboarding Skill
- Managed Service for Apache Airflow (formerly Cloud Composer) DAG troubleshooting guide
- Managed Service for Apache Airflow (formerly Cloud Composer) Migration Guide
- Managed Service for Apache Airflow (formerly Cloud Composer) recommendations
- Spanner Basics
- Spanner Graph Query Tuning Best Practices
- Spanner Graph Schema Design & Topology Best Practices
- Spanner Relational-to-Property-Graph Schema Conversion

### 开发者工具（16）

- Cloud Build Basics
- Cloud Deploy Pipelines
- Cloud Operator
- Developer Device Platform
- Developer Device Platform: Device Run
- gcloud CLI Skill for AI Agents
- Gerrit Code Review
- Google Agents CLI Onboarding
- Google Cloud CI/CD Deployment
- Google Cloud CI/CD Pipeline Design
- Google Cloud Release Radar
- Google Developer Knowledge
- Set up Cloud Operator for an organization
- Set up the operator agent
- Share existing Google Cloud context with the operator agent
- Terraform GCP Skill

### 应用开发（5）

- API Gateway OpenAPI Spec Authoring
- Application Integration Authoring
- Application Integration Basics
- Application Integration Troubleshooting
- Migrate Legacy Codebases to Safe Rust

### 管理工具（20）

- Cloud Logging Finops
- Cloud Monitoring Chart Generation Skill (`cloud-monitoring-chart-generation`)
- Cloud Monitoring ListTimeSeries Request Generator
- Cloud Monitoring Notification Channels Configuration
- Cloud Monitoring PromQL Generator
- Cloud Trace Querying Skill (`cloud-trace-querying`)
- Configure Cloud Monitoring Alerts
- Configuring Cloud Logging
- Configuring Cross-Project Logging
- Generate Logging Query Language queries
- GKE Cost Analysis
- GKE Cost Optimization
- GKE Observability
- GKE TPU Metrics Monitoring Guide
- Handle Disruption on GPUs and TPUs Troubleshooting
- Metric Selection (Service Query & Local Keyword Filtering)
- Personalized Service Health incident correlation
- SLO Alert Configuration Setup Wizard
- TPU Connection Failure and VBAR OOM Troubleshooting
- Workload Manager Basics

### Well-Architected Framework（6）

- Google Cloud Well-Architected Framework skill for the Cost Optimization pillar
- Google Cloud Well-Architected Framework skill for the Operational Excellence pillar
- Google Cloud Well-Architected Framework skill for the Performance Optimization pillar
- Google Cloud Well-Architected Framework skill for the Reliability pillar
- Google Cloud Well-Architected Framework skill for the Security, Privacy, and Compliance pillar
- Google Cloud Well-Architected Framework skill for the Sustainability pillar

### 安全与身份（24）

- API Gateway Backend Security and Rate Limiting
- Cloud Armor OWASP Rule Upgrader (CRS 3.0/3.3 -> 4.22)
- Compliance Environment Assessor Skill
- Custom Resource Authoring & Synthesis Skill (`assuredworkloads-frameworks-author`)
- Data Boundary Framework Navigator (`assuredworkloads-frameworks-navigator`)
- DPoP Adoption & Identity Security Architecture
- GKE Platform Security
- GKE Workload Identity Federation Troubleshooting Skill
- GKE Workload Security
- Google Cloud Assured Workloads Basics (V1 GA)
- Google Cloud Security Command Center Remediation
- Google SecOps Case Management Skill for AI Agents
- Google SecOps Detection Engineering Skill
- Google SecOps Incident & Entity Investigation Skill
- Google SecOps Security Alert Triage Specialist
- Google SecOps Threat Hunting Skill
- IAM Access Troubleshooter & Remediation Orchestrator on Google Cloud
- IAM Helper for Policy Management
- IAM Policy Simulator (v1 Allow)
- IAP troubleshooting for Gemini Enterprise Agent Platform
- Privileged Access Manager (PAM)
- SecOps Detection Coverage Skill
- Security Command Center Query Skill on Google Cloud
- Sign In With Google (SiwG) Integration & Security Architecture

### Web 与应用托管（4）

- API Gateway Troubleshooting
- Cloud Run Alert Configuration
- Cloud Run Basics
- Firebase Basics

### 广告（15）

- AI Migration Agent Instructions for the Google Mobile Ads SDK
- Data Manager API Audience Ingestion
- Data Manager API Event Ingestion
- Data Manager API Setup
- Data Manager API Troubleshooting
- Google Ads API Account Performance Diagnostics Skill
- Google Ads API MCP Server Installation
- Google Ads API Quickstart
- Google Mobile Ads SDK - Banner Ads
- Google Mobile Ads SDK - Install
- Google Mobile Ads SDK - Interstitial Ads
- Google Mobile Ads SDK - Rewarded Ads
- IMA DAI SDK
- IMA SDK client-side
- Validate Google Mobile Ads SDK Integration

### 其他（2）

- Getting Started with Google Analytics Admin API
- Getting Started with Google Analytics Data API

### 另：Additional Google skills（7 个外链库，不在主清单里）

- Advanced Google Cloud Storage Skills
- Agent Development Kit (ADK) Skills
- Android Skills
- Dart Skills
- Firestore Skills
- Flutter Skills
- Google Maps Platform Skills

### 另：Plugins（整包当插件装）

- Claude Code：`claude plugin marketplace add google/skills`，再 `claude plugin install <plugin>@google-plugins`
- Codex：`codex plugin marketplace add google/skills`，再从 `/plugins` 浏览器里装
- Antigravity CLI：`agy plugin install https://github.com/google/skills/<plugin-path>`

## 证据不支持什么

- 这份导读只核对了仓库 README 的清单与安装命令，没有逐个读 219 个 skill 的 SKILL.md——重点 skill 的内容以各自原文为准。
- star 数、skill 数都是 2026-11-28 的快照，仓库仍在快速长，别把本页的数字当现状引用。
