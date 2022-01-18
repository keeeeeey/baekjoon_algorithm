multi = 1
for i in range(1, 4):
    N = int(input())
    multi *= N
for j in range(0, 10):
    count = str(multi).count(str(j))
    print(count)