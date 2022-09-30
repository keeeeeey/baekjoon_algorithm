def perm(l):
    if l == n - 1:
        print(ch)
        cal()
    else:
        for i in range(4):
            if operator_cnt[i] == 0:
                continue
            ch[l] = i
            operator_cnt[i] -= 1
            perm(l + 1)
            ch[l] = -1
            operator_cnt[i] += 1

def cal():
    global min_v
    global max_v

    temp = numbers[0]
    for i in range(n - 1):
        if ch[i] == 0:
            temp += numbers[i + 1]
        elif ch[i] == 1:
            temp -= numbers[i + 1]
        elif ch[i] == 2:
            temp *= numbers[i + 1]
        elif ch[i] == 3:
            temp = int(temp / numbers[i + 1])

    min_v = min(min_v, temp)
    max_v = max(max_v, temp)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    operator_cnt = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    ch = [-1] * (n - 1)
    min_v = 100000000
    max_v = -100000000
    perm(0)
    print(f"#{tc} {max_v - min_v}")