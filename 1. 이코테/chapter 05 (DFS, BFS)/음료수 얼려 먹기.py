import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, M = map(int, input().split())
grid = list(list(map(int, input().strip())) for _ in range(N))
cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    grid[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 0:
                dfs(nx, ny)

for x in range(N):
    for y in range(M):
        if grid[x][y] == 0:
            cnt += 1
            dfs(x, y)

print(cnt)