N = list(map(str, input().split(" ")))
N[0] = N[0][::-1]
N[1] = N[1][::-1]
if N[0] > N[1]:
    print(N[0])
else:
    print(N[1])