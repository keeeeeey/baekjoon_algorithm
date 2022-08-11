dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    answer = 0
    for y in range(100):
        if ladder[0][y] == 1:
            visited = [[0] * 100 for _ in range(100)]
            i = 0
            j = y
            while i < 99:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < 100 and 0 <= ny < 100 and visited[nx][ny] == 0 and ladder[nx][ny] != 0:
                        visited[i][j] = 1
                        i = nx
                        j = ny
            if ladder[i][j] == 2:
                answer = y
                break
    print(f"#{tc} {answer}")