dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    start = []
    end = []
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                end = [i, j]

    flag = False

    def dfs(x, y):
        global flag
        if x == end[0] and y == end[1]:
            flag = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1:
                maze[nx][ny] = 1
                dfs(nx, ny)

    dfs(start[0], start[1])

    if flag:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
