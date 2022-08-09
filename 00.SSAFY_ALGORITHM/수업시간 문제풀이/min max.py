t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    min = int(1e9)
    max = 0
    for i in range(n):
        if arr[i] > max:
            max = arr[i]

        if arr[i] < min:
            min = arr[i]

    answer = max - min
    print(f"#{tc} {answer}")