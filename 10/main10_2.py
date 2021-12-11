import numpy as np

with open('input.txt') as f:
    display = [i.replace('\n', '') for i in f.readlines()]

syntax_dict = {'{': '}', '[': ']', '<': '>', '(': ')'}
points_dict = {'}': 3, ']': 2, '>': 4, ')': 1}


def complete_lines(syntax_list):
    complete_list = []
    for i in reversed(syntax_list):
        complete_list.append(syntax_dict[i])

    points = 0

    for i in complete_list:
        points *= 5
        points += points_dict[i]

    return points


def checker_syntax(display):
    syntax_list = []
    list_char = [i for i in display]

    for i in list_char:
        if i in ['{', '[', '<', '(']:
            syntax_list.append(i)
        elif i in ['}', ']', '>', ')']:
            if syntax_dict[syntax_list[-1]] == i:
                syntax_list.pop()
            else:
                return 0

    if len(syntax_list) == 0:
        return 0
    else:
        return complete_lines(syntax_list)


print(np.median(np.array([checker_syntax(i) for i in display if checker_syntax(i) != 0])))
