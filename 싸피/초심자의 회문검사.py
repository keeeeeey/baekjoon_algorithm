t = int(input())
s_list = list(input() for _ in range(t))
for i in range(t):
    s = s_list[i]
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            break

    if left >= right:
        print("#" + str(i + 1) + " 1")
    else:
        print("#" + str(i + 1) + " 0")