import sys
import heapq
INF = 1e9

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra_pq(graph, K):
    N = len(graph)
    dist = [INF] * N

    q = []
    heapq.heappush(q, (0, K))
    dist[K] = 0

    while q:
        acc, cur = heapq.heappop(q)
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

list = dijkstra_pq(graph, K)

for i in range(1, len(list)):
    if list[i] == INF:
        print("INF")
    else:
        print(list[i])