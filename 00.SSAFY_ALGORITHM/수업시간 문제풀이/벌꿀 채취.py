def perm(l, x, y):
    global honey
    if l == m:
        temp = 0
        bottle = c
        for i in range(m):
            if honey_box[x][y + ch[i]] <= bottle:
                bottle -= honey_box[x][y + ch[i]]
                temp += honey_box[x][y + ch[i]] ** 2
        honey = max(honey, temp)
    else:
        for i in range(m):
            if i not in ch:
                ch[l] = i
                perm(l + 1, x, y)
                ch[l] = -1

def check(x, y):
    flag = True
    for i in range(m):
        if visited[x][y + i] == 1:
            flag = False
            break
    return flag

t = int(input())
for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    honey_box = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    honey_max = [[0] * (n - m + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n - m + 1):
            honey = 0
            ch = [-1] * m
            perm(0, i, j)
            honey_max[i][j] = honey

    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n - m + 1):
            for z in range(m):
                visited[i][j + z] = 1

            for k in range(i, n):
                for s in range(n - m + 1):
                    if check(k, s):
                        answer = max(answer, honey_max[i][j] + honey_max[k][s])

            for z in range(m):
                visited[i][j + z] = 0

    print(f"#{tc} {answer}")