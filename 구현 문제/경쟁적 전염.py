import sys
input = sys.stdin.readline

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
temp = []

def spread(x, y, v_num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 0:
                temp.append([nx, ny, v_num])

for _ in range(s):
    for v_num in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if grid[i][j] == v_num:
                    spread(i, j, v_num)

        for t in temp:
            grid[t[0]][t[1]] = t[2]

        temp.clear()

print(grid[x - 1][y - 1])