# 第8章：可安装的离线日报 Cron

本例数据是 fixture，不抓取真实新闻，不需要 `daily-tech-brief` Skill。脚本单独运行不调用模型；Cron 总结仍需要可用模型和运行中的 Gateway。

## 1. 先验证脚本

从仓库根目录运行：

```sh
python examples/ch08-daily-tech-brief/scripts/tech_daily.py
python -m unittest discover -s examples/ch08-daily-tech-brief/tests -v
```

stdout 应只有一个 JSON 对象，`mode=offline-fixture`、`not_live_news=true`、`items` 有两项。错误写 stderr 并非零退出。

## 2. 安装到目标 Profile

```sh
hermes profile create book-lab
hermes -p book-lab model
hermes profile show book-lab
```

如果 Profile 已存在，跳过 create。记下 show 显示的真实 Profile 目录。将下面路径替换成它的绝对路径，不要照抄占位值：

```sh
python examples/ch08-daily-tech-brief/install.py --hermes-home /absolute/path/to/book-lab
```

PowerShell 同样支持命令，路径写成带引号的 `C:/实际目录/book-lab`。安装器将脚本和数据一起放进该 Profile 的 `scripts/book-daily-tech-brief/`，拒绝覆盖已存在的安装。升级时先人工备份、核对这个专用目录，再决定替换；不得清空整个 Profile。

## 3. 注册、调度与验收

在终端 A 保持 Gateway 前台运行（若已有同 Profile 的 Gateway，勿重复启动）：

```sh
hermes -p book-lab gateway run
```

在终端 B 执行：

```sh
hermes -p book-lab cron create "0 9 * * *" "根据脚本JSON生成三点摘要。标注离线样例，不把占位URL说成真实新闻。" --name book-daily-tech-brief --script book-daily-tech-brief/scripts/tech_daily.py --deliver local
hermes -p book-lab cron list
hermes -p book-lab cron run book-daily-tech-brief
```

`run` 请求下一个调度 tick 执行，并非命令返回就已完成。检查日志、任务实际状态以及该 Profile 的 `cron/output/<job-id>/` 下的新 Markdown。验收摘要应引用这两条输入、明确样例性质，没有编造实时访问。检查机器/Gateway 所用时区和 next run；`every 1d` 是间隔语义，不等同于每天当地时间 09:00。

测试后使用 `hermes -p book-lab cron --help` 中列出的暂停/移除命令，针对 list 返回的确切 ID 操作；保留需要长期运行的任务。前台测试 Gateway 用 Ctrl+C 停止。

## 4. 静默与扩展

`--deliver local` 只保存本地结果。`[SILENT]` 是成功任务最终响应的投递抑制标记，不是任务名称前缀；失败行为另行验证。先保持本地流程，再按[第10章](../ch10-telegram-assistant/README.md)设置 Telegram。

本目录 YAML 仅记录参数，不能通过“复制 YAML”注册任务。实时抓取属于扩展：需实现超时、来源验证、去重、失败处理和抓取日期，再删除 fixture 标记。

依据：[官方 Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)，核查日期 2026-09-18。
