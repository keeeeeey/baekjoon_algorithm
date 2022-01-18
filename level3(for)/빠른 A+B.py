import sys
T = int(sys.stdin.readline())
sum = 0
for t in range(1, T + 1):
    N = list(map(int, sys.stdin.readline().split(" ")))
    sum = N[0] + N[1]
    print(sum)