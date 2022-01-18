T = int(input())
for t in range(1, T + 1):
    a = 0
    score = 0
    N = str(input())
    for i in range(len(N)):
        if N[i] == "O":
            a += 1
            score += a
        else:
            a = 0
    print(score)