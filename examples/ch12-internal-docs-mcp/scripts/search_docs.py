from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def search(query: str) -> list[tuple[str, str]]:
    results: list[tuple[str, str]] = []
    query_lower = query.lower()
    for path in sorted(DOCS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if query_lower in text.lower() or query_lower in path.stem.lower():
            first_line = text.splitlines()[0].lstrip("# ").strip()
            results.append((path.name, first_line))
    return results


def main() -> None:
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        raise SystemExit("Usage: python scripts/search_docs.py <query>")
    for name, title in search(query):
        print(f"{name}: {title}")


if __name__ == "__main__":
    main()
