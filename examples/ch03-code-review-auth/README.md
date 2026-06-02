# 第3.6节示例：认证流程代码审查

本目录对应书中 **3.6 实战：用 Hermes 完成一次代码审查任务**。

示例目标不是让 Hermes 替代人工审批，而是复现一次可控的代码审查流程：限定仓库范围，阅读认证流程相关 diff，找出潜在 bug、行为回归风险和缺失测试，并把可复用提示词沉淀下来。

## 目录说明

| 路径 | 用途 |
| --- | --- |
| `src/auth_demo/auth.py` | 一个最小认证服务示例，包含登录、会话校验、退出登录和修改密码 |
| `tests/test_auth_flow.py` | 当前已有测试，故意没有覆盖所有回归风险 |
| `review/auth-change.diff` | 模拟需要审查的认证流程改动 |
| `review/hermes-review-prompt.md` | 可直接复制给 Hermes 的审查提示词 |
| `review/expected-findings.md` | 参考发现，用于对照 Hermes 输出 |

## 运行测试

在本目录执行：

```bash
python -m unittest discover -s tests
```

当前测试应当通过。通过测试并不代表改动没有问题，本示例特意保留了一个与“修改密码后旧会话是否失效”相关的回归风险，用于训练读者区分“测试通过”和“审查通过”。

## 建议审查流程

1. 先阅读 `review/auth-change.diff`，不要直接看参考答案。
2. 用 `review/hermes-review-prompt.md` 中的提示词让 Hermes 审查本目录。
3. 要求 Hermes 优先输出 bug、回归风险和缺失测试。
4. 对照 `review/expected-findings.md` 检查是否抓住关键问题。
5. 回到自己的仓库时，只替换路径、审查范围和业务背景，不照搬示例结论。

## 与正文的关系

正文只保留关键命令和检查点；本目录提供可运行项目、模拟 diff、可复用提示词和参考发现。读者可以先在这里走通一次，再迁移到自己的真实仓库。
