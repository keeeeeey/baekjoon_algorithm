import sys
T = int(input())
N_list = [sys.stdin.readline().strip() for _ in range(T)]
table = {")": "("}
for i in range(len(N_list)):
    stack = []
    b = True
    for s in N_list[i]:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if not stack or table[s] != stack.pop():
                print("NO")
                b = False
                break
    if b == True:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")