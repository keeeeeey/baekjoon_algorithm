import sys
input = sys.stdin.readline

N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = sorted(list(map(int, input().split())))

for i in range(M):
    start = 0
    end = N - 1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] < M_list[i]:
            start = mid + 1
        elif N_list[mid] > M_list[i]:
            end = mid - 1
        else:
            break

    if N_list[mid] == M_list[i]:
        print("yes", end=" ")
    else:
        print("no", end=" ")
