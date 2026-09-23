from pathlib import Path


def read_input(solution_file: str) -> str:
    return Path(solution_file).with_name("input.txt").read_text().strip()


def read_lines(solution_file: str) -> list[str]:
    return Path(solution_file).with_name("input.txt").read_text().splitlines()
