import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra_pq(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        acc, cur = heapq.heappop(q)

        if distance[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = acc + d
            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))

    return distance

list = dijkstra_pq(C)

cnt = 0
time = 0
for i in range(1, len(list)):
    if 0 < list[i] < INF:
        cnt += 1
        time = max(time, list[i])

print(cnt, time)

