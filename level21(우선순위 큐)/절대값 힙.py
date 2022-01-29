import sys
import heapq
T = int(input())
N_list = [int(sys.stdin.readline()) for _ in range(T)]
heap = []
for i in range(len(N_list)):
    if N_list[i] == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(N_list[i]), N_list[i]))