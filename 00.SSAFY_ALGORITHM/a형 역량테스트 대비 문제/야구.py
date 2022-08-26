import sys
input = sys.stdin.readline
def dfs(cnt):
    global answer
    if cnt == 9:
        start, score = 0, 0
        for inning in arr:
            out, b1, b2, b3 = 0, 0, 0, 0
            while out <= 2:
                p = select[start]
                if inning[p] == 0:
                    out += 1
                elif inning[p] == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[p] == 2:
                    score += b3 + b2
                    b1, b2, b3 = 0, 1, b1
                elif inning[p] == 3:
                    score += b3 + b2 + b1
                    b1, b2, b3 = 0, 0, 1
                else:
                    score += b3 + b2 + b1 + 1
                    b1, b2, b3 = 0, 0, 0

                start += 1
                start %= 9

        if score > answer:
            answer = score

    for i in range(9):
        if c[i]:
            continue
        c[i] = 1
        select[i] = cnt
        dfs(cnt + 1)
        c[i] = 0
        select[i] = 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
select = [0 for _ in range(9)]
c = [0 for _ in range(9)]
select[3] = 0
c[3] = 1
answer = 0
dfs(1)
print(answer)