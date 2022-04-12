import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
N_list = sorted(list(map(int, input().split())))
first = N_list.pop()
second = N_list.pop()
cnt = 0
ans = 0
print(first, second)
while cnt < M:
    for _ in range(K):
        if cnt < M:
            ans += first
            cnt += 1
        else:
            break

    if cnt < M:
        ans += second
        cnt += 1
    else:
        break

print(ans)

