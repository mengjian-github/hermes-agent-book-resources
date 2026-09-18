"""Read-only stdio MCP server. stdout is reserved for the protocol."""
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

sys.path.insert(0, str(Path(__file__).resolve().parent / "scripts"))
from knowledge_base import read_doc as read_document, search_docs as search_documents

mcp = FastMCP("book-internal-docs")
readonly = ToolAnnotations(readOnlyHint=True, destructiveHint=False,
                           idempotentHint=True, openWorldHint=False)

@mcp.tool(annotations=readonly)
def search_docs(query: str) -> list[dict[str, str]]:
    """Search local sample markdown documents by keyword; returns names and titles."""
    return search_documents(query)

@mcp.tool(annotations=readonly)
def read_doc(name: str) -> str:
    """Read the full text of a markdown filename returned by search_docs."""
    return read_document(name)

if __name__ == "__main__":
    mcp.run(transport="stdio")
