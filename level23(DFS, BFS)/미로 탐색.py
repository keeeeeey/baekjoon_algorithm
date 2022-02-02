from collections import deque
_x = [0, 0, 1, -1]
_y = [1, -1, 0, 0]
N, M = map(int, input().split())
grid = list(list(map(int, input())) for _ in range(N))

def bfs(row, col):
    q = deque([(row, col)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + _x[i]
            ny = y + _y[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or grid[nx][ny] != 1:
                continue
            grid[nx][ny] = grid[x][y] + 1
            q.append((nx, ny))

    return grid[N - 1][M - 1]

print(bfs(0, 0))