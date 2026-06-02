# 第9.6节示例：调研、实现、测试协作

本目录对应书中 **9.6 实战：调研、实现、测试协作**。

示例用一个极小的待办事项服务模拟“现有 Flask 项目增加 REST API”的任务。为了降低复现成本，核心逻辑使用 Python 标准库；读者可以把同样任务拆给研究、实现、测试三个子代理。

## 文件说明

| 路径 | 用途 |
| --- | --- |
| `src/todo_app/models.py` | 待办事项数据结构 |
| `src/todo_app/service.py` | CRUD 服务逻辑 |
| `tests/test_todo_service.py` | 测试子代理应补齐的测试 |
| `delegation-plan.md` | 三个子代理的任务边界 |
| `expected-summary.md` | 合并后的参考总结 |

## 运行测试

```bash
python -m unittest discover -s tests
```
