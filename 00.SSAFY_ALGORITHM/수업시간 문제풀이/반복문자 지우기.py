t = int(input())
for tc in range(1, t + 1):
    s = input()
    stack = []
    for a in s:
        if stack:
            if stack[-1] == a:
                stack.pop()
            else:
                stack.append(a)
        else:
            stack.append(a)
    print(f"#{tc} {len(stack)}")