t = int(input())
for tc in range(1, t + 1):
    n, p = map(int, input().split())
    answer = 1
    a = n // p
    b = n % p
    for _ in range(p - 1):
        if b:
            answer *= (a + 1)
            n -= a + 1
            b -= 1
        else:
            answer *= a
            n -= a
    answer *= n
    print(f"#{tc} {answer}")