import sys
import heapq
INF = 1e9

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())

def dijkstra_pq(start, end):
    N = len(graph)
    dist = [INF] * N

    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        acc, cur = heapq.heappop(q)
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist[end]

path1 = dijkstra_pq(1, v1) + dijkstra_pq(v1, v2) + dijkstra_pq(v2, V)

path2 = dijkstra_pq(1, v2) + dijkstra_pq(v2, v1) + dijkstra_pq(v1, V)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))