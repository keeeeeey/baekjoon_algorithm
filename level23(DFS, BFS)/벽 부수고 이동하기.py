import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
grid = list(list(map(int, input().rstrip())) for _ in range(n))
walls = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            walls.append((i, j))

answer = int(1e9)
q = deque()
for wall in walls:
    q.append((0, 0))
    temp = [[0] * m for _ in range(n)]
    for w in walls:
        temp[w[0]][w[1]] = 1
    temp[wall[0]][wall[1]] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = temp[x][y] + 1
                q.append((nx, ny))

    if temp[n - 1][m - 1] == 0:
        pass
    elif temp[n - 1][m - 1] < answer:
        answer = temp[n - 1][m - 1] + 1

if answer == int(1e9):
    print(-1)
else:
    print(answer)