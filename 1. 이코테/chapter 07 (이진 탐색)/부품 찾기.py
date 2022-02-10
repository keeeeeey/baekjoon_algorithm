import sys
input = sys.stdin.readline

N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))
print(N, N_list, M, M_list)
for i in range(M):
    start = 0
    end = len(N_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if M_list[i] < N_list[mid]:
            end = mid - 1
        elif M_list[i] > N_list[mid]:
            start = mid + 1
        else:
            break

    if N_list[mid] == M_list[i]:
        print('yes', end=' ')
    else:
        print('no', end=' ')