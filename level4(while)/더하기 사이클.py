N = str(input())
i = 1
result = 0

if 0 <= int(N) <= 9:
    result = str(int(N) * 10 + int(N))
else:
    result = str(int(N[-1]) * 10 + int(str(int(N[0]) + int(N[-1]))[-1]))
while True:
    if N == result:
        print(i)
        break;
    if 0 <= int(result) <= 9:
        result = str(int(result) * 10 + int(result))
    else:
        result = str(int(result[-1]) * 10 + int(str(int(result[0]) + int(result[-1]))[-1]))
    i += 1