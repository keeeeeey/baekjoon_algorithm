t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    bus_line = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    print(f"#{tc}", end=" ")
    for _ in range(p):
        c = int(input())
        cnt = 0
        for i in range(n):
            if bus_line[i][0] <= c <= bus_line[i][1]:
                cnt += 1
        print(cnt, end=" ")
    print()