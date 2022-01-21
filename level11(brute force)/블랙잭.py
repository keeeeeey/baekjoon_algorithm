T = list(map(int, input().split(" ")))
N = list(map(int, input().split(" ")))
n_list = []
for i in range(0, len(N) - 2):
    for j in range(i + 1, len(N) - 1):
        for k in range(j + 1, len(N)):
            if N[i] + N[j] + N[k] <= T[1]:
                n_list.append(N[i] + N[j] + N[k])
print(max(n_list))