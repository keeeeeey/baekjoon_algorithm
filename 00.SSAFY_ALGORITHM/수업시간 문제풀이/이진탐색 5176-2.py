def inorder(l):
    global i
    if 1 <= l <= n:
        inorder(l * 2)
        arr[l] = i
        i += 1
        inorder(l * 2 + 1)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [0] * (n + 1)
    i = 1
    inorder(1)
    print(f"#{tc} {arr[1]} {arr[n // 2]}")
