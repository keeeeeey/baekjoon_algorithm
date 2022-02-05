import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))
start = 0
end = N_list[N - 1]
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(N):
        if N_list[i] - mid > 0:
            total += N_list[i] - mid

    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)