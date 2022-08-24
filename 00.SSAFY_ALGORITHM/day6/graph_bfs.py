def bfs(g, v, n):
    visited = [False] * (n + 1)
    queue = []
    queue.append(v)
    visited[v] = True

    while queue:
        t = queue.pop(0)        # 큐에서 맨 앞의 원소 가져오기
        print(f"{t}", end=" ")
        # 현재 위치인 t에서 갈수 있는 정점들이 있는지 검사
        for i in g[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 인접 리스트
n = int(input())
graph = [[] for _ in range(n + 1)]
node = list(map(int, input().split()))
for a in range(0, len(node), 2):
    graph[node[a]].append(node[a + 1])
    graph[node[a + 1]].append(node[a])
bfs(graph, 1, 7)