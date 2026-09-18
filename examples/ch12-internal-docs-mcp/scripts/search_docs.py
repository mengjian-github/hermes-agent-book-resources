import sys
from knowledge_base import search_docs

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        raise SystemExit("Usage: python scripts/search_docs.py <query>")
    for item in search_docs(query):
        print(f"{item['name']}: {item['title']}")
