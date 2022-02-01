def merge(intervals):
    intervals.sort()
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1] = [result[-1][0], max(result[-1][1], intervals[i][1])]
        else:
            result.append(intervals[i])
    print(result)
    return result
merge([[1,3],[2,6],[8,10],[15,18]])