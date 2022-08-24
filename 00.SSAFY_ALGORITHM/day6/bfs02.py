dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 2차원 배열을 너비 우선 탐색으로 탐색하는 bfs 함수를 작성
def bfs(i, j, n):
    visited = [[0] * n for _ in range(n)]      # 2차원 배열로 방문 체크
    queue = []
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        i, j = queue.pop(0)
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                queue.append((ni, nj))

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]