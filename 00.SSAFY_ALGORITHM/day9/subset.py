# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# for i in range(0, (1 << n)):    # 1 << n : 부분집합의 개수
#     for j in range(0, n):       # 원소의 수만큼 비트를 비교함
#         if i & (1 << j):        # i의 j번째 비트가 1이면 j번째 원소 출력
#             print(arr[j], end=" ")
#     print()

def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end=" ")
        print()
    else:
        bit[i] = 0
        f(i + 1, k)
        bit[i] = 1
        f(i + 1, k)

arr = [3, 6, 7]
n = len(arr)
bit = [1] * n
f(0, n)