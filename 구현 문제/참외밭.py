import sys
input = sys.stdin.readline
k = int(input())

l_list = []

for _ in range(6):
    direction, length = map(int, input().split())
    l_list.append(length)

big = 0
small = 0

for i in range(6):
    temp = l_list[i] * l_list[(i + 1) % 6]
    if big < temp:
        big = temp
        idx = i

small = l_list[(idx + 3) % 6] * l_list[(idx + 4) % 6]

print(k * (big - small))