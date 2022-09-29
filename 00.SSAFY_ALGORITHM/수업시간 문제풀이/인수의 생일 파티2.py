import heapq

INF = int(1e9)

def dijkstra(start, graph):
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

t = int(input())
for tc in range(1, t + 1):
    N, M, X = map(int, input().split())
    graph_go = [[] for _ in range(N + 1)]
    graph_come = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph_go[x].append((y, c))
        graph_come[y].append((x, c))

    go_dist = dijkstra(X, graph_go)
    come_dist = dijkstra(X, graph_come)

    max_dist = 0
    for i in range(1, N + 1):
        if i == X:
            continue
        max_dist = max(max_dist, go_dist[i] + come_dist[i])
    print(f"#{tc} {max_dist}")