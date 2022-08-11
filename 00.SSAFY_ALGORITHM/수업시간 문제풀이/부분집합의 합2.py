def dfs(n, l, subset):
    if l == n + 1:
        subset_list.append(subset)
        print(subset_list)
    else:
        subset.append(l)
        dfs(n, l + 1, subset)
        subset.pop()
        dfs(n, l + 1, subset)

t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    subset_list = []
    subset = []
    dfs(n, 1, subset, subset_list)
    answer = 0

    # print(f"#{tc} {subset}")