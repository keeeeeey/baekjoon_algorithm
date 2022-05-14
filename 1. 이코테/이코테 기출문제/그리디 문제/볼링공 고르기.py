N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))
answer = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if N_list[i] == N_list[j]:
            continue
        answer += 1

print(answer)
