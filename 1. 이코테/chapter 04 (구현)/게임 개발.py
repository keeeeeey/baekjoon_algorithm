import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = [[0] * M for _ in range(N)]
A, B, direction = map(int, input().split())
d[A][B] = 1

grid = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = A + dx[direction]
    ny = B + dy[direction]
    if d[nx][ny] == 0 and grid[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if grid[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)