board = [list(map(str, input().strip())) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == "F":
            if i % 2 == 0 and j % 2 == 0:
                cnt += 1
            elif i % 2 == 1 and j % 2 == 1:
                cnt += 1

print(cnt)