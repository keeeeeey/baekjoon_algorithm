from collections import deque

T = int(input())
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for _ in range(T):
    I = int(input())
    grid = [[0] * I for _ in range(I)]
    sx, sy = map(int, input().split())
    _x, _y = map(int, input().split())
    start = deque([(sx, sy)])

    def bfs(q):
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= I or ny < 0 or ny >= I or grid[nx][ny] != 0:
                    continue
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx, ny))

    bfs(start)

    if (sx, sy) == (_x, _y):
        print(0)
    else:
        print(grid[_x][_y])