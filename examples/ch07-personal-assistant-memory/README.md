# 第7章：跨会话记忆

仓库 `memory/` 是材料，不会自动成为 Hermes 的持久记忆。先创建专用 book-lab Profile，用 `hermes profile show book-lab` 确认真实目录；本例记忆应合并到该目录的 `memories/USER.md` 与 `memories/MEMORY.md`。首次不存在可新建，已有内容先备份并逐条合并，不能直接覆盖个人记忆。

USER.md 放长期偏好，MEMORY.md 放经确认的项目事实；短期待办留在会话或看板。`project/AGENTS.md` 是项目规则样本，放入实际练习项目根目录，从该项目启动 Hermes。

先要求 Hermes 记住一条无敏感信息的偏好与事实，检查存放位置；退出后用同 Profile 开启**新会话**（不要 -c），使用 resume-prompt.md 的不显式读文件提示。核对它是否使用偏好且不编造未提供事实。随后可显式检查文件路径区分“记忆注入失败”和“内容没保存”。

其他题：`hermes -p book-lab sessions list` 查看最近五条，确认 ID 后 `hermes -p book-lab sessions rename <ID> "项目回顾"`，再 list 确认；`hermes -p book-lab memory status` 检查外部提供商。轻量个人偏好不必为完成练习而引入外部服务。

依据：[记忆](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)、[Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)。
