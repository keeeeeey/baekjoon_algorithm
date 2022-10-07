from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))

    flood_q = deque()

    for i in range(r):
        for j in range(c):
            if arr[i][j] == "*":
                flood_q.append((i, j))

    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            if arr[x][y] == "*":
                continue

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if arr[nx][ny] == "." or arr[nx][ny] == "D":
                        if arr[nx][ny] == "D":
                            return True

                        arr[nx][ny] = ","
                        q.append((nx, ny))

        for _ in range(len(flood_q)):
            fx, fy = flood_q.popleft()
            for d in range(4):
                nfx = fx + dx[d]
                nfy = fy + dy[d]
                if 0 <= nfx < r and 0 <= nfy < c:
                    if arr[nfx][nfy] != "D" and arr[nfx][nfy] != "X" and arr[nfx][nfy] != "*":
                        arr[nfx][nfy] = "*"
                        flood_q.append((nfx, nfy))

    return False

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
cnt = 0
flag = False
for i in range(r):
    for j in range(c):
        if arr[i][j] == "S":
            flag = True
            if bfs(i, j):
                print(cnt)
            else:
                print("KAKTUS")
            break
    if flag:
        break