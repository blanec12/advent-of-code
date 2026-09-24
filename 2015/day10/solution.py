from aoc import read_input

puzzle_input = read_input(__file__)


def expand(num: str) -> str:
    current_num = num[0]
    current_count = 1
    result = []

    for digit in num[1:]:
        if digit == current_num:
            current_count += 1
            continue

        result.append(str(current_count))
        result.append(current_num)

        current_num = digit
        current_count = 1

    result.append(str(current_count))
    result.append(current_num)

    return "".join(result)


for _ in range(40):
    puzzle_input = expand(puzzle_input)

print(f"part 1: {len(puzzle_input)}")

for _ in range(10):
    puzzle_input = expand(puzzle_input)

print(f"part 2: {len(puzzle_input)}")
