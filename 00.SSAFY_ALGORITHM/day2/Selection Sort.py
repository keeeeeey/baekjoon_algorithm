# 선택 정렬(Selection Sort)
# 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

# 정렬 과정
# 주어진 리스트 중에서 최소값을 찾는다.
# 그 값을 리스트의 맨 앞에 위치한 값과 교한한다.
# 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

# 시간 복잡도
# O(n^2)

def selectionSort(a, N):
    for i in range(N - 1):
        minIdx = i
        for j in range(i + 1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]

arr = [7, 2, 5, 3, 4, 6]
N = len(arr)
selectionSort(arr, N)
print(arr)

# 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.
# 파라미터(N)을 k로 주면 가능
# 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.