t = int(input())
for tc in range(1, t + 1):
    t_num = int(input())
    scores = list(map(int, input().split()))
    temp = [0] * 101
    for score in scores:
        temp[score] += 1

    answer = 0
    max_cnt = 0

    for i in range(101):
        if temp[i] >= max_cnt:
            max_cnt = temp[i]
            answer = i

    print(f"#{tc} {answer}")