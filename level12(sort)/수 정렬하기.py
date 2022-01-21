import sys

T = int(input())
n_list = [int(input()) for _ in range(T)]
n_list.sort()
for i in range(len(n_list)):
    print(n_list[i])