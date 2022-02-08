import sys
import heapq

input = sys.stdin.readline

INF = 1e9

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    des = []

    for _ in range(t):
        des.append(int(input()))

    des.sort()

    def dijkstra_pq(start, end):
        N = n + 1
        dist = [INF] * N

        q = []
        heapq.heappush(q, (0, start))
        dist[start] = 0

        while q:
            acc, cur = heapq.heappop(q)

            if dist[cur] < acc:
                continue

            for adj, d in graph[cur]:
                cost = dist[cur] + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(q, (cost, adj))

        return dist[end]

    for i in range(t):
        path1 = dijkstra_pq(s, g) + dijkstra_pq(g, h) + dijkstra_pq(h, des[i])
        path2 = dijkstra_pq(s, h) + dijkstra_pq(h, g) + dijkstra_pq(g, des[i])

        result = dijkstra_pq(s, des[i])

        if path1 == result or path2 == result:
            print(des[i], end=" ")