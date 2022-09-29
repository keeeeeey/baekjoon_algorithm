def prim(r):
    mst = [0] * (v + 1)
    key = [10] * (v + 1)
    key[r] = 0
    for _ in range(v):
        u = 0
        min_v = 10000
        for i in range(v + 1):
            if mst[i] == 0 and key[i] < min_v:
                u = i
                min_v = key[i]
        mst[u] = 1
        for i in range(len(graph[u])):
            if mst[graph[u][i][0]] == 0:
                key[graph[u][i][0]] = min(key[graph[u][i][0]], graph[u][i][1])
    return sum(key)

t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])
        graph[b].append([a, w])

    print(f"#{tc} {prim(0)}")