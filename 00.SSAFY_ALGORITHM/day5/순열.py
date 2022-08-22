def f(i, N):
    if i == N:
        print(P)
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i + 1, N)
            P[i], P[j] = P[j], P[i]

P = [1, 2, 3]
f(0, 3)