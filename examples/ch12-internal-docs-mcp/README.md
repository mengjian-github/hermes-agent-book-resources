# 第12章：真正的只读 stdio MCP 服务器

提供 `search_docs(query)`、`read_doc(name)` 两个实际 MCP 工具。仅访问随例 `docs/` 中单层 Markdown，不执行 shell、不修改文档、不联网。拒绝路径穿越和指向目录外的符号链接。工具只读注解用于声明，路径校验和不提供写操作才是本例实现边界；MCP 本身不提供操作系统沙箱。

## 安装与协议自测

从仓库根目录，使用自己的 Python 3.11+ 虚拟环境：

```sh
python -m pip install -r examples/ch12-internal-docs-mcp/requirements.txt
python -m unittest discover -s examples/ch12-internal-docs-mcp/tests -v
python examples/ch12-internal-docs-mcp/scripts/search_docs.py rollback
python examples/ch12-internal-docs-mcp/scripts/render_config.py
```

协议测试会真实启动 server.py，完成 initialize、list_tools、call_tool，验证搜索、读取及越界拒绝。server.py 单独运行会等待 stdio 协议输入，不应以“没有打印”判为失败，也不要向 stdout 添加日志。

本例固定 MCP Python SDK **v1 API**，依赖 `<2`；升级 SDK 主版本必须同时迁移并重跑协议测试，不声称始终使用 SDK 最新主版本。

## 连接 Hermes

render_config 输出含当前 Python 和 server.py 绝对路径的 JSON（也是合法 YAML）。将 `mcp_servers.book-internal-docs` 合并进目标 Profile 的 config.yaml，保留已有其他服务器和配置；不要覆盖整个文件。使用虚拟环境解释器生成，否则服务器可能找不到 mcp 包。静态 YAML 只供查看结构，不能保留 `/absolute/...` 占位路径。

本地 stdio 无远程认证令牌。`tools.include` 只允许这两项，`tools.prompts` 和 `tools.resources` 关闭；`sampling.enabled` 在 server 层关闭。

重启该 Profile 的会话/Gateway后检查工具发现，向 Hermes 提问：

> 搜索内部回滚流程，读出对应文档，列出步骤并标注文件名。只调用 book-internal-docs 的只读工具；找不到就说明缺失。

验收需保留工具调用中的 query、返回 name、随后 read_doc 的 name 与内容。要求读取 `../README.md` 应被拒绝；断开服务器后再建新会话，相关工具不应继续可用。stdio 自测通过不等于已完成 Hermes 集成验收。

依据：[Hermes MCP 配置](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference)、[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk/tree/v1.x)。
