t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    lt = 0
    rt = m - 1
    temp = 0
    for i in range(rt + 1):
        temp += arr[i]

    min_value = temp
    max_value = temp

    while rt < n - 1:
        rt += 1

        temp -= arr[lt]
        temp += arr[rt]

        if temp > max_value:
            max_value = temp

        if temp < min_value:
            min_value = temp

        lt += 1

    answer = max_value - min_value
    print(f"#{tc} {answer}")