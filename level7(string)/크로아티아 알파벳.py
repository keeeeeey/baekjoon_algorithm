s = str(input())
alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt_sum = 0
for i in range(len(alpha_list)):
    count = s.count(alpha_list[i])
    cnt_sum += count
    s = s.replace(alpha_list[i], " ")
s = s.replace(" ", "")
print(cnt_sum + len(s))
