from collections import Counter
from more_itertools import windowed

with open('input.txt') as f:
    row = [i.replace('\n', '') for i in f.readlines()]
    template = row[0]

    pairs = [row[i].split(' -> ') for i in range(2, len(row))]
    rules = {i[0]: i[1] for i in pairs}
    template = [i for i in template]
    dif_pairs = [i[0][0] + i[0][1] for i in pairs]

    pair_count = dict.fromkeys(Counter(dif_pairs), 0)
    list_polymer = [i[0]+i[1] for i in windowed(template, 2)]
    for i in list_polymer:
        pair_count[i] += 1

    dict_polymer = Counter(template)

for n in range(40):
    pair_count_zero = dict.fromkeys(pair_count, 0)
    for i in pair_count.keys():
        if pair_count[i] != 0:
            pair_count_zero[i[0] + rules[i]] += pair_count[i]
            pair_count_zero[rules[i] + i[1]] += pair_count[i]
            if dict_polymer[rules[i]]:
                dict_polymer[rules[i]] += pair_count[i]
            else:
                dict_polymer[rules[i]] = 1

    pair_count = pair_count_zero

s = sorted(dict_polymer.values())
print(s[-1] - s[0])

