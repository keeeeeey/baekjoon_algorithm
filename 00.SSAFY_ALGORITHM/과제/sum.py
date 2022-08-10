for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0
    for i in range(100):
        rs = 0
        for j in range(100):
             rs += arr[i][j]
        if rs > max_value:
            max_value = rs

    for i in range(100):
        cs = 0
        for j in range(100):
            cs += arr[j][i]
        if cs > max_value:
            max_value = cs

    temp = 0
    for i in range(100):
        temp += arr[i][i]
    if temp > max_value:
        max_value = temp

    reverse = 0
    for i in range(100):
        reverse += arr[i][99 - i]
    if reverse > max_value:
        max_value = reverse

    print(f"#{tc} {max_value}")