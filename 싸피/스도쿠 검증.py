t = int(input())
for tc in range(1, t + 1):
    sudoku = list(list(map(int, input().split())) for _ in range(9))
    flag = True
    for i in range(9):
        temp = []
        for j in range(9):
            if sudoku[i][j] not in temp:
                temp.append(sudoku[i][j])
            else:
                flag = False
                break

    for i in range(9):
        temp = []
        for j in range(9):
            if sudoku[j][i] not in temp:
                temp.append(sudoku[j][i])
            else:
                flag = False
                break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for a in range(i, i + 3):
                for b in range(j, j + 3):
                    if sudoku[a][b] not in temp:
                        temp.append(sudoku[a][b])
                    else:
                        flag = False
                        break

    if flag:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))

