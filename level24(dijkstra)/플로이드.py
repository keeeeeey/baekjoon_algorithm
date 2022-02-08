import sys
input = sys.stdin.readline
INF =1e9

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def floyd_warshall():
    N = len(graph)
    dist = [[INF] * N for _ in range(N)]

    for idx in range(1, N):
        dist[idx][idx] = 0

    for start, adjs in enumerate(graph):
        for adj, d in adjs:
            if dist[start][adj] > d:
                dist[start][adj] = d

    for k in range(1, N):
        for a in range(1, N):
            for b in range(1, N):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist

list = floyd_warshall()
for i in range(1, len(list)):
    print(' '.join([str(el) if el != INF else '0' for el in list[i][1:]]))