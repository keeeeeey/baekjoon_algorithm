import sys

def fn(s):
    return s[-1], s[0]

T = int(input())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
N = sorted(n_list, key=fn)
for i in range(T):
    print("{} {}".format(N[i][0], N[i][1]))