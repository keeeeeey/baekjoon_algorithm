from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
M, N = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
start = deque([])
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            start.append((i, j))


def bfs(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or grid[nx][ny] != 0:
                continue
            grid[nx][ny] = grid[x][y] + 1
            q.append((nx, ny))

bfs(start)
cnt = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(grid[i]))
print(cnt - 1)