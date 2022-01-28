N = list(map(int, input().split()))
N_queue = list(i for i in range(1, N[0] + 1))
ans_list = []
num = N[1] - 1
for i in range(N[0]):
    if num < len(N_queue):
        ans_list.append(N_queue.pop(num))
        num += N[1] - 1
    elif num >= len(N_queue):
        num = num % len(N_queue)
        ans_list.append(N_queue.pop(num))
        num += N[1] - 1

print("<", ', '.join(str(i) for i in ans_list), ">", sep = '')