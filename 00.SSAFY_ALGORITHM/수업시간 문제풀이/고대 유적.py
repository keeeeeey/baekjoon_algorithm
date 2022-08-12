t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    answer = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                cnt = 0
            else:
                cnt += 1
            if cnt > answer:
                answer = cnt
        cnt = 0

    cnt = 0
    for j in range(m):
        for i in range(n):
            if grid[i][j] == 0:
                cnt = 0
            else:
                cnt += 1
            if cnt > answer:
                answer = cnt
        cnt = 0

    print(f"#{tc} {answer}")