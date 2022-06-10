import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s_list = [deque(map(str, input().rstrip())) for _ in range(7)]

for s in s_list:
    cnt = 0
    while s:
        if s[0] == s[-1]:
            s.popleft()
            s.pop()
        else:
            if cnt > 1:
                break

            if s[0] == s[-2]:
                s.pop()
                cnt += 1
            elif s[1] == s[-1]:
                s.popleft()
                cnt += 1
            else:
                break

    if s:
        print(2)
    else:
        if cnt == 0:
            print(0)
        elif cnt == 1:
            print(1)