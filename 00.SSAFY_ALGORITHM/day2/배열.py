# 배열
# 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

# 6개의 변수를 하나의 배열로 바꾼 예시
Num0 = 0
Num1 = 1
Num2 = 2
Num3 = 3
Num4 = 4
Num5 = 0

Num = [0, 1, 2, 3, 4, 5]

# 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을
# 이용하여 자료에 접근하는 것은 매우 비효율적

# 배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있다.

# 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든
# 작업을 배열을 활용해 쉽게 할 수 있다.

# 1차원 배열의 선언
Arr = list()
Arr = []
Arr = [1, 2, 3]
Arr = [0] * 10 # 비어있는 배열

# 1차원 배열의 접근
Arr[0] = 10 # 배열 Arr의 0번 원소에 10을 저장하라
# Arr[idx] = 20 # 배열 Arr의 idx번 원소에 20을 저장하라

# 2차원 배열의 선언
# 1차원 List를 묶어놓은 List
# 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
# 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
# Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

# 배열 순회
# n X m 배열의 n * m 개의 모든 원소를 빠짐없이 조사하는 방법
Array = []
n = 3
m = 3

# 행 순회
for i in range(n):
    for j in range(m):
        Array[i][j]

# 열 순회
for j in range(m):
    for i in range(n):
        Array[i][j]

# 지그재그 순회
# 공식 쓰는 것보다 홀수열 짝수열 나누는게 나음
for i in range(n):
    for j in range(m):
        Array[i][j + (m-1-2*j) * (i%2)]

# 델타를 이용한 2차 배열 탐색
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(n):
    for j in range(m):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                pass

for i in range(n):
    for j in range(m):
        for di, dj in [[0, 1][0, -1][1, 0][-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= nx < n and 0 <= ny < m:
                pass

# 전치 행렬
arr = [[1, 2, 3][4, 5, 6][7, 8, 9]] # 3 * 3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
