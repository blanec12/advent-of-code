import argparse
from pathlib import Path
import os
from dotenv import load_dotenv
import requests


def get_input(url: str, session: str) -> str:
    response = requests.get(url, cookies={"session": session}, timeout=10)
    response.raise_for_status()
    return response.text


def save_input_to_file(path: Path, text: str) -> None:
    path.parent.mkdir(exist_ok=True)
    path.write_text(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, required=True)
    args = parser.parse_args()

    if not 1 <= args.day <= 25:
        parser.error("--day must be between 1 and 25")

    load_dotenv()

    session = os.getenv("AOC_SESSION_COOKIE")
    if not session:
        raise RuntimeError("AOC_SESSION_COOKIE is not set.")

    url = f"https://adventofcode.com/2015/day/{args.day}/input"
    input_file_path = Path(f"day{args.day:02}/input.txt")

    print(f"GET: {url}")
    puzzle_input = get_input(url, session)
    save_input_to_file(input_file_path, puzzle_input)
    print(f"Puzzle input saved to: {input_file_path}")


if __name__ == "__main__":
    main()
