# 정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
# 배열이 0이 아닌 1부터 시작하는 것으로 한다.
# 이미 오름차순으로 정렬된 배열이 입력값으로 주어진다.

# def twoSum(numbers, target):
#     i = 0 # 시작 인덱스 값
#     j = len(numbers) - 1 # 끝 인덱스 값
#     while i < j: # i 와 j가 만날때 while문 종료
#         if numbers[i] + numbers[j] > target:
#             j -= 1
#         elif numbers[i] + numbers[j] < target:
#             i += 1
#         else:
#             return [i + 1, j + 1]
#
# twoSum([2,7,11,15], 9)

# def twoSum_binarySearch(numbers, target):
#     for i in range(len(numbers)):
#         ans = target - numbers[i]
#         def bs(start, end):
#             if start > end:
#                 return - 1
#
#             mid = (start + end) // 2
#             if numbers[mid] > ans:
#                 return bs(start, mid - 1)
#             elif numbers[mid] < ans:
#                 return bs(mid + 1, end)
#             else:
#                 return mid
#
#         N = bs(i + 1, len(numbers) - 1)
#
#         if N == -1:
#             continue
#         else:
#             return [i + 1, N + 1]
#
# print(twoSum_binarySearch([1,2,3,4,4,9,56,90], 8))

def twoSum_binarySearch(numbers, target):
    for i in range(len(numbers)):
        left, right = i + 1, len(numbers) - 1
        expected = target - numbers[i]
        # 이진 검색으로 나머지 값 판별
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] < expected:
                left += mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return i + 1, mid + 1

print(twoSum_binarySearch([1,2,3,4,4,9,56,90], 8))