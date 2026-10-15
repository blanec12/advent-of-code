from aoc import read_lines


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


def main():

    data = read_lines(__file__)

    replacements, molecule = data[:-2], data[-1]

    print(len(distinct_molecules(replacements, molecule)))


if __name__ == "__main__":
    main()
