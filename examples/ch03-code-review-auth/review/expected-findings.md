# 参考发现

以下内容用于对照 Hermes 输出，不建议在第一次审查前阅读。

## P1：修改密码后旧会话仍然有效

位置：`src/auth_demo/auth.py` 的 `AuthService.change_password`

改动删除了“修改密码后清理该用户所有现有会话”的逻辑。这样用户修改密码后，旧设备、被盗 token 或已登录浏览器仍可继续通过 `authenticate_request`。对认证系统来说，这通常是行为回归和安全风险。

建议修复：

- 修改密码成功后，删除该用户已有 session；
- 或根据业务要求区分“普通改密”和“安全改密”，但必须在代码、测试和产品语义中明确。

## P1：缺少旧会话失效测试

位置：`tests/test_auth_flow.py`

新增测试只验证旧密码不能再次登录、新密码可以登录，但没有验证“改密前已经存在的 token 是否失效”。因此测试通过并不能覆盖本次风险。

建议补充测试：

```python
def test_change_password_invalidates_existing_sessions(self) -> None:
    service = AuthService()
    service.create_user("u_1", "reader@example.com", "old-secret")
    token = service.login("reader@example.com", "old-secret")

    service.change_password("u_1", "old-secret", "new-secret")

    self.assertIsNone(service.authenticate_request(token or ""))
```

## 可接受的审查结论

如果 Hermes 输出能同时指出“旧会话未失效”和“测试只覆盖重新登录，没有覆盖已有 token”，就抓住了本示例的关键问题。
