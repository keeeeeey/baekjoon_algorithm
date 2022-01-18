list = []
for i in range(1, 10):
    N = int(input())
    list.append(N)
max_num = max(list)
index_num = list.index(max_num)
print(max_num)
print(index_num + 1)