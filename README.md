# Hermes Agent 极简入门配套资源

本仓库用于配合《Hermes Agent 极简入门》阅读和练习，提供与章节一一对应的示例项目、配置片段、提示词、Skills 模板、脚本样例和章节练习参考答案。

## 使用方式

1. 先阅读书中对应章节，再打开本仓库的章节目录。
2. 优先运行 `examples/` 中的示例，确认自己能复现书中的关键流程。
3. 复制 `prompts/`、`configs/`、`skills/` 和 `examples/` 中的模板时，先替换为自己的项目路径、模型提供商、密钥变量名和输出目录。
4. 所有 API Key、Bot Token、SSH 密钥和生产环境地址都不要提交到仓库。示例中只保留变量名和占位符。

## 章节资源索引

| 章节 | 书中落点 | 仓库目录 | 验证方式 |
| --- | --- | --- | --- |
| 1-12 | 每章练习 | `exercises/answers.md` | 对照每章练习目标和完成标准 |
| 3.6 | 认证流程代码审查 | `examples/ch03-code-review-auth/` | `python -m unittest discover -s tests` |
| 5.7 | Web 研究任务 | `examples/ch05-web-research/` | 对照 `expected-report.md` |
| 6.7 | SEO 关键词调研 Skill | `examples/ch06-seo-keyword-skill/`、`skills/seo-keyword-research/` | 按 `input-brief.md` 生成内容简报 |
| 7.6 | 记住项目偏好的个人助理 | `examples/ch07-personal-assistant-memory/` | 检查 USER/MEMORY/AGENTS 示例是否能支撑恢复提示 |
| 8.5 | 每日技术日报 Cron | `examples/ch08-daily-tech-brief/` | `python scripts/tech_daily.py` |
| 9.6 | 调研、实现、测试协作 | `examples/ch09-multi-agent-todo-api/` | `python -m unittest discover -s tests` |
| 10.5 | 7x24 Telegram 在线助理 | `examples/ch10-telegram-assistant/` | 按 `verification-checklist.md` 逐项确认 |
| 11 | 生产部署检查 | `examples/ch11-production-deploy/` | 按 `deployment-checklist.md` 和 `rollback-runbook.md` 演练 |
| 12.7 | 内部知识库 MCP 接入 | `examples/ch12-internal-docs-mcp/` | `python scripts/search_docs.py rollback` |

## 目录说明

| 目录 | 内容 |
| --- | --- |
| `examples/` | 与书中实战章节一一对应的示例项目和检查清单 |
| `exercises/` | 12 章练习答案、检查清单和常见问题 |
| `prompts/` | 可直接改写使用的提示词模板 |
| `configs/` | Profile、Cron、项目上下文等配置样例 |
| `skills/` | 可复用 Skill 模板 |
| `scripts/` | 轻量脚本样例 |

## 与书内二维码的关系

本仓库提供图书配套材料，适合读者复现书中的命令、配置和练习。书中 AI 破局俱乐部二维码用于领取延伸学习资源，包括直播、实操课、项目手册和实战工具。

建议读者先完成书内基础配置、章节练习和本仓库示例，再结合二维码资源继续做项目拆解、工具上手和案例复盘。
