N = int(input())
N_list = sorted(list(map(int, input().split())))
i = 0
j = N - 1
max_num = 2e+9+1
result = []

while i < j:
    sum_num = N_list[i] + N_list[j]

    if abs(sum_num) < max_num:
        max_num = abs(sum_num)
        result = [N_list[i], N_list[j]]

    if sum_num < 0:
        i += 1
    else:
        j -= 1

print(result[0], result[1])