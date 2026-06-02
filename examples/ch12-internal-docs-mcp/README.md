# 第12.7节示例：内部知识库 MCP 接入

本目录对应书中 **12.7 实战：把内部知识库接入 Hermes**。

真实环境中的 MCP 服务通常由团队已有系统提供。本目录提供一个只读知识库样例、查询脚本和 Hermes 配置片段，用于复现“先从低风险只读能力开始”的接入思路。

## 文件说明

| 路径 | 用途 |
| --- | --- |
| `docs/*.md` | 内部知识库样例文档 |
| `scripts/search_docs.py` | 只读搜索脚本，模拟 `search_docs` |
| `mcp-config-snippet.yaml` | Hermes MCP 配置片段 |
| `review-checklist.md` | 权限和验证检查清单 |

## 运行查询

```bash
python scripts/search_docs.py rollback
python scripts/search_docs.py release
```

如果把该示例替换为真实 MCP 服务，应先只开放 `search_docs` 和 `read_doc`，不要一开始开放写入类工具。
