t = int(input())
for tc in range(1, t + 1):
    p, a, b = map(int, input().split())
    startA = 1
    endA = p
    cntA = 0
    startB = 1
    endB = p
    cntB = 0
    while startA <= endA:
        cntA += 1
        midA = int((startA + endA) / 2)

        if midA > a:
            endA = midA
        elif midA < a:
            startA = midA
        else:
            break

    while startB <= endB:
        cntB += 1
        midB = int((startB + endB) / 2)

        if midB > b:
            endB = midB
        elif midB < b:
            startB = midB
        else:
            break

    if cntA == cntB:
        print(f"#{tc} 0")
    elif cntA > cntB:
        print(f"#{tc} B")
    else:
        print(f"#{tc} A")