"""Generate a local PDF fixture; does not contact Telegram."""
import argparse
from pathlib import Path
from reportlab.pdfgen import canvas


def generate(path):
    path = Path(path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation protects existing user files.
    with path.open("xb") as stream:
        pdf = canvas.Canvas(stream)
        pdf.setTitle("Hermes book attachment verification")
        pdf.drawString(72, 780, "Hermes book: PDF attachment test")
        pdf.drawString(72, 756, "Fixture only. No private data.")
        pdf.save()
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    print("MEDIA:" + str(generate(parser.parse_args().output)))
