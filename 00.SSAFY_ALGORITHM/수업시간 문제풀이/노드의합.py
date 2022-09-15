def postorder(l):
    if 1 <= l <= n:
        postorder(l * 2)
        postorder(l * 2 + 1)
        if arr[l] == 0:
            if l * 2 + 1 <= n:
                arr[l] = arr[l * 2] + arr[l * 2 + 1]
            else:
                arr[l] = arr[l * 2]

t = int(input())
for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    arr = [0] * (n + 1)
    for _ in range(m):
        node, value = map(int, input().split())
        arr[node] = value
    postorder(1)
    print(f"#{tc} {arr[l]}")