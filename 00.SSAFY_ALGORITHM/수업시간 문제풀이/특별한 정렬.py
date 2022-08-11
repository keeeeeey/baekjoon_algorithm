t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    for i in range(n - 1):
        idx = i
        value = numbers[i]
        if i % 2 == 0:
            for j in range(i, n):
               if value < numbers[j]:
                   value = numbers[j]
                   idx = j
            numbers[i], numbers[idx] = numbers[idx], numbers[i]
        else:
            for j in range(i, n):
               if value > numbers[j]:
                   value = numbers[j]
                   idx = j
            numbers[i], numbers[idx] = numbers[idx], numbers[i]

    print(f"#{tc}", end=" ")
    for i in range(10):
        print(numbers[i], end=" ")
    print()