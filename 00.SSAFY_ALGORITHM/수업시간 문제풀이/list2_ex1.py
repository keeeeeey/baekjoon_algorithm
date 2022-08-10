N = 3 # 행
M = 4 # 열

# N개의 원소를 갖는 0으로 초기화된 1차원 배열
arr1 = [0] * N
print(arr1)

# 크기가 N x M 이고 0으로 초기화된 2차원 배열
# arr2 = [[0] * M] * N
arr2 = [[0] * M for _ in range(N)]
print(arr2)

arr3 = [[1], [2, 3], [4, 5, 6]]