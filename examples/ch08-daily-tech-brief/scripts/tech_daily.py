"""Offline fixture input for Hermes Cron. stdout contains JSON only."""
import argparse
import json
from pathlib import Path


def load_brief(path):
    items = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(items, list) or not all(
        isinstance(item, dict) and all(isinstance(item.get(k), str) and item[k].strip()
        for k in ("source", "title", "url", "summary")) for item in items
    ):
        raise ValueError("Expected a list of source/title/url/summary objects")
    return {"mode": "offline-fixture", "not_live_news": True, "items": items}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path,
                        default=Path(__file__).resolve().parents[1] / "data" / "sample-feeds.json")
    args = parser.parse_args()
    print(json.dumps(load_brief(args.data), ensure_ascii=True))


if __name__ == "__main__":
    main()
