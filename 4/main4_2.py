with open('input.txt') as f:

    input = f.readlines()
    rounds = input.pop(0).split(',')
    del input[0]
    boards = []
    check_boards = []
    newboard = []
    new_check_board = []

    for i in input:
        if i[0] == '\n':
            boards.append(newboard)
            newboard = []
            check_boards.append(new_check_board)
            new_check_board = []
        else:
            line = i.split(' ')
            line[-1] = line[-1].replace('\n', '')
            values = [int(j) for j in line if j.isdecimal()]
            newboard.append(values)
            new_check_board.append([0, 0, 0, 0, 0])

break_value = 0
result = 0

for i in rounds:

    for j, board in enumerate(boards):
        for k, line in enumerate(board):
            for m, value in enumerate(line):
                if int(i) == value:
                    check_boards[j][k][m] = 1

    for k, board in enumerate(check_boards):
        for line in board:
            if sum(line) == 5:
                if len(boards) == 1:
                    for m, board_line in enumerate(boards[0]):
                        for n, value_board in enumerate(board_line):
                            if check_boards[0][m][n] == 0:
                                result += value_board
                    result = result * int(i)
                    del (check_boards[k])
                    del (boards[k])
                else:
                    del (boards[k])
                    del (check_boards[k])
                    break_value = 1

        if break_value == 0:
            for m in range(len(board[0])):
                column = [board[n][m] for n in range(len(board))]
                if sum(column) == 5:
                    if len(boards) == 1:
                        for m, board_line in enumerate(boards[0]):
                            for n, value_board in enumerate(board_line):
                                if check_boards[0][m][n] == 0:
                                    result += value_board
                        result = result * int(i)
                        del (check_boards[k])
                        del (boards[k])
                    else:
                        del (check_boards[k])
                        del (boards[k])

    if len(boards) == 0:
        break
    break_value = 0

print(result)
