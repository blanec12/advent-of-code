import re


def is_nice1(s):
    # contains at least three vowels (a, e, i, o, u)?
    has_3_vowels = sum(c in "aeiou" for c in s) >= 3

    # has a letter that appears twice in a row?
    has_double = re.search(r"(.)\1", s) is not None

    # does not contain (ab, cd, pq, or xy)?
    has_forbidden = re.search(r"ab|cd|pq|xy", s) is not None

    return has_3_vowels and has_double and not has_forbidden


def is_nice2(s):
    # has a pair of any two letters that appear twice without overlapping?
    has_pair = re.search(r"(..).*\1", s) is not None

    # has a letter that repeats with exactly one letter between them?
    has_repeat = re.search(r"(.).\1", s) is not None

    return has_pair and has_repeat


def main():
    with open("/home/bcummings/repos/advent-of-code/2015/05/input.txt", "r") as f:
        strings = f.read().splitlines()

    num_nice_strings_p1 = 0
    num_nice_strings_p2 = 0

    for s in strings:
        if is_nice1(s):
            num_nice_strings_p1 += 1

        if is_nice2(s):
            num_nice_strings_p2 += 1

    print(f"Nice strings (part1) = {num_nice_strings_p1}")
    print(f"Nice strings (part2) = {num_nice_strings_p2}")


if __name__ == "__main__":
    main()
