t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    corridor = [0] * 401
    for _ in range(n):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        if start % 2 == 0:
            start -= 1
        if end % 2 == 1:
            end += 1
        for i in range(start, end + 1):
            corridor[i] += 1
    cnt = max(corridor)

    print(f"#{tc} {cnt}")
