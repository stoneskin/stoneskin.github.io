# Mr. Sun

**Tech Lead | Software Architect | AWS Cloud Specialist**

stoneskin@gmail.com | [linkedin.com/in/stoneskin](https://www.linkedin.com/in/stoneskin/) | [github.com/stoneskin](https://github.com/stoneskin/)

---

## Professional Summary

Software Architect and Tech Lead with **20+ years** of experience in .NET, full-stack, and AWS cloud solutions — now focused on taking AI agents from demo to production: memory, evaluation, and human-in-the-loop control. iPipeline's Ping/OAuth identity expert. Recently led the **Tiger Team Ping Identity AWS migration** — moved PingAccess, PingFederate, PingDirectory, and PingDelegatedAdmin from on-prem to a dedicated AWS account with GitHub Actions CI/CD, dual-layer IaC (Terraform + CloudFormation), and blue/green cut-over; production cut-over completed November 7, 2026.

---

## Core Skills

- **Cloud:** AWS (EC2, ASG, ECS Fargate, Lambda, S3, EFS, ECR, ALB/NLB, Route 53, SSM, KMS, CloudFormation, Image Builder, SAM)
- **CI/CD:** GitHub Actions (OIDC), Jenkins, Docker, blue/green deployment
- **Languages:** C#, TypeScript/JavaScript, Python, Java, SQL, Bash, PowerShell
- **Web:** ASP.NET Core, React.js, Redux, Node.js, REST APIs
- **Auth:** SAML, OAuth, PingFederate, PingAccess, PingDirectory
- **AI/ML:** LLM, NLP, RAG, MCP, agent frameworks (Strands), evals, OpenAI, HuggingFace, MS Copilot Studio
- **Leadership:** Team lead (6 devs + 2 QA), architecture, mentorship

---

## Experience

### iPipeline, Inc. (Roper Technologies) — Expert Software Engineer (Tech Lead, Tiger Team)
*April 2013 – Present (12+ years)*
*Title progression: Lead Developer → Solution Architect → Expert Software Engineer*

Lead a team of 6 developers and 2 QA managing **40+ applications**. Architect AWS cloud-native and serverless solutions. iPipeline's Ping/OAuth identity expert — go-to resource for PingFederate, PingAccess, PingDirectory, and enterprise SSO (SAML/OAuth) integrations across teams.

**Tiger Team — Ping Identity AWS Migration (2025–2026):**
- Technical lead for all Ping-Configuration IaC (Terraform base layer + CloudFormation), CI/CD, and migration architecture. Production cut-over completed November 7, 2026 — the new AWS platform fully replaced the on-prem environment.
- Retired Jenkins + Octopus; delivered **GitHub Actions + OIDC** pipeline with a **3-workflow release architecture** (infrastructure / Golden AMI image build / application) and one-click bootstrap orchestrator.
- Designed **blue/green topology** (primary/secondary slots `DEV→QD0`, `QA→{TD0→STG, UAT→PROD}`) with Route 53 DNS cut-over and manual active-pointer flip for zero-downtime migration.
- Authored **CloudFormation** stacks for the full Ping stack (PingFederate, PingAccess, PingDirectory, PingDelegator, EFS, NLB, S3, OIDC CI worker role); built a **500-user load-test harness** with on-prem vs AWS baseline and autoscaling policies; fixed a customer (NYL) SAML session-timeout issue with a PingFederate path rewriter.

**Other Key Projects:**
- **Calc-Engine AWS Serverless** — Migrated to AWS SAM + Lambda + DynamoDB with GitHub Actions CI/CD (**70% performance improvement**).
- **iSolve Quoting Solution** — iPipeline's **first cloud-native application** on AWS.
- **Quote Client & Web API** — React/Redux SPA + .NET Core with blue/green deployment.
- **Next-Gen Quote Engine (CalcStorm)** — Node.js/React/MongoDB.
- **Quote AI Agent** — LLM/prompt-engineering prototype for Quote Web UI.

### Comcast Corp (via Turnberry) — Senior .NET Lead Developer
*Sep 2012 – Apr 2013* — Led CI/CD implementation; delivered widget-based customer management GUI (MVC3 + jQuery) and auto-deployment tooling.

### Kemper Corporation — Senior Web Application Developer
*May 2010 – Aug 2012* — Built New Policy Holder Service (ASP.NET 4 / MVC3); refactored UDILibrary to 3-tier IoC/WCF; led source-control and auto-build revolution.

### Broadview Networks — Web Application Developer
*Apr 2003 – May 2010* — Independently designed internal web apps across MS SQL Server, Oracle, and MySQL; built billing management and jeopardy reporting GUIs (ASP.NET, C#, nHibernate, J2EE/JSP).

---

## AI Projects & Open Source

- **open-memex** — Creator of a local-first memory layer for AI coding agents (MCP server + CLI, published on npm). Markdown as source of truth, SQLite search, human-reviewed capture. [Repo](https://github.com/stoneskin/open-memex)
- **PingPilot** — Leading the design of an AI agent that triages identity-platform service-desk requests: case grouping, precedent matching, deterministic execution with human approval.
- **WorkBuddy / AiHarness** — Personal AI assistant orchestrating GitHub Copilot CLI (plan–execute–verify loop, scheduled work, Teams command); multi-model harness with trust labels and injection scanning.
- **muse-thinktank** — Open-source multi-model deliberation jury console: one question goes to a panel of models, then judge → synth, with human final review. [Repo](https://github.com/stoneskin/muse-thinktank)

---

## Education

- **MS Computer Science** — Villanova University (GPA 3.85/4.00)
- **Software Engineering Certificate** — Villanova University
- **Sun Certified Programmer for Java 2**; **OCA Oracle 9i DBA (SQL)**

---

## Community

- **MLCCC Chinese Characters Recognition App** (2023–present) — Donated web app to Mainline Chinese Culture Center; mentors high-school/college contributors. [Repo](https://github.com/MlcccCodingClass/ChineseCharactersRecognitionApp)
- **Minecraft-Python** (2019–2020) — Created tutorials on learning Python through Minecraft; developed multiple Minecraft plugins using Python. [Repo](https://github.com/stoneskin/python-minecraft)
- **Programming Classes (MLCCC)** — Teach Scratch (G2-5) and Java + AP CSA (G8+); taught Python (G6+) until July 2026.

---

*Updated: November 2026*
