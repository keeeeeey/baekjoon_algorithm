N = int(input())
N_list = sorted(list(map(int, input().split())))

answer = 0
answer_list = []

for i in range(N):
    answer_list.append(N_list[i])
    if max(answer_list) == len(answer_list):
        answer += 1
        answer_list.clear()

print(answer)