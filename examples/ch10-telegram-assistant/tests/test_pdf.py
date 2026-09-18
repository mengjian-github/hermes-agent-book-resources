import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("pdf_fixture", Path(__file__).resolve().parents[1] / "generate_pdf.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PDFTests(unittest.TestCase):
    def test_pdf_and_overwrite_protection(self):
        with tempfile.TemporaryDirectory() as folder:
            path = module.generate(Path(folder) / "sample.pdf")
            self.assertTrue(path.read_bytes().startswith(b"%PDF-"))
            self.assertIn(b"%%EOF", path.read_bytes())
            with self.assertRaises(FileExistsError):
                module.generate(path)
