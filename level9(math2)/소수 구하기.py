# 시간 초과

N = list(map(int, input().split(" ")))
for n in range(N[0], N[1] + 1):
    b = True
    if n != 1:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                b = False
        if b == True:
            print(n)

N = list(map(int, input().split(" ")))
for n in range(N[0], N[1] + 1):
    for i in range(2, n + 1):
        if n % i == 0:
            if n == i:
                print(i)
            else:
                break