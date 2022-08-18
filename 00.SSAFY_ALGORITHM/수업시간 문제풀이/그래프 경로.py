t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    graph = [[0] * (v + 1) for _ in range(v + 1)]

    for _ in range(e):
        start, end = map(int, input().split())
        graph[start][end] = 1
    s, g = map(int, input().split())
    visited = [0] * (v + 1)
    visited[s] = 1
    stack = []
    cur = s
    stack.append(s)
    while stack:
        for i in range(1, v + 1):
            if graph[cur][i] == 1 and visited[i] == 0:
                stack.append(i)
        cur = stack.pop()
        visited[cur] = 1

    print(f"#{tc} {visited[g]}")