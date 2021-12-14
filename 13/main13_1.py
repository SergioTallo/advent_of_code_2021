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

print(folding_points_list)

folder = []
for i in range(1311):
    folder_row = []
    for j in range(895):
        folder_row.append('.')
    folder.append(folder_row)

for i in coordinates_list:
    folder[i[0]][i[1]] = '#'

count = 0
if folding_points_list[0][0] == 'x':
    for i in range(folding_points_list[0][1]):
        for j in range(895):
            if folder[i][j] != '#':
                folder[i][j] = folder[i + ((folding_points_list[0][1] - i) * 2)][j]

for i in range(folding_points_list[0][1]):
    for j in range(895):
        if folder[i][j] == '#':
            count += 1

print(count)



