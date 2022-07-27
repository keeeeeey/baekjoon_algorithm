from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(maze, start, end):
    q = deque([start])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if nx == end[0] and ny == end[1]:
                    return 1

                if maze[nx][ny] == 0:
                    maze[nx][ny] = 1
                    q.append([nx, ny])
    return 0

for _ in range(10):
    tc = int(input())
    maze = list(list(map(int, input().strip())) for _ in range(16))

    start = [0, 0]
    end = [0, 0]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                end = [i, j]

    print(f"#{tc} {bfs(maze, start, end)}")
