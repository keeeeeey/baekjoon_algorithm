def inorder(node):
    if 0 < node <= n:
        inorder(ch1[node])
        print(arr[node], end="")
        inorder(ch2[node])

for tc in range(1, 11):
    n = int(input())
    arr = [0] * (n + 1)
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)
    for _ in range(n):
        info = list(input().split())
        # arr[int(info[0])].append(info[1])
        arr[int(info[0])] = info[1]
        if len(info) == 3:
            ch1[int(info[0])] = int(info[2])
        elif len(info) == 4:
            ch1[int(info[0])] = int(info[2])
            ch2[int(info[0])] = int(info[3])
    print(f"#{tc} ", end="")
    inorder(1)
    print()