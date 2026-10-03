from aoc import read_input
import json


def sum_numbers(value: list | dict | int | str) -> int:
    if isinstance(value, list):
        total = 0

        for item in value:
            total += sum_numbers(item)

        return total

    if isinstance(value, dict):
        if "red" in value.values():
            return 0

        total = 0

        for item in value.values():
            total += sum_numbers(item)

        return total

    if isinstance(value, int):
        return value

    return 0


raw = read_input(__file__)
data = json.loads(raw)

answer = sum_numbers(data)

print(answer)
