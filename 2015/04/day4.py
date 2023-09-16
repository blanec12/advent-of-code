import hashlib

seed = 'bgvyzdsv'

solved = False
part1_solved = False
part2_solved = False
counter = 0

while not solved:
    hash = hashlib.md5((seed + str(counter)).encode()).hexdigest()

    if not part1_solved and hash.startswith('00000'):
        print(f'Part1 = {counter}')
        part1_solved = True
    elif not part2_solved and hash.startswith('000000'):
        print(f'Part2 = {counter}')
        part2_solved = True
    else: 
        counter += 1

    if part1_solved and part2_solved:
        solved = True
