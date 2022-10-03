def prim(r, V):
    mst = [0] * (V + 1)
    key = [10000] * (V + 1)
    key[r] = 0
    for _ in range(V):
        u = 0
        min_v = 10000
        for i in range(V + 1):
            if mst[i] == 0 and key[i] < min_v:
                u = i
                min_v = key[i]
        mst[u] = 1

        for i in range(V + 1):
            if mst[i] == 0 and arr[u][i] > 0:
                key[i] = min(key[i], arr[u][i])
    return sum(key)

import heapq

INF = int(1e9)

def dijkstra(s, V):
    dist = [INF] * V
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))