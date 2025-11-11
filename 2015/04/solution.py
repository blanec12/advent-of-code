import hashlib

seed = "bgvyzdsv"

counter = 0
p1_solved = False
p2_solved = False

while True:
    hash = hashlib.md5((seed + str(counter)).encode()).hexdigest()

    if not p1_solved and hash.startswith("00000"):
        print(counter)
        p1_solved = True
    elif not p2_solved and hash.startswith("000000"):
        print(counter)
        p2_solved = True

    if p1_solved and p2_solved:
        break

    counter += 1
