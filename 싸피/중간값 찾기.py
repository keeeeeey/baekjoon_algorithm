n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
print(n_list[len(n_list) // 2])