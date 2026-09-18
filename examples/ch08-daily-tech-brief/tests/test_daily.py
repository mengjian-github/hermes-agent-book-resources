import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("daily_installer", ROOT / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class DailyTests(unittest.TestCase):
    def test_source_json(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/tech_daily.py")],
                                check=True, capture_output=True, text=True)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["not_live_news"])
        self.assertEqual(len(payload["items"]), 2)

    def test_install_and_run_from_unrelated_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            home = Path(folder) / "profile"
            home.mkdir()
            script = installer.install(home)
            self.assertTrue(script.is_relative_to(home / "scripts"))
            result = subprocess.run([sys.executable, str(script)], cwd=folder,
                                    check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)["mode"], "offline-fixture")
            with self.assertRaises(FileExistsError):
                installer.install(home)

    def test_bad_input_fails_without_json(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.json"
            path.write_text("{}", encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/tech_daily.py"),
                                     "--data", str(path)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
