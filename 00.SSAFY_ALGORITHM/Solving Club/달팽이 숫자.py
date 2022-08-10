dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    answer = [[0] * n for _ in range(n)]

    r, c = 0, 0
    d = 0

    for i in range(1, n * n + 1):
        answer[r][c] = i

        r = r + dx[d]
        c = c + dy[d]

        if r < 0 or r >= n or c < 0 or c >= n or answer[r][c] != 0:
            r = r - dx[d]
            c = c - dy[d]

            d = (d + 1) % 4

            r = r + dx[d]
            c = c + dy[d]

    print(f"#{tc}")
    for i in range(n):
        for j in range(n):
            print(answer[i][j], end=" ")
        print()