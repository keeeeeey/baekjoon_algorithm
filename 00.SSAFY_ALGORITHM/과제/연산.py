from collections import deque

def bfs(n):
    q = deque()
    cnt = 0
    q.append([n, cnt])
    visited = set()
    visited.add(n)
    while q:
        n, cnt = q.popleft()

        if n == m:
            return cnt

        if n < 1 or n > 1000000:
            continue

        for next in (n + 1, n - 1, n * 2, n - 10):
            if next not in visited:
                visited.add(next)
                q.append([next, cnt + 1])

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    print(f"#{tc} {bfs(n)}")