import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)
time = 0
while trucks:
    bridge.popleft()
    bridge.append(0)
    time += 1
    if trucks[0] + sum(bridge) <= l and bridge[-1] == 0:
        bridge[-1] = trucks.popleft()

print(time + w)

