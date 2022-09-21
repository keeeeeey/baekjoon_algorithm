def perm(cnt, s):
    global max_prize
    if cnt == c:
        max_prize = max(int("".join(n_list)), max_prize)
    else:
        for i in range(s, len_n):
            for j in range(i + 1, len_n):
                n_list[i], n_list[j] = n_list[j], n_list[i]
                perm(cnt + 1, i)
                n_list[i], n_list[j] = n_list[j], n_list[i]

t = int(input())
for tc in range(1, t + 1):
    n, c = map(int, input().split())
    n_list = list(str(n))
    len_n = len(n_list)
    cnt = 0
    if c > len_n:
        if (c - len_n) % 2 == 1:
            n_list[0], n_list[1] = n_list[1], n_list[0]
            cnt += 1
        c = len_n
    max_prize = 0
    perm(cnt, 0)
    print(f"#{tc} {max_prize}")