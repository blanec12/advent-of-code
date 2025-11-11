with open("/home/bcummings/repos/advent-of-code/2015/03/input.txt", "r") as f:
    directions = f.readline().strip()

coordinates = {
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
    "<": (-1, 0),
}

def deliver_presents(directions, num_people=1): 
    people = [[0, 0] for _ in range(num_people)]
    visited = set()
    visited.add((0, 0))

    for i, direction in enumerate(directions):
        person = people[i % num_people]
        person[0] += coordinates[direction][0]
        person[1] += coordinates[direction][1]
        visited.add(tuple(person))

    return visited

part1 = len(deliver_presents(directions))
print(part1)

part2 = len(deliver_presents(directions, num_people=2))
print(part2)
