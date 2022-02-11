import sys
input = sys.stdin.readline

def f():
    N, M, K = map(int, input().split())
    N_list = sorted(list(map(int, input().split())), reverse=True)

    result = 0
    k = 0
    first = N_list[0]
    second = N_list[1]
    while True:
        if k < K:
            result += first
            k += 1
        else:
            result += second
            k = 0

        M -= 1

        if M == 0:
            return result


print(f())
