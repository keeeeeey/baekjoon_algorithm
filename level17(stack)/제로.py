import sys
N = int(input())
N_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
ans = []
sum_num = 0
for i in range(len(N_list)):
    if N_list[i] == 0:
        ans.pop()
    else:
        ans.append(N_list[i])
for i in range(len(ans)):
    sum_num += ans[i]
print(sum_num)