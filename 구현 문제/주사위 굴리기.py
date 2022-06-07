import sys
input = sys.stdin.readline

N, M, x, y, k = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
direction_list = list(map(int, input().split()))
dice = [0 for _ in range(6)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k):
    dir = direction_list[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not 0 <= nx < N or not 0 <= ny < M:
        continue

    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0

    x = nx
    y = ny
    print(dice[0])