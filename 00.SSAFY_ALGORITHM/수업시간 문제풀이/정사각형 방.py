dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y):
    cnt = 1
    temp = board[x][y]
    q = [(x, y)]
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == board[x][y] + 1:
                cnt += 1
                q.append((nx, ny))
                break
    return cnt, temp

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    room = 0
    for i in range(n):
        for j in range(n):
            cnt, temp = move(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                room = temp
            elif max_cnt == cnt:
                if room > temp:
                    room = temp
    print(f"#{tc} {room} {max_cnt}")