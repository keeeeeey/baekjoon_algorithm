N = str(input())
alpha_dict = {2 : ["A", "B", "C"], 3 : ["D", "E", "F"], 4 : ["G", "H", "I"], 5 : ["J", "K", "L"], 6 : ["M", "N", "O"], 7 : ["P", "Q", "R", "S"], 8 : ["T", "U", "V"], 9 : ["W", "X", "Y", "Z"]}
time = 0
for i in range(len(N)):
    for j in range(2, 10):
        if N[i] in alpha_dict[j]:
            time += j + 1
print(time)