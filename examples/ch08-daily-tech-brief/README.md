# 第8.5节示例：每日技术日报推送到 Telegram

本目录对应书中 **8.5 实战：每日技术日报推送到 Telegram**。

示例将 script、Cron、Skill 和投递目标组合起来。为了便于离线复现，`scripts/tech_daily.py` 默认读取本地样例数据并输出 JSON。

## 文件说明

| 路径 | 用途 |
| --- | --- |
| `scripts/tech_daily.py` | Cron 预运行脚本示例 |
| `data/sample-feeds.json` | 离线输入数据 |
| `cron-daily-tech-brief.yaml` | Cron 任务配置示例 |
| `prompt.md` | 日报生成提示词 |
| `expected-output.md` | 参考输出结构 |

## 运行脚本

```bash
python scripts/tech_daily.py
```

正式使用时，可以把 `data/sample-feeds.json` 替换为 RSS、GitHub API 或内部数据源。
