x_list = []
y_list = []
x = ""
y = ""
for i in range(1, 4):
    N = list(map(int, input().split()))
    x_list.append(N[0])
    y_list.append(N[1])
for j in range(0, 3):
    if x_list.count(x_list[j]) == 1:
        x = x_list[j]
    if y_list.count(y_list[j]) == 1:
        y = y_list[j]
print("{} {}".format(x, y))