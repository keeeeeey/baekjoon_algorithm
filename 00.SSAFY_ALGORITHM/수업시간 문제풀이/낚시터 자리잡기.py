def permutation(l, temp):
    if l == 3:
        fish(temp)
    else:
        for i in range(3):
            if ch[i] == 0:
                ch[i] = 1
                temp.append(i)
                permutation(l + 1, temp)
                ch[i] = 0
                temp.pop()

def fish(temp):
    global answer
    for t in temp:
        cnt = 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(3)]

    ch = [0] * 3
    answer = 0
    place = [0] * (n + 1)

    permutation(0, [])

