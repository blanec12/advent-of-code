from aoc import read_lines


def count_on(state: list[str]) -> int:
    return sum(row.count("#") for row in state)


def count_off(state: list[str]) -> int:
    return sum(row.count(".") for row in state)


def get_neighbors(state: list[str], pos: tuple[int, int]) -> list[str]:
    neighbors = []
    rows = len(state)
    cols = len(state[0]) if rows else 0
    for i in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):
        for j in range(max(0, pos[1] - 1), min(cols, pos[1] + 2)):
            if (i, j) != pos:
                neighbors.append(state[i][j])
    return neighbors


def get_next_state(state: list[str]) -> list[str]:
    new_state = []

    for row in range(len(state)):
        new_row = ""

        for col in range(len(state[row])):
            neighbors = get_neighbors(state, (row, col))
            on = count_on(neighbors)
            curr = state[row][col]

            if curr == "#":
                new_row += "#" if on in (2, 3) else "."
            else:
                new_row += "#" if on == 3 else "."

        new_state.append(new_row)

    return new_state


def simulate(state: list[str], steps: int, stuck_corners: bool = False) -> list[str]:
    if stuck_corners:
        state = turn_on_corners(state)

    for _ in range(steps):
        state = get_next_state(state)

        if stuck_corners:
            state = turn_on_corners(state)

    return state


def turn_on_corners(state: list[str]) -> list[str]:
    state = state.copy()

    state[0] = "#" + state[0][1:-1] + "#"
    state[-1] = "#" + state[-1][1:-1] + "#"

    return state


def main():
    initial = read_lines(__file__)

    state = simulate(initial, 100, stuck_corners=True)

    on = count_on(state)

    print(on)


if __name__ == "__main__":
    main()
