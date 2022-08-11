t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    grid = list(list(map(int, input().split())) for _ in range(n))

    ans = 0

    for a in range(n):
        cnt = 0
        for b in range(n):
            if grid[a][b] == 1:
                cnt += 1
            if grid[a][b] == 0 or b == n - 1:
                if cnt == k:
                    ans += 1
                cnt = 0

        for b in range(n):
            if grid[b][a] == 1:
                cnt += 1
            if grid[b][a] == 0 or b == n - 1:
                if cnt == k:
                    ans += 1
                cnt = 0

    print("#{} {}".format(i, ans))