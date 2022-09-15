def inorder(i, l):
    if 1 <= l <= n:
        inorder(i, l * 2)
        if arr[l] == 0 and i not in arr:
            arr[l] = i
            return
        inorder(i, l * 2 + 1)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        inorder(i, 1)
    print(f"#{tc} {arr[1]} {arr[n // 2]}")
