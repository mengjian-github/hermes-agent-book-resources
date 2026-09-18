# 验证记录

日期：2026-09-18。Windows 11（10.0.26200），Python 3.12.14；独立venv，未使用真实Hermes Profile或消息账号。

## 实测结果

命令：从仓库根运行 `python scripts/validate.py`，退出码0。

| 检查 | 结果 |
| --- | --- |
| 12章57题编号、顺序、四项答案字段 | 通过 |
| Markdown本地链接 | 通过 |
| YAML/JSON解析、Python语法、Skills元数据 | 通过 |
| Telegram变量与MCP配置层级/开关回归 | 通过 |
| ch03认证材料 | 4项通过，故意保留审查缺陷 |
| ch08日报 | 3项通过：原脚本、安装后异目录执行、坏输入；含拒绝覆盖 |
| ch09 Todo | 10项通过：原4项服务测试+6项HTTP测试 |
| ch10 PDF | 1项通过：PDF头/尾与拒绝覆盖 |
| ch12 MCP | 5项通过：4项知识库测试+1项真实stdio集成 |

代码测试合计23项。MCP集成真实启动子进程，完成initialize、工具发现、搜索、读取和越界拒绝。Flask通过test_client实际请求路由，但未将开发服务器公开到网络。生成器和安装器使用临时目录，不改真实用户配置。

`git diff --check`按Windows CRLF规则检查通过；Git的LF/CRLF转换提示不属于内容错误。

## 依赖基线

Flask 3.1.3、mcp 1.30.0、PyYAML 6.0.3、reportlab 4.5.1。直接依赖精确版本记录在requirements-tested.txt；不是完整传递依赖锁文件。MCP使用v1 API，主版本升级需迁移。

## 未实测的边界

未安装/运行真实Hermes、未调用模型、未注册真实Cron、未连接Telegram或启动Docker/systemd。Linux、Python3.11及GitHub Actions远端矩阵尚未运行；仅已提供CI配置，不能等同验证通过。按[联网验收表](live-acceptance.md)继续验证。

书稿和官网的交叉核查与运行时测试分开记录，不将文档验证说成端到端成功。
