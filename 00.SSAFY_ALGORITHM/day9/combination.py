# N = 10
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             print(i, j, k)

# def nCr(n, r, s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n - r + 1):
#             comb[r - 1] = A[i]
#             nCr(n, r - 1, i + 1)
#
A = [1, 2, 3, 4, 5]
n = len(A)
r = 3
comb = [0] * r
# nCr(n, r, 0)

def combination(l, s):
    if l == r:
        print(*comb)
    else:
        for i in range(s, n + 1):
            if i not in comb:
                comb[l] = i
                combination(l + 1, i)

combination(0, 1)