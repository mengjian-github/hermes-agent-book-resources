# 《Hermes Agent极简入门》书稿勘误与补充建议

核查日期：2026-09-18。定位依据：用户提供的9.1待确认书稿正文；按章节和题号定位，避免Word重排后页码失效。官网是滚动文档，以下为核查日行为；不把自定义保守配置误写为错误默认值。

本清单与仓库优化分开：只列需要改正文、题干或补充说明的事项。没有改动原书稿正文；建议由作者确认后统一回填。范围是本次配套练习复现与相关技术段落，并非声称完成全书逐字校对。

## 一、明确需改的技术表述（8项）

### E01｜3.8第1题：命令被误译

原文定位：`/工具 list`。

建议替换：`/tools list`。完整顺序可写为 `/title demo-cli-workflow`、`/status`、`/model`、`/tools list`、`/history`；说明这些在Hermes会话内输入。

依据：[斜杠命令](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)。

### E02｜3.8第5题：-q不保证非交互退出

原文定位：“分别用hermes -z和hermes chat -q完成一次非交互调用”。

建议替换：“分别使用 `hermes -z "问题"` 和 `hermes chat --oneshot -q "问题"` 完成一次调用，比较输出和退出行为。”

说明：真实TTY中的 `chat -q` 可在首轮后继续交互，不应作为保证退出的示例。

依据：[CLI参考](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)。

### E03｜8.7第4题：静默标记作用对象不清

原文定位：“创建一个带[SILENT]前缀的低优先级任务，并将结果仅保存到本地文件。”

建议替换：“先创建 `deliver=local` 的任务，验证结果仅保存本地；再在测试投递目标上，让成功任务的最终响应包含 `[SILENT]`，验证投递被抑制。分别检查任务成功状态和本地产物。”

说明：不是给任务名称添加前缀；不能将投递失败误判为静默成功，错误通知另有行为。

依据：[Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)。

### E04｜9.2.1及表9-2：max_iterations不是当前工具调用参数

原文定位：调用中有 `max_iterations=50`；小节标题为“goal、context与max_iterations”；表9-2把它列为delegate_task主要参数。

建议：删除调用中的该参数；标题改“goal、context与执行轮数配置”，表中只列实际调用参数，并另述 `delegation.max_iterations` 为Profile全局配置。轮数不应机械等同于独立工具调用次数。

替换代码示意（调用说明，不是可独立执行的Python脚本）：

```python
delegate_task(
    goal="审查指定认证代码，返回风险与测试建议",
    context="项目路径、允许范围、已知背景和验证要求；本轮仅审查，不修复。"
)
```

如需示范限额，另列配置 `delegation: {max_iterations: 50}`，标“本例自定义保守值”。当前官方默认为250，并非50。

依据：[委派配置和参数](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)。

### E05｜9.3末段：旧并发默认值

原文定位：“并行委派默认最多同时运行3个子智能体数量”。

建议替换：“核查日官方默认并发上限为10，可通过 `delegation.max_concurrent_children` 调整。本书为便于观察，练习使用3个独立子任务。”

9.5中的 `max_concurrent_children: 3` 可作为自定义值保留，但加“示例值，不是默认值”。同理 `max_iterations: 50` 可保留为主动限额。

依据：[委派](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)。

### E06｜9.11第2题：工具与工具集的术语

定位：将 `send_message` 与 `web` 并列讨论工具集。

建议替换：“为代码审查选择父会话需要的工具集，分别说明是否需要联网检索、是否需要向消息平台发送结果。检查子任务最终可见的工具。”

说明：send_message是工具名；不能将toolsets作为delegate_task参数。正文9.4关于继承的方向本来正确，应保留。

依据：[工具集](https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference)、[委派](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)。

### E07｜11.9第3题：检查点开关和编号缺失

原文定位：“执行一次文件修改操作，让Hermes生成检查点，然后使用/rollback diff查看差异。”

建议替换：“先用 `hermes chat --checkpoints` 或Profile的 `checkpoints.enabled: true` 启用检查点。在练习项目中让工具修改测试文件，执行 `/rollback` 查编号，再用 `/rollback diff <N>` 预览差异。”

说明：默认关闭；应先预览，不直接覆盖用户手工修改。

