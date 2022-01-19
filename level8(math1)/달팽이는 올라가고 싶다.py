N = list(map(int, input().split(" ")))
h = N[0] - N[1]
h2 = N[2] - N[0]
d = 0
if h2 % h == 0:
    d = h2 / h + 1
else:
    d = h2 // h + 2

print("{:.0f}".format(d))