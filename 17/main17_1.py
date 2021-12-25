def parse_file(file_name: str) -> tuple:
    with open(file_name) as f:
        row = f.readline().replace('\n', '').split(": ")[1].split(", ")
        x = row[0].split('=')[1].split('..')
        y = row[1].split('=')[1].split('..')

    return (min(int(x[0]), int(x[1])), max(int(y[0]), int(y[1]))), (
        max(int(x[0]), int(x[1])), min(int(y[0]), int(y[1])))


def step(x_velocity: int, y_velocity: int, x_position: int, y_position: int) -> tuple:
    x_position = x_position + x_velocity
    y_position = y_position + y_velocity

    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1
    else:
        x_velocity = 0

    y_velocity -= 1

    return (x_velocity, y_velocity), (x_position, y_position)


def shoot(initial_x_velocity: int, initial_y_velocity: int, initial_x_position: int, initial_y_position: int) -> tuple:
    highest_y = 0

    while True:

        new_velocity, new_position = step(x_velocity=initial_x_velocity, y_velocity=initial_y_velocity,
                                          x_position=initial_x_position,
                                          y_position=initial_y_position)

        if new_position[1] > highest_y:
            highest_y = new_position[1]

        if target_area[0][0] <= new_position[0] <= target_area[1][0] and target_area[1][1] <= new_position[1] <= \
                target_area[0][1]:
            return 'success', highest_y

        if new_position[0] > target_area[1][0] or new_position[1] < target_area[1][1]:
            return 'failed', highest_y

        initial_x_velocity = new_velocity[0]
        initial_y_velocity = new_velocity[1]
        initial_x_position = new_position[0]
        initial_y_position = new_position[1]


target_area = parse_file('input.txt')

print(target_area)

success_atemps = []

for v_x in range(0, target_area[1][0] + 1):
    for v_y in range(-(target_area[1][0] + 1), -(target_area[1][1] - 1)):

        value = shoot(initial_x_position=0, initial_y_position=0, initial_x_velocity=v_x, initial_y_velocity=v_y)

        if value[0] == 'success':
            success_atemps.append(value)


print(max(success_atemps))
