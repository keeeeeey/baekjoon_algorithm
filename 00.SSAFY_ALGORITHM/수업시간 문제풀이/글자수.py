t = int(input())
for tc in range(1, t + 1):
    str1 = input()
    str2 = input()
    answer = 0
    for a in str1:
        cnt = 0
        for b in str2:
            if a == b:
                cnt += 1
        if cnt > answer:
            answer = cnt
    print(f"#{tc} {answer}")