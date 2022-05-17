key = list(list(map(int, input().split())) for _ in range(3))
lock = list(list(map(int, input().split())) for _ in range(3))
for i in range(len(lock)):
    for j in range(len(lock[0])):
        if lock[i][j] == 1:
            continue
