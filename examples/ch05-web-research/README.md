# 第5.7节示例：Web 研究任务

本目录对应书中 **5.7 实战：让 Hermes 自动化一个 Web 研究任务**。

示例任务：调研一个开源项目的安装方式、能力边界和常见问题，并输出结构化报告。

## 文件说明

| 路径 | 用途 |
| --- | --- |
| `research-prompt.md` | 可复制给 Hermes 的研究提示词 |
| `sources.json` | 研究资料来源清单示例 |
| `notes/raw-notes.md` | 手工或 Hermes 提取后的资料笔记示例 |
| `expected-report.md` | 结构化研究报告参考格式 |
| `checklist.md` | 工具选择和验证检查清单 |

## 使用方式

1. 复制 `research-prompt.md` 给 Hermes；
2. 将目标项目名、官网和仓库地址替换为自己的研究对象；
3. 要求 Hermes 先列资料来源，再提取信息，最后输出报告；
4. 对照 `expected-report.md` 检查报告是否覆盖安装、能力边界、风险和下一步验证。

本示例不要求读者访问固定网站；`sources.json` 和 `raw-notes.md` 用于说明书中流程的落地结构。
