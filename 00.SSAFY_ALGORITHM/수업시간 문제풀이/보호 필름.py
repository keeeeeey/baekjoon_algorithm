from copy import deepcopy

def subset(l, c):
    global answer
    if k == 1:
        answer = 0
        return

    if l == d:
        if c // 2 >= answer:
            return

        if check_films():
            answer = min(answer, c // 2)
    else:
        ch[l] = -1
        subset(l + 1, c - 1)
        ch[l] = 0
        subset(l + 1, c + 1)
        ch[l] = 1
        subset(l + 1, c + 1)

def check_films():
    temp = []
    for i in range(len(ch)):
        if ch[i] == 0:
            temp.append([i, films[i]])
            films[i] = [0] * w
        elif ch[i] == 1:
            temp.append([i, films[i]])
            films[i] = [1] * w

    flag = True
    for i in range(w):
        cnt = 1
        for j in range(1, d):
            if films[j][i] == films[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt == k:
                break

        if cnt != k:
            flag = False
            break

    for tmp in temp:
        films[tmp[0]] = tmp[1]

    return flag

t = int(input())
for tc in range(1, t + 1):
    d, w, k = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(d)]
    ch = [1] * d
    answer = d
    subset(0, d)
    print(f"#{tc} {answer}")