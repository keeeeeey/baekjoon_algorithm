t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    numbers = input()
    cnt = 0
    answer = 0
    for number in numbers:
        if number == "0":
            cnt = 0
        else:
            cnt += 1
        if cnt > answer:
            answer = cnt
    print(f"#{tc} {answer}")