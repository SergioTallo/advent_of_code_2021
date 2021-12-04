counter = 0

with open('input.txt') as f:
    values = [int(i) for i in f.readlines()]

for i in range(1, len(values)):
    if values[i] > values[i-1]:
        counter += 1

print(counter)
