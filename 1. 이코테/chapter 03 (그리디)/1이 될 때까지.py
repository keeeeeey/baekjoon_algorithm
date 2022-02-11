N, K = map(int, input().split())
cnt = 0
while N != 1:
    if N % K == 0:
        cnt += 1
        N /= K
    else:
        cnt += 1
        N -= 1
print(cnt)