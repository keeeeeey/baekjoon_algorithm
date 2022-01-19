N = list(map(int, input().split(" ")))
n_list = [N[0], N[1], N[2] - N[0], N[3] - N[1]]
ans = min(n_list)
print(ans)