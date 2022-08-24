dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j, s, n):
    global minV
    if maze[i][j] == 3:
        if minV < s:
            minV = s
        return
    else:
        visited[i][j] = 1
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni, nj, s + 1, n)
        visited[i][j] = 0

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    answer = 0

    sti = -1
    stj = -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    minV = n * n
    visited = [[0] * n for _ in range(n)]
    dfs(sti, stj, 0, n)
    if minV == n * n:
        minV = -1