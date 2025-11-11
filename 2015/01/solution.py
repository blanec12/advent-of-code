with open("/home/bcummings/repos/advent-of-code/2015/01/input.txt", "r") as f:
    directions = f.read().strip()

floor = 0
first_basement_pos = None
for pos, direction in enumerate(directions, start=1):
    if direction == "(":
        floor += 1
    elif direction == ")":
        floor -= 1

    if floor == -1 and first_basement_pos is None:
        first_basement_pos = pos


print("Destination floor:", floor)
print("First basement position:", first_basement_pos)
