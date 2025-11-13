def decode(s):
    s = s[1:-1]

    i = 0
    total = 0

    while i < len(s):
        if s[i] == "\\":
            if s[i + 1] == "\\":
                total += 1
                i += 2
            elif s[i + 1] == '"':
                total += 1
                i += 2
                pass
            elif s[i + 1] == "x":
                total += 1
                i += 4
                pass
        else:
            total += 1
            i += 1

    return total


def encode(s):
    total = 2

    for c in s:
        if c == "\\" or c == '"':
            total += 2
        else:
            total += 1
    return total


total_code = 0
total_mem = 0
total_encoded = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        total_code += len(line)
        total_mem += decode(line)
        total_encoded += encode(line)

print(f"part 1: {total_code - total_mem}")
print(f"part 2: {total_encoded - total_code}")
