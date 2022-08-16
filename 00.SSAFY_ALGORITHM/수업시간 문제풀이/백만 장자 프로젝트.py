t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [10001] + list(map(int, input().split()))
    answer = 0
    max_idx = n
    temp = 0
    cnt = 0
    for i in range(n, 0, -1):
        if arr[max_idx] >= arr[i - 1]:
            cnt += 1
            temp += arr[i - 1]
        else:
            if arr[max_idx] * cnt - temp > 0:
                answer += arr[max_idx] * cnt - temp
            max_idx = i - 1
            temp = 0
            cnt = 0
    print(f"#{tc} {answer}")

# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2