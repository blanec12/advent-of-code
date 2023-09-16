input = open('inputs.txt', 'r').read().split('\n')

total_paper_needed = 0
total_ribbon_needed = 0
for dimension in input[:-1]:
    l, w, h = map(int, dimension.split('x'))

    # part 1
    surface_area = (2*l*w) + (2*w*h) + (2*h*l)
    extra = min(l*w, w*h, h*l)
    total_paper_needed += surface_area + extra

    # part 2
    shortest_side = min(2*l+2*w, 2*w+2*h, 2*h+2*l) 
    bow = (l * w * h)
    total_ribbon_needed += shortest_side + bow
    

print(f'total_paper_needed={total_paper_needed}')
print(f'total_ribbon_needed={total_ribbon_needed}')
