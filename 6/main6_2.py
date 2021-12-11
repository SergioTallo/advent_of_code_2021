from collections import Counter

with open('input.txt') as f:
    fishlist = f.readline().split(',')
    fishlist[-1] = fishlist[-1].replace('\n', '')
    fishlist = [int(i) for i in fishlist]

fish_dict = Counter(fishlist)

for i in range(9):
    if i not in fish_dict.keys():
        fish_dict[i] = 0

new_dict = fish_dict.copy()

for i in range(256):

    for i in sorted(fish_dict.items()):
        if i[0] == 0:
            new_dict[8] = i[1]
        elif i[0] == 7:
            new_dict[6] = i[1] + fish_dict[0]
        else:
            new_dict[i[0] -1] = i[1]

    fish_dict = new_dict.copy()

print(fish_dict)
print(sum(fish_dict.values()))






