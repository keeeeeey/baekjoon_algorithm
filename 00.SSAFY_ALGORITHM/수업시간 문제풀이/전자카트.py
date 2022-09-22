def cart(l):
    global answer
    if l == n:
        temp = 0
        for i in range(n):
            temp += arr[ch[i]][ch[i + 1]]
        answer = min(answer, temp)
    else:
        for i in range(1, n):
            if i not in ch:
                ch[l] = i
                cart(l + 1)
                ch[l] = -1

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ch = [0] * (n + 1)
    answer = n * n * 10
    cart(1)
    print(f"#{tc} {answer}")
