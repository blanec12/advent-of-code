import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--day", type=int, required=True)
args = parser.parse_args()

if not 1 <= args.day <= 25:
    parser.error("--day must be between 1 and 25")

path = Path(f"day{args.day:02}") / "input.txt"

print("Paste puzzle input, then press Ctrl-D:")
path.write_text(sys.stdin.read())

print(f"Saved to {path}")
