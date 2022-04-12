from collections import deque
N, K = map(int, input().split())
N_list = deque(i for i in range(1, N + 1))
cnt = 1
result = []
while len(N_list) > 0:
    N_list.append(N_list.popleft())
    cnt += 1
    if cnt == 3:
        result.append(N_list.popleft())
        cnt = 1
print(result)
