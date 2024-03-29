# 카운팅 정렬(Counting Sort)
# 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여
# 선형 시간에 정렬하는 효율적인 알고리즘

# 시간 복잡도
# O(n + k) : n은 리스트 길이, k는 정수의 최대값

# 제한 사항
# 정수나 정수로 표현할 수 있느 자료에 대해서만 적용가능
# 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
# 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.

# 통상 백만까지만 사용함

def Counting_Sort(A, B, k):
    # A[] -- 입력 배열(1 to k)
    # B[] -- 정렬된 배열.
    # C[] -- 카운트 배열.
    C = [0] * (k + 1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range((len(B) - 1, -1, -1)): # 뒤에서 부터 조회하는 이유? : stable한 정렬을 하기 위해 -> 정렬된 후에도 중복된 숫자의 순서를 유지하기 위해서
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]