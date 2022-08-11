t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    grid = [[0] * 10 for _ in range(10)]
    paints = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for k in range(n):
        for i in range(paints[k][0], paints[k][2] + 1):
            for j in range(paints[k][1], paints[k][3] + 1):
                grid[i][j] += paints[k][4]
                if grid[i][j] == 3:
                    answer += 1

    print(f"#{tc} {answer}")