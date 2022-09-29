import heapq

INF = int(1e9)

def dijkstra(start, end):
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

    return dist[end]

t = int(input())
for tc in range(1, t + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))

    max_dist = 0
    for i in range(1, N + 1):
        if i == X:
            continue
        max_dist = max(max_dist, dijkstra(i, X) + dijkstra(X, i))
    print(f"#{tc} {max_dist}")