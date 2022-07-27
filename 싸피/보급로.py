from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(field, visited, time, start):
    q = deque([start])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if nx == 0 and ny == 0:
                    continue
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + field[nx][ny]
                    q.append([nx, ny])
                else:
                    if time[nx][ny] > time[x][y] + field[nx][ny]:
                        time[nx][ny] = time[x][y] + field[nx][ny]
                        q.append([nx, ny])

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    field = list(list(map(int, input())) for _ in range(n))

    visited = [[0] * n for _ in range(n)]
    time = [[0] * n for _ in range(n)]
    start = [0, 0]
    bfs(field, visited, time, start)
    print(f"#{tc} {time[n - 1][n - 1]}")





