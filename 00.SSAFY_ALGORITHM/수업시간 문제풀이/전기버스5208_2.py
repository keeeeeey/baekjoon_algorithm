def subset(l, v):
    global answer
    if v >= answer:
        return

    if l == n - 1:
        if arrive():
            answer = v
        return

    ch[l] = 1
    subset(l + 1, v + 1)
    ch[l] = 0
    subset(l + 1, v)

def arrive():
    now = 0
    battery = batteries[0]
    while battery:
        now += 1
        battery -= 1

        if ch[now] == 1:
            battery = batteries[now]
            if now + batteries[now] >= n - 1:
                now = n - 1
                break

    if now == n - 1:
        return True
    else:
        return False

t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    n = arr[0]
    batteries = arr[1:n]
    ch = [0] * (n - 1)
    answer = n - 2
    subset(1, 0)
    print(f"#{tc} {answer}")
