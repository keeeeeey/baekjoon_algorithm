import sys
input = sys.stdin.readline
N = int(input())
list = list(list(map(int, input().split())) for _ in range(N))
list.sort(key=lambda x: (-x[1], -x[0]))
N_list = []
cnt = 0
for _ in range(N):
    start, end = list.pop()
    if not N_list:
        N_list.append([start, end])
        cnt += 1
    else:
        if N_list[-1][1] <= start:
            N_list.append([start, end])
            cnt += 1
print(cnt)