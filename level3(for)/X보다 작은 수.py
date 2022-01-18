T = list(map(int, input().split(" ")))
N = list(map(int, input().split(" ")))
list = []
for n in N:
    if n < T[1]:
        list.append(str(n))
print(" ".join(list))