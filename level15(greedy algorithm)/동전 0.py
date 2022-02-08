import sys
input = sys.stdin.readline
N, K = map(int, input().split())
N_list = list(int(input()) for _ in range(N))
cnt = 0
while K > 0:
    M = N_list.pop()
    if M <= K:
        A = K // M
        cnt += A
        K -= M * A
print(cnt)
