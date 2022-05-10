S = list(map(int, input().strip()))
S_list = []
S_list.append(S[0])
cnt_0 = 0
cnt_1 = 0
for i in range(1, len(S)):
    S_list.append(S[i])

    if i == len(S) - 1:
        if S[i] == 0:
            cnt_0 += 1
        elif S[i] == 1:
            cnt_1 += 1

    if S_list[i - 1] == S[i]:
        continue
    else:
        if S[i - 1] == 0:
            cnt_0 += 1
        elif S[i - 1] == 1:
            cnt_1 += 1

print(min(cnt_0, cnt_1))