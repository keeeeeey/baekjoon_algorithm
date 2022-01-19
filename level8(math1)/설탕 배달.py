N = int(input())
cnt = 0
if N < 5:
    if N % 3 == 0 :
        print(1)
    else:
        print(-1)
else:
    if N % 5 == 3 or N % 5 == 1:
        cnt = N // 5 + 1
        print(cnt)
    elif N % 5 == 2 or N % 5 == 4:
        if N == 7:
            print(-1)
        else:
            cnt = N // 5 + 2
            print(cnt)
    elif N % 5 == 0:
        cnt = N // 5
        print(cnt)