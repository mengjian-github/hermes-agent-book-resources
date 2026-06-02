# 第10.5节示例：7x24 Telegram 在线助理

本目录对应书中 **10.5 7x24 在线助理实战**。

由于 Telegram Bot Token 和用户 ID 都属于敏感信息，本目录只提供可复制的配置模板、投递任务和验证清单，不包含真实凭证。

## 文件说明

| 路径 | 用途 |
| --- | --- |
| `.env.example` | Gateway 所需环境变量示例 |
| `gateway-setup-notes.md` | 配置步骤记录模板 |
| `cron-delivery-example.yaml` | 投递到 Telegram 的 Cron 示例 |
| `verification-checklist.md` | 上线前验证清单 |

## 使用方式

1. 从 BotFather 创建 Bot，拿到 Token；
2. 复制 `.env.example` 为 `.env`，填入自己的变量；
3. 运行 `hermes gateway setup` 或按当前版本配置 Gateway；
4. 私聊 Bot 验证回复，再设置 Home Channel；
5. 创建 Cron 任务前，先用 local 投递验证输出。
