def parse_instruction(line):
    if line.startswith("toggle"):
        action = "toggle"
        coords = line[len("toggle ") :]
    elif line.startswith("turn on"):
        action = "on"
        coords = line[len("turn on ") :]
    elif line.startswith("turn off"):
        action = "off"
        coords = line[len("turn off ") :]
    else:
        raise ValueError(f"Unknown instruction: {line}")

    p1, _, p2 = coords.split()
    return action, p1, p2


# part one
# def apply_instruction(grid, action, p1, p2):
#     x1, y1 = map(int, p1.split(","))
#     x2, y2 = map(int, p2.split(","))
#
#     for x in range(x1, x2 + 1):
#         for y in range(y1, y2 + 1):
#             if action == "on":
#                 grid[x][y] = 1
#             elif action == "off":
#                 grid[x][y] = 0
#             elif action == "toggle":
#                 grid[x][y] = 1 - grid[x][y]


# part two
def apply_instruction(grid, action, p1, p2):
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == "on":
                grid[x][y] += 1
            elif action == "off":
                grid[x][y] = max(0, grid[x][y] - 1)
            elif action == "toggle":
                grid[x][y] += 2


def main():
    with open("/home/bcummings/repos/advent-of-code/2015/06/input.txt", "r") as f:
        instructions = f.read().splitlines()

        grid = [[0 for _ in range(1000)] for _ in range(1000)]

        for line in instructions:
            action, p1, p2 = parse_instruction(line)
            apply_instruction(grid, action, p1, p2)

        total_on = sum(sum(row) for row in grid)
        print(total_on)


if __name__ == "__main__":
    main()
