from aoc import read_lines

RACE_DURATION_SECONDS = 2503


def simulate_race(reindeer: dict[str, dict[str, int]]):
    for second in range(1, RACE_DURATION_SECONDS + 1):
        for stats in reindeer.values():
            cycle_duration = stats["speed_duration"] + stats["rest_duration"]

            position_in_cycle = (second - 1) % cycle_duration

            if position_in_cycle < stats["speed_duration"]:
                stats["distance"] += stats["speed"]

        leading_distance = max(stats["distance"] for stats in reindeer.values())

        for stats in reindeer.values():
            if stats["distance"] == leading_distance:
                stats["points"] += 1


def main():
    data = read_lines(__file__)

    reindeer = {}

    for line in data:
        values = line.split()

        name = values[0]

        reindeer[name] = {
            "speed": int(values[3]),
            "speed_duration": int(values[6]),
            "rest_duration": int(values[-2]),
            "distance": 0,
            "points": 0,
        }

    simulate_race(reindeer)

    winner_distance = max(reindeer.items(), key=lambda item: item[1]["distance"])

    winner_points = max(reindeer.items(), key=lambda item: item[1]["points"])

    print(winner_distance)

    print(winner_points)


if __name__ == "__main__":
    main()
