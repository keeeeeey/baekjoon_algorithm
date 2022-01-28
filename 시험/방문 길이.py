def solution(dirs):
    command = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    curx, cury = (0, 0)
    road = set()
    for d in dirs:
        nextx, nexty = curx + command[d][0], cury + command[d][1]
        if -5 <= curx <= 5 and -5 <= cury <= 5:
            road.add((curx, cury, nextx, nexty))
            road.add((nextx, nexty, curx, cury))
            curx, cury = nextx, nexty
    print(len(road) // 2)
    return len(road) // 2

solution("ULURRDLLU")