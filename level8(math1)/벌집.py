N = int(input())
answer = ""
i = 1
while True:
    if i * (i + 1) / 2 < N:
        i += 1
    else:
        break
a = N - (i - 1) * i / 2
if i % 2 == 1:
    print("{:.0f}/{:.0f}".format(i - a + 1, a))
else:
    print("{:.0f}/{:.0f}".format(a, i - a + 1))
