t = int(input())
for i in range(t):
    n = int(input())
    ss = list(list(map(str, input().split())) for _ in range(n))
    answer = ""
    print("#" + str(i + 1))
    for s in ss:
        for _ in range(int(s[1])):
            answer += s[0]
            if len(answer) == 10:
                print(answer)
                answer = ""
    print(answer)