import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n, m = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(n))
year = 0
ice_cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melting_cnt(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 0:
                cnt += 1
    return cnt

def count_ice(x, y, temp):
    temp[x][y] == 0

    if x < 0 or x >= n or y < 0 or y >= m:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if temp[nx][ny] != 0:
            count_ice(nx, ny, temp)

while ice_cnt < 2:
    year += 1
    graph = []
    for x in range(n):
        for y in range(m):
            if grid[x][y] != 0:
                graph.append([x, y, melting_cnt(x, y)])

    for a in range(len(graph)):
        x = graph[a][0]
        y = graph[a][1]
        grid[x][y] -= graph[a][2]
        if grid[x][y] < 0:
            grid[x][y] = 0

    temp = grid

    for x in range(n):
        for y in range(m):
            if temp[x][y] != 0:
                ice_cnt += 1
                count_ice(x, y, temp)

print(year)