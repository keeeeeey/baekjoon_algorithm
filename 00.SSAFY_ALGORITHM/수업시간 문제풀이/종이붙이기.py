t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cnt_list = [1, 3]
    for i in range(2, n // 10):
        cnt_list.append(cnt_list[i - 1] + cnt_list[i - 2] * 2)
    print(f"#{tc} {cnt_list[n // 10 - 1]}")
