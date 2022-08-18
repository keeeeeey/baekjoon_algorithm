for tc in range(1, 11):
    n, s = input().split()
    stack = []
    for i in range(int(n)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    print(f"#{tc} {''.join(stack)}")