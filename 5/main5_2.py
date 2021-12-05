import numpy as np

with open('input.txt') as f:
    inputstring = [i.strip().split(' -> ') for i in f.readlines()]
    endarray = []
    for i in inputstring:
        element = [(int(i[0].split(',')[0]), int(i[0].split(',')[1])),
                   (int(i[1].split(',')[0]), int(i[1].split(',')[1]))]
        endarray.append(element)

map_ = np.full((999, 999), 0)

for i in endarray:

    if (i[0][0] == i[1][0]) or (i[0][1] == i[1][1]):
        for j in range(min(i[0][0], i[1][0]), max(i[0][0], i[1][0]) + 1):
            for k in range(min(i[0][1], i[1][1]), max(i[0][1], i[1][1]) + 1):
                map_[j][k] += 1

    elif (max(i[0][0], i[1][0]) - min(i[0][0], i[1][0])) == (max(i[0][1], i[1][1]) - min(i[0][1], i[1][1])):
        for j in range(max(i[0][0], i[1][0]) - min(i[0][0], i[1][0]) + 1):
            map_[i[0][0] - (j * (np.sign(i[0][0] - i[1][0])))][i[0][1] - (j * (np.sign(i[0][1] - i[1][1])))] += 1

counter = 0

for i in range(len(map_)):
    for j in range(len(map_[0])):
        if map_[i][j] > 1:
            counter += 1

print(counter)
