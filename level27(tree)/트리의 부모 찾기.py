import sys
sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
par = [-1] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(n):
    for i in tree[n]:
        if par[i] == -1:
            par[i] = n
            dfs(i)

dfs(1)
for i in range(2, len(par)):
    print(par[i])