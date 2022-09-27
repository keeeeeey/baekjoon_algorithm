def bus():
    global cnt
    now = 0
    battery = batteries[0]
    while battery:
        idx = 0
        temp = 0
        for i in range(now + 1, now + battery + 1):
            if temp < i + batteries[i]:
                temp = i + batteries[i]
                idx = i
        cnt += 1
        battery = batteries[idx]
        now = idx

        if now + battery >= n - 1:
            break

t = int(input())
for tc in range(1, t + 1):
    batteries = list(map(int, input().split()))
    n = batteries.pop(0)
    cnt = 0
    bus()
    print(f"#{tc} {cnt}")