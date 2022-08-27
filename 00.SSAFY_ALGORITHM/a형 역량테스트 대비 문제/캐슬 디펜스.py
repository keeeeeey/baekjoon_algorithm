def dfs(l, s):
    global answer
    if l == 3:
        temp = 0
        x = n
        ch = [[0] * m for _ in range(n)]
        while x > 0:
            for j in range(m):
                shoot = [0] * m
                flag = True
                for i in range(x - 1, -1, -1):
                    for k in range(m):
                        if grid[i][j] == 1 and position[k] == 1:
                            if abs(x - i) + abs(k - j) <= d:
                                if ch[i][j] == 0:
                                    if shoot[k] == 0:
                                        temp += 1
                                        ch[i][j] = 1
                                        shoot[k] = 1
                                else:
                                    if shoot[k] == 0:
                                        shoot[k] = 1
                            else:
                                if k == j:
                                    flag = False
                                    break
                if not flag:
                    break
            x -= 1

        if temp > answer:
            answer = temp
    else:
        for i in range(s, m):
            if position[i] == 0:
                position[i] = 1
                dfs(l + 1, i)
                position[i] = 0

n, m, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
position = [0] * m
answer = 0
dfs(0, 0)
print(answer)