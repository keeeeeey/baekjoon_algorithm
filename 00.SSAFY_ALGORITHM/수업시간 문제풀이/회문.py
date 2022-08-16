t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    answer = ""
    for i in range(n):
        for j in range(n - m + 1):
            flag = True
            start = 0
            for k in range(m // 2):
                if arr[i][j + k] != arr[i][j + m - k - 1]:
                    flag = False
                    break
            if flag:
                start = j
                for s in range(start, start + m):
                    answer += arr[i][s]
                break

            flag = True
            start = 0
            for k in range(m // 2):
                if arr[j + k][i] != arr[j + m - k - 1][i]:
                    flag = False
                    break
            if flag:
                start = j
                for s in range(start, start + m):
                    answer += arr[s][i]
                break
    print(f"#{tc} {answer}")