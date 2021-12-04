with open('input.txt') as f:
    gamma = []
    epsilon = []
    input = f.readlines()

    for i in range(0, len(input[0]) - 1):

        count_1 = 0
        count_0 = 0

        for j in input:
            if j[i] == '1':
                count_1 += 1
            elif j[i] == '0':
                count_0 += 1

        if count_0 > count_1:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)

result_gamma = 0
result_epsilon = 0

for i, value in enumerate(gamma):
    result_gamma += (2 ** ((len(gamma) - 1) - i)) * value

for i, value in enumerate(epsilon):
    result_epsilon += (2 ** ((len(epsilon) - 1) - i)) * value

print(result_gamma * result_epsilon)
