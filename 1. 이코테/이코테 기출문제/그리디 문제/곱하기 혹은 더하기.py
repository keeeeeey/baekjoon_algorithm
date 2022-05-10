S = list(map(int, input().strip()))
answer = 0
for i in range(len(S)):
    if S[i] == 0 or S[i] == 1 or answer == 0:
        answer += S[i]
    else:
        answer *= S[i]

print(answer)