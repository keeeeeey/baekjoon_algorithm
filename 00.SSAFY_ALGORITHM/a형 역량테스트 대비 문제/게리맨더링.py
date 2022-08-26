def bfs(g):
    visited = [0] * (n + 1)
    q = []
    q.append(g[0])
    visited[g[0]] = 1
    cnt = 1
    answer = 0
    while q:
        cur = q.pop(0)
        answer += population[cur]
        for adj in graph[cur]:
            if adj in g and visited[adj] == 0:
                q.append(adj)
                visited[adj] = 1
                cnt += 1

    if cnt == len(g):
        return answer
    else:
        return False

def division(l):
    global answer
    if l == n:
        g1 = []
        g0 = []
        for i in range(1, n + 1):
            if ch[i]:
                g1.append(i)
            else:
                g0.append(i)

        if not g1 or not g0:
            return

        p1 = bfs(g1)

        if not p1:
            return

        p0 = bfs(g0)

        if not p0:
            return

        if abs(p1 - p0) < answer:
            answer = abs(p1 - p0)

    else:
        if ch[l] == 0:
            ch[l] = 1
            division(l + 1)
            ch[l] = 0
            division(l + 1)

n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(n):
    city = list(map(int, input().split()))
    for j in range(1, city[0] + 1):
        graph[i + 1].append(city[j])

answer = 1000
ch = [0] * (n + 1)
division(1)

if answer == 1000:
    print(-1)
else:
    print(answer)