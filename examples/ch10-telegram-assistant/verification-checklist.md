# Telegram 在线助理验证清单

- [ ] Bot Token 只保存在 `.env` 或 Secret 管理系统；
- [ ] allowed users 已限制为本人或团队白名单；
- [ ] 私聊 Bot 能收到回复；
- [ ] Home Channel 已设置；
- [ ] Cron 任务先投递到 local，再投递到 Telegram；
- [ ] 群聊场景已设置唤醒词或明确权限边界；
- [ ] 日志目录和错误排查步骤已记录。
- [ ] 未授权用户不能调用 Agent；环境变量使用 TELEGRAM_ALLOWED_USERS 和 TELEGRAM_HOME_CHANNEL。
- [ ] 语音转写得到可核对的文本，STT 前提已记录。
- [ ] Topic 模式和两个会话 ID 已记录，没有把会话隔离误当长期记忆隔离。
- [ ] 实际收到可打开的 PDF；MEDIA 使用 Gateway 宿主路径。
- [ ] 测试任务按确切 ID 清理，真实 Token 不进入截图或日志报告。
