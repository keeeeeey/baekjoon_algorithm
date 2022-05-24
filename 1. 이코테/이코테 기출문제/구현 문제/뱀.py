N = int(input())
K = int(input())
K_list = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
L_list = [list(map(str, input().split())) for _ in range(K)]
grid = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(K):
    x = K_list[i][0]
    y = K_list[i][1]
    grid[x][y] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    grid[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= N and 1 <= ny and ny <= N and grid[nx][ny] != 2:
            if grid[nx][ny] == 0:
                grid[nx][ny] == 2
                q.append((nx, ny))
                px, py = q.pop(0)
                grid[px][py] = 0
            else:
                grid[nx][ny] == 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == int(L_list[index][0]):
            direction = turn(direction, L_list[index][1])
            index += 1
    return time

print(simulate())