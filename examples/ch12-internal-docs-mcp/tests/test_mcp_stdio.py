import asyncio
import json
import sys
import unittest
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER = Path(__file__).resolve().parents[1] / "server.py"


class StdioIntegrationTests(unittest.TestCase):
    def test_handshake_discovery_and_calls(self):
        async def scenario():
            async with asyncio.timeout(30):
                params = StdioServerParameters(command=sys.executable, args=[str(SERVER)])
                async with stdio_client(params) as (reader, writer):
                    async with ClientSession(reader, writer) as session:
                        await session.initialize()
                        listed = await session.list_tools()
                        self.assertEqual({tool.name for tool in listed.tools}, {"search_docs", "read_doc"})
                        self.assertTrue(all(tool.annotations.readOnlyHint for tool in listed.tools))
                        results = await session.call_tool("search_docs", {"query": "rollback"})
                        self.assertFalse(results.isError)
                        self.assertIn("rollback-runbook.md", json.dumps(results.model_dump(), ensure_ascii=False))
                        result = await session.call_tool("read_doc", {"name": "rollback-runbook.md"})
                        self.assertFalse(result.isError)
                        self.assertIn("回滚步骤", json.dumps(result.model_dump(), ensure_ascii=False))
                        rejected = await session.call_tool("read_doc", {"name": "../README.md"})
                        self.assertTrue(rejected.isError)
        asyncio.run(scenario())

if __name__ == "__main__":
    unittest.main()
