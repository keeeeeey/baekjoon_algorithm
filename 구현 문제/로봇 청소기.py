import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited[r][c] = 1
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                flag = 1
                break

    if flag == 0:
        if graph[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        else:
            r = r - dx[d]
            c = c - dy[d]