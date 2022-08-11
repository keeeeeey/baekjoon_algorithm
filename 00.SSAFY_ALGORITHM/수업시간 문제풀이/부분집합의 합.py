t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = list(range(1, 13))
    answer = 0
    for i in range(1<<12):
        subset_sum = 0
        cnt = 0
        for j in range(12):
            if i & (1<<j):
                subset_sum += arr[j]
                cnt += 1
        if cnt == n and subset_sum == k:
            answer += 1

    print(f"#{tc} {answer}")
