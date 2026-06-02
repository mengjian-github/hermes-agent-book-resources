# Hermes 代码审查提示词

请审查当前目录中的认证流程改动，重点关注 `review/auth-change.diff` 和相关实现、测试。

审查范围：

- `src/auth_demo/auth.py`
- `tests/test_auth_flow.py`
- `review/auth-change.diff`

审查重点：

1. 是否引入认证或会话管理相关 bug；
2. 是否存在行为回归风险，尤其是密码变更、退出登录、禁用用户和会话有效期；
3. 是否缺少必要测试；
4. 当前测试通过是否足以说明改动安全。

输出格式：

- Findings：按严重程度排序，包含文件路径、函数名或行号；
- Questions：仍需业务确认的问题；
- Tests：已运行或建议运行的命令；
- Summary：一句话说明本次改动的主要风险。

请先读 diff，再读相关代码和测试；不要只根据函数名猜测。
