def perm(n, k):
    if n == k:
        print(p)
    else:
        for i in range(1, k + 1):
            if i not in p:
                p[n] = i
                perm(n + 1, k)
                p[n] = 0

p = [0] * 4
perm(0, 4)

# def f(i, k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i + 1, k)
#             p[i], p[j] = p[j], p[i]
#
# p = [1, 2, 3]
# f(0, 3)

# def f(i, k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j] 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 f(i + 1, k)         # p[i + 1] 값을 결정하러 이동
#                 used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제
#
# N = 3
# a = [i for i in range(1, N + 1)]
# used = [0] * N
# p = [0] * N
# f(0, N)