import sys
from collections import deque
T = int(input())
queue = deque()
for _ in range(T):
    q_list = list(map(str, sys.stdin.readline().split()))
    if q_list[0] == "push":
        queue.append(q_list[1])
    elif q_list[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif q_list[0] == "size":
        print(len(queue))
    elif q_list[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif q_list[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif q_list[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)