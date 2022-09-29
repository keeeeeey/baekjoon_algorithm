from collections import deque

def divide(now):
    q = deque()
    q.append(now)
    ch[now] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if ch[next] == 0:
                ch[next] = 1
                q.append(next)

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ch = [0] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if ch[i] == 0:
            cnt += 1
            divide(i)
    print(f"#{tc} {cnt}")