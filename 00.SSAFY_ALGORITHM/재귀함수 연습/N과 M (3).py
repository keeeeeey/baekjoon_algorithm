def recursive(l):
    if l == m:
        for i in range(m):
            print(n_list[i], end=" ")
        print()
    else:
        for i in range(1, n + 1):
            n_list[l] = i
            recursive(l + 1)
            n_list[l] = 0

n, m = map(int, input().split())
n_list = [0] * (m)
recursive(0)