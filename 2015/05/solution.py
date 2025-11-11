with open("/home/bcummings/repos/advent-of-code/2015/05/input.txt", "r") as f:
    strings = f.read().splitlines()

nice_strings = 0
vowels = ["a", "e", "i", "o", "u"]
forbidden = ["ab", "cd", "pq", "xy"]


for s in strings:
    num_vowels = sum(1 for ch in s if ch in vowels)
    has_repeating = any(s[i] == s[i + 1] for i in range(len(s) - 1))
    has_forbidden = any(f in s for f in forbidden)

    if num_vowels >= 3 and has_repeating and not has_forbidden:
        nice_strings += 1

    log = f"{s}: vowels={num_vowels}, has_repeating={has_repeating}, has_forbidden={has_forbidden}"
    print(log)

print(f"Nice strings = {nice_strings}")
