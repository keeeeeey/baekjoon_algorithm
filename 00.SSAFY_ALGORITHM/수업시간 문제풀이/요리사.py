def comb(l, s):
    global min_v
    if l == n // 2:
        ch2 = []
        for i in range(n):
            if i not in ch:
                ch2.append(i)
        value_a = cuisine(ch)
        value_b = cuisine(ch2)
        min_v = min(min_v, abs(value_a - value_b))
    else:
        for i in range(s, n):
            if i not in ch:
                ch[l] = i
                comb(l + 1, i)

def cuisine(c):
    temp = 0
    for i in range(n // 2 - 1):
        for j in range(i + 1, n // 2):
            temp += arr[c[i]][c[j]] + arr[c[j]][c[i]]
    return temp

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ch = [-1] * (n // 2)
    min_v = 20000
    comb(0, 0)
    print(f"#{tc} {min_v}")