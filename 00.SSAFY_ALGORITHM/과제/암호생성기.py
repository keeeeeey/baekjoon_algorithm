for _ in range(10):
    tc = int(input())
    numbers = list(map(int, input().split()))
    flag = True
    while True:
        for i in range(1, 6):
            first = numbers.pop(0) - i
            if first <= 0:
                numbers.append(0)
                flag = False
                break
            else:
                numbers.append(first)
        if not flag:
            break

    print(f"#{tc} {' '.join(map(str, numbers))}")
