dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(grid, k):
    answer = -1
    field = [list(map(str, grid[i].rstrip())) for i in range(len(grid))]
    n = len(grid)
    m = len(grid[0])
    location = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if field[nx][ny] == "." or field[nx][ny] == "F":
                        location[nx][ny] = 1



    return answer

solution(["..FF", "###F", "###."], 4)