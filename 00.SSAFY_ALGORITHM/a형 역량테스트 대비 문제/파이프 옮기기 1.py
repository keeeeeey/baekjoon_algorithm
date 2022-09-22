dx = [1, 0, 1]
dy = [0, 1, 1]
def dfs(x, y, idx):
    global answer

    if x == n - 1 and y == n - 1:
        answer += 1
        return

    for d in range(3):
        if d == idx:
            continue

        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if dx[d] == dy[d]:
                if room[nx][ny] == 0 and room[nx - 1][ny] == 0 and room[nx][ny - 1] == 0:
                    dfs(nx, ny, 3)
            elif dx[d] == 1:
                if room[nx][ny] == 0:
                    dfs(nx, ny, 1)
            elif dy[d] == 1:
                if room[nx][ny] == 0:
                    dfs(nx, ny, 0)

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(0, 1, 0)
print(answer)