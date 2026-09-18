from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from todo_app.app import create_app

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5050, debug=False)
