T = int(input())
cnt = 0
for t in range(1, T + 1):
    N = str(input())
    for i in range(len(N) - 1):
        if N[i] != N[i + 1]:
            if N[i] in N[i+1:]:
                cnt += 1
                break;
print(T - cnt)