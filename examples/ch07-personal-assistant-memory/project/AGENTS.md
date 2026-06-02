# 项目规则示例

## 项目定位

这是 Hermes 图书配套资源仓库。所有示例应服务于书中章节，不添加与章节无关的演示项目。

## 常用命令

```bash
python -m unittest discover -s examples/ch03-code-review-auth/tests
python -m unittest discover -s examples/ch09-multi-agent-todo-api/tests
python examples/ch08-daily-tech-brief/scripts/tech_daily.py
python examples/ch12-internal-docs-mcp/scripts/search_docs.py rollback
```

## 编辑规则

- 新增示例必须包含 README；
- 涉及密钥的配置只能使用 `.env.example` 或占位符；
- 可运行代码优先使用 Python 标准库，降低读者复现成本。
