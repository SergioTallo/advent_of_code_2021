from collections import defaultdict

cave_map = defaultdict(list)

with open('input.txt') as f:
    row = [i.replace('\n', '') for i in f.readlines()]
    for i in row:
        p = i.split('-')
        cave_map[p[0]].append(p[1])
        cave_map[p[1]].append(p[0])

path = [['start']]
number_paths = 0

while path:

    position = path.pop(0)

    for cave in cave_map[position[-1]]:
        if cave == 'end':
            number_paths += 1
        elif not cave.islower() or cave not in position:
            path.append(position + [cave])

print(number_paths)
