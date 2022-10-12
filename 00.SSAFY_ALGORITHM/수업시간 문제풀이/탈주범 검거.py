from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dir_dict = {1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3], 4: [1, 2], 5: [0, 2], 6: [0, 3], 7: [1, 3]}

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    flag = True

    while q:
        x, y = q.popleft()

        for d in dir_dict[arr[x][y]]:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] != 0:
                if dist[x][y] + 1 == l + 1:
                    flag = False
                    break

                if d == 0 and 1 not in dir_dict[arr[nx][ny]]:
                    continue
                elif d == 1 and 0 not in dir_dict[arr[nx][ny]]:
                    continue
                elif d == 2 and 3 not in dir_dict[arr[nx][ny]]:
                    continue
                elif d == 3 and 2 not in dir_dict[arr[nx][ny]]:
                    continue

                visited[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

        if not flag:
            break

t = int(input())
for tc in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    dist[r][c] = 1
    bfs(r, c)
    answer = 0
    for i in range(n):
        for j in range(m):
            if dist[i][j] != 0:
                answer += 1
    print(f"#{tc} {answer}")