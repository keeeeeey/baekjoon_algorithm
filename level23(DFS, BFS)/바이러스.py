T = int(input())
N = int(input())
matrix = [[0] * (T + 1) for _ in range(T + 1)]
visited = [0] * (T + 1)
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

def dfs(S):
    visited[S] = 1
    global cnt
    for i in range(1, T + 1):
        if visited[i] == 0 and matrix[S][i] == 1:
            cnt += 1
            dfs(i)
    return cnt
print(dfs(1))