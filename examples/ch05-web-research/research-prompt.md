# Web 研究任务提示词

请调研目标开源项目，并输出结构化研究报告。

目标项目：

- 名称：Hermes Agent
- 官网：https://hermes-agent.nousresearch.com
- 仓库：请通过搜索确认当前入口

研究步骤：

1. 用 web_search 找到官网、GitHub 仓库、官方文档和常见问题入口；
2. 用 web_extract 提取 README、Quickstart、Configuration、FAQ 等页面；
3. 只有页面需要点击、筛选或动态加载时才使用 browser；
4. 如果遇到截图或图表，再考虑 vision；
5. 输出前列出资料来源和不确定项。

输出格式：

- 一句话定位；
- 安装方式；
- 核心能力；
- 依赖和配置；
- 常见问题；
- 适合/不适合场景；
- 需要读者自己验证的事项。
