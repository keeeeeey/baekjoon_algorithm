def find_palindrome(N, arr):
    ans = ''
    for n in range(100):
        for s in range(n+1):
            for r in range(N):
                flag = True
                M = N - n

                for idx1 in range(M // 2):
                    start = s + idx1
                    end = s + M - 1 - idx1
                    if arr[r][start] != arr[r][end]:
                        flag = False
                        break
                if flag:
                    return len(arr[r][s:s + M])

                flag = True
                for idx2 in range(M // 2):
                    start = s + idx2
                    end = s + M - 1 - idx2
                    if arr[start][r] != arr[end][r]:
                        flag = False
                        break
                if flag:
                    for i in range(M):
                        ans += arr[s+i][r]
                    return len(ans)


for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    print(f"#{tc} {find_palindrome(100, arr)}")