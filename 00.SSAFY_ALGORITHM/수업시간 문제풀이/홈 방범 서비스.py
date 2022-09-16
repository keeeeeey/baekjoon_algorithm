dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def secom(x, y, k):
    global answer
    visited = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    q = [(x, y)]
    cnt = 0

    if city[x][y] == 1:
        cnt += 1

    flag = True
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                if dist[nx][ny] == k:
                    flag = False
                    break
                if city[nx][ny] == 1:
                    cnt += 1
        if not flag:
            break

    if cnt * m >= cost and cnt > answer:
        answer = cnt

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for k in range(n + 1, 0, -1):
        cost = k * k + (k - 1) * (k - 1)
        for i in range(n):
            for j in range(n):
                secom(i, j, k)
        if answer != 0:
            break
    print(f"#{tc} {answer}")