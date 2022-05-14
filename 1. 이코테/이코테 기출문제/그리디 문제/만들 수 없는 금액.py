N = int(input())
N_list = sorted(list(map(int, input().split())))
answer = 1
print(N_list)
for i in range(N):
    if answer < N_list[i]:
        break
    answer += N_list[i]

print(answer)
