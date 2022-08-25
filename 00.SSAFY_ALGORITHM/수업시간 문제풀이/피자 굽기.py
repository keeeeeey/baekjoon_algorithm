t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = []
    for i in range(n):
        q.append([arr.pop(0), i + 1])
        m -= 1

    cnt = 1
    while len(q) > 1:
        pizza = q.pop(0)

        pizza[0] //= 2
        if pizza[0] == 0:
            if m > 0:
                q.append([arr.pop(0), n + cnt])
                cnt += 1
                m -= 1
        else:
            q.append(pizza)

    print(f"#{tc} {q[0][1]}")