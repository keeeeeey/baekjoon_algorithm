import sys
n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
cnt = 0
i = 0
j = len(n_list) - 1
while i != j:
    if n_list[i] + n_list[j] > x:
        j -= 1
    elif n_list[i] + n_list[j] < x:
        i += 1
    elif n_list[i] + n_list[j] == x:
        cnt += 1
        i += 1
print(cnt)