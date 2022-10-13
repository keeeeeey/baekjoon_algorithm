from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))

    while q:
        x, y, sword = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] >= visited[x][y] + 1:
                if nx == n - 1 and ny == m - 1:
                    visited[nx][ny] = visited[x][y] + 1
                    return True

                if visited[x][y] + 1 > t:
                    return False

                if sword:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny, 1))
                else:
                    if arr[nx][ny] != 1:
                        visited[nx][ny] = visited[x][y] + 1
                        if arr[nx][ny] == 2:
                            q.append((nx, ny, 1))
                        else:
                            q.append((nx, ny, 0))

    return False

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[200] * m for _ in range(n)]
visited[0][0] = 0
if bfs(0, 0):
    print(visited[n - 1][m - 1])
else:
    print("Fail")