def do_sum_num(n: int):
    sum_num = 0
    for i in range(0, len(str(n))):
        sum_num += int(str(n)[i])
    return sum_num

N = int(input())
n_list = []
for i in range(1, N):
    if do_sum_num(i) + i == N:
        print(i)
        n_list.append(i)
        break
if not n_list:
    print(0)
