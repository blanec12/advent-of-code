from aoc import read_lines
from itertools import permutations

data = read_lines(__file__)

locations = set()
distances = {}

for line in data:
    route, distance = line.split("=")
    start, end = route.split("to")

    start = start.strip()
    end = end.strip()

    locations.add(start)
    locations.add(end)

    distances[frozenset((start, end))] = int(distance)


best_route = None
best_distance = float("inf")

worst_route = None
worst_distance = float("-inf")

for route in permutations(locations):
    distance = sum(
        distances[frozenset((start, end))] for start, end in zip(route, route[1:])
    )

    if distance < best_distance:
        best_route = route
        best_distance = distance

    if distance > worst_distance:
        worst_route = route
        worst_distance = distance

print(f"Best route: {best_route}")
print(f"Distance: {best_distance}")

print(f"Worst route: {worst_route}")
print(f"Distance: {worst_distance}")
