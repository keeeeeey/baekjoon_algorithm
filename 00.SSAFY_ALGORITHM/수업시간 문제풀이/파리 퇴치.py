t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    grid = list(list(map(int, input().split())) for _ in range(n))
    ans = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            fly = 0
            for a in range(i, i + m):
                for b in range(j, j + m):
                    fly += grid[a][b]
            ans = max(ans, fly)

    print("#{} {}".format(tc, ans))