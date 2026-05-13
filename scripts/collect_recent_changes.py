"""Collect a compact summary of recent git changes for Hermes review prompts."""

from __future__ import annotations

import subprocess
from pathlib import Path


def run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True, encoding="utf-8", errors="replace")


def main() -> None:
    root = Path.cwd()
    print(f"# Recent changes in {root}")
    print()
    print("## Status")
    print("```text")
    print(run(["git", "status", "--short"]).strip())
    print("```")
    print()
    print("## Diff stat")
    print("```text")
    print(run(["git", "diff", "--stat"]).strip())
    print("```")
    print()
    print("## Changed files")
    print("```text")
    print(run(["git", "diff", "--name-only"]).strip())
    print("```")


if __name__ == "__main__":
    main()

