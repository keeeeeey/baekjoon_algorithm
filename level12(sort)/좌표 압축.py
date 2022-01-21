import sys

T = int(input())
N = list(map(int, sys.stdin.readline().split()))
N_set = sorted(list(set(N)))
N_dict = {N_set[i] : i for i in range(len(N_set))}
for i in N:
    print(N_dict[i], end=' ')