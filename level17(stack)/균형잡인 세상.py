import sys
table = {
    ")": "(",
    "]": "["
}
while True:
    S = sys.stdin.readline().rstrip()
    stack = []
    b = True
    if S == ".":
        break
    for a in S:
        if a == "(" or a == "[":
            stack.append(a)
        elif a == ")" or a == "]":
            if not stack or table[a] != stack.pop():
                print("no")
                b = False
                break
    if b == True:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")