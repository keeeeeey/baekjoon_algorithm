import sys
import bisect
input = sys.stdin.readline
N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))

for i in range(M):
    left_idx = bisect.bisect_left(N_list, M_list[i])
    right_idx = bisect.bisect_right(N_list, M_list[i])
    print(right_idx - left_idx, end=' ')