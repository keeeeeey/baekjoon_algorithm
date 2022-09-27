from collections import deque

def mergesort(arr):
    if len(arr) == 1:
        return arr

    left_arr = deque()
    right_arr = deque()
    middle = len(arr) // 2

    for i in range(middle):
        left_arr.append(arr[i])
    for i in range(middle, len(arr)):
        right_arr.append(arr[i])

    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    global cnt
    result = deque()

    if left_arr[-1] > right_arr[-1]:
        cnt += 1

    while len(left_arr) > 0 or len(right_arr) > 0:
        if len(left_arr) > 0 and len(right_arr) > 0:
            if left_arr[0] <= right_arr[0]:
                result.append(left_arr.popleft())
            else:
                result.append(right_arr.popleft())
        elif len(left_arr) > 0:
            result.append(left_arr.popleft())
        elif len(right_arr) > 0:
            result.append(right_arr.popleft())

    return result

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    answer = mergesort(arr)

    print(f"#{tc} {answer[n // 2]} {cnt}")