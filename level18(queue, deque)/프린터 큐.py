import sys
from collections import deque
T = int(input())

for i in range(T):
    N = list(map(int, input().split()))
    N_list = deque(map(int, sys.stdin.readline().split()))
    cnt = 0
    while N_list:
        max_num = max(N_list)
        p_num = N_list.popleft()
        N[1] -= 1

        if max_num == p_num:
           cnt += 1
           if N[1] < 0:
               print(cnt)
               break
        else:
            N_list.append(p_num)
            if N[1] < 0:
                N[1] = len(N_list) - 1