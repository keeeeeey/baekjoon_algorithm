T = int(input())
for t in range(1, T + 1):
    floor = int(input())
    room_num = int(input())
    cnt = []
    for r in range(1, room_num + 1):
        cnt.append(r)
    for f in range(floor):
        for i in range(1, room_num):
            cnt[i] += cnt[i-1]

    print(cnt[-1])