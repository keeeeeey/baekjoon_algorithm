n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

s = 0
for i in range(n):
    for j in range(n):
        if i == j:
            s += arr[i][j]

s = 0
for i in range(n):
    s += arr[i][i]

s = 0
for i in range(n):
    s += arr[i][n - 1 - i]