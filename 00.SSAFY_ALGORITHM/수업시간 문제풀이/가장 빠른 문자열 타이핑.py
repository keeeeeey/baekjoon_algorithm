t = int(input())
for tc in range(1, t + 1):
    a, b = input().split()
    al = len(a)
    bl = len(b)
    cnt = 0
    i = 0
    while i < al:
        cnt += 1
        if a[i] == b[0]:
            flag = True
            for j in range(1, bl):
                if i + j >= al or a[i + j] != b[j]:
                    flag = False
                    break
            if flag:
                i += bl - 1
        i += 1

    print(f"#{tc} {cnt}")