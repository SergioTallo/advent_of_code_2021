import numpy as np

with open('input.txt') as f:
    fishlist = f.readline().split(',')
    fishlist[-1] = fishlist[-1].replace('\n', '')
    fishlist = [int(i) for i in fishlist]
    crab_pos = np.array(fishlist)

    perdidas = []


def loss_function(crab_pos):
    for i in range(max(crab_pos)):
        loss = sum((np.abs(crab_pos - i) + (np.abs(crab_pos - i) ** 2)) / 2)
        perdidas.append(loss)


loss_function(crab_pos)

print(min(perdidas))

