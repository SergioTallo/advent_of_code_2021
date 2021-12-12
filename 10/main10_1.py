with open('input.txt') as f:
    display = [i.replace('\n', '') for i in f.readlines()]

syntax_dict = {'{': '}', '[': ']', '<': '>', '(': ')'}
points_dict = {'}': 1197, ']': 57, '>': 25137, ')': 3, '0': 0}


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
                return i

    return '0'


list_illegal = [checker_syntax(i) for i in display]

points = 0

for i in list_illegal:
    points += points_dict[i]

print(points)
