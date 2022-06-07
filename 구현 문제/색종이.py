n = int(input())
grid = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            grid[i][j] = 1

ans = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] == 1:
            ans += 1

print(ans)