# 第9章：多 Agent 协作的 Flask Todo REST API

本版在既有 TodoService 上补齐真实 HTTP 层，保留服务层测试。仅供本机教学：无认证、无数据库，重启清空数据，不可直接公开部署。

## 运行

从仓库根目录执行；Windows 和 macOS/Linux 均可：

```sh
python -m pip install -r examples/ch09-multi-agent-todo-api/requirements.txt
python -m unittest discover -s examples/ch09-multi-agent-todo-api/tests -v
python examples/ch09-multi-agent-todo-api/run.py
```

服务绑定 `127.0.0.1:5050`，不启用调试器。浏览器打开 `http://127.0.0.1:5050/todos` 初始得到 `[]`，Ctrl+C 停止。

PowerShell 操作示例：

```powershell
Invoke-RestMethod http://127.0.0.1:5050/todos -Method Post -ContentType application/json -Body '{"title":"补充测试"}'
Invoke-RestMethod http://127.0.0.1:5050/todos/1 -Method Patch -ContentType application/json -Body '{"completed":true}'
Invoke-RestMethod http://127.0.0.1:5050/todos/1 -Method Delete
```

macOS/Linux 可用 curl，正文与 Content-Type 相同。自动 HTTP 测试通过 Flask test_client 发请求，无需开放端口。

## 接口约定

| 方法/路径 | 输入 | 成功 | 失败 |
| --- | --- | --- | --- |
| GET /todos | 无 | 200，数组 | — |
| POST /todos | 仅 title，非空字符串 | 201，对象及 Location | 400/415 |
| GET /todos/{id} | 无 | 200，对象 | 404 |
| PATCH /todos/{id} | title 和/或 completed 布尔值 | 200，对象 | 400/404/415 |
| DELETE /todos/{id} | 无 | 204，无正文 | 404 |

ID 为正整数。未知字段、空 PATCH、空白标题、字符串形式的布尔值均拒绝。无效 PATCH 不可部分修改已有数据。不同 app 实例的内存互不共享。

## 委派与验收

按[委派计划](delegation-plan.md)先约定接口，再分文件协作；本项目不是 Kanban 实现，Kanban 与 Webhook 练习见[独立操作手册](kanban-webhook.md)。完成后提交测试输出、接口样例和文件变更清单，不能只展示子 Agent 的文字总结。

参考：[Flask 测试](https://flask.palletsprojects.com/en/stable/testing/)、[Hermes 委派](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)。
