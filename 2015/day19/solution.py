from aoc import read_lines
import re


def find_all_positions(element: str, molecule: str) -> list[tuple[int, int]]:
    positions = []

    for i, _ in enumerate(molecule):
        if molecule[i : i + len(element)] == element:
            positions.append((i, i + len(element)))

    return positions


def distinct_molecules(replacements: list[str], molecule: str) -> set[str]:
    molecules = set()

    for rule in replacements:
        element, replacement = rule.split(" => ")

        for start, end in find_all_positions(element, molecule):
            new_molecule = molecule[:start] + replacement + molecule[end:]
            molecules.add(new_molecule)

    return molecules


def minimum_steps(molecule: str) -> int | None:
    elements = re.findall(r"[A-Z][a-z]?", molecule)

    return (
        len(elements)
        - elements.count("Rn")
        - elements.count("Ar")
        - 2 * elements.count("Y")
        - 1
    )


def main():

    data = read_lines(__file__)

    replacements, molecule = data[:-2], data[-1]

    print("Part1: ", len(distinct_molecules(replacements, molecule)))
    print("Part2: ", minimum_steps(molecule))


if __name__ == "__main__":
    main()
