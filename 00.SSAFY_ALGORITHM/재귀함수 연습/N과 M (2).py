def recursive(l, s):
    if l == m:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:
        for i in range(s, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                recursive(l + 1, i)
                ch[i] = 0

n, m = map(int, input().split())
ch = [0] * (n + 1)
recursive(0, 1)