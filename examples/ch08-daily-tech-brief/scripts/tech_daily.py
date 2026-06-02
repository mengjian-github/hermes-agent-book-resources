from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample-feeds.json"


def main() -> None:
    items = json.loads(DATA.read_text(encoding="utf-8"))
    output = {
        "date": date.today().isoformat(),
        "sources": sorted({item["source"] for item in items}),
        "items": items,
        "instruction": "Summarize these items into a Chinese daily tech brief within 500 words.",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
