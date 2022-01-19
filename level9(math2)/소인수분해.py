N = int(input())
n_list = []
if N > 1:
    for i in range(2, N + 1):
        while N % i == 0:
            N /= i
            n_list.append(i)
for n in n_list:
    print(n)