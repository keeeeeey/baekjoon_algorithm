t = int(input())
for tc in range(1, t + 1):
    strs = list(input())
    l = len(strs)
    temp = []
    flag = True
    for i in range(l):
        if strs[i] == "(" or strs[i] == "{":
            temp.append(strs[i])
        if strs[i] == ")":
            if len(temp) == 0:
                flag = False
            elif temp[-1] == "(":
                temp.pop()
            else:
                flag = False
                break
        if strs[i] == "}":
            if len(temp) == 0:
                flag = False
            elif temp[-1] == "{":
                temp.pop()
            else:
                flag = False
                break

    if len(temp) != 0:
        flag = False

    if flag:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")