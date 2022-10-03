dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def game_start(x, y, d, cnt):
    global max_score
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        if arr[x][y] == -1:
            max_score = max(max_score, cnt + 1)
            return
        elif arr[nx][ny] == 0:
            if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                game_start(nx, ny, (d + 2) % 4, cnt + 1)
            else:
                game_start(nx, ny, d, cnt + 1)
        elif arr[nx][ny] == 1:
            if d == 3:
                game_start(nx, ny, 0, cnt + 1)
            elif d == 2:
                game_start(nx, ny, 1, cnt + 1)
            else:
                game_start(nx, ny, (d + 2) % 4, cnt + 1)
        elif arr[nx][ny] == 2:
            if d == 3:
                game_start(nx, ny, 2, cnt + 1)
            elif d == 0:
                game_start(nx, ny, 1, cnt + 1)
            else:
                game_start(nx, ny, (d + 2) % 4, cnt + 1)
        elif arr[nx][ny] == 3:
            if d == 1:
                game_start(nx, ny, 2, cnt + 1)
            elif d == 0:
                game_start(nx, ny, 3, cnt + 1)
            else:
                game_start(nx, ny, (d + 2) % 4, cnt + 1)
        elif arr[nx][ny] == 4:
            if d == 1:
                game_start(nx, ny, 0, cnt + 1)
            elif d == 2:
                game_start(nx, ny, 3, cnt + 1)
            else:
                game_start(nx, ny, (d + 2) % 4, cnt + 1)
        elif arr[nx][ny] == 5:
            game_start(nx, ny, (d + 2) % 4, cnt + 1)
        else:
            for i in range(2):
                if wormhole[arr[nx][ny] - 6][i][0] == nx and wormhole[arr[nx][ny] - 6][i][1] == ny:
                    continue
                game_start(wormhole[arr[nx][ny] - 6][i][0], wormhole[arr[nx][ny] - 6][i][1], d, cnt + 1)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    wormhole = [[] for _ in range(5)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 6:
                wormhole[0].append([i, j])
            if arr[i][j] == 7:
                wormhole[1].append([i, j])
            if arr[i][j] == 8:
                wormhole[2].append([i, j])
            if arr[i][j] == 9:
                wormhole[3].append([i, j])
            if arr[i][j] == 10:
                wormhole[4].append([i, j])

    max_score = 0
    for i in range(n):
        for j in range(n):
            for d in range(4):
                game_start(i, j, d, 0)

    print(f"#{tc} {max_score}")