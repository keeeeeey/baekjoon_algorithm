t = int(input())
for tc in range(1, t + 1):
    str1 = input()
    str2 = input()
    l1 = len(str1)
    l2 = len(str2)
    flag = False
    for i in range(l2 - l1 + 1):
        temp = ""
        for j in range(i, i + l1):
            temp += str2[j]
            if temp == str1:
                flag = True
                break

    if flag:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
