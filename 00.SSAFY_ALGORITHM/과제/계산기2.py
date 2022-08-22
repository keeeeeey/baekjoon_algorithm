icp = {"+" : 1, "*" : 2}

def get_postfix(n, infix):
    stack = []
    postfix = ""

    for i in range(n):
        if "0" <= infix[i] <= "9":
            postfix += infix[i]
        else:
            if stack and icp[stack[-1]] >= icp[infix[i]]:
                postfix += stack.pop()
            stack.append(infix[i])

    while stack:
        postfix += stack.pop()
    return postfix

def calculate(n, postfix):
    stack = []
    for i in range(n):
        if "0" <= postfix[i] <= "9":
            stack.append(postfix[i])
        else:
            first = int(stack.pop())
            second = int(stack.pop())
            temp = 0
            if postfix[i] == "+":
                temp = second + first
            else:
                temp = second * first
            stack.append(temp)

    return stack[0]


for tc in range(1, 11):
    n = int(input())
    infix = input()

    postfix = get_postfix(n, infix)
    answer = calculate(n, postfix)

    print(f"#{tc} {answer}")