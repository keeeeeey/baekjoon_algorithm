N = int(input())
N_list = sorted(list(map(int, input().split())))
N_max = N_list[-1]
answer = 0

def sum():


for i in range(N_max + 1):
    for j in range(len(N_list)):
        if i == N_list[j]:
            break
        else:
