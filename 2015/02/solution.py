with open("/home/bcummings/repos/advent-of-code/2015/02/input.txt", "r") as f:
    dimensions = f.read().splitlines()

total_paper = 0
total_ribbon = 0
for dimension in dimensions:
    l, w, h = map(int, dimension.split("x"))

    lw = l * w
    wh = w * h
    hl = h * l

    total_paper += (2 * lw) + (2 * wh) + (2 * hl) + min(lw, wh, hl)
    total_ribbon += (l * w * h) + min((2 * (l + w)), (2 * (w + h)), (2 * (h + l)))

print("Total wrapping paper:", total_paper)
print("Total ribbon:", total_ribbon)
