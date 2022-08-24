q = []
n = 1000000 # 마이쮸의 개수
m = 0 # 지금까지 나눠준 마이쮸의 개수
p = 1 # 마이쮸를 나눠주기 시작할 사람의 번호
v = 0 # 마지막에 받는 사람이 누군지?

while m < n:
    q.append((p, 1, 0))     # 마이쮸를 받을 사람을 줄에 세운다. (번호표 주기)
    v, c, my = q.pop(0)
    m += c
    q.append((v, c + 1, my + c))
    p += 1

from collections import deque

# dequeue 를 이용해서 ㄱ ㅜ현해보기
p = 1
q = deque()
n = 1000000
m = 0
v = 0

while m < n:
    q.append((p, 1, 0))
    v, c, my = q.popleft()
    m += c
    q.append((v, c + 1, my + c))
    p += 1