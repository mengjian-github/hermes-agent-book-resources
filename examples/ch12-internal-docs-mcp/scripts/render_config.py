"""Print YAML (JSON syntax) with this interpreter and an absolute server path."""
import json
from pathlib import Path
import sys

print(json.dumps({"mcp_servers": {"book-internal-docs": {
    "command": sys.executable,
    "args": [str(Path(__file__).resolve().parents[1] / "server.py")],
    "tools": {"include": ["search_docs", "read_doc"], "prompts": False, "resources": False},
    "sampling": {"enabled": False}
}}}, indent=2))
