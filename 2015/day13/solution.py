from aoc import read_lines
from itertools import permutations


def get_possible_seat_orders(people: list[str]) -> list[tuple[str, ...]]:
    fixed_person = people[0]
    arrangements = permutations(people[1:])

    seat_orders = []
    for a in arrangements:
        seat_orders.append((fixed_person,) + a)

    return seat_orders


def get_attendees(data: list[str]) -> list[str]:
    attendees = set()
    for line in data:
        attendees.add(line.split()[0])
    return list(attendees)


def build_happiness_map(data: list[str]) -> dict[str, dict[str, int]]:
    happiness_map = {}

    for line in data:
        values = line.split()

        person = values[0]
        next_to = values[-1].rstrip(".")
        gain_or_lose = values[2]
        amount = int(values[3])

        if gain_or_lose == "lose":
            amount *= -1

        if person not in happiness_map:
            happiness_map[person] = {}

        happiness_map[person][next_to] = amount

    return happiness_map


def get_happiness(
    order: tuple[str, ...], happiness_map: dict[str, dict[str, int]]
) -> int:
    total = 0

    for i in range(len(order)):
        person = order[i]
        neighbor = order[(i + 1) % len(order)]

        total += happiness_map[person][neighbor]
        total += happiness_map[neighbor][person]
    return total


data = read_lines(__file__)

attendees = get_attendees(data)
happiness_map = build_happiness_map(data)

best = max(
    get_happiness(order, happiness_map) for order in get_possible_seat_orders(attendees)
)


print(best)
