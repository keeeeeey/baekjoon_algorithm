def solution(grade):
    answer = []
    n = len(grade)
    for i in range(n):
        order = n
        for j in range(n):
            if i != j:
                if grade[i] >= grade[j]:
                    order -= 1
        answer.append(order)

    return answer