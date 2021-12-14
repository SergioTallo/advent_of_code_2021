with open('input.txt') as f:
    row = f.readlines()
    coordinates_list = []
    folds = []
    for i in row:
        if not(i.startswith('\n')) and not(i.startswith('fold')):
            i = i.replace('\n', '')
            coordinates = i.split(',')
            coordinates_list.append((int(coordinates[0]), int(coordinates[1])))
        elif i.startswith('fold'):
            i = i.replace('\n', '')
            folds.append(i)

folding_points_list = []

for i in folds:
    ind_folds = i.split(' ')
    for j in ind_folds:
        fold_points = []
        if (j.startswith('x')) or (j.startswith('y')):
            k = j.split('=')
            folding_points_list.append([(k[0]), int(k[1])])

folder = []
for i in range(1311):
    folder_row = []
    for j in range(895):
        folder_row.append('.')
    folder.append(folder_row)

for i in coordinates_list:
    folder[i[0]][i[1]] = '#'

count = 0
for k in folding_points_list:
    if k[0] == 'x':
        for i in range(k[1]):
            for j in range(895):
                if folder[i][j] != '#':
                    folder[i][j] = folder[i + ((k[1] - i) * 2)][j]
    if k[0] == 'y':
        for i in range(1311):
            for j in range(k[1]):
                if folder[i][j] != '#':
                    p = j + ((k[1] - j) * 2)
                    folder[i][j] = folder[i][p]

result = []

for i in range (40):
    row_result = []
    for j in range(6):
        if folder[i][j] == '#':
            row_result.append('#')
        else:
            row_result.append(' ')
    print(row_result)






