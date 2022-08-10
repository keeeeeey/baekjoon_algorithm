n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

maxV = 0
for i in range(n):
    rs = 0
    for j in range(n):
        rs += arr[i][j]
    if rs > maxV:
        maxV = rs
print(maxV)