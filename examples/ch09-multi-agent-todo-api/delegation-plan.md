# 委派计划

先由主 Agent 明确 README 中的 HTTP 契约。父会话选择所需工具集；`delegate_task` 不接受 `toolsets` 或每次调用的 `max_iterations` 参数。

| 子任务 | goal | context | 交付/文件所有权 |
| --- | --- | --- | --- |
| A：审查 | 找出现有服务层边界 | service.py、models.py、接口契约；本轮不写文件 | 风险与测试场景清单 |
| B：实现 | 依契约实现 HTTP 行为 | A 的结论及 README；不得更改接口约定 | app.py、run.py、service.py |
| C：测试 | 验证接口状态码与原子性 | A 的结论及冻结接口；不要依赖 B 的私有实现 | tests/test_http_api.py |

A 先完成；B/C 可在契约稳定后并行，不能让两者同时写 service.py。主 Agent 汇总、运行全部测试、检查 git diff。需要硬只读时依靠工具限制和文件系统权限，不能把“不写文件”的 context 当成沙箱。

支持后台结果投递的会话可能先返回任务状态；其他方式可能同步。用 `/agents` 查看，等待最终结果再汇总。不要把已排队、子任务摘要或可持久化结果通知写成代码已验证或进程崩溃后执行自动续跑。
