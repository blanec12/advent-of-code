with open('inputs.txt') as input:
    directions = input.readlines()[0]

floor = 0
position = None
found_basement = False

for index, direction in enumerate(directions):
    match direction:
        case '(':
            floor += 1
        case ')':
            floor -= 1

    if not found_basement and floor == -1:
        position = index + 1
        found_basement = True

print(f'part1 answer = {floor}, part2 answer = {position}')
