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
    if break_value == 1:
        break

    for j, board in enumerate(boards):
        for k, line in enumerate(board):
            for m, value in enumerate(line):
                if int(i) == value:
                    check_boards[j][k][m] = 1

    for j, board in enumerate(check_boards):
        for k, line in enumerate(board):
            if sum(line) == 5:
                for m, board_line in enumerate(boards[j]):
                    for n, value_board in enumerate(board_line):
                        print(value_board)
                        print(check_boards[j][m][n])
                        if check_boards[j][m][n] == 0:
                            print(value_board)
                            result += value_board
                result = result * int(i)
                break_value = 1
                break


        for k in range(len(board[0])):

            column = [board[m][k] for m in range(len(board))]
            if sum(column) == 5:
                for m, board_line in enumerate(boards[j]):
                    for n, value_board in enumerate(board_line):
                        print(value_board)
                        print(check_boards[j][m][n])
                        if check_boards[j][m][n] == 0:
                            print(value_board)
                            result += value_board
                result = result * int(i)
                break_value = 1
                break

print(result)
