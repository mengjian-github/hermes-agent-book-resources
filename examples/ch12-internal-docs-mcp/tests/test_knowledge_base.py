import sys
import unittest
import tempfile
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from knowledge_base import read_doc, search_docs


class KnowledgeTests(unittest.TestCase):
    def test_empty_document(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "empty.md").write_text("", encoding="utf-8")
            with patch("knowledge_base.DOCS", root):
                self.assertEqual(search_docs("empty"), [{"name": "empty.md", "title": "empty"}])
                self.assertEqual(read_doc("empty.md"), "")

    def test_search_and_read(self):
        self.assertEqual(search_docs("rollback")[0]["name"], "rollback-runbook.md")
        self.assertIn("回滚步骤", read_doc("rollback-runbook.md"))
        self.assertTrue(search_docs("发布"))
        self.assertEqual(search_docs("missing-xyz"), [])

    def test_invalid_query(self):
        for value in ("", "  ", None):
            with self.assertRaises(ValueError):
                search_docs(value)

    def test_reject_escape(self):
        for value in ("../README.md", "/etc/passwd", "C:\\secret.md",
                      "..\\README.md", "not-found.md", "release-runbook.md:stream"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                read_doc(value)

if __name__ == "__main__":
    unittest.main()
