import sys

input = sys.stdin.readline

INF = 1e9

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def floyd_warshall():
    N = len(graph)
    dist = [[INF] * N for _ in range(N)]

    for start, adjs in enumerate(graph):
        for adj, d in adjs:
            if dist[start][adj] > d:
                dist[start][adj] = d

    for k in range(1, N):
        for a in range(1, N):
            for b in range(1, N):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist
print(floyd_warshall())
min_num = 1e9

list = floyd_warshall()
for i in range(1, len(list)):
    min_num = min(min_num, list[i][i])
if min_num == INF:
    print(-1)
else:
    print(min_num)