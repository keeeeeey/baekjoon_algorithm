n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

s = 0
for i in range(n):
    for j in range(n):
        s += arr[i][j]

print(s)