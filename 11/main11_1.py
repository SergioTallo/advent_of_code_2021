with open('input.txt') as f:
    row = [i.replace('\n', '') for i in f.readlines()]
    matrix = []
    for i in row:
        matrix.append([int(j) for j in i])

flashes = 0


def give_energy(matrix, coordinates, flash_list):
    i = coordinates[0]
    j = coordinates[1]

    # up
    if (i - 1) >= 0:

        # up - left
        if (j - 1) >= 0:
            matrix[i - 1][j - 1] += 1
            if matrix[i - 1][j - 1] == 10:
                flash_list.append((i - 1, j - 1))

        # up - same
        matrix[i - 1][j] += 1
        if matrix[i - 1][j] == 10:
            flash_list.append((i - 1, j))

        # up - right
        if (j + 1) < len(matrix[i]):
            matrix[i - 1][j + 1] += 1
            if matrix[i - 1][j + 1] == 10:
                flash_list.append((i - 1, j + 1))

    # same
    # same - left
    if (j - 1) >= 0:
        matrix[i][j - 1] += 1
        if matrix[i][j - 1] == 10:
            flash_list.append((i, j - 1))

    # same - right
    if (j + 1) < len(matrix[i]):
        matrix[i][j + 1] += 1
        if matrix[i][j + 1] == 10:
            flash_list.append((i, j + 1))

    # down
    if (i + 1) < len(matrix):
        # down - left
        if (j - 1) >= 0:
            matrix[i + 1][j - 1] += 1
            if matrix[i + 1][j - 1] == 10:
                flash_list.append((i + 1, j - 1))

        # down - same
        matrix[i + 1][j] += 1
        if matrix[i + 1][j] == 10:
            flash_list.append((i + 1, j))

        # down - right
        if (j + 1) < len(matrix[i]):
            matrix[i + 1][j + 1] += 1
            if matrix[i + 1][j + 1] == 10:
                flash_list.append((i + 1, j + 1))

    return matrix, flash_list


for n in range(100):

    flash_list = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 10:
                flash_list.append((i, j))

    while len(flash_list) > 0:
        coord = flash_list.pop()
        matrix, flash_list = give_energy(matrix, coord, flash_list)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] >= 10:
                flashes += 1
                matrix[i][j] = 0

print(flashes)
