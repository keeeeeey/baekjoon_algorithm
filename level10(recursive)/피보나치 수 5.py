N = int(input())
n_list = [0, 1]
for i in range(2, N + 1):
    n_list.append(n_list[i - 1] + n_list[i - 2])
print(n_list[N])