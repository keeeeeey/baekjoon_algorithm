dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, n):
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        # 3번인가??
        if maze[i][j] == 3:
            return 1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[i][j] + 1
    return 0

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    sti = -1
    stj = -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    print(f"#{tc} {bfs(sti, stj, n)}")