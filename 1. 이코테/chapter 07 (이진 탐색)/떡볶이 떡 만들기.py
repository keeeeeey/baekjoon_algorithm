import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

bottom = 0
top = N_list[-1]

while bottom <= top:
    mid = (bottom + top) // 2
    length = 0

    for i in range(len(N_list)):
        result = N_list[i] - mid
        if result > 0:
            length += result

    if length >= M:
        bottom = mid + 1
    else:
        top = mid - 1

print(top)

