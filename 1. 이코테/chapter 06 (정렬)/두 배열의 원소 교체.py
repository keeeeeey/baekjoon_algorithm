N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

while K > 0:
    for i in range(N):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
            K -= 1

print(sum(A))

