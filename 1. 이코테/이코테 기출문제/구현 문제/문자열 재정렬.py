S = str(input())
result = []
value = 0

for s in S:
    if s.isalpha():
        result.append(s)
    else:
        value += int(s)

result.sort()

if value != 0:
    result.append(str(value))

print("".join(result))

