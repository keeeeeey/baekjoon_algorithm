T = int(input())
for t in range(1, T + 1):
    N = list(map(int, input().split(" ")))
    room_num = 0
    if N[2] % N[0] == 0:
        room_num = N[0] * 100 + N[2] / N[0]
    else:
        room_num = N[2] % N[0] * 100 + N[2] // N[0] + 1
    print("{:.0f}".format(room_num))