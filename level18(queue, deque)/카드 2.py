from collections import deque
N = int(input())
N_queue = deque(i for i in range(1, N + 1))
while len(N_queue) > 1:
    N_queue.popleft()
    N_queue.append(N_queue.popleft())
print(N_queue[0])