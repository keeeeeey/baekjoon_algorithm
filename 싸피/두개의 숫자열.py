t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = -int(1e9)
    for i in range(abs(n - m) + 1):
        value = 0
        for j in range(min(n, m)):
            if n == m:
                value += a[j] * b[j]
            elif n > m:
                value += a[i + j] * b[j]
            elif n < m:
                value += a[j] * b[i + j]
        ans = max(ans, value)

    print("#{} {}".format(tc, ans))
