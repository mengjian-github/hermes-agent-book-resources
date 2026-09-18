"""Local-only release checks. No Hermes account, network, or real profile needed."""
from pathlib import Path
import json
import os
import re
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [2, 3, 5, 5, 5, 6, 5, 5, 7, 6, 5, 3]
SECTIONS = ["1.7", "2.8", "3.8", "4.8", "5.8", "6.9", "7.8", "8.7",
            "9.11", "10.9", "11.9", "12.10"]


def project_files():
    for directory, children, files in os.walk(ROOT):
        children[:] = [name for name in children if name not in
                       {".git", ".venv", "venv", "__pycache__", "output", "dist", ".pytest_cache"}]
        for name in files:
            yield Path(directory) / name


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def static_checks():
    for chapter, (count, section) in enumerate(zip(COUNTS, SECTIONS), 1):
        path = ROOT / "exercises" / f"ch{chapter:02}.md"
        content = path.read_text(encoding="utf-8")
        ids = re.findall(r"^## (\d+\.\d+-\d+) ", content, re.M)
        require(ids == [f"{section}-{i}" for i in range(1, count + 1)],
                f"Exercise IDs mismatch: {path}")
        for marker in ("前提：", "参考步骤：", "验收：", "排查与边界："):
            require(content.count(marker) == count, f"Incomplete answer fields: {path}")
    print("PASS: 12 chapters / 57 unique ordered answers")

    files = list(project_files())
    for path in (p for p in files if p.suffix == ".md"):
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            require((path.parent / target.split("#")[0]).exists(),
                    f"Broken local link: {path.relative_to(ROOT)} -> {target}")
    print("PASS: local Markdown links")

    for path in (p for p in files if p.suffix in {".yaml", ".yml"}):
        yaml.safe_load(path.read_text(encoding="utf-8"))
    for path in (ROOT / "skills").glob("*/SKILL.md"):
        content = path.read_text(encoding="utf-8")
        require(content.startswith("---\n"), f"Missing frontmatter: {path}")
        meta = yaml.safe_load(content.split("---", 2)[1])
        require(meta.get("name") == path.parent.name and meta.get("description"),
                f"Invalid skill metadata: {path}")
    mcp = yaml.safe_load((ROOT / "examples/ch12-internal-docs-mcp/mcp-config-snippet.yaml").read_text(encoding="utf-8"))
    server = next(iter(mcp["mcp_servers"].values()))
    require(set(server["tools"]["include"]) == {"search_docs", "read_doc"}, "MCP tool filter")
    require(server["tools"]["prompts"] is False and server["tools"]["resources"] is False,
            "MCP feature nesting")
    require(server["sampling"]["enabled"] is False, "MCP sampling")
    env = (ROOT / "examples/ch10-telegram-assistant/.env.example").read_text(encoding="utf-8")
    require("TELEGRAM_ALLOWED_USERS=" in env and "TELEGRAM_HOME_CHANNEL=" in env, "Telegram vars")
    require("TELEGRAM_ALLOWED_USER_IDS" not in env and "TELEGRAM_HOME_CHAT_ID" not in env, "Legacy vars")
    for path in (p for p in files if p.suffix == ".json"):
        json.loads(path.read_text(encoding="utf-8"))
    for path in (p for p in files if p.suffix == ".py"):
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
    print("PASS: YAML, JSON, Skill metadata and critical config regressions")


def main():
    static_checks()
    env = dict(os.environ, PYTHONUTF8="1")
    for tests in sorted((ROOT / "examples").glob("*/tests")):
        print(f"RUN: {tests.parent.name}", flush=True)
        subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", str(tests), "-v"],
                       cwd=ROOT, env=env, check=True, timeout=90)
    print("PASS: all local checks; live Hermes/Telegram/Docker acceptance remains separate")


if __name__ == "__main__":
    main()
