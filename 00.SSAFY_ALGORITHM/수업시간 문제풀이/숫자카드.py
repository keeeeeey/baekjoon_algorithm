t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input()))
    cnt_list = [0] * 10

    for i in range(n):
        cnt_list[arr[i]] += 1

    idx = 0
    max_cnt = 0
    for i in range(10):
        if cnt_list[i] >= max_cnt:
            idx = i
            max_cnt = cnt_list[i]

    print(f"#{tc} {idx} {max_cnt}")