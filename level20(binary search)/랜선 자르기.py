import sys
input = sys.stdin.readline
K, N = map(int, input().split())
N_list = sorted(list(int(input().strip()) for _ in range(K)))
left = 1
right = N_list[K - 1]
while left <= right:
    cnt = 0
    mid = (left + right) // 2

    for i in range(K):
        cnt += N_list[i] // mid

    if cnt < N:
        right = mid - 1
    else:
        left = mid + 1

print(right)