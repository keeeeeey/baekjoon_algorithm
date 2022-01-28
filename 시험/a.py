def solution(progresses, speeds):
    answer = []
    left = []
    date = []
    for i in range(len(progresses)):
        left.append(100 - progresses[i])

    for i in range(len(progresses)):
        count = 0
        while left[i] > speeds[i] * count:
            count += 1
        date.append(count)
    k = 1
    cnt = 1
    while True:
        try:
            if date[0] < date[k]:
                answer.append(cnt)
                for j in range(1, k + 1):
                    date.pop(0)
                cnt = 1
                k = 1
            elif date[0] >= date[k]:
                cnt += 1
                k += 1
        except:
            answer.append(cnt)
            break
    print(answer)
    return answer

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])