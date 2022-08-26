def dfs(l, temp, left, s):
    global answer
    if l == p - 1:
        if temp * left > answer:
            answer = temp * left
    else:
        for i in range(s, left + 1):
            temp *= i
            dfs(l + 1, temp, left - i, i)
            temp //= i

t = int(input())
for tc in range(1, t + 1):
    n, p = map(int, input().split())
    answer = 0
    dfs(0, 1, n, 2)
    print(answer)
