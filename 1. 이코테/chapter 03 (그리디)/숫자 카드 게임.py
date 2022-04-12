import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
ans = 0
for i in range(N):
    min_value = min(grid[i])
    if min_value > ans:
        ans = min_value

print(ans)
