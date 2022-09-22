dx = [1, 0]
dy = [0, 1]

def dfs(x, y):
    global answer
    if x == n - 1 and y == n - 1:
        answer = min(answer, distance[x][y])

    if distance[x][y] > answer:
        return

    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            distance[nx][ny] = distance[x][y] + arr[nx][ny]
            dfs(nx, ny)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = n * n * 10
    distance = [[0] * n for _ in range(n)]
    distance[0][0] = arr[0][0]
    dfs(0, 0)
    print(f"#{tc} {answer}")