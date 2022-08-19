t = int(input())
for tc in range(1, t + 1):
    n, x = map(int, input().split())
    runway = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    ch_row = [[0] * n for _ in range(n)]
    ch_col = [[0] * n for _ in range(n)]
    for i in range(n):
        flag_row = True
        for j in range(n - 1):
            if runway[i][j] > runway[i][j + 1]:
                for k in range(j + 1, j + x + 1):
                    if k >= n:
                        flag_row = False
                        break
                    if runway[i][k] != runway[i][j] - 1 or ch_row[i][k] == 1:
                        flag_row = False
                        break
                if flag_row:
                    for s in range(j + 1, j + x + 1):
                        ch_row[i][s] = 1

            if runway[i][j] < runway[i][j + 1]:
                for k in range(j, j - x, -1):
                    if k < 0:
                        flag_row = False
                        break
                    if runway[i][k] != runway[i][j + 1] - 1 or ch_row[i][k] == 1:
                        flag_row = False
                        break
                if flag_row:
                    for s in range(j, j - x):
                        ch_row[i][s] = 1
        if flag_row:
            answer += 1

    for i in range(n):
        flag_col = True
        for j in range(n - 1):
            if runway[j][i] > runway[j + 1][i]:
                for k in range(j + 1, j + x + 1):
                    if k >= n:
                        flag_col = False
                        break
                    if runway[k][i] != runway[j][i] - 1 or ch_col[k][i] == 1:
                        flag_col = False
                        break
                if flag_col:
                    for s in range(j + 1, j + x + 1):
                        ch_col[s][i] = 1

            if runway[j][i] < runway[j + 1][i]:
                for k in range(j, j - x, -1):
                    if k < 0:
                        flag_col = False
                        break
                    if runway[k][i] != runway[j + 1][i] - 1 or ch_col[k][i] == 1:
                        flag_col = False
                        break
                if flag_col:
                    for s in range(j, j - x):
                        ch_col[s][i] = 1

        if flag_col:
            answer += 1

    print(f"#{tc} {answer}")