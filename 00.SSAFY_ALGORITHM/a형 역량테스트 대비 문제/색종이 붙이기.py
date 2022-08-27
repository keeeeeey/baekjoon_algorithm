def check(x, y, n):
    for nx in range(x, x + n):
        for ny in range(y, y + n):
            if nx < 0 or nx >= 10 or ny < 0 or ny >= 10 or paper[nx][ny] != 1:
                return False
    return True

def back_tracking(x, y, cnt):
    global answer
    if x >= 10:
        answer = min(answer, cnt)
        return

    if y >= 10:
        back_tracking(x + 1, 0, cnt)
        return

    if paper[x][y] == 1:
        for k in range(1, 6):
            if paper_dict[k] == 0:
                continue

            flag = check(x, y, k)

            if flag:
                for i in range(x, x + k):
                    for j in range(y, y + k):
                        paper[i][j] = 0
                paper_dict[k] -= 1
                back_tracking(x, y + k, cnt + 1)
                paper_dict[k] += 1
                for i in range(x, x + k):
                    for j in range(y, y + k):
                        paper[i][j] = 1
    else:
        back_tracking(x, y + 1, cnt)



paper = [list(map(int, input().split())) for _ in range(10)]
paper_dict = {1 : 5, 2 : 5, 3 : 5, 4 : 5, 5 : 5}
answer = 26
back_tracking(0, 0, 0)

if answer == 26:
    print(-1)
else:
    print(answer)


# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0