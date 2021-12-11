def create_heightmap() -> list:
    with open('input.txt') as f:
        display = [i.replace('\n', '') for i in f.readlines()]

        heightmap = []

        heightmap.append([10 for i in range(len(display[0]) + 2)])

        for i in display:
            row = [int(j) for j in i]
            row.append(10)
            row.insert(0, 10)

            heightmap.append(row)

        heightmap.append([10 for i in range(len(display[0]) + 2)])

    return heightmap


def search_low_points(heightmap) -> int:
    sizes = []

    for i in range(1, len(heightmap) - 1):
        for k in range(1, len(heightmap[i]) - 1):

            if heightmap[i][k] < heightmap[i - 1][k]:
                if heightmap[i][k] < heightmap[i][k - 1]:
                    if heightmap[i][k] < heightmap[i + 1][k]:
                        if heightmap[i][k] < heightmap[i][k + 1]:
                            size = 0
                            size = search_basin(heightmap, (i, k), size, [(i, k)])
                            sizes.append(size)

    return sorted(sizes)[-1] * sorted(sizes)[-2] * sorted(sizes)[-3]


def search_basin(heightmap, coordinates, size, list_coord):

    i = coordinates[0]
    k = coordinates[1]

    size += 1

    #h1
    if (heightmap[i][k] < (heightmap[i - 1][k])) and not((i - 1, k) in list_coord) and (heightmap[i - 1][k] < 9):
        list_coord.append((i - 1, k))
        size = search_basin(heightmap, (i - 1, k), size, list_coord)

    #h2
    if (heightmap[i][k] < (heightmap[i][k - 1])) and not((i, k - 1) in list_coord) and (heightmap[i][k - 1] < 9):
        list_coord.append((i, k - 1))
        size = search_basin(heightmap, (i, k - 1), size, list_coord)

    #h3
    if (heightmap[i][k] < (heightmap[i + 1][k])) and not((i + 1, k) in list_coord) and (heightmap[i + 1][k] < 9):
        list_coord.append((i + 1, k))
        size = search_basin(heightmap, (i + 1, k), size, list_coord)

    #h4
    if (heightmap[i][k] < (heightmap[i][k + 1])) and not((i, k + 1) in list_coord) and (heightmap[i][k + 1] < 9):
        list_coord.append((i, k + 1))
        size = search_basin(heightmap, (i, k + 1), size, list_coord)
    return size


heightmap = create_heightmap()
print(search_low_points(heightmap))
