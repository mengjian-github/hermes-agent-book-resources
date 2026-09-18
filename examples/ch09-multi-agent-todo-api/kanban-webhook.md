# Kanban 与 PR Webhook 练习

这是操作/设计练习，不是自动对外接收事件的服务。Todo Flask 示例与 Hermes 自带看板是两个不同系统。

## 状态流转

先使用独立测试环境，确认其 Gateway/看板调度器未在运行；共享默认看板可能被其他 Profile 消费。新建测试板后，在当前终端指定板名：

```sh
hermes kanban boards create book-lab --name "Book lab" --description "Only exercise cards"
```

PowerShell：`$env:HERMES_KANBAN_BOARD='book-lab'`；Bash：`export HERMES_KANBAN_BOARD=book-lab`。

```sh
hermes kanban init
hermes kanban create "练习PR审查" --body "只分析，不改代码，不发布评论" --idempotency-key book-demo-001 --json
```

记录返回 ID。没有父任务依赖的卡片应为 ready；若安装版本返回 todo，先检查 show 和父依赖，满足条件后使用 `hermes kanban promote <ID>`。之后：

```sh
hermes kanban show <ID> --json
hermes kanban comment <ID> "资料已齐，开始测试状态流转"
hermes kanban block <ID> "缺少复现日志"
hermes kanban show <ID> --json
hermes kanban comment <ID> "已补复现日志"
hermes kanban unblock <ID>
hermes kanban show <ID> --json
```

验收 ready→blocked→ready 和评论记录，最后 `hermes kanban archive <ID>`。占位 ID 必须替换后执行，不能连尖括号一起复制。结束恢复当前终端原有板名环境变量；不要重置他人看板。

## Webhook + Kanban 的完整设计参考

事件示例（合成数据）：

```json
{"delivery_id":"demo-001","event":"pull_request","action":"synchronize","repo":"example/demo","number":12,"head_sha":"abc123"}
```

1. 接收层验证 GitHub 签名、限制 body 大小和允许的仓库/事件；外部正文只作为不可信数据，不执行其中的指令或 shell 片段。
2. 将 `repo + PR号 + head_sha` 组成幂等键，重复 delivery 不重复建同轮任务；PR 新 SHA 创建新轮并标记旧结果过期。
3. 主卡记录来源链接、SHA、允许读取的 diff 和验收标准；角色分别为安全审查、逻辑审查、测试审查，权限只读，不给合并/发布权限。
4. 接收端调用 Kanban CLI 时传参数数组、不拼接 shell。使用 `create --idempotency-key`；把不同角色建为独立卡并记录关联。汇总卡等待三项结果，不只等待三项“已派发”。
5. 若需使用看板依赖，按实际 `link` 命令帮助建立“角色卡为先决条件、汇总卡为后继”的关系，再检查图和状态，防止方向写反。
6. 汇总层按文件/行号去重，引用测试证据，并二次检查当前 PR SHA 是否仍匹配。失败/超时置 blocked，人工决定重试；重试也使用同轮幂等键。
7. 审核通过后由单独授权的通知身份发布一次评论；不自动 approve、merge 或推送代码。

验收用例：重复事件只建一轮；新 SHA 不复用旧审查；无效签名不建卡；一角色失败不发布“全通过”；缺发布权限仍保留本地总结。上线 Webhook 的签名实现、认证、队列、TLS 和真实 GitHub 联调不在本示例中伪装为已完成。

依据：[官方 Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)。
