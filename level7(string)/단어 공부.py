s = str(input()).lower()
list_s2 = list(set(s))
list_count = []
for i in range(len(list_s2)):
    list_count.append(s.count(list_s2[i]))
if list_count.count(max(list_count)) > 1:
    print("?")
else:
    max_index = list_count.index(max(list_count))
    print(list_s2[max_index].upper())
