T = int(input())
for t in range(1, T + 1):
    word = ""
    N = list(map(str, input().split(" ")))
    for i in range(len(N[1])):
        word += "".join(N[1][i] * int(N[0]))
    print(word)