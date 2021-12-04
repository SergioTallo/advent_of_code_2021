with open('input.txt') as f:
    input = f.readlines()

    input_oxygen = input
    l = len(input_oxygen[0]) - 1
    for i in range(0, l):

        count_1 = 0
        count_0 = 0

        for j in input_oxygen:
            if j[i] == '1':
                count_1 += 1
            elif j[i] == '0':
                count_0 += 1

        if count_0 > count_1:
            input_new = [k for k in input_oxygen if k[i] == '0']
        elif count_0 < count_1:
            input_new = [k for k in input_oxygen if k[i] == '1']
        elif count_0 == count_1:
            input_new = [k for k in input_oxygen if k[i] == '1']

        input_oxygen = input_new

        if len(input_oxygen) == 1:
            break

    input_co2 = input
    l = len(input_co2[0]) - 1
    for i in range(0, l):

        count_1 = 0
        count_0 = 0

        for j in input_co2:
            if j[i] == '1':
                count_1 += 1
            elif j[i] == '0':
                count_0 += 1

        if count_0 < count_1:
            input_new = [k for k in input_co2 if k[i] == '0']
        elif count_0 > count_1:
            input_new = [k for k in input_co2 if k[i] == '1']
        elif count_0 == count_1:
            input_new = [k for k in input_co2 if k[i] == '0']
        input_co2 = input_new
        if len(input_co2) == 1:
            break

result_o = [m for m in input_oxygen[0] if m == '0' or m == '1']
result_o_dec = 0

result_co2 = [m for m in input_co2[0] if m == '0' or m == '1']
result_co2_dec = 0

for i, value in enumerate(result_o):
    result_o_dec += (2 ** ((len(result_o) - 1) - i)) * int(value)

for i, value in enumerate(result_co2):
    result_co2_dec += (2 ** ((len(result_co2) - 1) - i)) * int(value)

print(result_co2_dec * result_o_dec)
