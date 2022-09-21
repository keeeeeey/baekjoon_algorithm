def subset(l):
    global cnt
    if l == 10:
        subset_sum = 0
        for i in range(10):
            if s[i] != 0:
                subset_sum += s[i]
        if subset_sum == 0:
            cnt += 1
    else:
        s[l] = n[l]
        subset(l + 1)
        s[l] = 0
        subset(l + 1)

n = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
s = [0] * 10
cnt = -1
subset(0)
print(cnt)