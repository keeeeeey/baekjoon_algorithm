import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(N)]
min_list = []
for i in range(len(list)):
    min_list.append(min(list[i]))
print(max(min_list))