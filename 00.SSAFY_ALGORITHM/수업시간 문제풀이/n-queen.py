n = int(input())
answer = 0
row = [0] * n

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def dfs(x):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)

dfs(0)
print(answer)