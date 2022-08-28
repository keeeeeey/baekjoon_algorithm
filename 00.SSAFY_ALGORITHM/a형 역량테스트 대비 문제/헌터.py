dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(l):
    global answer
    if l == m:
        temp = []
        for i in range(m):
            if mc[ch[i]][0] < 0:
                if -mc[ch[i]][0] not in temp:
                    return
            temp.append(mc[ch[i]][0])

        total = bfs([0, 0], [mc[ch[0]][1], mc[ch[0]][2]])
        for i in range(m - 1):
            distance = bfs([mc[ch[i]][1], mc[ch[i]][2]], [mc[ch[i + 1]][1], mc[ch[i + 1]][2]])
            total += distance
            if total > answer:
                return

        answer = min(answer, total)
    else:
        for i in range(m):
            if ch[i] == -1:
                ch[i] = l
                dfs(l + 1)
                ch[i] = -1

def bfs(start, end):
    q = []
    visited = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    x, y = start
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1
    return dist[end[0]][end[1]]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    mc = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                mc.append((grid[i][j], i, j))
    m = len(mc)
    ch = [-1] * m
    answer = int(1e9)
    dfs(0)
    print(f"#{tc} {answer}")