dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move():
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                ni = i + dx[grid[i][j][1]]
                nj = j + dy[grid[i][j][1]]
                if 0 <= ni < n and 0 <= nj < n:
                    if temp[ni][nj] == 0:
                        temp[ni][nj] = grid[i][j]
                    else:
                        if temp[ni][nj][0] < grid[i][j][0]:
                            temp[ni][nj][1] = grid[i][j][1]
                        temp[ni][nj][0] += grid[i][j][0]

                    if ni == 0 or ni == n - 1 or nj == 0 or nj == n - 1:
                        temp[ni][nj][0] //= 2
                        if temp[ni][nj][1] == 0:
                            temp[ni][nj][1] = 1
                        elif temp[ni][nj][1] == 1:
                            temp[ni][nj][1] = 0
                        elif temp[ni][nj][1] == 2:
                            temp[ni][nj][1] = 3
                        elif temp[ni][nj][1] == 3:
                            temp[ni][nj][1] = 2

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]

t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    for _ in range(k):
        x, y, cnt, dir = map(int, input().split())
        grid[x][y] = [cnt, dir - 1]

    for _ in range(m):
        move()

    answer = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                answer += grid[i][j][0]

    print(f"#{tc} {answer}")