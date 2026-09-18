"""Install a NEW self-contained fixture under an explicit Hermes profile home."""
import argparse
from pathlib import Path
import shutil


def install(home):
    home = Path(home).expanduser().resolve(strict=True)
    if not home.is_dir():
        raise ValueError("Hermes profile home must be an existing directory")
    scripts = home / "scripts"
    scripts.mkdir(exist_ok=True)
    if scripts.resolve().parent != home:
        raise ValueError("Refusing scripts directory outside the selected profile")
    target = scripts / "book-daily-tech-brief"
    target.mkdir()  # Never overwrite an existing installation.
    source = Path(__file__).resolve().parent
    (target / "scripts").mkdir()
    (target / "data").mkdir()
    shutil.copy2(source / "scripts" / "tech_daily.py", target / "scripts" / "tech_daily.py")
    shutil.copy2(source / "data" / "sample-feeds.json", target / "data" / "sample-feeds.json")
    return target / "scripts" / "tech_daily.py"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hermes-home", required=True, type=Path)
    args = parser.parse_args()
    print(install(args.hermes_home))
