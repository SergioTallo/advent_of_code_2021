with open('input.txt') as f:
    fishlist = f.readline().split(',')
    fishlist[-1] = fishlist[-1].replace('\n', '')
    fishlist = [int(i) for i in fishlist]

print(fishlist)

for i in range(80):

    new = 0

    for j, f in enumerate(fishlist):
        if fishlist[j] == 0:
            new += 1
            fishlist[j] = 6
        else:
            fishlist[j] -= 1

    for k in range(new):
        fishlist.append(8)

print(len(fishlist))
