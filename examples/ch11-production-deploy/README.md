# 第11章：部署与隔离验收

本目录是 **Linux Docker + systemd 教学模板**，不是直接部署脚本。Windows 可完成本地测试，Linux 服务安装另需授权和环境。本仓库不会实际安装服务。

1. 服务账户先安装 Docker 和 Hermes，确认 `docker info`、`hermes --version`；初始化独立 Profile、模型、必要平台。Docker 组权限接近宿主 root，按部署策略评估，不盲目加组。
2. 在宿主创建 `/srv/hermes/input`、`/srv/hermes/output`，仅授予服务账户必要权限。放入无敏感内容的 `input/sample.txt`。
3. 将 [配置片段](config/production-profile.yaml) 合并到 Profile，替换宿主路径；模型配置由 `hermes model` 生成。不挂载宿主根、Docker socket、密钥目录。
4. 运行目标 Profile 的 doctor，然后实际调用终端工具读取 `/data/sample.txt`，尝试向 `/data/write-test.txt` 写入应报只读错误；向 `/output/book-test.txt` 写入应成功。宿主应看到同名输出。保留后端身份、路径和结果，doctor 成功本身不够。
5. 让 Gateway 发送 `MEDIA:/srv/hermes/output/book-test.txt` 验证宿主路径。终端 cwd 只是工作目录，不是访问控制。
6. 核对 systemd 模板中 User/Group、HERMES_HOME、ExecStart 的真实路径后再安装服务；不要直接用 root 运行。可优先使用官方 Gateway 服务管理流程，避免手写服务与已安装服务重复。

## 检查点

在专用 Git 练习项目运行 `hermes -p book-lab chat --checkpoints`，要求只改测试文件一个值。`/rollback` 找实际编号，`/rollback diff 1` 预览；需要恢复时只恢复所选测试文件。检查点默认关闭，也不替代完整备份。

## 凭据和恢复

Linux 使用 `stat` 确认目标 Profile 的 `.env` 由服务账户拥有且权限为 600、目录限制访问；Windows 用 `icacls "实际Profile路径\.env"` 检查 ACL，按实际账户收紧，不能照搬 chmod。`config.yaml` 仅保留非敏感选项。备份和日志也可能含机密，必须受保护。

恢复顺序见[运行手册](rollback-runbook.md)。执行部署前逐项填写[验收清单](deployment-checklist.md)，未实测项标“待验收”，不要仅勾选“已配置”。

依据：[官方配置](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)、[检查点](https://hermes-agent.nousresearch.com/docs/user-guide/checkpoints-and-rollback)。
