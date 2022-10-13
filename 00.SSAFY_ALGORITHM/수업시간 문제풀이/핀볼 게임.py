dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def game_start(i, j, d):
    stack = []
    stack.append((i, j, d))
    while stack:
        x, y, d = stack.pop()
        nx = x + dx[d]
        ny = y + dy[d]

        if nx == i and ny == j:
            break

        

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    wormhole = [[] for _ in range(5)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 6:
                wormhole[0].append([i, j])
            if arr[i][j] == 7:
                wormhole[1].append([i, j])
            if arr[i][j] == 8:
                wormhole[2].append([i, j])
            if arr[i][j] == 9:
                wormhole[3].append([i, j])
            if arr[i][j] == 10:
                wormhole[4].append([i, j])

    max_score = 0
    for i in range(n):
        for j in range(n):
            for d in range(4):
                game_start(i, j, d)

    print(f"#{tc} {max_score}")