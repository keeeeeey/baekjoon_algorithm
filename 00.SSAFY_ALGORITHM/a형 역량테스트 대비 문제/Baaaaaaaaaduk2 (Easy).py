import sys
from copy import deepcopy

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(x, y, temp):
    cnt = 1
    flag = True
    q = []
    q.append([x, y])
    temp[x][y] = -1
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    flag = False
                elif temp[nx][ny] == 2:
                    cnt += 1
                    temp[nx][ny] = 1
                    q.append([nx, ny])
    if flag:
        return cnt
    else:
        return flag

def dfs(l):
    global answer
    if l == 2:
        temp = deepcopy(board)
        total = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    tmp = check(i, j, temp)
                    if not tmp:
                        pass
                    else:
                        total += tmp
        if total > answer:
            answer = total
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    dfs(l + 1)
                    board[i][j] = 0

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(0)
print(answer)