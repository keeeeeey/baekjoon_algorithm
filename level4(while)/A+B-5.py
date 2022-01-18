while True:
    N = list(map(int, input().split(" ")))
    if N[0] == 0 and N[1] == 0:
        break;
    print(N[0] + N[1])