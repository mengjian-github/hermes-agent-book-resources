# 第10章：Telegram 六项练习

这些步骤需要自己的 Bot、模型和网络权限；仓库测试不会发消息或替你创建定时任务。

## 接入与白名单

使用 `hermes -p book-lab gateway setup` 配置专用 Bot。手工方式参考 [.env.example](.env.example)，写入 `hermes profile show book-lab` 所示目录的 `.env`。启动 `hermes -p book-lab gateway run`，不要让多个 Gateway 共用一个 Token。允许用户发送“只回复连接成功”；另一名未经授权的测试用户不应获得 Agent 服务。日志和截图必须脱敏。

## Home Channel 与定时投递

在希望接收消息的聊天发 `/sethome`，再运行：

```sh
hermes -p book-lab cron create "in 30m" "发送一句：配套练习投递测试成功。" --name book-telegram-check --deliver telegram
hermes -p book-lab cron run book-telegram-check
hermes -p book-lab cron list
```

等待实际收到消息，保存任务 ID 和接收时间。`run` 不是立即执行完成。测试后按确切 ID `hermes -p book-lab cron remove <ID>`，避免遗留任务；每天推送时改为 `0 9 * * *`，核对时区和 next run。日报输入使用[第8章](../ch08-daily-tech-brief/README.md)。

## 群聊触发

把以下片段合并进该 Profile 的 config.yaml 后重新启动 Gateway：

```yaml
telegram:
  require_mention: true
  mention_patterns:
    - '^小赫[，,：: ]'
```

授权用户在测试群发送普通闲聊（不应响应）、`@实际Bot用户名 请回复收到`（应响应）、`小赫，请回复收到`（应响应）。自定义唤醒词要求 Telegram 实际投递该消息；隐私模式可能阻止普通消息到达，按官网调整并重新加入测试群。不要通过开放所有用户来“修复”触发问题。

## 语音转写

在 Hermes 的 STT 设置选择可用提供商：本地 faster-whisper 需安装相应依赖；远程提供商需自己的密钥。发送短语音“明天下午三点整理会议纪要，请只复述不创建提醒”，验收返回文本包含日期、时间和事项。失败先检查 STT 是否启用、提供商和音频下载日志，而不是要求模型猜内容。成功转写不等于 TTS 也已配置。

## DM Topic（二选一）

固定模式：先在 Telegram 私聊信息中启用 Topics，将下面片段合并（替换 chat_id），重启 Gateway：

```yaml
platforms:
  telegram:
    extra:
      dm_topics:
        - chat_id: 123456789
          topics:
            - name: Book-A
            - name: Book-B
```

自建模式：在 BotFather 的 Threads Settings 打开 Threaded Mode，允许用户创建 topic；在根私聊发送 `/topic`，再从客户端创建两个 topic。不要把此模式的 BotFather 前提与固定配置模式混成一个开关。

在 A 写“本会话测试码 ALPHA，仅保留在本会话，不写记忆”，在 B 问当前会话测试码，不能自动回答 ALPHA。Topic 隔离会话历史，不代表隔离共享的 Profile 记忆或工具权限。记录两个会话 ID。

## PDF 附件

从仓库根目录安装 requirements-dev.txt 后运行：

```sh
python examples/ch10-telegram-assistant/generate_pdf.py output/telegram-test.pdf
```

脚本输出绝对 `MEDIA:` 路径，只生成文件，不发送。让 Telegram 会话中的 Hermes 读取该**宿主可访问**路径并在最终回复给出 `MEDIA:/实际路径/telegram-test.pdf`。收到原生附件、可打开且显示测试正文才算通过。Docker 文件要用输出卷映射后的宿主路径，不是容器 `/output/...`。脚本拒绝覆盖旧文件，复跑换文件名。

依据：[官方 Telegram](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)，2026-09-18。
