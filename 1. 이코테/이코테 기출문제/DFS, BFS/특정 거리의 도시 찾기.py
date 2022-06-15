import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


distance = [-1] * (n + 1)
distance[x] = 0
q = deque([x])
while q:
    now = q.popleft()
    for i in range(len(graph[now])):
        if distance[graph[now][i]] == -1:
            distance[graph[now][i]] = distance[now] + 1
            q.append(graph[now][i])

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)