def prim(s):
    mst = [0] * n
    key = [int(1e16)] * n
    key[s] = 0
    for _ in range(n):
        u = 0
        min_v = int(1e16)
        for i in range(n):
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
    n = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    e = float(input())
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            lij = ((island_x[i] - island_x[j])**2 + (island_y[i] - island_y[j])**2) * e
            graph[i].append([j, lij])
            graph[j].append([i, lij])

    answer = round(prim(0))
    print(f"#{tc} {answer}")