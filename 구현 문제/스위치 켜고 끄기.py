import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

status = [0]
for s in map(int, input().split()):
    status.append(s)
student = int(input())



for _ in range(student):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(1, n + 1):
            if i % num == 0:
                if status[i] == 1:
                    status[i] = 0
                elif status[i] == 0:
                    status[i] = 1
    elif gender == 2:
        num_plus = num + 1
        num_minus = num - 1

        if status[num] == 1:
            status[num] = 0
        elif status[num] == 0:
            status[num] = 1

        while True:
            if num_plus > n or num_minus < 1:
                break

            if status[num_plus] == status[num_minus]:
                if status[num_plus] == 1:
                    status[num_plus] = 0
                    status[num_minus] = 0
                elif status[num_plus] == 0:
                    status[num_plus] = 1
                    status[num_minus] = 1
            else:
                break

            num_plus += 1
            num_minus -= 1


for i in range(1, n + 1):
    if i % 20 == 0:
        print(status[i])
    else:
        print(status[i], end=" ")