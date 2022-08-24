icp = {"+" : 1, "*" : 2, "(" : 3}
isp = {"+" : 1, "*" : 2, "(" : 0}

def get_postfix(n, infix):
    stack = []
    postfix = ""

    for i in range(n):
        if "0" <= infix[i] <= "9":
            postfix += infix[i]
        else:
            if infix[i] == ")":
                while True:
                    if stack[-1] == "(":
                        stack.pop()
                        break
                    else:
                        postfix += stack.pop()
            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                stack.append(infix[i])

    while stack:
        postfix += stack.pop()
    return postfix

def calculate(postfix):
    stack = []
    for i in range(len(postfix)):
        if "0" <= postfix[i] <= "9":
            stack.append(postfix[i])
        else:
            first = int(stack.pop())
            second = int(stack.pop())
            if postfix[i] == "+":
                stack.append(second + first)
            else:
                stack.append(second * first)

    return stack[0]


for tc in range(1, 11):
    n = int(input())
    infix = input()

    postfix = get_postfix(n, infix)
    answer = calculate(postfix)

    print(f"#{tc} {answer}")