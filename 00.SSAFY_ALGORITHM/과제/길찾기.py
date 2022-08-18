for _ in range(1, 11):
    tc, n = map(int, input().split())
    graph = [[] * 100 for _ in range(100)]
    e = list(map(int, input().split()))
    for i in range(0, n * 2, 2):
        graph[e[i]].append(e[i + 1])
    visited = [0] * 100
    stack = [0]
    cur = 0
    visited[cur] = 1

    while stack:
        for v in graph[cur]:
            stack.append(v)
        cur = stack.pop()
        visited[cur] = 1
        if cur == 99:
            break
    print(f"#{tc} {visited[99]}")
