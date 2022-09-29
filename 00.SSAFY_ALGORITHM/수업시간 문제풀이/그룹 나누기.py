from collections import deque

def divide(now):
    q = deque()
    q.append(now)
    visited[now] = 1
    while q:
        now = q.popleft()
        for i in range(len(graph[now])):
            if visited[graph[now][i]] == 0:
                visited[graph[now][i]] = 1
                q.append(graph[now][i])

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]

    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i + 1])
        graph[arr[i + 1]].append(arr[i])

    visited = [0] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if visited[i] == 0:
            cnt += 1
            divide(i)

    print(f"#{tc} {cnt}")