T = int(input())
N = list(map(int, input().split(" ")))
cnt = 0
for n in range(len(N)):
    b = True
    if N[n] == 1:
        b = False
    else:
        for i in range(2, N[n] // 2 + 1):
            if N[n] % i == 0:
                b = False
    if b == True:
        cnt += 1
print(cnt)