T = int(input())
for t in range(1, T + 1):
    sum_score = 0
    sum_avg = 0
    count = 0
    N = list(map(int, input().split(" ")))
    for i in range(1, len(N)):
        sum_score += N[i]
    sum_avg = sum_score / N[0]
    for i in range(1, len(N)):
        if N[i] > sum_avg:
            count += 1
    percent = count / N[0] * 100
    print("{:.3f}%".format(percent))