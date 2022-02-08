n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

print(graph)
INF = int(1e9)

def dijkstra_naive(graph, start):
    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N):
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                idx = i
        return idx

    N = len(graph)
    visited = [False] * N
    dist = [INF] * N

    visited[start] = True
    dist[start] = 0

    for adj, d in range(graph[start]):
        dist[adj] = d

    for _ in range(N - 1):
        cur = get_smallest_node()
        visited[cur] = True
        for adj, d in range(graph[cur]):
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost
    return dist
