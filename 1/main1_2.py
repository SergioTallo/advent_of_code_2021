counter = 0

with open('input.txt') as f:
    values = [int(i) for i in f.readlines()]

prev_value = (values[0] + values[1] + values[2])

for i in range(1, len(values) - 2):
    value = (values[i] + values[i+1] + values[i+2])
    if value > prev_value:
        counter += 1
    prev_value = value

print(counter)