依据：[检查点与回滚](https://hermes-agent.nousresearch.com/docs/user-guide/checkpoints-and-rollback)。

### E08｜12.7：两工具验收与开关值不一致；层级本身正确

原文定位：配置为 `tools.include: [search_docs, read_doc]` 且 `prompts: true`、`resources: true`；随后要求“确认工具列表只包含search_docs和read_doc”。

再次检查DOCX原始段落空格后确认：**书稿的prompts/resources已经正确位于tools之下，不存在此前报告所称的书稿层级错误。错误层级来自旧仓库模板，不能混为一谈。**

建议二选一：若坚持“只出现两项”，将两个开关改为false；若保留true，验收改为“原生工具仅开放两项，服务器提供相应能力时可能另有资源/提示词辅助工具”。本次仓库采用前者：

```yaml
tools:
  include: [search_docs, read_doc]
  prompts: false
  resources: false
sampling:
  enabled: false
```

依据：[MCP过滤与辅助工具策略](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference)。

## 二、补足前提与验收（8项，不一概判为事实错误）

### A01｜3.8第4题；7章记忆；11.9第4题：明确活动Profile路径

修改建议：默认Profile可写 `~/.hermes/`；命名Profile先用 `hermes profile show <name>` 确认实际目录。SOUL、memories和.env都应定位到该Profile。已有文件先备份并合并，不要求读者新建覆盖个人文件。

依据：[Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)、[记忆](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)。

### A02｜4.8第4、5题；11.9第1、2题：诊断不等于实际隔离

修改建议：doctor之后增加真实终端调用；验证输入卷读成功/写失败、输出卷写成功/宿主可读。注明CLI通常采用启动目录，Gateway/Cron应分别验证配置cwd/任务workdir。cwd不是文件权限边界。

依据：[配置](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)。

### A03｜6.9第5题：Skill文件布局

修改建议：明确路径为 `$HERMES_HOME/skills/<skill-name>/SKILL.md`，补name/description元数据、新会话发现和加载测试。Workflow/Verification可作为推荐组织，不规定必须使用这两个英文标题。

依据：[Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)。

### A04｜8.7第1题：一次性任务手动执行后的生命周期

修改建议：创建30分钟后任务，记ID、run、等待下一调度tick并检查实际输出；随后检查任务是否完成。不能假定手动执行后仍会在原计划时间再执行一次；需要另一次提醒时另建任务。

依据：[Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)。

### A05｜8.5实战与8.7第3题：把脚本安装与注册写完整

修改建议：脚本真实路径须在活动Profile的scripts目录内；同时安装其数据依赖。改用本次仓库安装器和正式cron create命令，再检查真实产物。正文“将脚本中的stdout”可润色为“将脚本的标准输出”。保存参数YAML不等于注册。

依据：[Cron脚本](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)。

### A06｜9.5生命周期；9.11第3、5题：补适用条件，不撤销后台能力

修改建议：写为“支持异步结果投递的运行方式可后台返回，其他方式可能同步；主智能体应等待最终结果并验证产物”。只读分析的提示不等于强制只读权限，需工具限制或文件系统隔离。

说明：第9章允许后台委派的方向不能一概判错；`max_spawn_depth=3`是有效示例，不应被改成“硬上限3”。结果通知持久化也不等于执行进程能在崩溃后续跑。

依据：[委派](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)。

### A07｜10.9第4—6题：语音、Topic、附件的可验收前提

修改建议：语音写明STT提供商及依赖；固定dm_topics和用户/topic两种模式分开列前提；Topic只隔离会话历史，不承诺隔离Profile记忆。MEDIA路径必须由Gateway宿主可读取，Docker路径需映射。补收到PDF且能打开的标准。

依据：[Telegram](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)。

### A08｜12.7实战：同步新的可运行交付

原文定位：“基于本地Markdown文档和search_docs.py构建的示例知识库”。

建议替换：“配套目录提供基于本地Markdown的只读stdio MCP服务器server.py，暴露search_docs与read_doc，附依赖、协议自测、绝对路径配置生成器及Hermes接入验收。HTTP地址保留为远程场景示意，不可直接访问。”

第9.6的Flask REST API目标无需降格：本次仓库已经补HTTP层，可保留目标并更新测试/入口说明。两处属于配套材料同步，不把原先实现缺失全算正文技术错误。

## 三、顺带发现的编辑勘误（5项）

| 编号 | 位置 | 原文字样 | 建议 |
| --- | --- | --- | --- |
| T01 | 9.2.1表9-2 context说明 | 提供完成子智能体完成任务所需的背景信息 | 提供子智能体完成任务所需的背景信息 |
| T02 | 9.2.3输出契约 | 可以求子智能体 | 可以要求子智能体 |
| T03 | 9.2.3表格引用 | 正文说表9-3，紧接表题却为表9-4 | 统一表号并核对后续表号和交叉引用，不只孤立改一处 |
| T04 | 9.5标题 | 任务声明周期 | 任务生命周期 |
| T05 | 9.5 child_timeout_seconds说明 | 子智能体的的运行时间上限 | 子智能体的运行时间上限 |

## 四、应保留与需要撤回的旧判断

- 不把57道题都判为错误：主要问题是旧在线答案仅12段章节概要，粒度不匹配。
- 不把旧仓库两个Telegram变量名误记为书稿同样写错；本次已修仓库，书稿变量需以原文逐处定位后再认定。
- 保留第3章刻意的认证缺陷，它是代码审查练习对象。
- 撤回此前将后台委派一概说成同步、深度硬上限一概说成3的批注结论。
- 更正此前核查报告对12.7的层级归因：DOCX缩进正确；需调整的是开关值与“仅两工具”验收的一致性。不能依赖去掉空格的纯文本判断YAML层级。

本清单包含8项技术勘误、8项前提/验收补充和5项编辑勘误。回填时建议标注“作者已确认/待确认”，并为官网默认值注明核查日期或版本。
