t = int(input())

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

rd = 0
ld = 1
lu = 2
ru = 3

def travel(visited, dir, now):
    global answer

    if now == start and dir == ru:
        answer = max(answer, len(visited))
        return

    for d in range(2):
        dir += d

        if dir > 3:
            break

        nr = now[0] + dr[dir]
        nc = now[1] + dc[dir]

        if 0 <= nr < n and 0 <= nc < n and cafe_map[nr][nc] not in visited:
            visited.append(cafe_map[nr][nc])
            travel(visited, dir, (nr, nc))
            visited.remove(cafe_map[nr][nc])

for tc in range(1, t + 1):
    n = int(input())

    cafe_map = [list(map(int, input().split())) for _ in range(n)]
    answer = -1

    for i in range(n):
        for j in range(n):
            start = (i, j)
            visited = []
            travel(visited, 0, (i, j))

    print(f"#{tc} {answer}")