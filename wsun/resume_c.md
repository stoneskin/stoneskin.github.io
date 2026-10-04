# Mr. Sun

**AI Solutions Architect | Tech Lead | AWS Cloud Specialist**

📧 stoneskin@gmail.com | 🔗 [linkedin.com/in/stoneskin](https://www.linkedin.com/in/stoneskin/) | 💻 [github.com/stoneskin](https://github.com/stoneskin/)

---

## Professional Summary

Seasoned Software Architect and Tech Leader with **20+ years** of experience in .NET web development, system architecture, and cloud solutions. Expertise in full-stack development, DevOps, and SaaS solutions. Proven track record in leading teams, driving innovation, and optimizing system performance.

**Currently leading:** AWS Migration Initiative at iPipeline (Tiger Team) - migrating legacy on-prem applications to AWS with modern CI/CD pipelines.

**Open source:** Creator of [open-memex](https://github.com/stoneskin/open-memex), a local-first memory layer for AI coding agents (MCP server + CLI, published on npm).

---

## Core Competencies

- ✅ AI/ML Integration (LLM, NLP, RAG, AI Agent Systems)
- ✅ Software Architecture & Cloud Solutions (AWS)
- ✅ Full-Stack Development (C#, React, Node.js, Python)
- ✅ DevOps & CI/CD Automation (AWS CodePipeline, Jenkins, Docker)
- ✅ Team Leadership & Technical Mentorship
- ✅ System Integration & Performance Optimization

---

## Technical Skills

| Category | Skills |
|----------|--------|
| **Programming** | C#, JavaScript/TypeScript, Python, Java, SQL |
| **Web** | ASP.NET Core, React.js, Redux, HTML5/CSS, REST APIs |
| **Cloud** | AWS (Lambda, EC2, S3, DynamoDB, SAM, CloudFormation, Fargate) |
| **Databases** | MS SQL Server, MongoDB, Redis, PostgreSQL, Oracle, MySQL |
| **DevOps** | GitHub Actions, Jenkins, Docker, Terraform, CI/CD |
| **Tools** | Git, Jira, Docker, Jenkins, Postman, VSCode |
| **Auth** | SAML, OAuth, PingFederate, Ping Access, Ping Directory |
| **AI/ML** | LLM, NLP, RAG, MCP, OpenAI, HuggingFace, MS Copilot Studio, Google Colab |
| **Methodologies** | Agile, Scrum, TDD, CI/CD, SOLID, Design Patterns |

---

## Professional Experience

### iPipeline, Inc. (A Roper Technologies Company) — PA
**Expert Software Engineer (Tech Lead, Tiger Team), R&D** | *April 2013 – Present (12+ years)*
*Title progression: Lead Developer → Solution Architect → Expert Software Engineer*

- Lead a team of 6 developers and 2 QA engineers, managing and building **40+ applications** (legacy and new)
- Architect and deploy multiple AWS serverless solutions, reducing operational costs
- Design and implement blue-green deployment strategy, reducing downtime and release risks
- iPipeline's Ping/OAuth identity expert — go-to resource for PingFederate, PingAccess, PingDirectory, and enterprise SSO (SAML/OAuth) integrations across teams

**🚀 Key Projects:**

| Project | Description | Tech Stack | Impact |
|---------|-------------|------------|--------|
| **Quote AI Agent** | NLP-powered prototype using LLMs and prompt engineering for Quote Web UI | OpenAI, LLM, Prompt Engineering | Prototype |
| **Calc-Engine AWS Serverless** | Migrated quote engine to AWS SAM with GitHub Actions CI/CD | AWS SAM, Lambda, DynamoDB, GitHub Actions | **70% performance improvement** |
| **iSolve Quoting Solution** | iPipeline's **first cloud-native application** | AWS (EC2, S3, Lambda, API Gateway, DynamoDB, SQS, CloudFormation) | Pioneering cloud adoption |
| **Quote Client & Web API** | SPA with modern deployment | React.js, Redux, .NET Core, Docker | Blue-Green deployment |
| **Next-Gen Quote Engine (CalcStorm)** | Node.js-based calculation engine | Node.js, React.js, MongoDB, JWT, Webpack | Modern architecture |
| **Auth/PingFederate** | Enterprise SSO integration | SAML, OAuth, PingFederate | Secure authentication |
| **Tiger Team - Ping Identity AWS Migration** (2025-2026) | Lift-and-shift PingAccess, PingFederate, PingDirectory, PingDelegatedAdmin from on-prem to a dedicated AWS account | CloudFormation, EC2/ASG, ECS Fargate, EFS, ECR, ALB/NLB, Route 53, SSM, KMS, EC2 Image Builder, GitHub Actions (OIDC) | In Progress |

---

### Comcast Corp (via Turnberry Solutions) — PA
**Senior .NET Lead Developer** | *Sep 2012 – Apr 2013*

- Designed, developed, and maintained .NET (C#) web applications
- Led CI/CD pipeline implementation, reducing deployment time

**🚀 Key Projects:**
- **Café:** Widget-based customer management GUI using .NET MVC3 & jQuery
- **Auto Deployment Solution:** Windows Service & Web GUI for automated deployments

---

### Kemper Corporation — PA
**Senior Web Application Developer** | *May 2010 – Aug 2012*

- Designed and maintained .NET web applications with mobile app & API integrations
- Led source control & auto-build deployment revolution, improving development efficiency

**🚀 Key Projects:**
- **New Policy Holder Service:** Built with ASP.NET 4 & MVC3, optimizing user experience
- **UDILibrary (3-Tier Architecture):** Refactored using IoC & WCF, improving modularity

---

### Broadview Networks — PA
**Web Application Developer** | *Apr 2003 – May 2010 (7+ years)*

- Independently designed and developed multiple internal web applications
- Developed applications across MS SQL Server, Oracle, MySQL
- Built J2EE/JSP-based solutions

**🚀 Key Projects:**
- **Billing Management Web GUI:** Architected using ASP.NET 3.5 & MVC Frameworks
- **Jeopardy Reporting & Management GUI:** ASP.NET 2.0, C#, JavaScript, nHibernate, SQL Server

---

## Current Focus (2025-2026)

### Tiger Team - Ping Identity AWS Migration

**Objective:** Lift-and-shift iPipeline's on-prem Ping Identity stack (PingAccess, PingFederate, PingDirectory, PingDelegatedAdmin) into a dedicated AWS account (us-east-1, multi-AZ), with zero-downtime blue/green cut-over across Dev, QA, UAT, and Production.

**Role:** Technical lead for migration architecture, infrastructure-as-code, and CI/CD — owner of the migration guideline and cross-team coordination (IT/Ops, security, application teams) on network segmentation, secrets management, and cut-over rehearsals.

**Key deliverables:**
- Retired Jenkins + Octopus Deploy; built GitHub Actions pipelines with OIDC federation (no long-lived AWS keys) and environment-gated approvals (Dev / QA / UAT / Prod). Designed a three-workflow release architecture (infrastructure / Golden AMI image build / application) plus a one-click bootstrap orchestrator for fresh AWS accounts.
- Designed blue/green topology with parallel primary/secondary slots and Route 53 DNS cut-over for zero-downtime migration.
- Authored CloudFormation IaC for the full Ping stack: PingFederate (Admin/Runtime on EC2 + ASG), PingAccess (Admin EC2 + engines on ECS Fargate with self-built Docker images and per-account ECR fallback), PingDirectory, PingDelegator on Fargate — plus networking and security (IAM, KMS cross-account grants, SSM).
- Built a 500-concurrent-user load-test harness; delivered an on-prem vs AWS comparative baseline report and autoscaling policies for PingAccess/PingFederate runtime services.
- Resolved customer-facing issues surfaced during migration, including a PingFederate path rewriter that fixed a NYL SAML session-timeout.

---

## Open Source & Community

### open-memex
*2026 – Present*

- Open-source project: a local-first memory layer for AI coding agents.
- Markdown as source of truth with SQLite FTS5 search; MCP server + CLI + editor integrations; human-reviewed memory capture; team knowledge sharing through git PRs.
- Published on npm with public development on GitHub.
- 🌐 [Repository](https://github.com/stoneskin/open-memex)

### MLCCC Chinese Characters Recognition App
*July 2023 – Present*

- Developed and donated a web application to the Mainline Chinese Culture Center for community use
- **Tech:** JavaScript, HTML (responsive), PHP, MySQL, Google Dictionary API, Hugging Face OpenAI API (LLM)
- Open-sourced project and mentored multiple high school and college students
- 🌐 [Repository](https://github.com/MlcccCodingClass/ChineseCharactersRecognitionApp)

### Minecraft-Python
*2019-2020*

- Created tutorials on learning Python through Minecraft, making programming engaging and interactive
- Developed multiple Minecraft plugins using Python
- Enhanced gameplay and customization for educational purposes
- 🌐 [Repository](https://github.com/stoneskin/python-minecraft)

### Programming Classes (MLCCC)
Teaching programming to K-12 students:

| Class | Grade | Tech | Schedule |
|-------|-------|------|----------|
| Scratch | G2-5 | Scratch Animation & Game | Sunday 3-4PM |
| Python | G6+ | Python syntax, algorithms, web | Ended July 2026 |
| Java | G8+ | Java + AP CSA prep | Private/Online |

---

## Education & Certifications

| Credential | Institution/Organization | Details |
|------------|------------------------|---------|
| 🎓 **MS Computer Science** | Villanova University, PA | GPA: 3.85/4.00 |
| 🏆 **Software Engineering Certificate** | Villanova University | |
| 🏆 **Sun Certified Programmer for Java 2** | Sun Microsystems | |
| 🏆 **OCA Oracle 9i DBA Certification (SQL)** | Oracle | |

---

## Career History Summary

```
2003 ───► 2010 ───► 2012 ───► 2013 ───► 2025
   │         │         │         │         │
Broadview  Kemper   Comcast  iPipeline  Present
  7年       2年      7月      12+年
```

---

## Additional Links

- 🌐 Personal Site: [stoneskin.github.io](https://stoneskin.github.io/)
- 💻 GitHub: [github.com/stoneskin](https://github.com/stoneskin/)
- 🔗 LinkedIn: [linkedin.com/in/stoneskin](https://www.linkedin.com/in/stoneskin/)

---

*Updated: October 2026*
