dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def othello(x, y, value):
    board[x][y] = value
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 0 and board[nx][ny] != value:
            flag = False
            change = []
            while True:
                change.append((nx, ny))
                nx += dx[d]
                ny += dy[d]
                if nx < 1 or nx > n or ny < 1 or ny > n:
                    break
                elif board[nx][ny] == 0:
                    break
                elif board[nx][ny] == value:
                    flag = True
                    break

            if flag:
                for c in change:
                    board[c[0]][c[1]] = value

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    board[n // 2 + 1][n // 2] = 1
    board[n // 2][n // 2 + 1] = 1
    board[n // 2][n // 2] = 2
    board[n // 2 + 1][n // 2 + 1] = 2

    for _ in range(m):
        x, y, value = map(int, input().split())
        othello(x, y, value)

    cnt_1 = 0
    cnt_2 = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] == 1:
                cnt_1 += 1
            elif board[i][j] == 2:
                cnt_2 += 1

    print(f"#{tc} {cnt_1} {cnt_2}")