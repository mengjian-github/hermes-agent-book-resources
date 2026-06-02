# 第11章示例：生产部署检查

本目录对应书中第11章生产部署相关内容。

这里不提供可直接用于生产的最终配置，而是提供一套部署前检查模板。生产环境必须根据自己的系统用户、密钥管理、网络边界和审计要求调整。

## 文件说明

| 路径 | 用途 |
| --- | --- |
| `systemd/hermes-gateway.service` | Linux systemd 服务示例 |
| `config/production-profile.yaml` | 生产 Profile 配置片段 |
| `.env.example` | 环境变量占位示例 |
| `deployment-checklist.md` | 部署前检查清单 |
| `rollback-runbook.md` | 回滚和故障恢复记录模板 |

## 使用方式

1. 先在测试环境验证 Profile；
2. 再切换终端后端和 Gateway 配置；
3. 最后按 `deployment-checklist.md` 确认权限、日志、备份和回滚路径。
