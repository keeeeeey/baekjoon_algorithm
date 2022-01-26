import sys
T = int(input())
N = list(map(int, sys.stdin.readline().split()))

for i in range(T - 1):
    for j in range(i + 1, T):
        max_num = N[i]
        if N[j] > max_num:
            max_num = N[j]
            print(max_num, end=" ")
            break
    if max_num == N[i]:
        print(-1, end=" ")
print(-1, end=" ")