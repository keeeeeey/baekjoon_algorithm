import sys
input = sys.stdin.readline

N, C = map(int, input().split())
N_list = sorted(list(int(input()) for _ in range(N)))
start = 1
end = N_list[-1] - N_list[0]

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    cur = N_list[0]

    for i in range(1, N):
        if N_list[i] >= cur + mid:
            cur = N_list[i]
            cnt += 1

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1
print(end)