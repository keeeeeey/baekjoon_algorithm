start = int(input())
end = int(input())
n_list = []
for i in range(start, end + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            if j == i:
                n_list.append(j)
            else:
                break
sum_num = 0
for k in range(len(n_list)):
    sum_num += n_list[k]
if not n_list:
    print(-1)
else:
    print(sum_num)
    print(n_list[0])