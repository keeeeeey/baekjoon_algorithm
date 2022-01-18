T = int(input())
sum = 0
for t in range(1, T + 1):
    N = list(map(int, input().split(" ")))
    sum = N[0] + N[1]
    print("Case #{}: {}".format(t, sum))