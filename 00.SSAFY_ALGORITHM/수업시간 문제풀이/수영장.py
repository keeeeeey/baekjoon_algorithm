combination = []
ch = [-1] * 4

def comb(l, s):
    if l == 4:
        temp = []
        for i in range(4):
            temp.append(ch[i])
        combination.append(temp)
    else:
        for i in range(s, 15):
            if i not in ch:
                if l > 0 and i - ch[l - 1] < 3:
                    continue
                ch[l] = i
                comb(l + 1, i)

comb(0, 0)

def day_or_month():
    global min_v
    for i in range(12):
        if cost[i] > m:
            cost[i] = m
    min_v = min(min_v, sum(cost))

def month_or_3month(c):
    global min_v
    temp = [0] * 14

    for i in range(12):
        temp[i] = cost[i]

    for i in range(4):
        if c[i] >= 12:
            continue
        if cost[c[i]] + cost[c[i] + 1] + cost[c[i] + 2] > m3:
            temp[c[i]] = m3
            temp[c[i] + 1] = 0
            temp[c[i] + 2] = 0
        min_v = min(min_v, sum(temp))

t = int(input())
for tc in range(1, t + 1):
    d, m, m3, y = map(int, input().split())
    plan = list(map(int, input().split()))
    cost = [0] * 14

    for i in range(12):
        cost[i] = plan[i] * d
    min_v = min(y, sum(cost))

    day_or_month()

    for c in combination:
        month_or_3month(c)

    print(f"#{tc} {min_v}")