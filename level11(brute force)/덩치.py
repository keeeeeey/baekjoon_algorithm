T = int(input())
info_list = []
for t in range(1, T + 1):
    weight, height = list(map(int, input().split(" ")))
    info_list.append([weight, height])
count_list = []
for i in range(len(info_list)):
     count = 1
     for j in range(len(info_list)):
          if info_list[i][0] < info_list[j][0] and info_list[i][1] < info_list[j][1]:
               count += 1
     count_list.append(str(count))
print(" ".join(count_list))