def prim1(r, v):
    mst = [0] * (v + 1)
    key = [10000] * (v + 1)
    key[r] = 0
    for _ in range(v):
        u = 0
        min_v = 10000
        for i in range(v + 1):
            if mst[i] == 0 and key[i] < min_v:
                u = i
                min_v = key[i]
        mst[u] = 1
        for v2 in range(v + 1):
            if mst[v2] == 0 and adj_arr[u][v2] > 0:
                key[v2] = min(key[v2], adj_arr[u][v2])
    return sum(key)

v, e = map(int, input().split())
adj_arr = [[0] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adj_arr[u][v] = w
    adj_arr[v][u] = w

print(prim1(0, v))