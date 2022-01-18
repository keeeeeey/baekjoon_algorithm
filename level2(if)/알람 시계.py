alarm = list(map(int, input().split(" ")))
time = alarm[0] * 60 + alarm[1] - 45
hour = time // 60
minute = time % 60
if hour == -1:
    print("{} {}".format("23", minute))
else:
    print("{} {}".format(hour, minute))