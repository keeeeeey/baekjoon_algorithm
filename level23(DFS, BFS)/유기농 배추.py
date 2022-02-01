import sys
sys.setrecursionlimit(10 ** 6)
_x = [0, 0, 1, -1]
_y = [1, -1, 0, 0]

T = int(input())

def worms(x, y, grid):
    if x < 0 or x >= W or y < 0 or y >= H:
        return False
    if grid[y][x] == 1:
        grid[y][x] = 0
        for n in range(4):
            worms(x + _x[n], y + _y[n], grid)
        return True
    return False

for _ in range(T):
    W, H, N = map(int, input().split())

    grid = [[0] * W for _ in range(H)]

    for _ in range(N):
        x, y = map(int, input().split())
        grid[y][x] = 1

    cnt = 0

    for i in range(W):
        for j in range(H):
            if worms(i, j, grid) == True:
                cnt += 1

    print(cnt)