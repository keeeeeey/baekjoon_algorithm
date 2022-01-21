import sys

def fn(s):
    return len(s), str(s)

T = int(input())
s_list = list(set(sys.stdin.readline().strip() for _ in range(T)))
S = sorted(s_list, key=fn)
for i in range(len(S)):
    print(S[i])