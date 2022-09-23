def janghoon(l):
    global answer
    if l == n:
        temp = sum(ch) - b
        if temp < 0:
            return
        answer = min(answer, temp)
    else:
        ch[l] = heights[l]
        janghoon(l + 1)
        ch[l] = 0
        janghoon(l + 1)

t = int(input())
for tc in range(1, t + 1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = sum(heights)
    ch = [0] * n
    janghoon(0)
    print(f"#{tc} {answer}")