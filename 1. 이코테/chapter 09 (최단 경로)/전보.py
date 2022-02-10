import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra_pq(C):
    n = len(graph)
    dist = [INF] * n

    q = []
    heapq.heappush(q, (0, C))
    dist[C] = 0

    while q:
        acc, cur = heapq.heappop(q)
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

list = dijkstra_pq(C)

cnt = 0
time = 0
for i in range(1, len(list)):
    if 0 < list[i] < INF:
        cnt += 1
        time = max(time, list[i])

print(cnt, time)