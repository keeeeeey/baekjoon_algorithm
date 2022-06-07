import math

room_number = input()
r_list = [0 for _ in range(10)]
for n in room_number:
    if n == "9":
        r_list[6] += 1
    else:
        r_list[int(n)] += 1

r_list[6] = math.ceil(r_list[6] / 2)

print(max(r_list))
