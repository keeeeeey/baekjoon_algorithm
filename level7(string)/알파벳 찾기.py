s = str(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
index = []
for i in range(len(alpha)):
    if alpha[i] not in s:
        index.append("-1")
    else:
        index.append(str(s.index(alpha[i])))
a = " ".join(index)
print(a)