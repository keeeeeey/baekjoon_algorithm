import sys

def fn(s):
    return s[0]

T = int(input())
n_list = []
for i in range(T):
    age, name = list(sys.stdin.readline().split())
    n_list.append([int(age), name])
N = sorted(n_list, key=fn)
for i in range(len(N)):
    print(int(N[i][0]), N[i][1])