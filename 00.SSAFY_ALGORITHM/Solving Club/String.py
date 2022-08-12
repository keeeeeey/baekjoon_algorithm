for _ in range(1, 11):
    tc = int(input())
    str1 = input()
    str2 = input()
    l1 = len(str1)
    l2 = len(str2)
    i = 0
    j = 0
    answer = 0
    while i < l1 and j < l2:
        if str1[i] != str2[j]:
            j = j - i
            i = -1
        i += 1
        j += 1

        if i == l1:
            answer += 1
            i = 0

    print(f"#{tc} {answer}")