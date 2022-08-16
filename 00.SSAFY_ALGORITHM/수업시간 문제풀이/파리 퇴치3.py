dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    fly_arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            for z in range(2):
                max_catch = fly_arr[i][j]
                for k in range(4):
                    for s in range(1, m):
                        nx = i + dx[k + 4 * z] * s
                        ny = j + dy[k + 4 * z] * s
                        if 0 <= nx < n and 0 <= ny < n:
                            max_catch += fly_arr[nx][ny]
                if max_catch > answer:
                    answer = max_catch
    print(f"#{tc} {answer}")