t = int(input())
for tc in range(1, t + 1):
    s = list(input().split())
    l = len(s)
    stack = []
    flag = True
    for i in range(l):
        if "0" <= s[i] <= "9":
            stack.append(s[i])
        else:
            if s[i] == ".":
                break

            if len(stack) < 2:
                flag = False
                break

            first = int(stack.pop())
            second = int(stack.pop())
            if s[i] == "+":
                stack.append(second + first)
            elif s[i] == "-":
                stack.append(second - first)
            elif s[i] == "*":
                stack.append(second * first)
            elif s[i] == "/":
                stack.append(second // first)

    if not flag:
        print(f"#{tc} error")
    else:
        if len(stack) > 1:
            print(f"#{tc} error")
        else:
            print(f"#{tc} {stack[-1]}")