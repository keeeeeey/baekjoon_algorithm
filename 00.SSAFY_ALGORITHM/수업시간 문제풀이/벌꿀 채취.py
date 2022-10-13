t = int(input())
for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    honey_box = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    print(f"#{tc} {answer}")