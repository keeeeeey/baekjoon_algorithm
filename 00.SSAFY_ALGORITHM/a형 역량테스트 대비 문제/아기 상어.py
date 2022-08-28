dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
fishes = [list(map(int, input().split())) for _ in range(n)]
x, y, size = 0, 0, 2
for i in range(n):
    for j in range(n):
        if fishes[i][j] == 9:
            x, y = i, j

def biteFish(x, y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((x, y))
    visited[x][y] = 1
    temp = []
    while q:
        cur_x, cur_y = q.pop(0)
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if fishes[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if fishes[nx][ny] < shark_size and fishes[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))

    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))

cnt = 0
result = 0
while True:
    shark = biteFish(x, y, size)

    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    result += dist
    fishes[x][y], fishes[nx][ny] = 0, 0
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(result)