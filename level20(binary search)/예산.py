import sys
input = sys.stdin.readline
N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
left = 1
right = N_list[N - 1]
while left <= right:
    total = 0
    mid = (left + right) // 2
    for i in range(len(N_list)):
        total += min(mid, N_list[i])

    if total > M:
        right = mid - 1
    else:
        left = mid + 1

print(right)