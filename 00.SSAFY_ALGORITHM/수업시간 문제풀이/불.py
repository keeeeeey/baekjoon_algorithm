from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global cnt

    if x == 0 or x == h - 1 or y == 0 or y == w - 1:
        cnt += 1
        return True

    q = deque()
    q.append((x, y))

    fire_q = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == "*":
                fire_q.append((i, j))

    while q:
        cnt += 1
        for _ in range(len(fire_q)):
            fx, fy = fire_q.popleft()
            for d in range(4):
                nfx = fx + dx[d]
                nfy = fy + dy[d]
                if 0 <= nfx < h and 0 <= nfy < w and arr[nfx][nfy] != "*" and arr[nfx][nfy] != "#":
                    arr[nfx][nfy] = "*"
                    fire_q.append((nfx, nfy))

        for _ in range(len(q)):
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == ".":
                    if nx == 0 or nx == h - 1 or ny == 0 or ny == w - 1:
                        cnt += 1
                        return True

                    arr[nx][ny] = ","
                    q.append((nx, ny))

    return False

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    cnt = 0
    flag = False
    for i in range(h):
        for j in range(w):
            if arr[i][j] == "@":
                flag = True
                if bfs(i, j):
                    print(cnt)
                else:
                    print("IMPOSSIBLE")
                break
        if flag:
            break