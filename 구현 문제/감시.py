n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cctv = []
wall = []

for i in range(n):
    for j in range(m):
        if grid[i][j] and grid[i][j] != 6:
            cctv.append([i, j, grid[i][j]])
        elif grid[i][j] == 6:
            wall.append([i, j, grid[i][j]])



