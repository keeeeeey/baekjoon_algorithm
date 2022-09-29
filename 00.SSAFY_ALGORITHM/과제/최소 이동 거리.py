import heapq
INF = int(1e9)
def dijkstra(s):
    dist = [INF] * (N + 1)

    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist[N]

t = int(input())
for tc in range(1, t + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    print(f"#{tc} {dijkstra(0)}")
