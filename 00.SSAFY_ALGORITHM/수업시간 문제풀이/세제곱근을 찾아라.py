t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    start = 1
    end = n
    answer = 0
    flag = False
    while start <= end:
        mid = (start + end) // 2
        temp = mid * mid * mid
        if temp > n:
            end = mid - 1
        elif temp < n:
            start = mid + 1
        else:
            answer = mid
            flag = True
            break
    if flag:
        print(f"#{tc} {answer}")
    else:
        print(f"#{tc} -1")