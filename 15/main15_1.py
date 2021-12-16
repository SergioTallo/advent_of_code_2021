# This solution gives 1 too much. The correct solution is this solution -1 (I have to find the bug)


import numpy as np

with open('input.txt') as f:
    rows = [i.replace('\n', '') for i in f.readlines()]
    cave = []
    for i in rows:
        row = [int(j) for j in i]
        cave.append(row)
    cave = np.array(cave)
    print(cave.shape)
    print(cave)


def find_neighbors(position: tuple, cave_shape: tuple) -> list:
    neighbors = []

    down = position[0] + 1
    right = position[1] + 1

    if down < cave_shape[0]:
        neighbors.append((down, position[1]))
    if right < cave_shape[1]:
        neighbors.append((position[0], right))

    return neighbors


def calculate_short_distance(cave: np.array, start: tuple, end: tuple) -> int:
    risk_matrix = np.full(cave.shape, 9999999, dtype=int)
    risk_matrix[0][0] = 0

    for i in range(start[0], cave.shape[0]):
        for j in range(start[1], cave.shape[1]):

            if (i, j) == end:
                return risk_matrix[i][j]

            neighbors = find_neighbors((i, j), cave.shape)

            for n in neighbors:
                neighbor_risk = risk_matrix[i][j] + cave[n[0]][n[1]]
                if neighbor_risk < risk_matrix[n[0]][n[1]]:
                    risk_matrix[n[0]][n[1]] = neighbor_risk


print(calculate_short_distance(cave, (0, 0), (cave.shape[0] - 1, cave.shape[1] - 1)))
