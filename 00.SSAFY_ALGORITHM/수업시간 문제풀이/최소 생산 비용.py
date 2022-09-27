def perm(l, v):
    global answer
    if v > answer:
        return

    if l == n:
        answer = min(answer, v)
    else:
        for i in range(n):
            if i not in ch:
                ch[l] = i
                perm(l + 1, v + arr[l][ch[l]])
                ch[l] = -1

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ch = [-1] * n
    answer = 99 * n
    perm(0, 0)
    print(f"#{tc} {answer}")