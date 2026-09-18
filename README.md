# Hermes Agent 极简入门配套资源

面向 9.1 待作者确认书稿，现按 **12章57题** 提供一一对应的参考步骤、验收和失败排查。核查日期：2026-09-18；源仓库基线：`05d2bff5dd6379216d265cd39b7a21127c11a9ab`。官网为滚动文档，本仓库没有伪造“已实测的 Hermes 版本”；本地测试版本和待联调项见[验证记录](docs/validation-2026-09-18.md)。

## 从这里开始

- [57题答案](exercises/answers.md)：按书中原题号查找。
- [章节实战](examples/README.md)：代码、配置、运行和验收。
- [书稿勘误](docs/book-errata-2026-09-18.md)：独立列出正文/题干需改之处。
- [本次优化说明](docs/changes-2026-09-18.md)：仓库变更，不混同书稿错误。
- [联网验收表](docs/live-acceptance.md)：需自己的模型、Bot、Docker及Hermes环境。

## 离线代码测试（先安装依赖）

Python 3.11+。从仓库根目录执行。PowerShell 不必激活虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts/validate.py
```

macOS/Linux：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

随后示例中的 `python` 指该虚拟环境的解释器；未激活时用完整解释器路径替代。测试不调用付费模型、不向 Telegram 发消息、不修改真实 Hermes Profile。安装依赖需要联网，安装完成后测试使用本地数据和子进程 stdio。

## 实战与边界

| 章节 | 交付 | 本地验证 | 仍需实际环境 |
| --- | --- | --- | --- |
| 3 | 刻意含认证缺陷的审查材料 | 既有测试 | Hermes 审查轨迹 |
| 5–7 | 调研、Skill、记忆工作流 | 文档/元数据检查 | 来源访问、加载、跨会话验收 |
| 8 | JSON脚本及安全安装器 | 安装后异目录运行 | 模型、Cron、Gateway |
| 9 | Flask CRUD及委派/看板手册 | 服务层和HTTP测试 | Hermes委派/看板 |
| 10 | Bot配置、六项练习、PDF脚本 | PDF产物与覆盖保护 | Telegram/STT/Topic/附件 |
| 11 | Docker卷与Linux服务模板 | YAML静态检查 | 容器、权限、恢复演练 |
| 12 | 两工具只读stdio MCP服务器 | 真实协议握手与调用 | Hermes工具发现与问答 |

配置均标明“片段/参数记录”，不能把所有 YAML 都直接导入。合并同名键，不整体覆盖已有 Profile；先替换占位路径，Key/Token 只放受保护凭据文件，真实 .env 不进入 Git。示例中的提示词约束不等同强制权限。

MCP 例使用 v1 SDK API，固定 `<2`；升级主版本需迁移。Flask 是本机内存教学服务，不能当生产 API；第3章缺陷是审查练习材料，不应为追求“测试全绿”而删除。

## 维护约定

每次更新同步题号覆盖、书稿勘误、官网核查日期与测试记录。CI 已提供 Linux/Windows、Python 3.11/3.12 测试矩阵；配置文件存在不代表远端 CI 已运行。正式发布时由维护者复核联调表，再打与书稿匹配的标签。

## 与书内二维码的关系

本仓库提供基础配套练习；书内 AI 破局俱乐部二维码用于延伸学习资源。先完成章节练习和验证，再按需开展扩展项目。
