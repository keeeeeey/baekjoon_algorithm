import sys

N_list = []
blank = []
for N in range(9):
    N_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if N_list[i][j] == 0:
            blank.append([i, j])

def check_x(x, a):
    for i in range(9):
        if N_list[x][i] == a:
            return False
    return True

def check_y(y, a):
    for i in range(9):
        if N_list[i][y] == a:
            return False
    return True

def check_r(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if N_list[i][j] == a:
                return False
    return True

def sudoku(idx):
    if idx >= len(blank):
        for i in range(9):
            print(" ".join(map(str, N_list[i])))
        return

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if check_x(x, i) and check_y(y, i) and check_r(x, y, i):
            N_list[x][y] = i
            sudoku(idx + 1)
            N_list[x][y] = 0
sudoku(0)