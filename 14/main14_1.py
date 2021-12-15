from collections import Counter

with open('input.txt') as f:
    row = [i.replace('\n', '') for i in f.readlines()]
    template = row[0]

    pairs = [row[i].split(' -> ') for i in range(2, len(row))]
    template = [i for i in template]

jump_i = 0

for n in range(10):
    i = 0
    while i < len(template) - 1:
        if jump_i == 1:
            jump_i = 0
            i += 1
            continue
        for j in pairs:
            if template[i] == j[0][0] and template[i + 1] == j[0][1]:
                template += '1'
                for k in reversed(range(i + 2, len(template))):
                    template[k] = template[k - 1]
                template[i + 1] = j[1]
                jump_i = 1
                break
        i += 1

dict_template = Counter(template)
s = sorted(dict_template.values())
print(s[-1] - s[0])
