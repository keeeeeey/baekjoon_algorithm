dict = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "h":7, "i":8}
x, y = map(str, input())
x = dict[x]
dx = [2, -2, 2, -2, 1, -1, 1, -1]
dy = [1, 1, -1, -1, 2, 2, -2, -2]
cnt = 0
for i in range(8) :
    nx = x + dx[i]
    ny = int(y) + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1
print(cnt)
