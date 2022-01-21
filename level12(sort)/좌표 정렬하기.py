import sys

T = int(input())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
n_list.sort()
for i in range(len(n_list)):
    print("{} {}".format(n_list[i][0], n_list[i][1]))