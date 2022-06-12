def solution(grade):
    answer = []
    n = len(grade)
    list = []

    for i in range(n):
        list.append([i, grade[i]])

    list.sort(key=lambda x: -x[1])

    order = 1
    cnt = 1
    list[0].append(1)
    for i in range(1, n):
        if list[i][1] == list[i - 1][1]:
            list[i].append(order)
            cnt += 1
        else:
            order += cnt
            list[i].append(order)
            cnt = 1

    list.sort(key=lambda x: x[0])

    for i in range(n):
        answer.append(list[i][2])

    return answer

print(solution([3, 2, 1, 2]))