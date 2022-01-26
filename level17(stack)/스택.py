import sys
N = int(input())
order_list = [sys.stdin.readline().split() for _ in range(N)]
ans = []
for i in range(len(order_list)):
    if order_list[i][0] == "push":
        ans.append(order_list[i][1])
    if order_list[i][0] == "pop":
        if len(ans) == 0:
            print(-1)
        else:
            print(ans.pop())
    if order_list[i][0] == "size":
        print(len(ans))
    if order_list[i][0] == "empty":
        if len(ans) == 0:
            print(1)
        else:
            print(0)
    if order_list[i][0] == "top":
        if len(ans) == 0:
            print(-1)
        else:
            print(ans[-1])

