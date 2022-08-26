from copy import deepcopy

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(l):
    global answer
    if l == k:
        temp = deepcopy(a)
        for i in range(k):
            r, c, s = rotation[ch[i]]
            for j in range(s):
                top = [r - s + j - 1, c - s + j - 1]
                bottom = [r + s - j - 1, c + s - j - 1]
                nx, ny = top
                tmp = temp[nx][ny]

                for d in range(4):
                    while True:
                        nx = nx + dx[d]
                        ny = ny + dy[d]
                        if not (nx >= top[0] and nx <= bottom[0] and ny >= top[1] and ny <= bottom[1]):
                            nx = nx - dx[d]
                            ny = ny - dy[d]
                            break
                        tmp, temp[nx][ny] = temp[nx][ny], tmp

        for i in range(n):
            sum = 0
            for j in range(m):
                sum += temp[i][j]
            if sum < answer:
                answer = sum
    else:
        for i in range(k):
            if ch[i] == -1:
                ch[i] = l
                dfs(l + 1)
                ch[i] = -1

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
rotation = [list(map(int, input().split())) for _ in range(k)]
ch = [-1] * k
answer = 100 * m
dfs(0)
print(answer)