S = list(map(int, input().strip()))
answer = 0
for i in range(len(S)):
    if answer == 0 or S[i] == 1:
        answer += S[i]
    else:
        answer *= S[i]

print(answer)