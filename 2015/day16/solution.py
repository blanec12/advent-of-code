from aoc import read_lines

MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_sues(lines: list[str]) -> dict[str, dict[str, int]]:
    sues = {}

    for line in lines:
        name, attributes = line.split(": ", maxsplit=1)

        sues[name] = {}

        for attribute in attributes.split(","):
            key, value = attribute.strip().split(": ")
            sues[name][key] = int(value)

    return sues


def matches(sue: dict[str, int], part: int = 1) -> bool:
    for attribute, value in sue.items():
        expected = MFCSAM[attribute]

        if part == 2:
            if attribute in ("cats", "trees"):
                if value <= expected:
                    return False
                continue

            if attribute in ("pomeranians", "goldfish"):
                if value >= expected:
                    return False
                continue

        if value != expected:
            return False

    return True


def main():
    lines = read_lines(__file__)

    sues = parse_sues(lines)

    for sue, attributes in sues.items():
        if matches(attributes, 1):
            print(f"Part1: {sue}")

        if matches(attributes, 2):
            print(f"Part2: {sue}")


if __name__ == "__main__":
    main()
