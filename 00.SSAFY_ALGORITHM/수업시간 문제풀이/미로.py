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

    flag = 0
    stack = []
    stack.append(start)
    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 0:
                maze[nx][ny] = 1
                stack.append([nx, ny])

            if nx == end[0] and ny == end[1]:
                flag = 1
                break

        if flag == 1:
            break

    print(f"#{tc} {flag}")