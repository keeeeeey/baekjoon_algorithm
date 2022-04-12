import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

start = 0
end = N_list[N - 1]
mid = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in range(N):
        if N_list[i] > mid:
            length = N_list[i] - mid
            total += length

    if total > M:
        start = mid + 1
    elif total < M:
        end = mid - 1
    else:
        break

print(mid)

