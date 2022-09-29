from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    q = deque()
    q.append([x, y])

    dist = [[1000000] * n for _ in range(n)]
    dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] >= arr[x][y]:
                    temp = dist[x][y] + abs(arr[nx][ny] - arr[x][y]) + 1
                else:
                    temp = dist[x][y] + 1
                if dist[nx][ny] > temp:
                    q.append([nx, ny])
                    dist[nx][ny] = temp

    return dist[n - 1][n - 1]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{tc} {bfs(0, 0)}")
