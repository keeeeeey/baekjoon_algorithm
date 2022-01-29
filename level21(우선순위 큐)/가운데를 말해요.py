import sys
import heapq
import math
T = int(input())
heap = []
N_list = []
for i in range(T):
    N = int(sys.stdin.readline())
    heapq.heappush(heap, N)
    print(heap)