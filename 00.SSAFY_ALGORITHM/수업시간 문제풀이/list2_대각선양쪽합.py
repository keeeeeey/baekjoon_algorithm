n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

left = 0
right = 0
for i in range(n):
    for j in range(n):
        if i > j:
            left += arr[i][j]
        elif i < j:
            right += arr[i][j]

print(left, right)

left = 0
right = 0
for i in range(n):
    for j in range(iq + 1, n):
        right += arr[i][j]
        left += arr[j][i]
print(left, right)