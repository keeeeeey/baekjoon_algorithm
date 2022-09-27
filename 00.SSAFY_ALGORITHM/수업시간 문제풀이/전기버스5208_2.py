t = int(input())

def backtracking(idx, cnt):
    global min_v

    if cnt >= min_v:
        return

    if idx == n - 1:
        min_v = min(min_v, cnt)
        return

    for i in range(1, bus_stop[idx] + 1):
        backtracking(idx + i, cnt + 1)

for tc in range(1, t + 1):
    line = list(map(int, input().split()))
    n = line[0]
    bus_stop = line[1:] + [0]
    min_v = 101

    backtracking(0, -1)
    print(f"#{tc} {min_v}")