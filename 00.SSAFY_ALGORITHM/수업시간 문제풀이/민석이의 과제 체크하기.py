t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    temp = [0] * (n + 1)
    for i in arr:
        temp[i] = 1

    answer = f"#{tc}"

    for i in range(1, n + 1):
        if temp[i] == 0:
            answer += " " + str(i)

    print(answer)