horizontal = 0
vertical = 0
aim = 0

with open('input.txt') as f:
    for i in f.readlines():
        line = i.split(' ')
        if line[0] == 'forward':
            horizontal += int(line[1])
            vertical += int(line[1]) * aim
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])

print(horizontal*vertical)