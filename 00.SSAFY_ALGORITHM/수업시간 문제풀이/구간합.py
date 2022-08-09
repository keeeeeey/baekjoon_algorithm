t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    min_value = int(1e9)
    max_value = 0

    for i in range(n - m + 1):
        temp = 0
        for j in range(i, i + m):
            temp += arr[j]
        if temp < min_value:
            min_value = temp

        if temp > max_value:
            max_value = temp

    answer = max_value - min_value
    print(f"#{tc} {answer}")