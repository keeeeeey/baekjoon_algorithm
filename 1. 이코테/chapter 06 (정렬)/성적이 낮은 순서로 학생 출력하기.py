N = int(input())
N_list = list(list(map(str, input().split())) for _ in range(N))
N_list = sorted(N_list, key=lambda x: x[1])
for i in range(N):
    print(N_list[i][0], end=" ")