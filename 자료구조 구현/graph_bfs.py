from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        front = q.popleft()

        for adj in graph[front]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    print(visited)
    return visited

bfs_queue(1)