t = int(input())
for tc in range(1, t + 1):
    strs = input()
    ls = len(strs)
    cnt = 1
    answer = 0
    for i in range(1, ls):
        if strs[i] == "(":
            cnt += 1
        else:
            if strs[i - 1] == "(":
                answer += cnt - 1
                cnt -= 1
            else:
                answer += 1
                cnt -= 1
    answer += cnt
    print(f"#{tc} {answer}")

# 2
# ()(((()())(())()))(())
# (((()(()()))(())()))(()())