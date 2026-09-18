# 第6.7节示例：SEO 关键词调研 Skill

本目录对应书中 **6.7 实战：为 SEO 关键词调研编写一个专用 Skill**。

可复用 Skill 位于：

- `../../skills/seo-keyword-research/SKILL.md`

本目录提供一次完整输入和参考输出，帮助读者判断 Skill 是否真正可用。

## 文件说明

| 路径 | 用途 |
| --- | --- |
| `input-brief.md` | 给 Hermes 的任务输入 |
| `expected-content-brief.md` | 参考输出结构 |
| `quality-checklist.md` | Skill 输出质量检查 |

## 使用方式

1. 用 `hermes profile show <name>` 确认目标 Profile，将仓库根的 `skills/seo-keyword-research/` 合并到该 Profile 的 `skills/seo-keyword-research/`；同名存在时先人工比较，不能直接覆盖；新会话检查发现和加载；
2. 用 `input-brief.md` 发起一次调研任务；
3. 对照 `expected-content-brief.md` 和 `quality-checklist.md` 检查输出。
