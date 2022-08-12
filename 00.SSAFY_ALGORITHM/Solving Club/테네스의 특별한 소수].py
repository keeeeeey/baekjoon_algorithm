t = int(input())
for tc in range(1, t + 1):
    d, a, b = map(int, input().split())
    arr = [True] * (b + 1)
    arr[1] = False
    m = int(b ** 0.5)
    for i in range(2, m + 1):
        if arr[i]:
            for j in range(i + i, b + 1, i):
                arr[j] = False
    prime_number_list = [i for i in range(a, b + 1) if arr[i] == True]

    answer = 0
    for prime_number in prime_number_list:
        if str(d) in str(prime_number):
            answer += 1
    print(f"#{tc} {answer}")
