import sys
input = sys.stdin.readline
N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    left = 0
    right = len(N_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] > i:
            right = mid - 1
        elif N_list[mid] < i:
            left = mid + 1
        else:
            print(1)
            break
    if left > right:
        print(0)
