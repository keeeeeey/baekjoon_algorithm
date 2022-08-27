def subset(l):
    if l == n:
        for i in range(n):
            if ch[i] == 1:
                print(i + 1, end=" ")
        print()
    else:
        if ch[l] == 0:
            ch[l] = 1
            subset(l + 1)
            ch[l] = 0
            subset(l + 1)

n = int(input())
ch = [0] * (n + 1)
subset(0)