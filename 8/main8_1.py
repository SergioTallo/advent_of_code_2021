with open('input.txt') as f:
    display = [i.split(' | ') for i in f.readlines()]
    display2 = [i[1].replace('\n', '') for i in display]

results = {1:0, 4:0, 7:0, 8:0}

def check_input(digits):
    dict_digits = {}

    for j in digits:
        if len(j) == 2:
            dict_digits[1] = [k for k in j]
        elif len(j) == 3:
            dict_digits[7] = [k for k in j]
        elif len(j) == 4:
            dict_digits[4] = [k for k in j]
        elif len(j) == 7:
            dict_digits[8] = [k for k in j]

    check_5 = [i for i in dict_digits[4] if i not in dict_digits[1]]

    for j in digits:
        if len(j) == 6:
            if all(x in j for x in dict_digits[4]):
                dict_digits[9] = [k for k in j]
            elif all(x in j for x in dict_digits[1]):
                dict_digits[0] = [k for k in j]
            else:
                dict_digits[6] = [k for k in j]
        elif len(j) == 5:
            if all(x in j for x in dict_digits[1]):
                dict_digits[3] = [k for k in j]
            elif all(x in j for x in dict_digits[1]):
                dict_digits[3] = [k for k in j]
            elif all(x in j for x in check_5):
                dict_digits[5] = [k for k in j]
            else:
                dict_digits[2] = [k for k in j]

    return dict_digits

def check_output(dict_digits, display, results):
    for i in display.split(' '):
        i = [k for k in i]

        if set(dict_digits[1]) == set(i):
            results[1] += 1
        elif set(dict_digits[4]) == set(i):
            results[4] += 1
        elif set(dict_digits[7]) == set(i):
            results[7] += 1
        elif set(dict_digits[8]) == set(i):
            results[8] += 1

    return results

for n, i in enumerate(display):

    digits = i[0].split(' ')

    results_new = check_output(check_input(digits), display2[n], results)
    results = results_new.copy()

print(sum(results.values()))




