N = int(input())
N_list = []
cnt = 0

a = [False, False] + [True]*(N - 1)

for i in range(2, N + 1):
  if a[i]:
    N_list.append(i)
    for j in range(2 * i, N + 1, i):
        a[j] = False

for i in range(len(N_list)):
    sum_num = 0
    for j in range(i, len(N_list)):
        sum_num += N_list[j]
        if sum_num == N:
            cnt += 1
        elif sum_num > N:
            break

print(cnt)