t = int(input())
for tc in range(1, t + 1):
    number_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    c, l = input().split()
    arr = list(input().split())
    for i in range(int(l)):
        number_dict[arr[i]] += 1

    number_list = list(number_dict.items())
    print(f"#{tc}")
    for i in range(10):
        for _ in range(number_list[i][1]):
            print(number_list[i][0], end=" ")
    print()