import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append((y, 1))
    graph[y].append((x, 1))

X, K = map(int, input().split())

def floyd_warshall():
    n = len(graph)
    dist = [[INF] * n for _ in range(n)]

    for i in range(1, n):
        dist[i][i] = 0

    for start, adjs in enumerate(graph):
        for adj, d in adjs:
            if dist[start][adj] > d:
                dist[start][adj] = d

    for k in range(1, n):
        for a in range(1, n):
            for b in range(1, n):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist

list = floyd_warshall()
print(list[1][K] + list[K][X])