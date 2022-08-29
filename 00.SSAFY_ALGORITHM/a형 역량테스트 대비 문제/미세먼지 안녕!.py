dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cw_x = [0, 1, 0, -1]
cw_y = [1, 0, -1, 0]
ccw_x = [0, -1, 0, 1]
ccw_y = [1, 0, -1, 0]

def bfs():
    visited = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if a[x][y] != -1 and a[x][y] != 0:
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != -1:
                        visited[nx][ny] += a[x][y] // 5
                        cnt += 1
                visited[x][y] += a[x][y] - (a[x][y] // 5) * cnt

    for x in range(r):
        for y in range(c):
            if visited[x][y] != 0:
                a[x][y] = visited[x][y]

def clean():
    dir = 0
    cleaning = [[0] * c for _ in range(r)]
    x, y = cleaner[0], 1
    while True:
        nx = x + ccw_x[dir]
        ny = y + ccw_y[dir]

        if 0 <= nx < r and 0 <= ny < c and a[nx][ny] == -1:
            break

        if 0 > nx or nx > cleaner[0] or 0 > ny or ny >= c:
            dir = (dir + 1) % 4
            continue

        cleaning[nx][ny] = a[x][y]
        x = nx
        y = ny

    x2, y2 = cleaner[1], 1
    while True:
        nx2 = x2 + cw_x[dir]
        ny2 = y2 + cw_y[dir]

        if 0 <= nx2 < r and 0 <= ny2 < c and a[nx2][ny2] == -1:
            break

        if cleaner[1] > nx2 or nx2 >= r or 0 > ny2 or ny2 >= c:
            dir = (dir + 1) % 4
            continue

        cleaning[nx2][ny2] = a[x2][y2]
        x2 = nx2
        y2 = ny2

    for i in range(r):
        for j in range(c):
            if (i == 0 or i == cleaner[0] or i == cleaner[1] or i == r - 1 or j == 0 or j == c - 1) and a[i][j] != -1:
                a[i][j] = cleaning[i][j]

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            cleaner.append(i)

for _ in range(t):
    bfs()
    clean()

answer = 0
for i in range(r):
    for j in range(c):
        if a[i][j] != -1:
            answer += a[i][j]
print(answer)