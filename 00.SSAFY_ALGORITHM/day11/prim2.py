def prim2(r, v):
    mst = [0] * (v + 1)
    mst[r] = 1
    s = 0
    for _ in range(v):
        u = 0
        min_v = 10000
        for i in range(v + 1):
            if mst[i] == 1:
                for j in range(v + 1):
                    if adj_arr[i][j] > 0 and mst[j] == 0 and min_v > adj_arr[i][j]:
                        u = j
                        min_v = adj_arr[i][j]
        s += min_v
        mst[u] = 1
    return s

v, e = map(int, input().split())
adj_arr = [[0] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adj_arr[u][v] = w
    adj_arr[v][u] = w

print(prim2(0, v))