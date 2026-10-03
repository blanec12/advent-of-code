from aoc import read_input


def increment_string(s: str) -> str:
    chars = list(s)

    for i in range(len(chars) - 1, -1, -1):
        if chars[i] == "z":
            chars[i] = "a"
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            return "".join(chars)

    return "a" + "".join(chars)  # special case where all chars are 'z'


def has_straight(s: str) -> bool:
    for i in range(len(s) - 2):
        if (ord(s[i]) + 1 == ord(s[i + 1])) and (ord(s[i]) + 2 == ord(s[i + 2])):
            return True
    return False


def contains_illegal_char(s: str) -> bool:
    illegal_chars = ["i", "o", "l"]

    for char in illegal_chars:
        if char in s:
            return True
    return False


def has_two_pairs(s: str) -> bool:
    pairs = set()
    i = 0

    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            pairs.add(s[i])
            i += 2
        else:
            i += 1

    return len(pairs) >= 2


password = read_input(__file__)

while not (
    has_straight(password)
    and not contains_illegal_char(password)
    and has_two_pairs(password)
):
    password = increment_string(password)

print(password)
