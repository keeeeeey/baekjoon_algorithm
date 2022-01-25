import sys

T = int(input())
N = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))

max_ans, min_ans = -sys.maxsize - 1, sys.maxsize

def dfs(total, idx, add, sub, mul, div):
    global max_ans, min_ans
    if idx == T:
        max_ans = max(max_ans, total)
        min_ans = min(min_ans, total)
        return

    if add > 0:
        dfs(total + N[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        dfs(total - N[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        dfs(total * N[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        dfs(int(total / N[idx]), idx + 1, add, sub, mul, div - 1)

    return max_ans, min_ans

if __name__ == "__main__":
    dfs(N[0], 1, S[0], S[1], S[2], S[3])
    print(max_ans)
    print(min_ans)