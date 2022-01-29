from collections import deque
T = list(map(int, input().split()))
N = list(map(int, input().split()))
N_list = deque(i for i in range(1, T[0] + 1))
cnt = 0
for i in range(T[1]):
    if N_list.index(N[i]) > len(N_list) - 1 - N_list.index(N[i]):
        for _ in range(len(N_list) - N_list.index(N[i])):
            N_list.appendleft(N_list.pop())
            cnt += 1
        N_list.popleft()
    else:
        for _ in range(N_list.index(N[i])):
            N_list.append(N_list.popleft())
            cnt += 1
        N_list.popleft()
print(cnt)