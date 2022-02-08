import heapq

INF = int(1e9)

def networkDelayTime(times, n, k):
    graph = [[] for _ in range(n + 1)]
    for i in range(len(times)):
        a, b, c = times[i]
        graph[a].append((b, c))

    def dijkstra_pq(graph, k):
        N = len(graph)
        dist = [INF] * N

        q = []
        heapq.heappush(q, (0, k))
        dist[k] = 0

        while q:
            acc, cur = heapq.heappop(q)
            for adj, d in graph[cur]:
                cost = acc + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(q, (cost, adj))

        return dist

    ans = dijkstra_pq(graph, k)
    if INF not in ans[1:]:
        return max(ans[1:])
    else:
        return -1

print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))