import sys
import heapq

input = sys.stdin.readline

INF = 1e9

V, M = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

def dijkstra_pq(start):
    N = len(graph)
    dist = [INF] * N

    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    cnt = 0

    while q:
        acc, cur = heapq.heappop(q)

        if cnt >= V:
            return False

        if dist[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                cnt += 1
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

list = dijkstra_pq(1)

if list:
    for i in range(2, len(list)):
        if list[i] == INF:
            print(-1)
        else:
            print(list[i])
else:
    print(-1)