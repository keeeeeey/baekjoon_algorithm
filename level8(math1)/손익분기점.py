N = list(map(int, input().split(" ")))
a = N[2] - N[1]
if a <= 0:
    print("-1")
else:
    cnt = N[0] // a
    print(cnt + 1)