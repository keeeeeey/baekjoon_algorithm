import sys
input = sys.stdin.readline

def direction(head, tail):
    dx, dy, l = [], [], 0
    if head[0] == tail[0]:
        dx = [0, 1]
        dy = [1, 1]
        l = 2
    elif head[1] == tail[1]:
        dx = [1, 1]
        dy = [0, 1]
        l = 2
    elif head[0] != tail[0] and head[1] != tail[1]:
        dx = [1, 0, 1]
        dy = [0, 1, 1]
        l = 3

    return dx, dy, l

def dfs(head, tail):
    global answer
    dx, dy, l = direction(head, tail)

    for d in range(l):
        nx = head[0] + dx[d]
        ny = head[1] + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if dx[d] == dy[d]:
                if room[nx][ny] == 0 and room[nx - 1][ny] == 0 and room[nx][ny - 1] == 0:
                    if nx == n - 1 and ny == n - 1:
                        answer += 1
                        return
                    dfs([nx, ny], head)
            else:
                if room[nx][ny] == 0:
                    if nx == n - 1 and ny == n - 1:
                        answer += 1
                        return
                    dfs([nx, ny], head)

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs([0, 1], [0, 0])
print(answer)