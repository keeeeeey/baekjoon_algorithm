dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    distance = [[n * n * 10] * n for _ in range(n)]
    q = []
    q.append([x, y])
    distance[x][y] = arr[x][y]
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and distance[nx][ny] > distance[x][y] + arr[nx][ny]:
                distance[nx][ny] = distance[x][y] + arr[nx][ny]
                q.append([nx, ny])
    return distance[n - 1][n - 1]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = bfs(0, 0)
    print(f"#{tc} {answer}")