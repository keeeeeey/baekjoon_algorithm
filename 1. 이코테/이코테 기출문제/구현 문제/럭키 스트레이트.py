N = list(map(int, input().strip()))
end = len(N)
mid = end / 2
left = 0
right = 0
for i in range(end):
    if i < mid:
        left += N[i]
        continue
    right += N[i]

if left == right:
    print("LUCKY")
else:
    print("READY")