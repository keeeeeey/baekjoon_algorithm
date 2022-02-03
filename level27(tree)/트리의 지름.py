import sys
sys.setrecursionlimit(10 ** 9)
V = int(input())
grid = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(V):
    grid_list = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(grid_list) - 1, 2):
        if grid_list[i] == -1:
            break
        else:
            grid[grid_list[0]][grid_list[i]] = grid_list[i + 1]

visited = [[-1] * (V + 1) for _ in range(V + 1)]
ans = 0

def dfs(n):
    for i in range(1, len(grid[n])):
        global ans
        if grid[n][i] != 0 and visited[n][i] == -1 and visited[i][n] == -1:
            visited[n][i] = grid[n][i]
            visited[i][n] = grid[n][i]
            ans += grid[n][i]
            dfs(i)
dfs(1)
print(ans)
