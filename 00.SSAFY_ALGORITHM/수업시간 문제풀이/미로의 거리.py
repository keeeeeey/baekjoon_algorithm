dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = []
    q.append((x, y))
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1:
                maze[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    si, sj = 0, 0
    gi, gj = 0, 0
    dist = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                maze[i][j] = 0
                si, sj = i, j
            if maze[i][j] == 3:
                gi, gj = i, j

    bfs(si, sj)

    if dist[gi][gj] == 0:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {dist[gi][gj] - 1}")