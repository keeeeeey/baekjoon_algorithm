def work(l, v):
    global max_v
    if l == n:
        max_v = max(max_v, v * 100)
    if v * 100 <= max_v:
        return
    for i in range(n):
        if i not in ch:
            ch[l] = i
            temp = v * p[l][ch[l]] / 100
            work(l + 1, temp)
            ch[l] = -1

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    ch = [-1] * n
    max_v = 0
    work(0, 1)
    print(f"#{tc} {max_v:.6f}")