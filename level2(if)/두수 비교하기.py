N = list(map(int, input().split(" ")))
if N[0] < N[1]:
    print("<")
elif N[0] > N[1]:
    print(">")
else:
    print("==")