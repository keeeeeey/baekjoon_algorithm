left1 = []
for i in range(1, 11):
    N = int(input())
    left2 = N % 42
    left1.append(left2)
set_left1 = set(left1)
print(len(set_left1))