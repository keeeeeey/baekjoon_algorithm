def selection_sort(numbers, n):
    for i in range(n - 1):
        max_idx = i
        for j in range(i, n):
            if numbers[max_idx] > numbers[j]:
                max_idx = j
        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
    return numbers

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = selection_sort(numbers, n)
    print(f"#{tc}", end=" ")
    for i in range(n):
        print(answer[i], end=" ")
    print()
