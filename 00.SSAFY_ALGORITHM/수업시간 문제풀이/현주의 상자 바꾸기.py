t = int(input())
for tc in range(1, t + 1):
    n, q = map(int, input().split())
    boxes = [0] * (n + 1)
    for i in range(1, q + 1):
        start, end = map(int, input().split())
        for j in range(start, end + 1):
            boxes[j] = i
    print(f"#{tc}", end=" ")
    for i in range(1, n + 1):
        print(boxes[i], end=" ")
    print()
