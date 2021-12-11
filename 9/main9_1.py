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

    risk = 0

    for i in range(1, len(heightmap) -1):
        for k in range (1, len(heightmap[i]) - 1):
            if heightmap[i][k] < heightmap[i - 1][k]:
                if heightmap[i][k] < heightmap[i][k - 1]:
                    if heightmap[i][k] < heightmap[i + 1][k]:
                        if heightmap[i][k] < heightmap[i][k + 1]:
                            risk += heightmap[i][k] + 1

    return risk

heightmap = create_heightmap()
print(search_low_points(heightmap))