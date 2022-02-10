import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

X, K = map(int, input().split())

def dijkstra_pq(start):
    n = len(graph)
    dist = [INF] * n

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
    return dist

ans = dijkstra_pq(1)[K] + dijkstra_pq(K)[X]
if ans > INF:
    print(-1)
else:
    print(ans)