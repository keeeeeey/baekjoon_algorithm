dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, l, left):
    global answer

    if l > answer:
        answer = l

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if left:
                if arr[nx][ny] >= arr[x][y]:
                    temp = arr[nx][ny] - arr[x][y]
                    if temp < cnt:
                        visited[nx][ny] = 1
                        arr[nx][ny] -= temp + 1
                        dfs(nx, ny, cnt - temp - 1, l + 1, left - 1)
                        visited[nx][ny] = 0
                        arr[nx][ny] += temp + 1
                else:
                    visited[nx][ny] = 1
                    dfs(nx, ny, cnt, l + 1, left)
                    visited[nx][ny] = 0
            else:
                if arr[nx][ny] < arr[x][y]:
                    visited[nx][ny] = 1
                    dfs(nx, ny, cnt, l + 1, left)
                    visited[nx][ny] = 0

t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_height = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_height:
                max_height = arr[i][j]

    visited = [[0] * n for _ in range(n)]
    answer = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_height:
                visited[i][j] = 1
                dfs(i, j, k, 1, 1)
                visited[i][j] = 0

    print(f"#{tc} {answer}")