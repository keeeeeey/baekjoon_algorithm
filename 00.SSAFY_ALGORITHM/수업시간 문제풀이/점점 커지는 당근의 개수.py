t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    carrots = list(map(int, input().split()))
    answer = 1
    maxV = 0
    for i in range(1, n):
        if carrots[i] > carrots[i - 1]:
            answer += 1
        else:
            answer = 1
        if maxV < answer:
            maxV = answer
    print(f"#{tc} {maxV}")