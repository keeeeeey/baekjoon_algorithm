import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = list(list(map(int, input().strip())) for _ in range(N))
q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])

    while len(q) > 0:
        ox, oy = q.popleft()
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 1:
                    q.append([nx, ny])
                    grid[nx][ny] = grid[ox][oy] + 1
    print(grid)
    return grid

print(bfs(0, 0)[N - 1][M - 1])




