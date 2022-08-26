dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
    q = [start]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if maze[nx][ny] == 3:
                    return 1

                if maze[nx][ny] == 0:
                    maze[nx][ny] = 1
                    q.append([nx, ny])
    return 0

for _ in range(10):
    tc = int(input())
    maze = list(list(map(int, input().strip())) for _ in range(16))

    start = [0, 0]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]

    print(f"#{tc} {bfs(start)}")
