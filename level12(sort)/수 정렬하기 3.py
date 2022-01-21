import sys

T = int(input())
n_list = [int(sys.stdin.readline()) for _ in range(T)]
count_list = [n_list.count(i) for i in range(1, max(n_list) + 1)]
