def bfs(s):
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        cur = q.pop(0)
        if cur == g:
            return

        for adj in graph[cur]:
            if visited[adj] == 0:
                visited[adj] = 1
                dis[adj] = dis[cur] + 1
                q.append(adj)

t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    s, g = map(int, input().split())
    visited = [0] * (v + 1)
    dis = [0] * (v + 1)
    bfs(s)
    print(f"#{tc} {dis[g]}")
