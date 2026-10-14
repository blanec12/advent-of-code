from aoc import read_lines
from itertools import combinations

TARGET = 150

containers = [int(line) for line in read_lines(__file__)]

valid_combos = [
    combo
    for r in range(1, len(containers) + 1)
    for combo in combinations(containers, r)
    if sum(combo) == TARGET
]

min_containers = min(map(len, valid_combos))


part1 = len(valid_combos)
part2 = sum(len(combo) == min_containers for combo in valid_combos)

print(f"Part1: {part1}")
print(f"Part2: {part2}")
