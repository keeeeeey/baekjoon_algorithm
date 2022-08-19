t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    num_list = [2, 3, 5, 7, 11]
    print(f"#{tc}", end=" ")
    for num in num_list:
        cnt = 0
        while n % num == 0:
            n /= num
            cnt += 1
        print(cnt, end=" ")
    print()