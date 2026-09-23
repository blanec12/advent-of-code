from aoc import read_lines


def evaluate(circuit, output, cache):
    if output in cache:
        return cache[output]

    if output.isdigit():
        return int(output)

    expr = circuit[output]
    parts = expr.split()

    # one token -> direct assignment, e.g. "lx"
    if len(parts) == 1:
        val = evaluate(circuit, parts[0], cache)

    # two tokens -> NOT operation
    elif len(parts) == 2:
        _, rh = parts
        val = ~evaluate(circuit, rh, cache) & 0xFFFF

    # three tokens -> binary operation
    else:
        lh, op, rh = parts
        if op == "AND":
            val = evaluate(circuit, lh, cache) & evaluate(circuit, rh, cache)
        elif op == "OR":
            val = evaluate(circuit, lh, cache) | evaluate(circuit, rh, cache)
        elif op == "LSHIFT":
            val = evaluate(circuit, lh, cache) << int(rh)
        elif op == "RSHIFT":
            val = evaluate(circuit, lh, cache) >> int(rh)
        else:
            raise ValueError(f"Unknown operation: {op}")

    cache[output] = val
    return val


def main():
    instructions = read_lines(__file__)

    circuit = {}
    for line in instructions:
        expr, output = line.split(" -> ")
        circuit[output] = expr

    cache = {}
    p1 = evaluate(circuit, "a", cache)
    print(f"Part one: {p1}")

    circuit["b"] = str(p1)

    cache = {}
    p2 = evaluate(circuit, "a", cache)
    print(f"Part one: {p2}")


if __name__ == "__main__":
    main()
