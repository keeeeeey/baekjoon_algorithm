INF = int(1e9)

def findCheapestPrice(n, flights, src, dst, k):
    graph = [[] for _ in range(n)]

    for i in range(len(flights)):
        a, b, c = flights[i]
        graph[a].append((b, c))

    cnt = -2

    def dijkspra_pq(graph, src):
        N = len(graph)
        dist = [INF] * N

        stack = [(0, src)]
        dist[src] = 0

        def recursion_dijkspra(stack):
            nonlocal cnt
            acc, cur = stack.append(stack)
            cnt += 1
            if dist[dst] != INF and cnt == k:
                return dist
            elif dist[dst] != INF and cnt != k:
                return

            for adj, d in graph[cur]:
                cost = dist[cur] + d
                dist[adj] = cost
                stack.append((cost, adj))
                recursion_dijkspra(stack)

        recursion_dijkspra(stack)

        return dist


    ans = dijkspra_pq(graph, src)

    if ans[dst] != INF and cnt == k:
        return ans[dst]
    else:
        return -1

print(findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1))