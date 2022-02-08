import sys
T = int(input())
N = list(map(int, sys.stdin.readline().split()))
ans = [-1] * T
stack = []
stack.append(0)
for i in range(1, T):
    while stack and N[stack[-1]] < N[i]:
        ans[stack[-1]] = N[i]
        stack.pop()
    stack.append(i)

for i in ans:
    print(i, end=" ")
