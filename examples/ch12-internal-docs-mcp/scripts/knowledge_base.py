from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"


def allowed_document(name: str) -> Path:
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError("use a document name returned by search_docs")
    if "/" in name or "\\" in name or ":" in name:
        raise ValueError("paths are not allowed; use a document filename")
    root = DOCS.resolve()
    candidate = (root / name).resolve()
    if candidate.parent != root or candidate.suffix.lower() != ".md":
        raise ValueError("document must be a markdown file inside docs")
    if not candidate.is_file():
        raise ValueError("document not found")
    return candidate


def search_docs(query: str) -> list[dict[str, str]]:
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    query = query.strip().casefold()
    results = []
    for item in sorted(DOCS.glob("*.md")):
        # Reject symlinks resolving outside the documented root, including search.
        try:
            path = allowed_document(item.name)
        except ValueError:
            continue
        text = path.read_text(encoding="utf-8")
        if query in text.casefold() or query in path.stem.casefold():
            first_line = next((line.strip() for line in text.splitlines() if line.strip()), path.stem)
            results.append({"name": item.name, "title": first_line.lstrip("# ").strip()})
    return results


def read_doc(name: str) -> str:
    return allowed_document(name).read_text(encoding="utf-8")
