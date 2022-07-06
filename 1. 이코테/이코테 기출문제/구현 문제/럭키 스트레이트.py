n = list(map(int, input()))
left = 0
right = 0
length = len(n)
for i in range(length):
    if i < length // 2:
        left += n[i]
    else:
        right += n[i]

if left == right:
    print("LUCKY")
else:
    print("READY")

