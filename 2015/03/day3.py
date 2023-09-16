with open('inputs.txt') as input:
    directions = input.readlines()[0]

coordinates = {
    '^': [0, 1],
    '>': [1, 0],
    'v': [0, -1],
    '<': [-1, 0],
}

# part 1
x, y = 0, 0
houses_visited = set()
houses_visited.add((x, y))

for direction in directions[:-1]: 
    x += coordinates[direction][0]
    y += coordinates[direction][1]
    houses_visited.add((x, y))

print(len(houses_visited))

# part 2
santa_x, santa_y = 0, 0
santa_visited = set()
santa_visited.add((santa_x, santa_y))

robot_x, robot_y = 0, 0
robot_visited = set()
robot_visited.add((robot_x, robot_y))

for i, direction in enumerate(directions[:-1]):
    if i % 2 == 1:
        santa_x += coordinates[direction][0]
        santa_y += coordinates[direction][1]
        santa_visited.add((santa_x, santa_y))
    else: 
        robot_x += coordinates[direction][0]
        robot_y += coordinates[direction][1]
        robot_visited.add((robot_x, robot_y))

houses_visited = santa_visited.union(robot_visited)
print(len(houses_visited))
        
