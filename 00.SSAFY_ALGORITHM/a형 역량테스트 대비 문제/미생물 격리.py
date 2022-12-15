dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

def move():
    temp = list([[] for _ in range(n)] for _ in range(n))

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                nx = i + dx[arr[i][j][0][1]]
                ny = j + dy[arr[i][j][0][1]]
                if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                    if nx == 0:
                        temp[nx][ny].append([arr[i][j][0][0] // 2, 1])
                    elif nx == n - 1:
                        temp[nx][ny].append([arr[i][j][0][0] // 2, 0])
                    elif ny == 0:
                        temp[nx][ny].append([arr[i][j][0][0] // 2, 3])
                    elif ny == n - 1:
                        temp[nx][ny].append([arr[i][j][0][0] // 2, 2])
                else:
                    temp[nx][ny].append([arr[i][j][0][0], arr[i][j][0][1]])

    for i in range(n):
        for j in range(n):
            if temp[i][j]:
                temp[i][j].sort(key=lambda x: -x[0])
                sum = 0
                for tmp in temp[i][j]:
                    sum += tmp[0]
                arr[i][j] = [[sum, temp[i][j][0][1]]]
            else:
                arr[i][j] = temp[i][j]

for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    arr = list([[] for _ in range(n)] for _ in range(n))

    for _ in range(k):
        x, y, num, dir = map(int, input().split())
        arr[x][y].append([num, dir - 1])

    for _ in range(m):
        move()

    answer = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                answer += arr[i][j][0][0]

    print(f"#{tc} {answer}")