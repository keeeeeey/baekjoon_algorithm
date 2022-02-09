import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, M = map(int, input().split())
ICE = [list(map(int, input().strip())) for _ in range(N)]

cnt = 0

def dfs_recursion(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if ICE[x][y] == 0:
        ICE[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs_recursion(nx, ny)
        return True
    return False

def dfs():
    for x in range(N):
        for y in range(M):
            if dfs_recursion(x, y) == True:
                global cnt
                cnt += 1
    return cnt
print(dfs())